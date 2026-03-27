---
name: test-router
description: >
  새 제약사항이나 기능에 대해 PBT와 TDD 중 어떤 테스트가 적합한지 판단.
---

## 4문항 판단

Q1. "모든 X에 대해 Y가 성립"으로 표현되는가?
Q2. 입력 공간이 넓은가? (수십 가지 이상의 유효 조합)
Q3. shrink된 반례가 디버깅에 유의미한가?
Q4. 구현과 독립된 검증 방법(oracle)이 있는가?

3~4개 Yes → PBT (tests/properties/)
0~1개 Yes → TDD (tests/unit/)
2개 Yes → Mixed (PBT + TDD 예제 보완)

## DDD 구성 요소별 기본 성향

- Value Object: PBT 우선 (입력 공간 넓고 불변식 뚜렷)
- Entity 상태 전이: Mixed (stateful PBT + TDD 시나리오)
- 도메인 정책: 일반화 가능하면 PBT, 예외 많으면 TDD
- 서비스 오케스트레이션: TDD 우선
- 외부 어댑터: TDD 전용
