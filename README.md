# DDD + Property-Based Testing Multi-Agent Boilerplate

**경량 DDD · Hypothesis PBT · Codex Orchestrator + Claude Code + Gemini CLI**

이 boilerplate를 복사하면 다음 방법론이 즉시 적용됩니다:

- **경량 DDD**: 도메인 모델·제약사항·이벤트를 Python 카탈로그 객체로 구조화하고, docs/에 서사를 분리 관리
- **PBT + TDD 혼합 테스트**: 4문항 라우팅으로 PBT/TDD를 자동 판별
- **Multi-Agent Orchestration**: Codex가 Orchestrator, Claude Code가 도메인 추론, Gemini가 검증

## Quick Start

```bash
# 1. 복사
cp -r ddd-pbt-boilerplate/ my-new-project/
cd my-new-project/

# 2. 의존성 설치
pip install -e ".[dev]"

# 3. 예시 테스트 실행
pytest tests/ -q

# 4. 도메인 지식을 프로젝트에 맞게 교체
#    docs/glossary.md          → 용어 교체 (서사)
#    docs/<scope>/*.md         → 개념별 서사 작성 (필드·규칙·이벤트·Property 관점)
#    src/catalog/<scope>.py    → 스코프 카탈로그 작성 (구조적 관계)
#    docs/index.md             → Scope Registry와 서사 매핑 갱신

# 5. Agent와 작업 시작
#    Codex: codex (Orchestrator로 동작)
#    Claude Code: claude (도메인 추론 sub-agent로 동작)
#    Gemini: gemini (검증 sub-agent로 동작)
```

## 프로젝트 구조

```
├── AGENTS.md                    # Codex Orchestrator 설정
├── CLAUDE.md                    # Claude Code sub-agent 설정
├── GEMINI.md                    # Gemini CLI sub-agent 설정
│
├── docs/                        # 도메인 서사 (Source of Truth — 서사)
│   ├── index.md                 # 전체 지도 + 서사 파일 매핑
│   ├── glossary.md              # 용어집
│   └── <scope>/                 # 현재 스코프의 개념별 서사
│       ├── <model>.md           # 모델/규칙 서사
│       └── ...
│
├── src/
│   ├── catalog/                 # 도메인 카탈로그 (Source of Truth — 구조)
│   │   ├── types.py             # DomainModel, Constraint, Property, DomainEvent 타입
│   │   ├── <scope>.py           # 스코프별 카탈로그 인스턴스
│   │   └── __init__.py          # CATALOG 통합 객체 (impact_of 등)
│   └── domain/                  # 도메인 구현 (순수 Python)
│       ├── models.py            # Entity + Value Object
│       ├── events.py            # 도메인 이벤트 클래스
│       ├── services.py          # 도메인 서비스
│       └── exceptions.py        # 도메인 예외
│
├── tests/
│   ├── properties/              # PBT (Hypothesis)
│   ├── unit/                    # 예제 기반 TDD
│   └── conftest.py              # 공유 strategy + Hypothesis 프로파일
│
├── .agents/skills/              # Cross-agent Skills (공유)
│   ├── domain-scout/            # 도메인 탐색 (catalog + docs)
│   ├── property-extractor/      # Property 추출
│   ├── integrity-checker/       # 카탈로그·코드·테스트 정합성 검증
│   ├── impact-tracer/           # 변경 파급 추적 (CATALOG.impact_of)
│   ├── test-router/             # PBT/TDD 라우팅
│   ├── doc-sync/                # docs + catalog 동기화 안내
│   └── dispatch/                # 크로스 모델 호출
│
├── .claude/agents/              # Claude Code subagents
├── .codex/agents/               # Codex subagents
└── .task/                       # 임시 컨텍스트 전달용
```

## 두 레이어 원칙

| 레이어 | 위치 | 역할 | 형식 |
|--------|------|------|------|
| **서사** | `docs/` (개념별 `docs/<scope>/*.md` 등) | 왜 이 개념이 존재하는가 | Markdown (사람이 읽는 문서) |
| **구조** | `src/catalog/` | 개념들이 어떻게 연결되는가 | Python 객체 (LSP 추적 가능) |
| **구현** | `src/domain/` | 규칙이 어떻게 동작하는가 | Python 코드 |
| **검증** | `tests/` | 규칙이 실제로 성립하는가 | PBT + TDD |

## 세 가지 원칙

1. **깨뜨리지 마라** — 기존 테스트를 깨뜨리지 않는다
2. **빠뜨리지 마라** — 카탈로그·문서·코드·테스트를 항상 동기화한다
3. **추적 가능하게 하라** — 왜 이렇게 했는지 기록한다

## 방법론 문서

이 boilerplate의 설계 근거와 상세 가이드는 `docs/methodology/`에 있습니다:
- 경량 DDD 적용 범위
- PBT/TDD 라우팅 기준
- Multi-Agent Orchestrator 설계
- Context Discovery 3-Layer 아키텍처
- Sub-Agent Dispatch 패턴
