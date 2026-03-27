# Context Discovery 3-Layer 아키텍처

## 문제

AGENTS.md에 "docs/index.md를 읽어라"라고만 적어두면
에이전트는 어떤 파일이 있는지 알지만, **효율적으로 필요한 것만 꺼내는 방법**을 모른다.
모든 파일을 순차적으로 읽거나, 관련 없는 파일까지 로드하여 컨텍스트를 낭비한다.

## 해결: 3-Layer 아키텍처

```
Layer 1: 항상 로드됨 (agent config files)
  → 세션 시작 시 자동. ~60줄의 원칙 + 파일 구조 안내 + 도구 안내.
  → 도메인 지식 자체는 넣지 않음.

Layer 2: 요청 시 로드됨 (skills — progressive disclosure)
  → 메타데이터(이름+설명)만 미리 로드, 전체 내용은 필요할 때 로드.
  → 도메인 탐색, property 추출, 정합성 검증 등 워크플로우 번들.

Layer 3: 격리 탐색 (subagents)
  → 별도 컨텍스트 윈도우에서 파일 시스템을 탐색하고 결과만 반환.
  → 메인 컨텍스트를 오염시키지 않음.
```

## Layer 1: Agent Config Files

CLAUDE.md, AGENTS.md, GEMINI.md는 세션 시작 시 자동으로 읽힌다.
여기에는 원칙, 파일 구조 안내, 사용 가능한 도구 안내만 넣는다.

```markdown
## 컨텍스트를 파악하는 방법

작업 전에 docs/index.md를 먼저 읽어라.
더 깊은 탐색이 필요하면:
- domain-scout skill로 특정 ID의 관련 파일을 찾을 수 있다.
- impact-tracer skill로 변경의 파급 범위를 추적할 수 있다.
- Explore subagent를 사용하여 메인 컨텍스트 오염 없이 탐색할 수 있다.
```

이것이 핵심이다: **도메인 지식을 config 파일에 넣지 않고, "어디서 찾는지"만 안내한다.**
config 파일이 100줄을 넘으면 에이전트가 중요한 지시를 놓치기 시작한다.

## Layer 2: Skills (Progressive Disclosure)

Skills는 `.agents/skills/` 디렉토리에 두며, 세 에이전트가 공유한다.
Agent Skills는 2026년 현재 Claude Code, Codex, Gemini CLI 모두에서 동작하는 오픈 스탠다드다.

### Progressive Disclosure의 작동 방식

에이전트가 세션을 시작하면, 각 Skill의 **메타데이터(이름+설명)만** 로드된다.
예를 들어 7개 Skill이 있으면, 각각의 이름과 설명(2~3줄)만 인덱싱된다.
에이전트가 현재 작업과 관련 있다고 판단하면 그때 **전체 SKILL.md가 로드**된다.

이것이 CLAUDE.md에 모든 절차를 넣는 것보다 효율적인 이유:
- 7개 Skill × 30줄 = 210줄의 절차가 있지만, 한 작업에 필요한 것은 1~2개뿐
- Layer 1에 210줄을 넣으면 매 작업마다 전부 읽지만,
  Skill로 분리하면 필요한 30~60줄만 로드

### 이 boilerplate의 7개 Skill

| Skill | 역할 | 호출 시점 |
|-------|------|----------|
| domain-scout | 특정 주제의 관련 파일 탐색 | 새 작업 시작, 도메인 맥락 파악 |
| property-extractor | 제약사항 → property 추출 | 새 제약사항 추가 후 |
| integrity-checker | 문서-코드 동기화 검증 | 작업 완료 시, 커밋 전 |
| impact-tracer | 변경의 파급 범위 추적 | 기존 모델/제약사항 수정 시 |
| test-router | PBT/TDD 라우팅 판단 | 새 테스트 작성 전 |
| doc-sync | 문서 갱신 안내 | 코드 변경 후 문서 동기화 |
| dispatch | 크로스 모델 호출 패턴 | Orchestrator가 sub-agent 호출 시 |

### integrity-checker의 이중 구조

