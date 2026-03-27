# Multi-Agent Orchestrator 설계

## 설계 철학: 규칙이 아니라 원칙

이 Orchestrator는 Phase Selection Matrix, Gate Check 규칙, Retry 정책 같은
하드코딩된 워크플로우를 따르지 않는다.

대신 **3개의 원칙, 프로젝트 구조에 대한 이해, 과거 판단 예시**를 받고
나머지는 컨텍스트를 읽고 자율적으로 판단한다.

이 전환의 근거:

규칙 기반 설계의 문제는 에이전트가 "규칙을 이해하고 준수하는 데"
컨텍스트 윈도우를 소모한다는 것이다. 50개의 규칙이 150줄의 AGENTS.md에 있으면
에이전트는 실제 프로젝트 파일을 읽기 전에 이미 상당한 토큰을 소비한다.
그리고 규칙에 없는 상황을 만나면 멈추거나 잘못 판단한다.

원칙은 모든 상황에 적용된다. "깨뜨리지 마라"는 어떤 경로를 선택하든,
기존 테스트가 통과하면 괜찮다는 것을 의미한다.
예시는 LLM이 가장 잘하는 "패턴을 현재 상황에 적용하는 것"을 활용한다.

## 세 가지 원칙

### 1. 깨뜨리지 마라 (Don't break)

기존에 통과하던 테스트가 깨지면 안 된다.
기존 제약사항(카탈로그 및 `docs/<scope>/` 서사)을 임의로 삭제하거나 약화하지 마라.
작업 완료 후 전체 테스트를 돌려서 확인해라.

### 2. 빠뜨리지 마라 (Don't skip)

새 도메인 규칙을 코드에 구현했으면, 카탈로그와 `docs/<scope>/` 서사에도 기록해라.
새 제약사항을 문서에 추가했으면, 그것을 검증하는 테스트도 있어야 한다.
코드·문서·테스트는 항상 동기화 상태를 유지해라.

### 3. 추적 가능하게 하라 (Trace everything)

왜 이 작업을 이 순서로 했는지 기록해라.
어떤 sub-agent에게 무엇을 시키고 어떤 결과가 돌아왔는지 기록해라.
커밋 메시지에 변경 근거(제약사항 ID 등)를 남겨라.

## 에이전트 역할 분담

### Codex — Orchestrator

전체 워크플로우를 관리한다. 사용자 요청을 받아 현재 프로젝트 상태를 파악하고,
어떤 sub-agent를 어떤 순서로 호출할지 자율적으로 결정한다.

Orchestrator에 적합한 이유:
- **토큰 효율**: 라우팅 판단처럼 추론 깊이보다 판단 속도가 중요한 작업에 최적.
  Claude Code 대비 3~5배 적은 토큰 소비.
- **병렬 실행**: 클라우드 샌드박스에서 여러 sub-agent를 동시에 실행 가능.
- **CI 통합**: GitHub Action, PR 리뷰, Automations 내장.

### Claude Code — 도메인 추론 Sub-Agent

도메인을 이해하고 추론해야 하는 작업을 담당한다.
새 도메인 모델 설계, 제약사항에서 property 추출,
Hypothesis stateful 테스트 설계, 핵심 도메인 구현.

적합한 이유:
- Plan Mode로 분석 → 구현 전환이 자연스러움
- 78% first-pass 성공률로 장시간 자율 작업 가능
- subagent(Explore, Plan)로 코드베이스를 탐색하면서 메인 컨텍스트를 깨끗하게 유지

### Gemini CLI — 검증 Sub-Agent

전체를 한 번에 봐야 하는 검증 작업을 담당한다.
교차 참조 검증, 문서-코드 정합성 감사, 전체 코드베이스 분석.

적합한 이유:
- 1M 토큰 컨텍스트로 전체 docs/ + src/ + tests/를 한 번에 로드 가능
- 무료 티어가 넉넉하여 반복적 검증 작업에 비용 부담 없음
- JSON 출력으로 결과를 프로그래밍적으로 파싱 가능

## Orchestrator의 판단 과정

Orchestrator는 고정된 Phase를 따르는 것이 아니라,
현재 프로젝트의 파일들을 직접 읽고 상태를 파악하여 계획을 세운다.

