# Sub-Agent Dispatch 패턴

## 핵심 원칙: 최대한 단순하게

크로스 모델 에이전트 호출 방법은 여러 가지가 있지만,
이 프로젝트에서는 **가장 단순하고 검증된 방법**만 사용한다.

| 호출 유형 | 방법 | 복잡도 |
|----------|------|--------|
| 같은 모델 → 같은 모델 | 네이티브 subagent | 없음 (내장 기능) |
| 다른 모델 → 다른 모델 | headless CLI (-p 플래그) | 매우 낮음 (셸 명령어 한 줄) |

MCP 브릿지, hcom 같은 통신 프레임워크, ACP 프로토콜은 사용하지 않는다.
도메인과 관련 없는 인프라 복잡성을 최소화하기 위함이다.

## 같은 모델: 네이티브 Subagent

### Codex → Codex Worker

Codex의 `spawn_agent` / `wait_agent`를 사용한다.
.codex/agents/에 Worker를 정의해두면 자연어로 생성할 수 있다.

```
"tdd-writer subagent를 생성하여 tests/unit/에 테스트를 작성해줘.
 동시에 code-reviewer subagent도 생성하여 리뷰해줘.
 두 결과를 기다린 후 요약해줘."
```

이 boilerplate에 포함된 Codex Worker:
- `tdd-writer.md` — 예제 기반 TDD 테스트 작성
- `code-reviewer.md` — 구현 코드 리뷰 (구현 agent와 분리)

### Claude Code → Claude Code Subagent

내장 subagent(Explore, Plan)와 커스텀 subagent를 사용한다.

```
"domain-explorer subagent에게 위임해서
 POL-03과 관련된 모든 파일을 찾아줘."
```

이 boilerplate에 포함된 Claude Code Subagent:
- `domain-explorer.md` — 도메인 문서 탐색 (domain-scout skill preload)
- `code-scanner.md` — 코드/테스트 현황 파악

## 다른 모델: Headless CLI

각 에이전트의 공식 비대화형 모드를 그대로 사용한다.
추가 도구 설치가 필요 없고, 프롬프트에 명시한 것만 전달되므로 컨텍스트 제어가 정확하다.

### 호출 인터페이스

```bash
# Claude Code
claude -p "프롬프트" --allowedTools "Read,Edit,Write,Bash(pytest *)"

# Gemini CLI
gemini -p "프롬프트" --output-format json

# Codex CLI
codex exec "프롬프트"
codex exec --sandbox read-only --ephemeral "프롬프트"   # 읽기 전용
```

### 컨텍스트 전달: .task/ 디렉토리

에이전트 간 컨텍스트 전달을 위해 `.task/` 임시 디렉토리를 사용한다.

```
.task/
├── context.md    # 이번 작업에 필요한 컨텍스트 (발췌)
├── prompt.md     # sub-agent에게 보낼 프롬프트
└── result.json   # sub-agent의 결과물 (있으면)
```

프롬프트에 컨텍스트를 직접 넣으면 셸 이스케이핑 문제가 생기고,
파이프로 전달하면 길이 제한에 걸릴 수 있다.
파일로 쓰고 프롬프트에서 참조하면 이 문제가 모두 해결된다.

### 패턴 A: Orchestrator → Claude Code (도메인 추론)

Claude Code에게 보낼 때는 **grep으로 관련 부분만 발췌**하여 전달한다.
토큰 비용이 높으므로 정밀 발췌가 중요하다.

```bash
# 1. 관련 부분만 발췌
mkdir -p .task
grep -E "POL-03|주문 취소" docs/order/batch.md docs/order/order.md > .task/context.md

# 2. 프롬프트 작성
cat > .task/prompt.md << 'EOF'
.task/context.md를 읽고 POL-03에 대한
Hypothesis stateful PBT를 작성해줘.
출력: tests/properties/test_order_cancel.py
구현 코드는 작성하지 마.
EOF

# 3. 호출
claude -p "$(cat .task/prompt.md)" --allowedTools "Read,Write"
```