이 Skill은 다른 Skill과 달리 `scripts/check_sync.py`를 포함한다.

SKILL.md는 에이전트가 읽고 검증 절차를 안내받는 용도이고,
`check_sync.py`는 ID 기반 교차 참조를 **결정적(deterministic)으로** 검증하는 스크립트다.

이 스크립트는 Claude Code의 Stop Hook에 걸려 있어서
매 작업 완료 시 자동으로 실행된다:

```json
// .claude/settings.json
{
  "hooks": {
    "Stop": [{
      "command": "python .agents/skills/integrity-checker/scripts/check_sync.py"
    }]
  }
}
```

에이전트의 판단에 의존하지 않는 프로그래밍적 안전장치다.

## Layer 3: Subagents (격리된 탐색)

Subagent의 핵심 가치는 **메인 컨텍스트를 오염시키지 않는 것**이다.

코드 파일 100개를 읽어야 하는 탐색을 메인 에이전트가 직접 하면,
그 100개 파일의 내용이 메인 컨텍스트에 쌓여서
정작 중요한 도메인 지식이 밀려나는 "컨텍스트 로트(context rot)"가 발생한다.

Subagent는 별도의 컨텍스트 윈도우에서 탐색하고,
**요약된 결과만** 메인 에이전트에게 반환한다.

### Claude Code 내장 subagent

- **Explore**: 읽기 전용 탐색. "src/domain/에서 ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG을 참조하는 코드를 찾아줘"
- **Plan**: Plan Mode에서 자동 사용. 구현 전 코드 구조 파악

### 커스텀 subagent

이 boilerplate에는 2개의 커스텀 subagent가 있다:

**domain-explorer** — 도메인 문서 탐색 전문
```markdown
# .claude/agents/domain-explorer.md
allowed-tools: [Read, "Bash(grep:*)", "Bash(find:*)"]
skills: [domain-scout]  # ← domain-scout skill이 preload됨
```

`skills: [domain-scout]`로 선언하면 subagent 시작 시
domain-scout의 전체 내용이 subagent의 컨텍스트에 주입된다.
메인 에이전트의 컨텍스트는 깨끗하게 유지된다.
여기서 `grep`은 markdown 발췌용 fallback일 뿐이고,
경로 탐색의 1차 수단은 domain-scout가 안내하는 catalog/LSP 심볼 추적이다.

**code-scanner** — 코드/테스트 현황 파악
```markdown
# .claude/agents/code-scanner.md
allowed-tools: [Read, "Bash(grep:*)", "Bash(find:*)", "Bash(pytest:--collect-only*)"]
```

이 subagent도 구현과 테스트 위치를 먼저 심볼/참조 기준으로 좁히고,
raw ID 문자열 검색은 docstring 확인이 필요할 때만 사용한다.

## 에이전트가 컨텍스트를 찾는 흐름

```
1. AGENTS.md/CLAUDE.md 안내 → "docs/index.md를 먼저 읽어라"
2. index.md에서 전체 지도 파악 (모델 목록, 제약사항 수, 파일 위치)
3. 관련 Skill이 자동 매칭되어 활성화 (domain-scout, impact-tracer 등)
4. 더 깊은 탐색이 필요하면 Subagent에 위임 (Explore, domain-explorer)
5. 메인 컨텍스트에는 요약만 남음
```

이 흐름에서 에이전트의 컨텍스트 윈도우 사용량을 추정하면:

| 단계 | 로드되는 토큰 (추정) |
|------|---------------------|
| AGENTS.md | ~1,500 (60줄) |
| index.md | ~500 (20줄) |
| Skill 메타데이터 (7개) | ~700 (7 × 3줄) |
| 활성화된 Skill 1개 | ~800 (30줄) |
| Subagent 결과 요약 | ~300 (10줄) |
| **합계** | **~3,800** |

전체 docs/ + src/ + tests/를 한 번에 읽으면 10,000~20,000 토큰을 소비하는 것과 비교하면
3-Layer 아키텍처가 **70~80%의 컨텍스트를 절약**한다.