### 예시: "주문 취소 시 재고 해제 기능 추가"

```
[Orchestrator의 사고]

1. docs/index.md를 읽자.
   → ORD_POL_ORDER_CANCEL_RELEASES_ALLOC이 이미 카탈로그에 존재한다.

2. `src/catalog/`의 Property와 관련 모델의 `doc_file`을 보자.
   → 해당 Property의 test_file이 존재하는지 확인한다.

3. src/domain/services.py를 보자.
   → cancel_order() 함수가 아직 없다.

4. 상황 정리:
   - 제약사항은 이미 문서화됨 (새 도메인 모델링 불필요)
   - Property도 이미 추출됨 (새 property 추출 불필요)
   - 테스트와 구현만 필요

5. 실행:
   a. Claude Code: ORD_P_ALLOC_REQUIRES_MATCHING_SKU의 stateful PBT 작성
   b. Codex Worker: 구체 시나리오 TDD 작성 (병렬)
   c. Claude Code: cancel_order() 구현
   d. Codex Worker: 코드 리뷰
   e. 전체 테스트 실행 + integrity-checker
```

이 사고 과정은 어떤 Matrix도 참조하지 않는다.
현재 파일 상태를 기반으로 "뭐가 이미 있고 뭐가 없는지"를 판단한다.

## 결과 검증: 과정이 아니라 결과에 불변식을 건다

Orchestrator의 자율성을 보장하면서 안전을 유지하는 방법은
과정을 통제하는 것이 아니라, 결과에 불변식(invariant)을 거는 것이다.

작업이 끝났을 때 다음이 모두 참이면 된다:

```
INV-A: pytest tests/ 가 전부 통과
INV-B: mypy src/ 가 통과
INV-C: "코드에 있는 규칙" ⊆ "카탈로그에 있는 규칙"
INV-D: "카탈로그에 있는 규칙" ⊆ "테스트가 커버하는 규칙"
INV-E: 새로 추가된 모든 artifact에 ID가 있음
INV-F: 커밋 메시지에 변경 근거가 있음
```

어떤 순서로 작업했든, 최종 결과만 맞으면 된다.
INV-A, INV-B는 명령어로, INV-C, INV-D는 integrity-checker로,
INV-E, INV-F는 Orchestrator 자신이 확인한다.

## 에스컬레이션

다음 상황에서는 작업을 멈추고 사용자에게 보고한다:
- 기존 테스트가 깨졌는데 원인을 여러 번 시도해도 해결 못할 때
- 사용자의 요청이 기존 제약사항과 모순될 때
- 도메인 용어의 의미가 불확실할 때

Orchestrator가 판단하지 않는 것:
- "이 기능이 비즈니스적으로 필요한가" → 사람의 영역
- "기존 제약사항을 삭제해야 하는가" → 사람의 승인 필요
- "이 도메인 용어가 정확한가" → 도메인 전문가의 영역

## Trace: 판단 기록

세 번째 원칙 "추적 가능하게 하라"의 구현이다.

좋은 trace — **왜 그렇게 판단했는지**가 드러남:

```
## Trace: 주문 취소 기능 구현

### 상황 판단
- ORD_POL_ORDER_CANCEL_RELEASES_ALLOC, ORD_P_ALLOC_REQUIRES_MATCHING_SKU이 이미 문서에 존재하지만 테스트와 구현이 없음
- 도메인 문서 변경 불필요, 테스트 + 구현만 필요

### 실행
1. Claude Code에게 ORD_P_ALLOC_REQUIRES_MATCHING_SKU stateful PBT 작성 요청 → 4 properties
2. Codex Worker에게 취소 시나리오 TDD 작성 요청 (병렬) → 3 examples
3. 전체 테스트 → RED (7 FAILED)
4. Claude Code에게 구현 요청 → cancel_order() 추가
5. 전체 테스트 → 6 PASSED, 1 FAILED → 수정 요청
6. 전체 테스트 → GREEN
7. integrity-checker → PASS
```

나쁜 trace — **어떤 규칙을 적용했는지**만 드러남:

```
Phase 1: SKIP (Rule: existing constraint)
Phase 3: EXECUTED (Rule: always)
Phase 4: EXECUTED
  Gate 4: FAIL → Retry 1 → PASS
```
