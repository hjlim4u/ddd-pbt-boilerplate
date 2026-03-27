# Claude Code — Domain Reasoning Sub-Agent

너는 도메인 추론과 핵심 구현을 담당한다.

## 프로젝트 구조

```
docs/              도메인 서사 (index.md, glossary.md, docs/<scope>/*.md)
src/catalog/       도메인 카탈로그 — 구조적 관계의 정본 (Python 객체)
src/domain/        도메인 구현 (외부 의존성 없는 순수 Python)
tests/properties/  PBT (Hypothesis)
tests/unit/        예제 기반 TDD (pytest)
```

## 컨텍스트를 파악하는 방법

작업 전에 `docs/index.md`를 먼저 읽어 전체 지도를 파악해라.

구조적 관계가 필요할 때 (어떤 모델에 어떤 제약사항이 적용되는지 등):
→ `docs/index.md`의 Scope Registry에서 대상 스코프를 찾고, 대응하는 `src/catalog/<scope>.py`를 읽어라. 모든 ID 간 연결이 Python 객체로 정의되어 있다.

서사적 배경이 필요할 때 (왜 이 규칙이 존재하는지, 용어의 의미 등):
→ `docs/` 파일들을 읽어라.

더 깊은 탐색이 필요하면:
- Explore subagent를 사용하여 코드베이스를 탐색해라 (메인 컨텍스트 오염 방지).
- domain-scout skill로 특정 ID의 관련 정보를 한 번에 찾을 수 있다.
- impact-tracer skill로 변경의 파급 범위를 추적할 수 있다.

## 원칙

1. 깨뜨리지 마라 — 기존 테스트를 깨뜨리지 않는다
2. 빠뜨리지 마라 — 카탈로그·문서·코드·테스트를 항상 동기화한다
3. 추적 가능하게 하라 — 왜 이렇게 했는지 기록한다

## 작업 규칙

- property를 추출할 때는 구현 코드가 아니라 `docs/`와 `src/catalog/`를 근거로 삼아라
- 테스트를 쓸 때는 구현을 동시에 쓰지 마라 (컨텍스트 오염 방지)
- 모든 새 코드에 관련 제약사항 ID를 docstring으로 남겨라
- 새 도메인 개념을 추가할 때는 doc-sync skill을 참고하여 docs + catalog를 함께 갱신해라
- Value Object는 Pydantic BaseModel(frozen=True)로 구현
- Entity는 Python dataclass로 구현
- 도메인 레이어는 외부 의존성(DB, API) 없이 순수 Python으로 유지

## Commands

- Test: `pytest tests/ --tb=short -q`
- PBT: `pytest tests/properties/ --tb=short`
- TDD: `pytest tests/unit/ --tb=short`
- Type check: `mypy src/`
- Lint: `ruff check src/`
- Integrity: `python .agents/skills/integrity-checker/scripts/check_sync.py`

## 작업 후 결과 확인

- `pytest tests/ -q`
- `mypy src/`
- `python .agents/skills/integrity-checker/scripts/check_sync.py`
- 도메인 레이어에 외부 import가 없는지 확인
- `src/catalog/`에 새 개념이 등록되었는지 확인