컨텍스트 제어 포인트:
- grep으로 관련 부분만 .task/context.md에 발췌 → **컨텍스트 낭비 없음**
- 제약사항 ID를 명시 → **컨텍스트 유실 없음**

### 패턴 B: Orchestrator → Gemini CLI (검증)

Gemini에게 보낼 때는 **파일 경로만 알려주고 직접 읽게** 한다.
1M 토큰이므로 발췌보다 전체를 읽는 게 효율적이다.

```bash
# 1. 프롬프트 작성 (발췌 없이 경로만)
cat > .task/prompt.md << 'EOF'
다음 파일을 읽고 교차 참조를 검증해줘:
- src/catalog/__init__.py
- src/catalog/order.py
- docs/order/
- docs/index.md
결과를 JSON으로 출력해줘.
EOF

# 2. 호출 (JSON 출력)
gemini -p "$(cat .task/prompt.md)" --output-format json > .task/result.json
```

### 패턴 C: Orchestrator → Claude Code (구현)

코드를 직접 작성하는 경우, 결과물은 파일 시스템에 남으므로
별도 result 파일이 불필요하다.

```bash
claude -p "tests/의 실패하는 테스트를 읽고,
모든 테스트가 통과하도록 src/domain/services.py를 구현해줘.
테스트 파일은 수정하지 마." \
  --allowedTools "Read,Edit,Write,Bash(pytest *)"
```

## 컨텍스트 전달 규칙

### 규칙 1: 상대 에이전트의 특성에 맞게 전달

| 상대 | 전달 방식 | 이유 |
|------|----------|------|
| Claude Code | grep으로 발췌 → .task/context.md | 토큰 비용 높으므로 정밀 발췌 |
| Gemini CLI | 파일 경로만 전달 | 1M 컨텍스트이므로 직접 읽는 게 효율적 |
| Codex Worker | 네이티브 subagent 프롬프트 | 같은 모델이므로 파일 접근 공유 |

### 규칙 2: 프롬프트에 작업 범위를 명시

```
나쁜 예: "코드를 리뷰해줘"
좋은 예: "src/domain/services.py의 cancel_order()를 리뷰해줘.
         관련 제약사항은 POL-03."
```

### 규칙 3: sub-agent에게 다른 sub-agent의 존재를 알리지 않는다

```
나쁜 예: "이 작업을 끝내면 Gemini에게 검증을 요청할 거야"
좋은 예: "이 작업을 수행해줘."
```

각 sub-agent는 자기 작업만 알면 된다.
오케스트레이션 로직은 Orchestrator만 가지고 있다.

### 규칙 4: 작업 완료 후 정리

```bash
rm -rf .task/*
```

.task/는 .gitignore에 포함되어 있으므로 커밋에 포함되지 않는다.

## 전체 흐름 예시

```
[사용자] "주문 취소 시 재고 해제 기능을 만들어줘"

[Codex Orchestrator]

1. docs/index.md 읽기 → POL-03 존재, 테스트/구현 없음

2. Claude Code에게 PBT 위임:
   grep -E "POL-03|취소" docs/order/order.md docs/order/batch.md > .task/context.md
   claude -p "$(cat .task/prompt.md)" --allowedTools "Read,Write"

3. Codex Worker에게 TDD 위임 (2와 병렬):
   "tdd-writer subagent를 생성하여 POL-03 엣지 케이스 테스트 작성"

4. 두 작업 완료 → pytest --collect-only로 수집 확인

5. Claude Code에게 구현 위임:
   claude -p "실패하는 테스트를 통과시켜줘" --allowedTools "Read,Edit,Write,Bash(pytest *)"

6. Codex Worker에게 리뷰 위임:
   "code-reviewer subagent를 생성하여 리뷰"

7. Gemini에게 정합성 검증 위임:
   gemini -p "$(cat .task/prompt.md)" --output-format json > .task/result.json

8. result.json 확인 → PASS

9. rm -rf .task/* && git commit
```
