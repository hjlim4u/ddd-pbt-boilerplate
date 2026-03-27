# 방법론 가이드

이 디렉토리는 boilerplate의 설계 근거와 상세 가이드를 담고 있다.
각 문서는 독립적으로 읽을 수 있지만, 순서대로 읽으면 전체 방법론이 하나의 흐름으로 이해된다.

## 문서 목록

| 순서 | 문서 | 핵심 질문 |
|------|------|----------|
| 1 | [lightweight-ddd.md](lightweight-ddd.md) | DDD를 어디까지 적용하고, 어디서 멈추는가? |
| 2 | [test-routing.md](test-routing.md) | 이 제약사항은 PBT로 테스트할까, TDD로 테스트할까? |
| 3 | [orchestrator.md](orchestrator.md) | Codex Orchestrator는 어떻게 자율적으로 판단하는가? |
| 4 | [context-discovery.md](context-discovery.md) | 에이전트가 필요한 컨텍스트를 어떻게 효율적으로 찾는가? |
| 5 | [sub-agent-dispatch.md](sub-agent-dispatch.md) | Orchestrator가 sub-agent에게 작업을 어떻게 지시하는가? |

## 방법론 한 줄 요약

경량 DDD로 도메인을 구조화하고, 제약사항에서 Property를 추출하여 PBT/TDD로 검증하며,
Codex Orchestrator가 Claude Code(도메인 추론)와 Gemini CLI(전체 검증)를 자율적으로 호출한다.
