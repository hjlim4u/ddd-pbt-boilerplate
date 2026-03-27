# AI agent 활용한 DDD와 Property based test 개발 방법론

**Created:** 3/20/2026 10:22:00  
**Updated:** 3/25/2026 16:58:37  
**Exported:** 3/25/2026 20:36:05  
**Link:** [https://claude.ai/chat/0ad016c5-d377-44e1-aeb5-e54baa138df6](https://claude.ai/chat/0ad016c5-d377-44e1-aeb5-e54baa138df6)  

## Prompt:
2026. 3. 20. 오전 10:22:01

보다 더 안전하고 검증된 방식으로 AI agent 활용한 개발이 이루어지도록 Property based test와 도메인 주도 설계(DDD) 활용한 개발 방법론을 도입하고 싶어. 도메인 주도 설계를 통해 도메인 로직이 잘 드러나도록 컨텍스트를 관리하고 그렇게 드러난 도메인 로직이 Property 추출, Property based test로 이어지도록 AI agent를 활용한 최적의 개발 방법론을 찾아줘. (참고로, 모든 개발에 PBT를 적용하는 것이 아니라 Property 추출이 필요 없는 부분에서는 테스트 케이스 기반의 TDD 개발 방법론을 통한 테스트 코드 생성이 이루어지도록 유연함을 어느 정도 가져갔으면 좋겠어.)



## Response:
2026. 3. 20. 오전 10:22:16

````plaintext
Thought process: DDD와 PBT 결합한 AI 에이전트 개발 방법론 탐색했음.

The user wants to find an optimal development methodology that combines DDD (Domain-Driven Design) with Property-Based Testing (PBT) when using AI agents for development. They want flexibility - PBT where domain properties can be extracted, and traditional TDD where PBT isn't needed.

This is a detailed and specific query. Let me ask a few clarifying questions to make the research more targeted.
````

정말 흥미로운 주제네요! AI agent를 활용한 개발에서 DDD와 PBT를 결합하는 방법론을 찾아드리겠습니다. 더 정확한 리서치를 위해 몇 가지 확인하고 싶은 부분이 있습니다.

````plaintext
Tool: Generating ask_user_input_v0...
````

````plaintext
Thought process

I've asked the clarifying questions. Let me wait for the user's response before launching the research task.
````





## Prompt:
2026. 3. 20. 오전 10:22:50

질문: 어떤 AI agent를 주로 활용하고 계신가요? (해당하는 항목을 모두 선택)
답변: Claude Code (Anthropic)

질문: 주로 사용하시는 프로그래밍 언어/프레임워크는? (해당하는 항목을 모두 선택)
답변: Python

질문: 이 방법론의 적용 대상은?
답변: 개인 프로젝트 / 소규모 팀



## Response:
2026. 3. 20. 오전 10:33:30

````plaintext
Thought process: 사용자의 개발 환경과 선호도를 파악했다.

The user wants to find an optimal development methodology combining DDD, PBT, and AI agents (specifically Claude Code) for Python development in a small team/personal project context. The query is quite detailed and specific enough to launch research immediately.
````

감사합니다! Claude Code + Python 환경에서 DDD와 PBT를 결합한 AI agent 활용 개발 방법론을 깊이 있게 리서치하겠습니다. 바로 시작할게요!

````plaintext
Tool: launch_extended_search_task
````



Your research report on domain-driven development with AI agents and property-based testing is ready. It covers the synergy between DDD, property-based testing with Hypothesis, and Claude Code as an execution engine for small Python teams. The report includes a phased methodology from domain discovery through agentic TDD cycles, concrete implementation patterns using Pydantic v2 and dataclasses, CLAUDE.md configuration strategies, property extraction frameworks based on Wlaschin's seven patterns, guidance on when to use property-based vs. example-based tests, and Python project structure recommendations with essential tooling.

**Domain-Driven Development with AI Agents and Property-Based Testing**

````markdown
# Domain-driven development with AI agents and property-based testing

**The most effective Python development methodology for small teams using AI coding agents combines Domain-Driven Design as the structural foundation, Property-Based Testing as the verification backbone, and Claude Code as the execution engine.** This combination works because DDD makes domain logic explicit enough for AI agents to understand context deeply, PBT generates mathematically rigorous tests that catch edge cases no human would write, and Claude Code's agentic loop turns this structured context into high-quality code at unprecedented speed. Research from Anthropic, academic papers, and practitioner reports across English and Korean sources converge on a clear methodology: model your domain first, extract properties from invariants, then let AI agents implement against those properties in tight TDD cycles.

The approach rests on a key insight articulated by Eric Evans himself: **"A trained language model IS a bounded context."** When you feed an AI agent well-structured domain knowledge — ubiquitous language, aggregate boundaries, invariant rules — it generates code that respects your domain semantics rather than producing generic, architecturally incoherent output. Rod Johnson (creator of Spring) formalized this as DICE: Domain-Integrated Context Engineering.

---

## Why these three disciplines amplify each other

The synergy between DDD, PBT, and AI agents is not additive — it is multiplicative. Each discipline solves a weakness in the other two.

**DDD solves AI's context problem.** Without explicit domain models, AI agents "hallucinate APIs, violate architectural boundaries, and make incorrect assumptions about data flow." A semantic layer gives agents "the same system context your senior engineers have — the stuff they internalize over years." When "order" has a precise definition in your ubiquitous language, Claude Code generates `CustomerOrder` with `confirm_purchase_intent()` instead of generic `DataProcessor` with `handle_request()`. Research from Daniel Schleicher (January 2026) demonstrated that maintaining a living `domain-terms.md` glossary eliminates the ambiguity that causes AI to "amplify chaos."

**PBT solves AI's correctness problem.** TDFlow research showed that when provided human-written tests, AI agents achieve a **94.3% success rate** on SWE-Bench Verified — but only 69.8% when generating their own tests. The bottleneck is test quality, not code generation. Property-based tests are inherently higher quality than example-based tests for domain logic because they encode universal invariants ("balance must never go negative") rather than specific scenarios. Anthropic's own agentic PBT research demonstrated that AI-generated Hypothesis tests found real bugs in NumPy, SciPy, and AWS Lambda Powertools, with **86% validity rate** for top-scoring bug reports.

**AI agents solve DDD and PBT's productivity problem.** DDD is notoriously labor-intensive for small teams. PBT requires significant upfront thinking about properties. Claude Code collapses both costs: it can interview you about your domain, draft bounded context specifications, identify invariants from your domain models, generate Hypothesis strategies from Pydantic validators, and implement code against failing property tests — all within tight feedback loops. Boris Cherny (Claude Code team lead) confirmed that **Plan Mode alone yields 2-3x better results** for complex tasks.

---

## Phase 1: domain discovery and modeling

Every development cycle begins with domain modeling — before a single line of code or test exists. For small teams using Claude Code, this phase can be dramatically accelerated.

**Event storming with AI assistance.** Start by identifying domain events (things that happen), commands (things that trigger events), and aggregates (consistency boundaries). Tools like Qlerify can generate initial DDD workflows from text prompts, producing domain events, commands, and aggregate roots. Eric Evans participated in evaluating such tools and noted that "AI-generated models serve as a powerful starting point but require iterative refinement" — generic subdomains work well with AI generation, but core domains require more human involvement.

**Establish ubiquitous language as a living glossary.** Create a `docs/domain-terms.md` file that precisely defines every domain concept. This file serves dual purposes: it aligns the human team and it feeds AI agents with unambiguous context. The glossary should use this format:

```markdown
## Domain Terms
- **Order**: A customer commitment created at checkout. NOT a "request" or "reservation."
- **Reservation**: A temporary hold on inventory with a 15-minute TTL. Becomes an Order upon payment.
- **SKU**: Stock Keeping Unit — uniquely identifies a product variant (size + color + model).
- **Allocation**: The assignment of an OrderLine to a specific Batch, reducing available quantity.
```

**Define bounded contexts with clear boundaries.** Each bounded context becomes a self-contained Python package with its own domain layer, application layer, and infrastructure layer. For a small team, **two to four bounded contexts** is typical. Document the context map showing how contexts communicate — this becomes critical when AI agents work across boundaries.

**Use Claude Code's Plan Mode for domain discovery.** Start a session in Plan Mode and prompt:

> "I'm building a [system description]. Interview me about the core domain concepts, aggregate boundaries, invariants, and domain events. After the interview, write a domain model specification to docs/domain-model.md using DDD terminology."

Claude Code's `AskUserQuestion` tool enables this interactive discovery. The output specification becomes the foundation for all subsequent phases.

---

## Phase 2: encoding domain context for Claude Code

The CLAUDE.md file is the highest-leverage artifact in your entire development workflow. It transforms Claude Code from a generic code generator into a domain-aware development partner.

**Keep root CLAUDE.md under 200 lines.** Claude Code's system prompt wraps CLAUDE.md with a note that "this context may or may not be relevant" — meaning overly long instructions get uniformly degraded in attention. Frontier models can reliably follow approximately **150–200 total instructions**. Since Claude Code's built-in system prompt already contains ~50 instructions, your CLAUDE.md budget is roughly 100–150 lines of actionable directives.

**Use progressive disclosure for domain knowledge.** Instead of stuffing domain details into CLAUDE.md, create a `docs/` or `agent_docs/` directory and reference it:

```markdown
# Project: Warehouse Allocation System

## Tech Stack
Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2.0, Hypothesis

## Commands
- Test: `pytest --tb=short` | Type check: `mypy src/` | Lint: `ruff check src/`
- Single test: `pytest tests/unit/test_<module>.py -x -v`

## Architecture
DDD with hexagonal architecture. Bounded contexts in src/<context_name>/
- Domain layer has ZERO external dependencies (no SQLAlchemy, no FastAPI imports)
- See docs/domain-model.md for ubiquitous language and aggregate rules
- See docs/context-map.md for bounded context boundaries

## Development Workflow
1. ALWAYS write failing tests BEFORE implementation (Red-Green-Refactor)
2. Use property-based tests (Hypothesis) for domain invariants
3. Use example-based tests for specific edge cases and integration points
4. Run tests after EVERY code change
5. Never modify domain layer to accommodate infrastructure concerns

## Domain Rules (Critical)
- Available quantity can NEVER go negative
- Orders must ALWAYS have at least one OrderLine
- Allocations are idempotent — allocating the same line twice has no effect
```

**Subdirectory CLAUDE.md files map to bounded contexts.** Place context-specific rules in `src/ordering/CLAUDE.md`, `src/inventory/CLAUDE.md`, etc. These load only when Claude works in that directory — perfect for encoding aggregate-specific invariants without bloating the root file.

**Use Skills for reusable domain workflows.** Create `.claude/skills/domain-modeling/SKILL.md` and `.claude/skills/property-testing/SKILL.md` with YAML frontmatter defining when they activate. A PBT skill might specify: "When asked to test domain logic, always identify invariants first, then write Hypothesis property tests with custom strategies matching the aggregate's valid state space."

**Set up Hooks for automated guardrails.** Configure PostToolUse hooks to run tests after every file edit, and Stop hooks to run type checking and linting. As the HumanLayer team puts it: **"Never send an LLM to do a linter's job."** Deterministic quality gates belong in hooks, not in natural language instructions.

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write|MultiEdit",
      "command": "cd $PROJECT_DIR && python -m pytest tests/unit/ --tb=line -q 2>&1 | tail -5"
    }],
    "Stop": [{
      "command": "cd $PROJECT_DIR && mypy src/ --no-error-summary 2>&1 | tail -10"
    }]
  }
}
```

---

## Phase 3: extracting properties from domain models

The bridge between DDD and PBT is property extraction — the process of identifying universal invariants from your domain models that become executable tests. This is where the methodology produces its greatest value. Domain constraints expressed in pydantic validators, aggregate business rules, and value object definitions **directly map** to Hypothesis properties.

**Scott Wlaschin's seven property patterns** form the canonical framework for identifying testable properties. Applied to DDD domain models:

1. **"Different paths, same destination"** (commutativity) — allocating OrderLine A then B produces the same available quantity as allocating B then A.
2. **"There and back again"** (round-trip) — serializing then deserializing a Value Object yields an equal object. Every `model_dump()` / `model_validate()` pair should round-trip.
3. **"Some things never change"** (invariants) — after any valid operation on an aggregate, its invariants still hold. Available quantity stays non-negative. Order always has at least one item.
4. **"The more things change, the more they stay the same"** (idempotence) — allocating the same OrderLine twice has no additional effect. Processing the same domain event twice is safe.
5. **"Solve a smaller problem first"** (induction) — if a property holds for individual OrderLines, it holds for the full Order.
6. **"Hard to prove, easy to verify"** — computing a discount is complex, but verifying that the discounted price plus the discount amount equals the original price is trivial.
7. **"The test oracle"** — compare an optimized calculation against a naive but obviously correct reference implementation.

**Extract properties systematically from DDD artifacts.** Every pydantic `@field_validator` and `@model_validator` encodes an invariant that should hold for ALL valid instances — this is already a property. Every aggregate business rule expressed as a method precondition ("cannot allocate if insufficient quantity") maps to a property test. The pattern is mechanical:

| DDD Artifact | Property Type | Hypothesis Pattern |
|---|---|---|
| Value Object constructor validation | Type-level invariant | `@given(st.builds(Money))` → assert constraints |
| Aggregate business rule | Invariant preservation | `@given(valid_aggregate())` → perform operation → assert rule holds |
| Domain event handling | Idempotence | Apply event twice → state unchanged after second |
| Entity identity | Persistence through mutation | Mutate entity → identity unchanged |
| Bounded context serialization | Round-trip | `serialize(deserialize(x)) == x` |

**Use Claude Code to assist property extraction.** In a dedicated session, prompt: "Read docs/domain-model.md and src/ordering/domain/. For each aggregate and value object, identify all invariants that should hold as properties. List them in docs/properties.md using the format: [Aggregate] — [Property name] — [Property type from Wlaschin's categories] — [Natural language description]." Then in a separate session, generate the actual Hypothesis tests from this property list.

---

## When to use property-based tests versus example-based tests

The methodology is explicitly hybrid. Not every piece of code benefits from PBT, and forcing properties onto simple CRUD operations wastes effort. The decision framework:

**Use property-based tests when** the code has clear mathematical or business invariants ("for all valid X, property Y holds"), when there are complex parameter interactions that create combinatorial explosion (more than 10⁵ possible input combinations), when round-trip operations exist (serialization, encoding, conversion), when operations should be idempotent or commutative, and when the domain model has rich aggregate rules. Domain logic is PBT's sweet spot.

**Use example-based TDD when** you need to document specific known edge cases by name, when testing simple input-output mappings (CRUD operations), when behavior depends on specific external scenarios (API mocking), when the property assertion would effectively re-implement the function under test, and when testing integration points with infrastructure. Simple glue code is TDD's sweet spot.

**The practical hybrid pattern** follows Property-Driven Development: start with a concrete example test (TDD-style) to establish basic behavior, then promote it to a property by generalizing the assertion, then use the property to drive further implementation. As Johannes Link (jqwik creator) recommends: **"Start with an example first, then promote it to a property."** You end up with more concise tests AND more confidence.

Configure Hypothesis profiles for different environments: `max_examples=50` for local development (fast feedback), `max_examples=500` for CI (thorough), and `max_examples=10000` for nightly builds (exhaustive). This ensures PBT doesn't slow down the inner development loop while still providing comprehensive coverage in CI.

```python
from hypothesis import settings, HealthCheck
settings.register_profile("dev", max_examples=50, deadline=400)
settings.register_profile("ci", max_examples=500, deadline=None)
settings.register_profile("nightly", max_examples=10000, deadline=None,
                          suppress_health_check=[HealthCheck.too_slow])
```

---

## The agentic TDD cycle with Claude Code

The core development loop combines Red-Green-Refactor TDD with Claude Code's agentic capabilities. Research consistently shows that **TDD is not optional with AI agents — it is essential**. As one practitioner stated: "Tests are deterministic. Agents are not." Tests become the cage that constrains non-deterministic AI output into correct behavior.

**The TDAD paper (2026) revealed a critical insight**: telling AI agents HOW to do TDD actually increased regressions by 63% compared to baseline. What works is telling agents WHICH tests to check. The methodology therefore focuses on providing Claude Code with explicit test targets rather than procedural TDD instructions.

### Step 1: Write failing property tests (RED)

Start a new Claude Code session explicitly scoped to test writing:

> "Read docs/domain-model.md and docs/properties.md. Write failing Hypothesis property tests for the Money value object covering: non-negative amounts, currency format validation, addition commutativity, and serialization round-trip. Use custom strategies matching domain constraints. Do NOT write any implementation code."

Claude Code writes the tests, runs them, confirms they fail. Commit the failing tests.

```python
@st.composite
def valid_money(draw):
    amount = draw(st.decimals(min_value=Decimal("0"), max_value=Decimal("999999.99"),
                               places=2))
    currency = draw(st.sampled_from(["USD", "EUR", "GBP", "KRW"]))
    return Money(amount=amount, currency=currency)

@given(m1=valid_money(), m2=valid_money())
def test_money_addition_is_commutative(m1, m2):
    assume(m1.currency == m2.currency)
    assert m1 + m2 == m2 + m1

@given(money=valid_money())
def test_money_roundtrip_serialization(money):
    serialized = money.model_dump()
    deserialized = Money.model_validate(serialized)
    assert deserialized == money
```

### Step 2: Implement minimally (GREEN)

Start a **new session** (critical — prevents context pollution between test-writing and implementation):

> "Read the failing tests in tests/unit/test_money.py. Implement the minimum domain code in src/ordering/domain/value_objects.py to make all tests pass. Do NOT modify any test files."

Claude Code enters its agentic loop: write code → run tests → read failures → adjust → repeat. The tests act as an unambiguous specification. Commit when green.

### Step 3: Refactor with confidence (REFACTOR)

> "All tests are green. Refactor src/ordering/domain/value_objects.py for clarity and adherence to DDD patterns. Tests must stay green after every change."

### Step 4: Add example-based edge cases

> "Add example-based tests for known edge cases: zero-amount money, maximum precision decimals, currency mismatch errors. These complement the existing property tests."

**Context isolation matters.** The alexop.dev team documented a compelling architecture using separate Claude Code subagents (`.claude/agents/`) for each TDD phase — a test-writer agent with no implementation knowledge, an implementer that sees only failing tests, and a refactorer with fresh evaluation context. This prevents the "cheating" problem where an LLM's test-writing is unconsciously influenced by its implementation planning.

For teams wanting automated enforcement, the **tdd-guard** tool (github.com/nizos/tdd-guard) uses Claude Code hooks to intercept file modifications and block implementation when no relevant failing test exists, supporting pytest out of the box.

---

## Python implementation patterns and tooling

### Value objects with pydantic v2

Use `frozen=True` for immutability and validators for domain invariants. For single-field value objects, prefer `RootModel` over `BaseModel` — it acts as a transparent wrapper that integrates cleanly with FastAPI:

```python
from pydantic import BaseModel, ConfigDict, Field, RootModel, model_validator
from decimal import Decimal

class Money(BaseModel):
    model_config = ConfigDict(frozen=True)
    amount: Decimal = Field(ge=0, decimal_places=2)
    currency: str = Field(min_length=3, max_length=3)

    def __add__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise CurrencyMismatchError(self.currency, other.currency)
        return Money(amount=self.amount + other.amount, currency=self.currency)

class EmailAddress(RootModel):
    root: str
    model_config = ConfigDict(frozen=True)

    @model_validator(mode="before")
    @classmethod
    def validate_email(cls, v):
        if "@" not in v or "." not in v.split("@")[1]:
            raise ValueError("Invalid email format")
        return v.lower()
```

### Entities and aggregates with dataclasses

Keep the domain layer free of framework dependencies. Use `dataclasses` for entities and aggregates, reserving pydantic for API boundaries:

```python
from dataclasses import dataclass, field
from typing import Set

@dataclass(eq=False)
class Batch:
    reference: str
    sku: str
    purchased_quantity: int
    eta: date | None
    _allocations: Set[OrderLine] = field(default_factory=set, repr=False)

    def __eq__(self, other):
        return isinstance(other, Batch) and self.reference == other.reference

    def __hash__(self):
        return hash(self.reference)

    @property
    def available_quantity(self) -> int:
        return self.purchased_quantity - sum(l.qty for l in self._allocations)

    def allocate(self, line: OrderLine) -> None:
        if not self.can_allocate(line):
            raise CannotAllocateError(line, self)
        self._allocations.add(line)

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty
```

### Hypothesis strategies for pydantic v2

Since pydantic v2 removed the built-in Hypothesis plugin, use these workarounds:

- **`st.builds()`** works by inspecting `__signature__` — suitable for simple models
- **`@st.composite`** for models with cross-field validators or complex constraints
- **`hypothesis-jsonschema`** for schema-based generation via `model_json_schema()`
- **Factory classmethods** for models where random generation frequently violates validators

For the most direct DDD-to-PBT bridge, consider **icontract + icontract-hypothesis**: decorating domain classes with `@icontract.invariant`, `@icontract.require`, and `@icontract.ensure` automatically generates Hypothesis strategies from contracts — zero additional test code required. The CLI command `icontract_hypothesis ghostwrite --path my_module.py` produces ready-to-run test files.

### Stateful testing for aggregate lifecycles

Hypothesis's `RuleBasedStateMachine` maps directly to aggregate state machines. Define rules as domain operations, invariants as aggregate business rules, and preconditions as operation guards:

```python
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant, precondition

class BatchAllocationMachine(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.batch = Batch("batch-001", "WIDGET", 100, eta=date.today())
        self.allocated_qty = 0

    @rule(qty=st.integers(min_value=1, max_value=20))
    def allocate_line(self, qty):
        line = OrderLine(f"order-{qty}", "WIDGET", qty)
        if self.batch.can_allocate(line):
            self.batch.allocate(line)
            self.allocated_qty += qty

    @invariant()
    def available_quantity_never_negative(self):
        assert self.batch.available_quantity >= 0

    @invariant()
    def quantities_are_consistent(self):
        assert self.batch.available_quantity == 100 - self.allocated_qty
```

### Recommended project structure

Organize by bounded context with hexagonal architecture. Not every context needs full hexagonal treatment — use it for complex domains, keep simple CRUD contexts lightweight:

```
src/
├── ordering/                    # Complex domain → full DDD
│   ├── domain/
│   │   ├── model.py            # Entities, Aggregates, Value Objects
│   │   ├── events.py           # Domain events
│   │   └── exceptions.py
│   ├── application/
│   │   ├── services.py         # Use cases
│   │   └── unit_of_work.py
│   ├── infrastructure/
│   │   └── repository.py
│   └── CLAUDE.md               # Context-specific AI instructions
├── catalog/                     # Simple domain → lightweight CRUD
│   ├── models.py
│   ├── routes.py
│   └── CLAUDE.md
├── shared_kernel/
│   └── value_objects.py        # Money, EmailAddress, etc.
docs/
├── domain-model.md
├── domain-terms.md
├── context-map.md
└── properties.md
tests/
├── unit/
│   ├── test_money_properties.py      # PBT
│   ├── test_batch_properties.py      # PBT
│   └── test_batch_examples.py        # Example-based edge cases
├── integration/
└── conftest.py                       # Shared Hypothesis strategies
```

### Essential libraries

The Python ecosystem provides solid DDD and PBT tooling. For domain modeling, **pydantic v2** handles value objects and API boundaries while **dataclasses** keep the domain layer framework-free. The **eventsourcing** library (v9.5+) provides aggregate base classes with event sourcing if needed. For testing, **Hypothesis** (v6.x) with **pytest** is the standard PBT stack, complemented by **hypothesis-jsonschema** for schema-based generation and **polyfactory** for test fixture generation. For design-by-contract, **icontract** with **icontract-hypothesis** provides the most automated DDD-to-PBT bridge available.

---

## Adapting the methodology to project complexity

The AWS AI-DLC framework, extensively documented in both Korean and English sources, advocates that workflow depth should scale with project complexity. A lightweight utility doesn't need full DDD with event storming; a complex domain-heavy service does.

For **personal projects and prototypes**, compress the methodology: write a brief domain glossary in CLAUDE.md, identify the top three invariants for your core aggregate, write property tests for those invariants, and let Claude Code implement against them. The entire domain modeling phase might take 30 minutes.

For **small team production systems**, follow the full five-phase cycle. Korean fintech company Hyperithm recommends using Git Worktree to run parallel Claude Code sessions — one for bug fixes, one for feature development — each with separate context and CLAUDE.md awareness. Multiple Korean tech companies including Toss and 아임웹 now provide Claude Code Max to all engineers, treating AI tool proficiency as a core development skill.

A key lesson from Korean practitioner blogs: even for personal projects, **establish domain models before letting AI generate code**. One developer documented four months of "vibe coding" without structure that produced unmanageable code with documentation that diverged from implementation. Adopting DDD domain modeling in the construction phase immediately solved the structural decay problem.

---

## Conclusion

This methodology transforms three traditionally separate disciplines into a unified development workflow with a clear execution path: **model the domain explicitly, extract invariants as testable properties, then let AI agents implement against those properties in disciplined TDD cycles.** The combination works because each element addresses the others' blind spots — DDD gives AI agents the semantic precision to generate correct code, PBT provides mathematically rigorous verification that catches what example-based tests miss, and Claude Code's agentic loop collapses the labor cost that historically made DDD and PBT prohibitive for small teams.

Three non-obvious insights emerged from the research. First, the TDD prompting paradox: telling AI agents *how* to do TDD actually worsens results, but telling them *which tests to verify* improves results dramatically — structure the workflow around explicit test targets, not procedural instructions. Second, context isolation between test-writing and implementation is critical; use separate Claude Code sessions or subagents for each TDD phase to prevent the model from "cheating" by letting implementation knowledge leak into test design. Third, the **icontract + icontract-hypothesis** combination may be the most underutilized tool in this stack — design-by-contract decorators on domain classes automatically generate both runtime enforcement and Hypothesis test strategies, eliminating the manual property extraction step entirely.

The methodology is deliberately practical over theoretical. Start with a domain glossary and three invariants for your most important aggregate. Write property tests for those invariants. Let Claude Code implement. You will have a working, well-tested domain model in hours, not weeks — and a foundation that scales as your system grows.
````



## Prompt:
2026. 3. 24. 오후 3:04:47

> File: 

비교적 가벼운 서비스를 DDD + AI agent 기반으로 개발·확장하려고 해.

요구사항은 다음과 같아:

1. 목표
   - 기초적인 객체 지향 원칙(캡슐화, 불변 Value Object 등)을 지키는 선에서,
   - DDD가 불필요한 복잡함을 가중하지 않도록 **경량 DDD**로 적용하고 싶어.

2. DDD 적용 범위에 대한 생각
   - DDD가 제안하는 모든 전통적인 패턴/형식을 완전히 따르기보다는,
   - 에이전트가 다음 정보를 활용할 수 있을 정도까지만 도입하고 싶어:
     - 도메인 모델 정보 (모델 간 관계)
     - 주요 도메인 이벤트
     - 핵심 제약사항/불변식

3. AI agent에게 원하는 역할
   - 기존 도메인 모델/문서(예: 모델 정의, 이벤트 목록, 제약사항 목록)를 읽고,
   - 그 위에서:
     - 새로운 도메인 이벤트나 서브도메인 도입 제안
     - 도메인 규칙에서 Property를 추출하고 PBT 템플릿/테스트를 생성
   - 이때, DDD 형식을 과하게 강제하지 않고,
     - “새 이벤트/도메인 도입”에 필요한 컨텍스트를 충분히 활용하되
     - 전체 구조가 과도하게 복잡해지지 않도록 가이드해 줬으면 좋겠어.

4. 출력/결과물에 대한 기대
   - “어떤 DDD 요소를 어디까지 도입할지”에 대한 단계별/점진적 제안
   - 각 단계에서:
     - 도입해야 할 도메인 모델/이벤트/불변식 정리
     - Property 기반 테스트로 뽑을 부분 vs 예제 기반 TDD로 남길 부분 구분



## Response:
2026. 3. 24. 오후 3:05:12

````plaintext
Thought process: 경량 DDD와 AI 에이전트 워크플로우 문서 구성 계획했음.

The user wants a lightweight DDD methodology tailored for a relatively simple service, combined with AI agent-assisted development. They've provided a detailed document about a "DDD-first + selective PBT/TDD + eval-governed agent workflow" methodology, and now want me to adapt it to their specific needs:

1. Lightweight DDD - not full-blown DDD, just enough for AI agents to understand context
2. AI agent should read domain models/docs and suggest new events, extract properties for PBT
3. Gradual/phased approach to introducing DDD elements
4. Clear routing between PBT and TDD

They're using Claude Code + Python for a small/personal project.


I'll structure a practical methodology guide that covers the philosophy behind lightweight DDD, which elements to actually adopt versus skip, how to organize the context documents for AI agents, the property extraction workflow for routing between PBT and TDD, and concrete examples they can follow with Claude Code.
````

좋은 방향이에요. 첨부해 주신 운영모델 문서의 핵심 원칙들을 살리면서, "가벼운 서비스"에 맞는 경량 버전으로 재설계하겠습니다. 먼저 전체 방법론의 흐름을 시각적으로 정리한 뒤, 실행 가능한 가이드 문서를 만들어 드릴게요.

````plaintext
Tool: read_me
````

````plaintext
Thought process: 경량 DDD와 AI 에이전트 흐름도 설계 중입니다.

Now I have the design system loaded. Let me create a comprehensive visual diagram showing the methodology flow, then create the detailed guide document.

Let me think about the best approach:

1. First, I'll create a visual diagram showing the lightweight DDD + AI agent workflow
2. Then create a comprehensive markdown document with the full methodology

Let me design the diagram first - it should show the phased approach from domain modeling to implementation, with the PBT/TDD routing decision.
````

먼저 경량 DDD + AI agent 개발 흐름의 전체 구조를 시각적으로 정리해



## Prompt:
2026. 3. 24. 오후 3:05:45

첨부한 문서는 무시해도 좋아.



## Response:
2026. 3. 24. 오후 3:09:37

````plaintext
Thought process: 사용자 요구사항 재검토 후 DDD 방법론 구축 계획.

The user wants me to ignore the attached document and focus on their requirements for a lightweight DDD + AI agent development methodology. Let me re-read their requirements:

1. Lightweight DDD - basic OOP principles (encapsulation, immutable Value Objects), without unnecessary complexity
2. DDD scope - just enough for the agent to use: domain model info (relationships), key domain events, core constraints/invariants
3. AI agent role - read existing domain models/docs, suggest new events/subdomains, extract properties for PBT, generate tests
4. Output - step-by-step proposal for DDD adoption, with PBT vs TDD routing at each step


5. They want a comprehensive methodology guide with a visual flow diagram and detailed documentation to walk through the entire approach.
````

알겠습니다! 첨부 문서는 무시하고, 앞서 리서치한 내용과 요구사항을 바탕으로 경량 DDD + AI agent 개발 방법론을 설계해 드릴게요. 먼저 전체 흐름을 시각화하겠습니다.

````plaintext
Tool: show_widget
````

````plaintext
Thought process: 사용자 요청을 무시하고 포괄적 방법론 문서를 구성했다.

Now let me create the comprehensive methodology document. The user wants:
1. Lightweight DDD (not full-blown)
2. AI agent reads domain docs and proposes extensions
3. Property extraction from constraints → PBT
4. TDD for simpler parts
5. Step-by-step, progressive adoption guide

Let me create a detailed markdown document covering all of this.
````

이 흐름의 각 단계를 실행 가능한 수준의 가이드 문서로 만들겠습니다.

````plaintext
View: Check the docx skill for creating a Word document
````

````plaintext
Thought process: 사용자 요청 무시하고 문서 작성 계획 수립.

The user wants a methodology document. Given the complexity and length, I should create a markdown file that renders nicely. Let me create a comprehensive but practical guide.
````

````plaintext
Create File: Creating comprehensive lightweight DDD + AI agent development methodology guide
````

````plaintext
Thought process

Now let me present this file to the user.
````

````plaintext
Present File: /home/claude/lightweight-ddd-ai-methodology.md
````

````plaintext
Thought process: 문서 제시를 인지하고 간결한 요약 준비했다.

Good, the file is presented. Let me give a concise summary.
````

방법론 가이드 문서를 만들었습니다. 핵심 구조를 요약하면 이렇습니다.

**도입하는 DDD 요소는 딱 4가지**로 제한했습니다: 용어집, 모델 관계도, 도메인 이벤트, 제약사항. Bounded Context 분리, Aggregate Root 패턴, Repository 같은 무거운 요소는 모두 제외했고, "이 구조가 없으면 AI가 잘못된 코드를 생성하는가?"를 판단 기준으로 삼았습니다.

**PBT/TDD 라우팅은 4문항 판단**으로 자동화됩니다. 제약사항 하나마다 "일반 명제로 표현 가능한가? 입력 공간이 넓은가? 반례가 유의미한가? 독립 검증이 가능한가?"에 답하면, 3개 이상 Yes면 PBT, 1개 이하면 TDD, 2개면 Mixed로 나뉩니다.

**AI agent의 역할은 3단계로 구분**됩니다. Property 추출(제안) → 테스트 작성 → 구현, 각 단계 사이에 사람의 승인 지점이 있어서 AI가 과도하게 구조를 복잡하게 만드는 것을 방지합니다. 특히 테스트 작성과 구현은 별도 Claude Code 세션에서 수행해 컨텍스트 오염을 막습니다.

궁금한 부분이 있거나, 실제 프로젝트에 맞춰 조정하고 싶은 부분이 있으면 말씀해 주세요.

> File: /home/claude/lightweight-ddd-ai-methodology.md



## Prompt:
2026. 3. 24. 오후 3:33:17

이전 답변처럼 단순함을 유지하되, 도메인 모델이 복잡해지는 상황 속에서도 확장이 가능하도록 유연하게 설계되었으면 좋겠어.
일례로, 복잡한 도메인 모델 속에서도
- Agent가 필요한 컨텍스트를 효율적으로 추출할 수 있도록 도메인 모델이 구조화되어 있는지,
- 적절한 Property를 추출할 수 있는지,
- 기존의 도메인 모델 내용을 잘 파악할 수 있도록 구조화되어 있는지 등
확장의 여지가 있는 부분들을 다음 기준으로 검토해줘.
1. 현재 제안된 경량 DDD + AI agent 방법론 문서(`Lightweight ddd ai methodology`)에서
   - 구조적으로 확장에 취약한 부분
   - 도메인 복잡도가 올라갈 때 병목이 될 부분
2. 위 취약 지점을 보완하기 위한
   - 구체적인 폴더/파일 구조 개선 제안
   - 도메인 문서 작성/갱신 규칙
   - Agent가 컨텍스트를 로드/필터링하는 절차



## Response:
2026. 3. 24. 오후 3:37:52

````plaintext
Thought process: 경량 DDD 방법론의 확장성 약점을 진단하고 개선안을 설계했다.

The user wants me to review the previously created lightweight DDD + AI agent methodology document for scalability weaknesses, and propose concrete improvements that maintain simplicity while allowing extension as domain complexity grows. Let me analyze the document carefully and identify structural vulnerabilities.

Key areas to examine:
1. Structural weaknesses when domain complexity increases
2. Bottlenecks as domain models grow
3. Concrete folder/file structure improvements
4. Domain document writing/update rules
5. Agent context loading/filtering procedures

Let me think deeply about this...

Main weaknesses I can identify:

1. **Flat docs/ structure** - All domain docs in a single directory with no hierarchy. When models grow to 50+ entities, models.md becomes unmanageable. 

The agent has to load entire files even when working on a small feature, and there's no way to scope context to just the relevant models and constraints for a given task. As the domain grows, scanning through hundreds of rules to find what's actually applicable becomes increasingly noisy and inefficient.

2. **No model dependency graph** - The text-based relation notation in models.md doesn't scale well when models are deeply interconnected, making it hard for the agent to understand which models are affected by a change.

3. **No versioning or change tracking** - There's no mechanism to track how domain rules evolve over time, which becomes critical when multiple features are being developed concurrently.

4. **Properties catalog is flat** - properties.md grows linearly with no grouping by domain area, making it harder to navigate as it expands.

5. **All-or-nothing context loading** - The agent either loads everything or nothing, with no intermediate summary-to-detail hierarchy that would let it progressively load more context as needed.

I'm thinking about a "zoom-in" architecture where domain documents have an index or summary at the top level that gives the agent a map of what's available, then it can drill into specific areas based on the task. This maintains simplicity for small projects while scaling gracefully as the domain grows.

The key improvements would be a lightweight domain index summarizing all models and their relationships, moving constraints to live alongside the models they govern rather than in one monolithic file, tagging sections with scope identifiers so the agent can filter what it needs, making dependency relationships explicit in the models file, and organizing everything into a hierarchical structure that flows from summary down to granular details.
````

좋은 관점이에요. 현재 문서를 "도메인이 50개 이상의 모델로 성장했을 때"라는 렌즈로 재검토하겠습니다.

먼저 취약 지점을 분석한 뒤, 개선안을 하나의 보완 문서로 정리해 드릴게요.

````plaintext
View: Re-read the methodology to identify specific weak points
````

````plaintext
Thought process: 도메인 확장성 약점을 진단하고 ID 기반 상호참조로 보완하는 방안을 구상했다.

Now let me analyze the weaknesses systematically and create a comprehensive improvement document. Let me think about what breaks when the domain grows complex:

1. **Flat docs/ structure** - models.md becomes a 500-line monster. Agent has to load ALL models even when working on one feature.
2. **No dependency/impact tracking** - When changing Money, which constraints/events/properties are affected? No way to trace.
3. **Single constraints.md** - 100+ constraints in one file makes property extraction noisy.
4. **No scoping mechanism** - CLAUDE.md says "read all docs" with no way to filter by relevance.


5. **properties.md as flat file** - Property catalog grows unbounded.
6. **No model-to-model relationship graph** - Text-based "1 --- *" doesn't scale.
7. **events.md lacks cross-references** - Events don't link back to which models/constraints they relate to.
8. **No changelog/versioning** - When docs change, agent doesn't know what's new.

The core solution is introducing cross-referencing through IDs—every artifact gets a unique identifier and references others by ID, creating a navigable graph the agent can traverse selectively rather than loading everything at once.

Now I'm thinking about how to frame this as a scaling supplement that extends the existing methodology without replacing it.
````

````plaintext
Tool: show_widget
````

````plaintext
Thought process: 설계 원칙과 구체적 개선안을 체계화했다.

Now let me create the detailed improvement document. I need to be very specific about:
1. What's weak and why
2. Concrete file/folder structure changes
3. Document writing rules
4. Agent context loading procedure

The key design principle: everything gets an ID, everything cross-references. The agent loads a lightweight index first, then zooms into only what's needed.
````

이제 취약 지점별 구체적인 개선안을 하나의 보완 문서로 작성하겠습니다.

````plaintext
Create File: Creating the scalability supplement document with concrete improvements
````

````plaintext
Thought process

Now let me present the file to the user.
````

````plaintext
Present File: /home/claude/scalability-supplement.md
````

````plaintext
Thought process: 경량 DDD 방법론의 확장성 취약점을 분석했다.

Good, the file has been presented. Let me give a concise summary of the key improvements.
````

확장성 보완 가이드를 정리했습니다. 핵심 변경 사항을 간추리면 이렇습니다.

**취약 지점 4가지**를 식별했습니다. 평탄한 문서 구조(agent가 전부 로드), 교차 참조 부재(변경 영향도 추적 불가), 컨텍스트 스코핑 부재(토큰 낭비), 변경 추적 부재(문서-코드 괴리)입니다.

**해결의 핵심은 ID 기반 교차 참조**입니다. 모든 모델(`E-01`), 제약사항(`INV-01`), 이벤트(`EV-01`), Property(`P-001`)에 고유 ID를 부여하고, 각 항목에 `refs:` 줄로 연결된 ID를 명시합니다. 이것만으로 agent가 "Money를 수정하면 INV-03, FMT-02, P-003을 확인해야 한다"를 즉시 파악할 수 있습니다. 기존 파일 구조를 바꾸지 않고도 적용 가능합니다.

**파일 분리는 점진적**으로 합니다. 모델 15개까지는 현재 평탄한 구조에 ID만 추가, 15~40개면 `index.md` + 영역별(`@order`, `@inventory`) 파일 분리, 40개 이상이면 모델당 하나의 카드 파일로 전환합니다.

**Agent 로딩은 3단계 프로토콜**을 따릅니다. `index.md`로 전체 지도 파악 → 작업 영역의 상세 파일만 로드 → 관련 코드/테스트 확인. CLAUDE.md에 "docs/ 전체를 한 번에 읽지 않는다"를 명시하여 불필요한 컨텍스트 로딩을 방지합니다.

**가장 먼저 할 것 두 가지**: 기존 docs/ 파일에 ID와 refs 추가 (비용 최소), 그 다음 `index.md` 작성. 이 두 가지만으로 4개 취약 지점의 대부분이 해소됩니다.

> File: /home/claude/scalability-supplement.md



## Prompt:
2026. 3. 24. 오후 5:49:16

multi agent architecture(Claude Code, Gemini, Codex)를 기반으로, 정리한 “DDD + Property-based testing 기반 AI agent 개발 방법론”을 구현하고 싶습니다.

1. 이 방법론을 구현하기 위한 전체 워크플로우를 의미 있는 작업 단위로 나누고,
2. 각 작업 단위를 가장 잘 수행할 수 있는 에이전트(Claude Code, Gemini, Codex)를 역할과 이유와 함께 작성해주세요.



## Response:
2026. 3. 24. 오후 5:54:38

````plaintext
Thought process: 방법론을 작업 단위로 분해하고 에이전트 역할 배정 검토.

The user wants to design a multi-agent architecture using Claude Code, Gemini, and Codex to implement their DDD + PBT methodology. I need to:

1. Break the methodology into meaningful work units
2. Assign the best agent for each unit with reasoning

Let me first research the current capabilities of each agent to make accurate assignments.
````

좋은 질문이에요. 각 에이전트의 최신 특성을 정확히 파악한 뒤 워크플로우를 설계해야 하니, 먼저 현재 시점의 각 에이전트 역량을 조사하겠습니다.

````plaintext
Web Search: Claude Code 2026 capabilities agentic coding features
````

> **Claude Code overview - Claude Code Docs** [claude.com](https://code.claude.com/docs/en/overview)
>
> **Claude Code Is Changing How We Build Software In 2026** [medium.com](https://medium.com/techtrends-digest/claude-code-is-changing-how-we-build-software-in-2026-cba4a800297e)
>
> **GitHub - anthropics/claude-code: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands. · GitHub** [github.com](https://github.com/anthropics/claude-code)
>
> **2026 Agentic Coding Trends Report How coding agents are reshaping** [anthropic.com](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf?hsLang=en)
>
> **Optimizing Agentic Coding: How to Use Claude Code in 2026?** [aimultiple.com](https://aimultiple.com/agentic-coding)
>
> **What is Claude Code in 2026?** [techjacksolutions.com](https://techjacksolutions.com/ai/coding/what-is-claude-code-2/)
>
> **Claude Code Edges OpenAI's Codex in VS Code's Agentic AI Marketplace Leaderboard -- Visual Studio Magazine** [visualstudiomagazine.com](https://visualstudiomagazine.com/articles/2026/02/26/claude-code-edges-openais-codex-in-vs-codes-agentic-ai-marketplace-leaderboard.aspx)
>
> **Claude Code by Anthropic | AI Coding Agent, Terminal, IDE** [claude.com](https://claude.com/product/claude-code)
>
> **Claude Code Complete Guide 2026: From Zero to Hero - ClaudeWorld** [claude-world.com](https://claude-world.com/articles/claude-code-complete-guide-2026/)
>
> **5 Ways Claude Code Is Changing How Digital Agencies Work in 2026** [adventureppc.com](https://www.adventureppc.com/blog/5-ways-claude-code-is-changing-how-digital-agencies-work-in-2026)
>
````plaintext
Thought process

Good, now let me search for Codex and Gemini CLI capabilities.
````

````plaintext
Web Search: OpenAI Codex CLI 2026 capabilities autonomous coding agent
````

> **CLI – Codex | OpenAI Developers** [openai.com](https://developers.openai.com/codex/cli)
>
> **Introducing Codex | OpenAI** [openai.com](https://openai.com/index/introducing-codex/)
>
> **Codex | AI Coding Partner from OpenAI | OpenAI** [openai.com](https://openai.com/codex/)
>
> **OpenAI Codex App: A Guide to Multi-Agent AI Coding | IntuitionLabs** [intuitionlabs.ai](https://intuitionlabs.ai/articles/openai-codex-app-ai-coding-agents)
>
> **GitHub - openai/codex: Lightweight coding agent that runs in your terminal · GitHub** [github.com](https://github.com/openai/codex)
>
> **Introducing the Codex app | OpenAI** [openai.com](https://openai.com/index/introducing-the-codex-app/)
>
> **Claude Code vs OpenAI Codex: which is better in 2026? | Blog — Northflank** [northflank.com](https://northflank.com/blog/claude-code-vs-openai-codex)
>
> **What Is OpenAI Codex? The Guide to AI-Powered Coding (2026)** [deepstation.ai](https://deepstation.ai/blog/what-is-openai-codex-the-guide-to-ai-powered-coding-2026)
>
> **Codex | OpenAI Developers** [openai.com](https://developers.openai.com/codex)
>
> **ChatGPT Codex Review 2026: OpenAI's $20 AI Coding Agent That Runs 7+ Hour Tasks (Better Than Claude Code?) - AI Tool Analysis** [aitoolanalysis.com](https://aitoolanalysis.com/chatgpt-codex-review/)
>
````plaintext
Thought process

Now let me search for Gemini CLI capabilities.
````

````plaintext
Web Search: Gemini CLI 2026 agentic coding capabilities features
````

> **GitHub - google-gemini/gemini-cli: An open-source AI agent that brings the power of Gemini directly into your terminal. · GitHub** [github.com](https://github.com/google-gemini/gemini-cli)
>
> **Use the Gemini Code Assist agent mode | Google for Developers** [google.com](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer)
>
> **Google Gemini CLI: The 2026 Most Powerful Open-Source AI Terminal Agent That's Changing How Developers Code Forever** [vision.pk](https://vision.pk/google-gemini-cli-complete-guide/)
>
> **Google announces Gemini CLI: your open-source AI agent** [blog.google](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-open-source-ai-agent/)
>
> **Gemini Code Assist | AI coding assistant** [codeassist.google](https://codeassist.google/)
>
> **Gemini CLI documentation | Gemini CLI** [geminicli.com](https://geminicli.com/docs/)
>
> **Gemini CLI: Code & Create with an Open-Source Agent - DeepLearning.AI** [deeplearning.ai](https://learn.deeplearning.ai/courses/gemini-cli-code-and-create-with-an-open-source-agent/information)
>
> **Agentic Coding in Xcode with Gemini CLI** [peterfriese.dev](https://peterfriese.dev/blog/2026/agentic-coding-xcode-geminicli/)
>
> **Set up your coding agent | Gemini API | Google AI for Developers** [google.dev](https://ai.google.dev/gemini-api/docs/coding-agents)
>
> **Gemini 3 Flash is now available in Gemini CLI - Google Developers Blog** [googleblog.com](https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/)
>
````plaintext
Thought process: 세 에이전트의 특성을 분석하고 DDD 워크플로우 설계를 구상했습니다.

Now I have a good understanding of all three agents. Let me create the multi-agent architecture document.

Key characteristics:
- **Claude Code**: Terminal-first, deep autonomous work, subagents, CLAUDE.md context, hooks, plan mode, agent teams, MCP support. Best for complex reasoning, long-running autonomous tasks, deep codebase understanding.
- **Codex**: Cloud sandboxes for parallel tasks, CLI for local, AGENTS.md/Skills, interactive steering, worktrees, GitHub integration, automations. Best for parallel task delegation, CI/CD integration, code review.
- **Gemini CLI**: 1M token context, free tier generous, GEMINI.md, open-source, Google Search grounding, MCP, plan mode, subagents, model routing. 

Best for large context analysis, web-grounded research, cost-effective bulk operations. Now I'm designing the multi-agent workflow for the DDD + PBT methodology.
````

리서치가 완료됐습니다. 각 에이전트의 2026년 현재 특성을 파악했으니, 방법론의 각 작업 단위에 최적의 에이전트를 배정하겠습니다.

````plaintext
Tool: show_widget
````

````plaintext
Thought process: 종합 문서 작성을 준비했습니다.

Now let me create the comprehensive document.
````

이제 각 Phase의 구체적인 역할 배정과 근거를 문서로 정리합니다.

````plaintext
Create File: Creating comprehensive multi-agent architecture guide for DDD + PBT methodology
````

````plaintext
Thought process

The file is created, let me present it to the user.
````

````plaintext
Present File: /home/claude/multi-agent-architecture.md
````

````plaintext
Thought process: 다중 에이전트 아키텍처 기반 방법론 구현 계획 수립했습니다.

Done. Let me summarize the key points for the user.
````

문서를 정리했습니다. 핵심 배정 논리를 요약하면 이렇습니다.

**세 가지 배정 원칙**으로 역할을 나눴습니다. "도메인 추론이 깊은 작업"은 Claude Code, "전체를 한 번에 봐야 하는 작업"은 Gemini CLI, "병렬화·자동화가 핵심인 작업"은 Codex입니다.

가장 흥미로운 설계 지점은 **Phase 3(테스트 생성)의 병렬화**와 **Phase 4(구현-리뷰 분리)**입니다. Phase 3에서는 Claude Code가 PBT, Codex가 TDD, Gemini가 strategy를 각각 다른 파일에 동시 작성합니다. 파일 경계가 명확하므로 충돌이 없습니다. Phase 4에서는 구현한 에이전트(Claude Code)와 리뷰하는 에이전트(Codex)를 분리하여 "자기 코드를 자기가 검증하는" 편향을 제거합니다.

**비용 최적화 전략**도 포함했습니다. Claude Code는 Codex 대비 3~5배 토큰을 소비한다는 보고가 있으므로, "도메인 인터뷰, property 추출, stateful PBT, 핵심 구현"처럼 대체 불가능한 작업에만 Claude Code를 배치하고, 교차 참조 검증이나 문서 동기화 같은 반복 작업은 무료 티어가 넉넉한 Gemini CLI에 맡기는 구조입니다.

> File: /home/claude/multi-agent-architecture.md



## Prompt:
2026. 3. 24. 오후 10:27:22

Codex가 Orchestrator이자 GateKeeper로서 사용자가 요청한 작업을 분석하여 분석된 결과와 컨텍스트 정보(현재까지 구현완료된 코드, 도메인 모델 등)에 따라 기존의 워크 플로우에서 불필요한 호출을 줄이는 등 유연한 방식으로 작업을 수행하고 싶습니다. 기존 Human in the loop 방식 대신 Orchestrator가 전적으로 워크플로우 관리 및 sub-Agent 호출할 수 있도록 현재 워크플로우에 최적화된 설계를 알려주세요.



## Response:
2026. 3. 24. 오후 10:32:05

````plaintext
Thought process: Codex의 자율적 오케스트레이션 아키텍처 설계를 체계적으로 구상했습니다.

The user wants to redesign the multi-agent workflow so that Codex acts as the Orchestrator/GateKeeper instead of having human checkpoints. Codex would analyze tasks, manage the workflow, and call sub-agents (Claude Code, Gemini) as needed. This is a significant architectural shift from human-in-the-loop to fully autonomous orchestration.

Let me think about this carefully:

1. Codex as Orchestrator makes sense because:
   - It has cloud sandboxes for parallel task management
   - It has Skills for bundling workflows
   - It has AGENTS.md for project rules
   - It has interactive steering capabilities and GitHub Action integration for CI
   - It's more cost-efficient than Claude Code for handling orchestration overhead

2. The core challenge is designing how Codex will analyze incoming tasks, decide which phases to skip, invoke Claude Code and Gemini as sub-agents, validate their outputs, and ultimately replace human checkpoints with automated gatekeeper logic.
````

아주 좋은 방향이에요. Codex를 Orchestrator/GateKeeper로 승격시키면 사람의 개입 없이 전체 파이프라인이 자율적으로 돌아가는 구조가 됩니다. 먼저 기존 워크플로우와의 구조적 차이를 시각화한 뒤, 구체적인 설계를 정리하겠습니다.

````plaintext
Tool: read_me
````

````plaintext
Thought process: Codex 중심 오케스트레이터 아키텍처 설계를 구상했습니다.

Now let me design the Codex-as-Orchestrator architecture. This is a significant redesign where Codex sits at the center, analyzing tasks, routing to sub-agents, and managing the workflow autonomously.
````

먼저 Codex Orchestrator 중심 아키텍처의 구조를 시각화합니다.

````plaintext
Tool: show_widget
````

````plaintext
Thought process: Codex Orchestrator 아키텍처 상세 문서 작성을 준비했습니다.

Now let me create the detailed document for the Codex Orchestrator architecture.
````

이제 Codex Orchestrator 중심의 상세 설계를 문서화합니다.

````plaintext
Create File: Creating Codex Orchestrator architecture document - fully autonomous workflow
````

````plaintext
Thought process

The document is comprehensive. Let me present it to the user.
````

````plaintext
Present File: /home/claude/codex-orchestrator-architecture.md
````

````plaintext
Thought process: Codex의 Orchestrator 역할 최적화 설계 검토했습니다.

Good, the document is shared. Let me summarize the key points.
````

설계의 핵심 변경 사항을 정리하면 이렇습니다.

**가장 큰 구조적 변화는 "Phase Selection Matrix"입니다.** 기존에는 모든 요청이 6 Phase를 순차적으로 거쳤지만, 이제 Codex Orchestrator가 Task Type(6가지)과 Risk Level을 조합하여 **필요한 Phase만 실행**합니다. 예를 들어 `Money.__sub__` 추가 같은 단순 작업은 Phase 1(도메인 발견), Phase 2(Property 추출), Phase 5(전체 감사)를 모두 건너뛰어 약 50%의 시간과 비용을 절감합니다.

**Human-in-the-loop의 3개 승인 지점은 5개의 자동 Gate Check로 대체됩니다.** 각 Gate는 "모든 새 모델에 ID가 있는가", "교차 참조가 유효한가", "테스트가 전부 GREEN인가" 같은 결정적(deterministic) 규칙으로 판정합니다. 사람의 주관적 판단이 아니라 규칙 기반 검증이므로 자동화가 가능합니다. Gate FAIL 시 최대 2회 자동 재시도하고, 그래도 실패하면 사람에게 에스컬레이션합니다.

**Codex가 Orchestrator에 적합한 이유**는 세 가지입니다. 토큰 효율(라우팅 같은 가벼운 판단에 Claude Code를 쓰면 낭비), 병렬 실행(클라우드 샌드박스로 sub-agent 동시 호출), CI 통합(최종 커밋까지 한 파이프라인으로 연결). Claude Code는 "대체 불가능한 깊은 추론"에만 집중하게 되므로, 비용 대비 효과가 극대화됩니다.

> File: /home/claude/codex-orchestrator-architecture.md



## Prompt:
2026. 3. 24. 오후 11:41:14

제안한 설계는 워크플로우 실행 기준이 필요 이상으로 엄격하게 정의되어 있다보니 Orchestrator보다는  하나의 확장된 워크플로우에 가까운 거 같아. 이런 식으로 복잡하게 규칙을 적용하면 Agent 입장에서는 판단의 자유도가 줄어들어 진정한 의미의 Orchestrator라고 보기 어렵고, 오히려 규칙을 이해하고 준수하는 부담만 커지게 돼.
진짜 Orchestrator라면 고정된 Phase 선택 규칙이나 Gate Check 규칙을 그대로 따르는 게 아니라, 현재 컨텍스트(작업의 성격, 기존 코드 상태, 변경의 파급 범위 등)를 스스로 파악하고 어떤 sub-agent를 어떤 순서로 호출할지를 자율적으로 결정할 수 있어야 해.
이런 관점에서, 현재 설계를 다음 방향으로 개선해줘:
1. Phase Selection Matrix나 Gate Check 같은 하드코딩된 규칙 대신, Orchestrator가 컨텍스트를 기반으로 스스로 실행 계획을 수립하도록
2. AGENTS.md의 규칙 나열 방식보다는, Orchestrator가 판단할 때 참고할 수 있는 최소한의 원칙과 예시 중심으로 재구성
3. sub-agent 호출 여부와 순서를 Orchestrator가 동적으로 결정하되, 잘못된 판단에 대한 안전장치는 유지



## Response:
2026. 3. 24. 오후 11:45:00

````plaintext
Thought process: Orchestrator의 자율성을 위해 규칙 기반에서 컨텍스트 기반 설계로 전환했다.

The user wants a fundamentally different approach - instead of a rigid, rule-based orchestrator with hardcoded matrices and gate checks, they want a true autonomous orchestrator that reasons about context and makes its own decisions. The key insight is that over-specifying rules actually constrains the agent's intelligence rather than leveraging it.

Let me redesign this with:
1. Minimal principles instead of exhaustive rules
2. Context-based reasoning instead of lookup tables
3. Dynamic planning instead of fixed phases
4. Safety through invariants, not through process gates

This is actually a much more elegant design. The AGENTS.md should read like a senior engineer's onboarding doc, not a state machine specification.
````

정확한 지적이에요. 기존 설계는 Orchestrator라는 이름을 쓰고 있지만 실제로는 "프로그래밍된 워크플로우 실행기"에 가까웠습니다. 진짜 Orchestrator는 규칙 테이블을 따르는 게 아니라, 컨텍스트를 읽고 스스로 판단하는 에이전트여야 합니다. 근본적으로 다시 설계하겠습니다.

````plaintext
Tool: show_widget
````

````plaintext
Thought process: 설계를 규칙 기반에서 원칙 기반으로 재구성하기로 결정했다.

Now let me create the redesigned document. The key shift is from "rules to follow" to "principles to internalize + examples to learn from". The AGENTS.md should feel like mentoring a smart junior developer, not programming a state machine.
````

핵심 전환은 **"규칙 나열 → 원칙 + 예시"** 입니다. 이제 상세 설계를 작성합니다.

````plaintext
Create File: Creating the autonomous orchestrator design - principle-based, not rule-based
````

````plaintext
Thought process

The user wanted a fundamental redesign away from rigid rules toward autonomous reasoning. Let me present the file and summarize the key changes.
````

````plaintext
Present File: /home/claude/autonomous-orchestrator.md
````

````plaintext
Thought process: 오케스트레이터의 자율적 판단 능력 강화 방안 검토했음.

Let me summarize the key changes concisely.
````

근본적으로 다른 설계입니다. 핵심 전환점 세 가지를 짚으면 이렇습니다.

**첫째, 150줄 규칙 테이블을 60줄 원칙+예시로 교체했습니다.** Phase Selection Matrix, Gate Check 규칙, Retry 정책을 전부 제거하고, 대신 3개 원칙(깨뜨리지 마라, 빠뜨리지 마라, 추적 가능하게 하라)과 5개의 과거 판단 예시만 남겼습니다. 이것이 동작하는 이유는 LLM이 본질적으로 잘하는 것이 "규칙 테이블 조회"가 아니라 "예시의 패턴을 현재 상황에 적용하는 것"이기 때문입니다. 에이전트가 규칙을 이해하고 준수하는 데 쓰던 토큰을, 실제 프로젝트 컨텍스트를 분석하는 데 쓸 수 있게 됩니다.

**둘째, "Phase"라는 고정 단위 자체를 없앴습니다.** 기존에는 6개 Phase가 정해져 있고 그중 일부를 선택하는 구조였는데, 이것도 결국 고정된 프레임입니다. 새 설계에서 Orchestrator는 `docs/index.md`와 현재 코드 상태를 직접 읽고, "뭐가 이미 있고 뭐가 없는지"를 파악한 뒤, 필요한 작업을 자유로운 순서로 구성합니다. 문서의 "Orchestrator의 실제 사고 과정" 섹션에서 이 차이가 가장 잘 드러납니다.

**셋째, 안전장치를 "과정 통제"에서 "결과 검증"으로 전환했습니다.** Gate Check가 "매 단계마다 이 조건을 확인하라"고 과정을 규정했다면, 불변식(invariant)은 "작업이 끝났을 때 이 조건들이 참이면 된다"고 결과만 규정합니다. Orchestrator가 어떤 순서로 작업했든, 최종적으로 테스트가 전부 통과하고, 문서-코드-테스트가 동기화되어 있으면 OK입니다. 이렇게 하면 에이전트가 더 효율적인 작업 순서를 스스로 발견할 여지가 생깁니다.

> File: /home/claude/autonomous-orchestrator.md



## Prompt:
2026. 3. 25. 오전 5:19:06

Agent들이 작업에 필요한 컨텍스트들을 추출할 수 있도록 컨텍스트 파일(AGENTS, CLAUDE.md 등)에 파일 구조에 대한 안내나 중간에 컨텍스트를 추출하는 도구(sub agent, skills, mcp등)가 추가 되어야 할 거 같아. 현재 프로젝트에 최적인 컨텍스트 탐색방법을 찾아줘.



## Response:
2026. 3. 25. 오전 5:30:14

````plaintext
Thought process: 에이전트 컨텍스트 추출 메커니즘과 최적 도구 조합을 분석했다.

The user wants me to design the optimal context discovery mechanism for their multi-agent DDD+PBT project. They want agents to efficiently extract the context they need, and they're asking about what tools/methods (sub-agents, skills, MCP servers, etc.) should be used alongside the context files (AGENTS.md, CLAUDE.md, GEMINI.md).

Let me think about what each agent needs and what tools are available:

1. **Claude Code**: CLAUDE.md, custom slash commands, hooks, subagents, MCP servers
2. **Codex**: AGENTS.md, Skills, subagents, MCP servers


3. **Gemini CLI**: GEMINI.md, MCP servers, extensions, skills

The real challenge here is figuring out how to make context discovery efficient as the project grows—each agent needs to pull only what's relevant without drowning in unnecessary information. I should look into what the latest context discovery tools and patterns can offer.
````

좋은 포인트예요. 원칙만 주고 "알아서 하라"고 해도, 에이전트가 **어디서 어떤 정보를 꺼내야 하는지** 모르면 결국 비효율적으로 파일을 탐색하게 됩니다. 각 에이전트의 컨텍스트 탐색 도구를 조사한 뒤 최적 설계를 제안하겠습니다.

````plaintext
Web Search: Claude Code custom slash commands subagents context loading 2026
````

> **Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents | alexop.dev** [alexop.dev](https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/)
>
> **Slash Commands in the SDK - Claude API Docs** [claude.com](https://platform.claude.com/docs/en/agent-sdk/slash-commands)
>
> **GitHub - hesreallyhim/awesome-claude-code: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic · GitHub** [github.com](https://github.com/hesreallyhim/awesome-claude-code)
>
> **Create custom subagents - Claude Code Docs** [claude.com](https://code.claude.com/docs/en/sub-agents)
>
> **Slash Commands vs Subagents: How to Keep AI Tools Focused - Jason Liu** [jxnl.co](https://jxnl.co/writing/2025/08/29/context-engineering-slash-commands-subagents/)
>
> **How to Use Claude Code: A Guide to Slash Commands, Agents, Skills, and Plug-ins** [producttalk.org](https://www.producttalk.org/how-to-use-claude-code-features/)
>
> **Claude Code Slash Commands** [prg.sh](https://prg.sh/notes/Claude-Code-Slash-Commands)
>
> **Custom commands and skills - FAQ | SFEIR Institute** [sfeir.com](https://institute.sfeir.com/en/claude-code/claude-code-custom-commands-and-skills/faq/)
>
> **Custom commands and skills | SFEIR Institute** [sfeir.com](https://institute.sfeir.com/en/claude-code/claude-code-custom-commands-and-skills/)
>
> **Claude Code /context Command: See Where Your Tokens Go** [jdhodges.com](https://www.jdhodges.com/blog/claude-code-context-slash-command-token-usage/)
>
````plaintext
Thought process

Now I have a good understanding of the context discovery tools available. Let me also check Codex and Gemini's tools.
````

````plaintext
Web Search: Codex CLI AGENTS.md skills subagents context discovery 2026
````

> **Custom instructions with AGENTS.md – Codex | OpenAI Developers** [openai.com](https://developers.openai.com/codex/guides/agents-md)
>
> **Customization – Codex | OpenAI Developers** [openai.com](https://developers.openai.com/codex/concepts/customization)
>
> **Agent Skills – Codex | OpenAI Developers** [openai.com](https://developers.openai.com/codex/skills)
>
> **Subagents – Codex | OpenAI Developers** [openai.com](https://developers.openai.com/codex/subagents)
>
> **Codex CLI & Agent Skills Guide: Install, Usage & Cross-Platform Resources (2026)** [itecsonline.com](https://itecsonline.com/post/codex-cli-agent-skills-guide-install-usage-cross-platform-resources-2026)
>
> **CLI – Codex | OpenAI Developers** [openai.com](https://developers.openai.com/codex/cli)
>
> **Changelog – Codex | OpenAI Developers** [openai.com](https://developers.openai.com/codex/changelog)
>
> **GitHub - shinpr/sub-agents-skills: Cross-LLM sub-agent orchestration as an Agent Skills. Route tasks to Codex, Claude Code, Cursor, or Gemini from any compatible tool. · GitHub** [github.com](https://github.com/shinpr/sub-agents-skills)
>
> **Use Codex with the Agents SDK | OpenAI Developers** [openai.com](https://developers.openai.com/codex/guides/agents-sdk)
>
> **Codex Integration | obra/superpowers | DeepWiki** [deepwiki.com](https://deepwiki.com/obra/superpowers/5.2-codex-integration)
>
````plaintext
Thought process: 세 에이전트의 컨텍스트 도구를 분석하고 최적 설계안을 수립했다.

Now I have comprehensive information about the context discovery tools for all three agents. Let me synthesize this into a practical design.

Key findings:
1. **Claude Code**: Subagents (Explore, Plan, general-purpose), Skills with `context: fork`, custom slash commands, CLAUDE.md hierarchy, hooks, MCP
2. **Codex**: AGENTS.md hierarchy (walk from root to cwd), Skills with progressive disclosure (metadata first, full load on use), subagents with `spawn_agent`, MCP
3. **Gemini CLI**: GEMINI.md, MCP servers, extensions, skills (same open standard), plan mode


4. **Cross-platform**: Agent Skills is now an open standard (SKILL.md format) working across all three agents, with skills.sh as the package manager

The real breakthrough is that subagents excel at context discovery because they isolate exploration from the main context—Claude Code's Explore subagent demonstrates this pattern perfectly. For the DDD+PBT project, I need to solve how the agent discovers which parts of docs/, src/, and tests/ are relevant to each task, and the optimal approach is a lightweight "context scout" subagent that reads index.md and returns the relevant subset.
````

리서치가 완료됐습니다. 핵심 발견은 **Agent Skills가 3개 에이전트 모두에서 동작하는 오픈 스탠다드**라는 것과, **subagent의 Explore 패턴이 컨텍스트 오염 없이 탐색하는 최적 도구**라는 것입니다. 이 두 가지를 중심으로 설계하겠습니다.

````plaintext
Tool: show_widget
````

````plaintext
Thought process: 시각화 도구 실패 후 직접 문서 작성 진행.

The visualizer timed out. Let me proceed with creating the document directly.
````

시각화 도구에 일시적 문제가 있었지만, 바로 핵심 설계 문서를 작성하겠습니다.

````plaintext
Create File: Creating context discovery design - 3-layer architecture with skills and subagents
````

````plaintext
Thought process

Let me present the file to the user.
````

````plaintext
Present File: /home/claude/context-discovery-design.md
````

````plaintext
Thought process: 에이전트 컨텍스트 탐색 방법 분석 및 최적화 방안 검토했음.

The file has been created and presented. Let me give a concise summary of the key design decisions.
````

설계의 핵심 구조를 짚으면 이렇습니다.

**3-layer 아키텍처**로 컨텍스트 비용을 단계적으로 관리합니다. Layer 1(CLAUDE.md/AGENTS.md/GEMINI.md)은 60줄짜리 원칙과 파일 구조 안내로, 세션 시작 시 항상 로드됩니다. 여기에 도메인 지식은 넣지 않고, "더 알고 싶으면 어떤 도구를 쓸 수 있는지"만 안내합니다. Layer 2(Skills)는 progressive disclosure로 동작합니다. 메타데이터(이름+설명)만 미리 로드되고, 에이전트가 작업과 관련 있다고 판단하면 전체 내용이 로드됩니다. Layer 3(Subagents)는 격리된 컨텍스트에서 파일 시스템을 탐색하고 요약만 반환하여, 메인 컨텍스트를 오염시키지 않습니다.

**가장 중요한 설계 결정은 `.agents/skills/` 디렉토리 하나로 세 에이전트가 동일한 Skill을 공유하는 것**입니다. Agent Skills가 2026년 현재 Claude Code, Codex, Gemini CLI 모두에서 동작하는 오픈 스탠다드이기 때문에 가능합니다. `domain-scout`, `impact-tracer`, `integrity-checker` 같은 Skill을 한 번 만들면 어떤 에이전트가 호출하든 동일하게 동작합니다.

**`integrity-checker`의 이중 구조**도 주목할 부분입니다. `scripts/check_sync.py`는 ID 기반 교차 참조를 결정적(deterministic)으로 검증하는 Python 스크립트이고, 이것을 Claude Code의 Stop Hook에 걸어두면 매 작업 완료 시 자동으로 "빠뜨리지 마라" 원칙이 검증됩니다. 에이전트의 판단에 의존하지 않는 프로그래밍적 안전장치입니다.

> File: /home/claude/context-discovery-design.md



## Prompt:
2026. 3. 25. 오전 8:50:13

Multi agent orchestrator가 sub agent들에게 작업을 지시하는 최적의 방법을 탐색해줘. 같은 모델끼리는 공식적으로 지원하는 sub agent 기능을 활용하고 다른 모델의 agent에게 작업을 지시하는 경우에는 아래 기준에 따라 최적의 방법을 찾아주세요.

1. 도메인과 관련성이 적은 만큼 최대한 단순하고 구현하기 쉬운 방향으로 설계해주세요. 
1. 작업에 필요한 컨텍스트만 전달되어야 합니다. 컨텍스트 유실이나 과도하게 컨텍스트가 낭비되는 현상이 발생하면 안됩니다.



## Response:
2026. 3. 25. 오전 8:53:36

````plaintext
Thought process: 다중 모델 에이전트 간 작업 지시 방법 모색 중.

The user wants me to research the optimal methods for a multi-agent orchestrator to dispatch work to sub-agents, specifically:

1. Same-model agents: use official sub-agent features
2. Cross-model agents: find the simplest, most practical method

Key criteria:
- Simple and easy to implement (not domain-related complexity)
- Precise context passing (no loss, no waste)

Let me research the current state of cross-agent invocation methods.
````

좋은 기준이에요. "같은 모델 ↔ 다른 모델" 간 통신의 현재 최적 방법을 조사하겠습니다.

````plaintext
Web Search: Codex CLI invoke Claude Code subprocess cross-agent orchestration 2026
````

> **Same Framework, Different Engine: Porting AI Coding Workflows from Claude Code to Codex CLI - DEV Community** [dev.to](https://dev.to/shinpr/same-framework-different-engine-porting-ai-coding-workflows-from-claude-code-to-codex-cli-n3p)
>
> **GitHub - catlog22/Claude-Code-Workflow: JSON-driven multi-agent cadence-team development framework with intelligent CLI orchestration (Gemini/Qwen/Codex), context-first architecture, and automated workflow execution · GitHub** [github.com](https://github.com/catlog22/Claude-Code-Workflow)
>
> **GitHub - stellarlinkco/myclaude: Multi-agent orchestration workflow (Claude Code Codex Gemini OpenCode) · GitHub** [github.com](https://github.com/cexll/myclaude)
>
> **Agentmaxxing: Run Multiple AI Agents in Parallel (2026)** [vibecoding.app](https://vibecoding.app/blog/agentmaxxing)
>
> **Everything-Claude-Code: Production Agent Framework | byteiota** [byteiota.com](https://byteiota.com/everything-claude-code-production-agent-framework/)
>
> **GitHub - ruvnet/ruflo: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration** [github.com](https://github.com/ruvnet/ruflo)
>
> **Codex CLI vs Claude Code in 2026: Architecture Deep Dive** [blakecrosley.com](https://blakecrosley.com/blog/codex-vs-claude-code-2026)
>
> **Claude Code & Codex CLI: AI Agents Beyond Coding (2026)** [itecsonline.com](https://itecsonline.com/post/claude-code-codex-cli-ai-agents-beyond-coding-2026)
>
> **Codex vs Claude Code (2026): Benchmarks, Agent Teams & Limits Compared** [morphllm.com](https://www.morphllm.com/comparisons/codex-vs-claude-code)
>
> **OpenAI Codex App: A Guide to Multi-Agent AI Coding | IntuitionLabs** [intuitionlabs.ai](https://intuitionlabs.ai/articles/openai-codex-app-ai-coding-agents)
>
````plaintext
Thought process

Now let me search for the cross-agent skill that was found - the sub-agents-skills project that routes between Claude, Codex, and Gemini.
````

````plaintext
Web Fetch: Failed to fetch: https://github.com/shinpr/sub-agents-skills
````

````plaintext
Thought process

Let me search for more specific info about cross-agent CLI invocation patterns.
````

````plaintext
Web Search: claude -p headless mode codex exec gemini -p cross agent CLI invocation script
````

> **Headless mode reference | Gemini CLI** [geminicli.com](https://geminicli.com/docs/cli/headless/)
>
> **headless-cli-agents - Claude Skills** [claude-plugins.dev](https://claude-plugins.dev/skills/@timur-khakhalev/cc-plugins/headless-cli-agents)
>
> **Running headless Codex CLI inside Claude Code | amanhimself.dev** [amanhimself.dev](https://amanhimself.dev/blog/running-headless-codex-cli-inside-claude-code/)
>
> **Run Claude Code programmatically - Claude Code Docs** [claude.com](https://code.claude.com/docs/en/headless)
>
> **GitHub - openclaw/acpx: Headless CLI client for stateful Agent Client Protocol (ACP) sessions · GitHub** [github.com](https://github.com/openclaw/acpx)
>
> **GitHub - SpillwaveSolutions/mastering-gemini-cli-agentic-skill: Claude Code skill for mastering headless automation with Google's Gemini CLI · GitHub** [github.com](https://github.com/SpillwaveSolutions/mastering-gemini-cli-agentic-skill)
>
> **External Agents | Use Claude Agent, Gemini CLI, and Codex in Zed** [zed.dev](https://zed.dev/docs/ai/external-agents)
>
> **Gemini CLi vs. Claude Code : The better coding agent | Composio** [composio.dev](https://composio.dev/content/gemini-cli-vs-claude-code-the-better-coding-agent)
>
> **GitHub - aannoo/hcom: Connect Claude Code, Gemini CLI, and Codex so agents can message, watch, and spawn each other across terminals** [github.com](https://github.com/aannoo/hcom)
>
> **Bug: /octo:debate skill never executes — circular routing + incorrect CLI syntax · Issue #35 · nyldn/claude-octopus** [github.com](https://github.com/nyldn/claude-octopus/issues/35)
>
````plaintext
Thought process: 다중 에이전트 오케스트레이션을 위한 최적 전략을 체계화했다.

Now I have a clear picture. Let me synthesize the findings:

1. **Same-model sub-agents**: Each tool has native support
   - Claude Code: built-in subagents (Explore, Plan, general-purpose) + custom subagents in .claude/agents/
   - Codex: spawn_agent/wait_agent tools, subagent .md files
   - Gemini: subagents (experimental), Plan mode

2. **Cross-model invocation**: The simplest proven method is **headless CLI invocation**
   - `claude -p "prompt"` — Claude Code's Agent SDK / headless mode
   - `codex exec "prompt"` — Codex's non-interactive mode  
   - `gemini -p "prompt"` — Gemini's headless mode
   - All three output to stdout, can be captured
   - This is the approach used by real projects (amanhimself's blog, composio's comparison, the headless-cli-agents skill)

3. **Context passing for cross-model**: The key challenge is managing state between invocations—either writing context to temporary files and referencing them in prompts, piping context directly through stdin, or using structured JSON output for parsing results downstream.

4. **More complex options** like full multi-agent frameworks, MCP bridges, or emerging protocols exist but add unnecessary complexity. Since the user wants simplicity, the clear winner is headless CLI invocation with file-based context passing, and I should design that approach now.
````

리서치 완료. 핵심 발견을 정리하면, 크로스 모델 통신의 검증된 최단 경로는 **headless CLI 호출 + 파일 기반 컨텍스트 전달**입니다. 복잡한 프레임워크 없이 각 에이전트의 공식 CLI 인터페이스만 사용합니다.

````plaintext
Create File: Creating the sub-agent dispatch design - simplest proven method for cross-agent communication
````

````plaintext
Thought process

Good, now let me present the file.
````

````plaintext
Present File: /home/claude/sub-agent-dispatch.md
````

````plaintext
Thought process: 다중 에이전트 조율 전략을 체계적으로 분석했습니다.

Let me summarize the key points for the user.
````

핵심을 짚으면 이렇습니다.

**같은 모델 간에는 네이티브 subagent**를 씁니다. Codex는 `spawn_agent`/`wait_agent`, Claude Code는 내장 Explore + 커스텀 subagent(`.claude/agents/*.md`). 설정 파일 하나 만들면 바로 동작하고, 컨텍스트 격리가 자동으로 보장됩니다.

**다른 모델 간에는 headless CLI 호출**(`claude -p`, `gemini -p`, `codex exec`)이 가장 단순하고 검증된 방법입니다. 세 에이전트 모두 공식 지원하는 비대화형 모드이므로 추가 도구 설치가 필요 없고, 프롬프트에 명시한 것만 전달되므로 컨텍스트 제어가 정확합니다.

**컨텍스트 전달의 핵심 차이**는 상대 에이전트의 특성에 따라 달라집니다. Claude Code에게 보낼 때는 `grep`으로 관련 부분만 발췌하여 `.task/context.md`에 넣고 참조시킵니다. 토큰 비용이 높으므로 정밀 발췌가 중요합니다. Gemini에게 보낼 때는 파일 경로만 알려주고 직접 읽게 합니다. 1M 토큰이므로 발췌보다 전체를 읽는 게 오히려 효율적입니다. `.task/` 디렉토리를 임시 통신 채널로 쓰고, 작업 완료 후 비우는 구조라 git에 노이즈도 남지 않습니다.

> File: /home/claude/sub-agent-dispatch.md



## Prompt:
2026. 3. 25. 오전 10:58:30

위 대화 전체에서 정리한 DDD + Property-based testing 기반 멀티 에이전트 방법론을 바탕으로, 다른 Python 프로젝트에 재사용 가능한 boilerplate를 설계·생성해줘.
* 폴더/파일 구조
* AGENTS/CLAUDE.md 등 컨텍스트 파일 예시
* 예시 도메인 모델, 테스트(PBT/TDD 혼합), Orchestrator 스켈레톤
을 포함해서, 이 레포를 복사하면 바로 같은 방법론을 적용할 수 있을 정도의 템플릿을 만들어줘.



## Response:
2026. 3. 25. 오전 11:03:39

````plaintext
Thought process: 포괄적 보일러플레이트 프로젝트 구조 설계 및 생성 계획 수립했음.

The user wants me to create a complete boilerplate/template project that encapsulates everything we've discussed across the entire conversation. This is a significant undertaking - I need to create a full project structure with all the files. Let me plan this carefully.

Key components to include:
1. Folder/file structure
2. AGENTS.md, CLAUDE.md, GEMINI.md
3. docs/ domain documents (index, glossary, models, constraints, events, properties)
4. Example domain model code
5. Example tests (PBT + TDD)
6. Skills for context discovery
7. Subagent definitions


8. Orchestrator skeleton
9. integrity-checker script
10. conftest.py with Hypothesis profiles
11. pyproject.toml
12. .gitignore

Now I need to figure out the best way to deliver this - I could create a zip archive or present the files individually. Let me start building out the complete directory structure and all the necessary files systematically.
````

대화 전체에서 다룬 모든 설계를 하나의 재사용 가능한 boilerplate로 통합하겠습니다. 먼저 전체 구조를 잡고, 파일을 하나씩 생성합니다.

````plaintext
Bash Tool: Create the full boilerplate directory structure
````

````plaintext
Thought process: DDD와 Property-based testing 기반 보일러플레이트 파일 구조화 계획 수립.

Now I need to create all the files. Let me create them one by one, starting with the most important ones.
````

````plaintext
Create File: Create the main README with full methodology overview
````

````plaintext
Thought process: DDD와 Property-based testing 기반 재사용 가능한 보일러플레이트 생성 준비.

Now create all the context files and domain documents.
````

````plaintext
Create File: AGENTS.md - Codex Orchestrator config with principles and examples
````

````plaintext
Thought process: DDD와 Property-based testing 기반 재사용 가능한 보일러플레이트 생성 진행중.

Continue creating all the files.
````

````plaintext
Create File: CLAUDE.md - Claude Code sub-agent config
````

````plaintext
Thought process: 문서와 코드를 체계적으로 정렬하는 순서를 결정했다.

Continue with GEMINI.md, then all docs/ files, then source code, then tests, then skills, then subagent configs.
````

````plaintext
Create File: GEMINI.md - Gemini CLI sub-agent config
````

````plaintext
Thought process: 예시 도메인으로 모든 문서 파일 생성 준비했다.

Now create all docs/ files with the example domain.
````

````plaintext
Create File: docs/index.md - Domain index (the map)
````

````plaintext
Thought process: 문서 파일들의 나머지 부분을 계속 처리하기로 결정했다.

Continue with the remaining docs files.
````

````plaintext
Create File: docs/glossary.md
````

````plaintext
Thought process: DDD와 속성 기반 테스트 보일러플레이트 구조 설계 진행 중.

Continue with models.md, constraints.md, events.md, properties.md
````

````plaintext
Create File: docs/models.md
````

````plaintext
Thought process: DDD와 Property-based testing 기반 재사용 가능한 보일러플레이트 생성 계획 수립했음.

Continue creating the remaining doc files.
````

````plaintext
Create File: docs/constraints.md
````

````plaintext
Thought process: 문서 작성 계속 진행하기로 결정했습니다.

Continue with events.md and properties.md
````

````plaintext
Create File: docs/events.md
````

````plaintext
Thought process: 속성 문서 작성을 준비했습니다.

Now create the properties.md
````

````plaintext
Create File: docs/properties.md - Property catalog with routing results
````

````plaintext
Thought process

Now create the source code files.
````

````plaintext
Create File: src/domain/__init__.py
````

````plaintext
Thought process

Continue with source code files.
````

````plaintext
Create File: src/domain/__init__.py
````

````plaintext
Thought process

Continue with the domain models.
````

````plaintext
Create File: src/domain/exceptions.py
````

````plaintext
Thought process: 모델 계층 구축을 위해 값 객체와 엔티티 설계를 준비했다.

Now create the main models.py with both Value Objects and Entities
````

````plaintext
Create File: src/domain/models.py - Value Objects (Pydantic) + Entities (dataclass)
````

````plaintext
Thought process: 다음 모듈 구현을 준비했습니다.

Now events.py and services.py
````

````plaintext
Create File: src/domain/events.py
````

````plaintext
Thought process: 서비스 계층 구현을 준비했습니다.

Now services.py
````

````plaintext
Create File: src/domain/services.py - Domain services
````

````plaintext
Thought process: 테스트 파일 구조를 단계적으로 구성하기로 결정했다.

Now create the test files. First conftest.py, then PBT tests, then TDD tests.
````

````plaintext
Create File: tests/conftest.py - Shared strategies + Hypothesis profiles
````

````plaintext
Thought process

Now create the PBT and TDD test files. Create __init__.py files too.
````

````plaintext
Bash Tool: Create __init__.py files for test packages
````

````plaintext
Thought process

The directories probably don't exist yet under tests/. Let me check.
````

````plaintext
Bash Tool: Ensure test directories exist and create init files
````





## Prompt:
2026. 3. 25. 오후 1:53:30

이전 답변에 이어서 하나씩 생성해줘.



## Response:
2026. 3. 25. 오후 1:57:22

````plaintext
Thought process: 이전 대화 맥락 없이 요청 이해하기의 어려움 고려 중

The user wants me to continue creating the boilerplate files one by one. Let me pick up where I left off. I need to create the test files, skills, subagent configs, and remaining infrastructure files.

Let me start with the test __init__.py files, then the actual test files, skills, etc.
````

이어서 나머지 파일들을 하나씩 생성하겠습니다.

````plaintext
Bash Tool: Check current test directory state
````

````plaintext
Thought process

The directories exist but the __init__.py files inside them don't. Let me create them.
````

````plaintext
Create File: tests/properties/__init__.py
````

````plaintext
Thought process

Hmm, it says the file already exists. Let me check.
````

````plaintext
Bash Tool: Check subdirectory contents
````

````plaintext
Thought process

It looks like the files were already created in a previous attempt. Let me check if they have content.
````

이미 일부 테스트 파일이 생성되어 있네요. 내용을 확인하고 없으면 새로 작성하겠습니다.

````plaintext
View: Check existing PBT money test
````

````plaintext
Thought process

Good, the test files already have content. Let me check the other test files.
````

````plaintext
View: Check existing PBT batch test
````

````plaintext
Thought process

Good, these test files are well-written. Let me check the unit test file too.
````

````plaintext
View: Check existing TDD test
````

````plaintext
Thought process: 기존 파일 검토 후 누락된 항목 파악 중.

All the test files are already in good shape. Now I need to continue creating the remaining files that weren't created yet. Let me check what's still missing.
````

테스트 파일들이 이미 잘 작성되어 있습니다. 이제 Skills, Subagent 설정, 인프라 파일들을 이어서 생성합니다.

````plaintext
Create File: domain-scout skill
````

````plaintext
Thought process

The files seem to already exist. Let me check which files are missing by listing the whole directory structure.
````

````plaintext
Bash Tool: List all files to see what's already created
````

````plaintext
Thought process: 식별된 누락 파일들을 순차적으로 생성하기로 결정했다.

OK, so some files already exist from previous tool calls. The missing files are:

1. `.agents/skills/impact-tracer/SKILL.md`
2. `.agents/skills/test-router/SKILL.md`
3. `.agents/skills/doc-sync/SKILL.md`
4. `.agents/skills/dispatch/SKILL.md`
5. `.claude/agents/domain-explorer.md`
6. `.claude/agents/code-scanner.md`
7. `.codex/agents/tdd-writer.md`
8. `.codex/agents/code-reviewer.md`
9. `.task/.gitkeep`


10. `.gitignore`
11. `pyproject.toml`
12. `.claude/settings.json` (hooks)

Now I'll create these files one by one.
````

현재 상태를 파악했습니다. 아직 생성되지 않은 파일들을 이어서 만들겠습니다.

````plaintext
Create File: impact-tracer skill - change impact tracking
````

````plaintext
Thought process

Hmm, some files exist but weren't listed. Let me check more carefully.
````

````plaintext
Bash Tool: List ALL files and directories
````

````plaintext
Thought process: 디렉토리 정리하고 누락된 파일들 생성 중.

I see that some directories were created with literal brace expansion in their names (a shell quoting issue from the initial mkdir command). I need to clean those up and create the missing files. Let me identify what's missing:

Missing files:
1. `.agents/skills/dispatch/SKILL.md`
2. `.agents/skills/doc-sync/SKILL.md`
3. `.claude/agents/domain-explorer.md`
4. `.claude/agents/code-scanner.md`
5. `.codex/agents/tdd-writer.md`
6. `.codex/agents/code-reviewer.md`


7. `.task/.gitkeep`
8. `.gitignore`
9. `pyproject.toml`
10. `.claude/settings.json` (hooks)

I'll remove the malformed directories and then create all the missing files and configuration files.
````

디렉토리 정리 후 남은 파일들을 이어서 만들겠습니다.

````plaintext
Bash Tool: Remove malformed directories from brace expansion issue
````

````plaintext
Thought process: 이전 답변을 바탕으로 파일들을 순차적으로 생성하려 준비했다.

Let me create the remaining files now.
````

````plaintext
Create File: dispatch skill - cross-model agent invocation patterns
````

````plaintext
Thought process

Hmm, the file already exists but wasn't showing in the find output earlier. Let me just check all files again with a proper find and list the ones that truly need to be created.
````

````plaintext
Bash Tool: List only proper files (excluding junk brace dirs)
````

````plaintext
Thought process: 누락된 파일들을 식별하고 순차적으로 생성하기로 결정했다.

Most files are already created. The missing files are:
1. `.codex/agents/tdd-writer.md`
2. `.codex/agents/code-reviewer.md`
3. `.task/.gitkeep`
4. `.gitignore`
5. `pyproject.toml`
6. `.claude/settings.json` (hooks)

Let me create these remaining files.
````

대부분 이미 생성되어 있고, 나머지 6개 파일만 남았습니다. 하나씩 만들겠습니다.

````plaintext
Create File: Codex subagent - TDD test writer
````

````plaintext
Thought process

OK, it seems like more files were created than what the `find` showed. Let me just check what's in the .codex/agents/ and .claude/settings.json areas.
````

````plaintext
Bash Tool: Check remaining missing infrastructure files
````

````plaintext
Thought process: 누락된 파일들을 식별하고 생성 준비를 마쳤다.

So the missing files are:
1. `.gitignore`
2. `pyproject.toml`
3. `.task/.gitkeep`
4. `.claude/settings.json` (hooks)

Let me create these.
````

인프라 파일 4개만 남았습니다.

````plaintext
Create File: pyproject.toml - project configuration with all dependencies
````

````plaintext
Thought process: 이전 답변의 존재 여부를 재검토했습니다.

Let me check what exists more carefully.
````

````plaintext
Bash Tool: Final check of root-level and config files
````

````plaintext
Thought process

It looks like all the files are already created. The `find` earlier missed some because of the `-not -path` filter. Let me check if `.claude/settings.json` and `.task/.gitkeep` exist.
````

````plaintext
Bash Tool: Check for hooks config and task gitkeep
````

````plaintext
Thought process: 누락된 파일들을 생성하고 기존 내용을 검증했다.

These two files are missing. Let me create them, and also verify the content of the existing files that were created in a previous attempt to make sure they're correct.
````

2개 파일만 남았습니다.

````plaintext
Create File: Claude Code hooks - auto test run + integrity check
````

````plaintext
Thought process

Now create the .task/.gitkeep file.
````

````plaintext
Create File: .task directory placeholder
````

기존 세션에서 이미 모든 핵심 파일이 생성되어 있었습니다. 마지막 2개(`.claude/settings.json`, `.task/.gitkeep`)를 추가하여 완성했습니다.

이제 기존 파일들의 내용이 올바른지 검증하고 테스트를 실행하겠습니다. 다만 tool-use 한도에 도달했으므로, 다음 메시지에서 이어서 검증 + 최종 패키징을 진행할 수 있습니다. 현재까지 생성된 파일 목록은 다음과 같습니다:

**에이전트 설정 (Layer 1)**: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` — 원칙 + 파일 구조 안내 + sub-agent 호출 방법

**도메인 문서**: `docs/index.md`(지도), `glossary.md`, `docs/order/*.md`(개념별 서사); 구조(ID 교차참조)는 `src/catalog/order.py`

**예시 도메인 구현**: `src/domain/models.py`(Money VO + Batch Entity), `events.py`, `services.py`(allocate, cancel_order), `exceptions.py`

**혼합 테스트**: `tests/properties/test_money_properties.py`(PBT: round-trip, commutativity), `test_batch_properties.py`(PBT: stateful machine, idempotence, SKU), `tests/unit/test_order.py`(TDD: Order 생성, 취소 시나리오, allocate 서비스), `tests/conftest.py`(Hypothesis 프로파일 3단계 + 공유 strategy)

**Skills (Layer 2)**: `domain-scout`, `property-extractor`, `integrity-checker`(+check_sync.py 스크립트), `impact-tracer`, `test-router`, `doc-sync`, `dispatch` — 7개 cross-agent skill

**Subagents (Layer 3)**: `.claude/agents/domain-explorer.md`, `code-scanner.md`, `.codex/agents/tdd-writer.md`, `code-reviewer.md`

**인프라**: `pyproject.toml`, `.gitignore`, `.claude/settings.json`(hooks), `.task/.gitkeep`

다음 메시지에서 `pip install` + `pytest` 실행으로 동작 검증과 최종 패키징을 이어갈 수 있습니다.



## Prompt:
2026. 3. 25. 오후 2:04:21

네 이어서 진행해주세요.



## Response:
2026. 3. 25. 오후 2:09:37

````plaintext
Thought process

The user wants me to continue with verification and final packaging of the boilerplate. Let me:
1. Check all existing files for correctness
2. Install dependencies and run tests
3. Fix any issues
4. Package everything for download
````

````plaintext
Bash Tool: Check pyproject.toml content first
````

````plaintext
Thought process

Good, pyproject.toml exists. Let me install dependencies and run tests.
````

````plaintext
Bash Tool: Install project with dev dependencies
````

````plaintext
Thought process

Good, installed. Let me run the tests.
````

````plaintext
Bash Tool: Run all tests with verbose output
````

````plaintext
Thought process: 할당 함수의 정렬 로직을 수정하고 있습니다.

One test failure: `test_allocate_in_stock_before_shipment`. The test expects that in-stock batches (eta=None) should be allocated before shipment batches (eta=date). Let me look at the `allocate` function to fix the sorting logic.

The current sorting: `key=lambda b: (b.eta is None, b.eta)` — this puts `None` last (True > False), which is wrong. In-stock (eta=None) should come FIRST.

The fix: `key=lambda b: (b.eta is not None, b.eta)` — this puts None first.


But wait, I need to handle the comparison issue since None can't be directly compared with dates. I'll use `b.eta or date.min` to provide a fallback value when eta is None, so the sorting tuple becomes `(b.eta is not None, b.eta or date.min)`.
````

테스트 1개 실패 — in-stock Batch(eta=None)가 shipment보다 우선 배정되어야 하는데, 정렬 로직이 반대입니다. 수정합니다.

````plaintext
View: Check the allocate function sort logic
````

````plaintext
Thought process: 정렬 로직 버그를 진단하고 수정 방안을 검증했습니다.

The bug: `(b.eta is None, b.eta)` puts None-eta batches at the END because `True > False`. In-stock batches (eta=None) should be FIRST.

Fix: Use `(b.eta is not None, b.eta or date.min)` — this way None-eta gets (False, date.min) and comes first.

Actually wait, we can't compare None with date either. Let me use a sentinel.

`key=lambda b: (b.eta is not None, b.eta or date.min)`

When eta is None: (False, date.min) 
When eta is date(2024,1,1): (True, date(2024,1,1))


False sorts before True, so in-stock batches come first, then the dated ones in chronological order.
````

````plaintext
Edit: Fix sort: in-stock (eta=None) should come before shipments
````

````plaintext
Thought process

Now let me run tests again to verify the fix.
````

````plaintext
Bash Tool: Re-run all tests after fix
````

````plaintext
Thought process

All 21 tests pass. Now let me run the integrity checker script to verify it works too.
````

전체 21개 테스트 통과. 이제 integrity-checker 스크립트도 검증합니다.

````plaintext
Bash Tool: Run integrity checker to verify docs-code sync
````

````plaintext
Thought process

The integrity checker passes too. Now let me verify mypy.
````

````plaintext
Bash Tool: Run mypy type check
````

````plaintext
Thought process

All checks pass. Now let me also run ruff.
````

````plaintext
Bash Tool: Run ruff lint
````

````plaintext
Thought process

Let me auto-fix the lint issues.
````

````plaintext
Bash Tool: Auto-fix lint issues
````

````plaintext
Thought process

Just one remaining issue - a line too long in a docstring. Let me fix that.
````

````plaintext
Edit: Shorten the module docstring to fit line length
````

````plaintext
Thought process

Now let me verify everything passes.
````

````plaintext
Bash Tool: Run all 4 verification checks
````

````plaintext
Thought process: 검증 완료 후 파일 패키징 준비 중.

All 4 checks pass. Now let me verify all the existing skill files and subagent files have correct content, then package it all up.
````

4개 검증 모두 통과. 이제 기존 생성된 Skills/Subagent 파일 내용을 빠르게 검증합니다.

````plaintext
Bash Tool: Quick scan all skill and subagent files
````

````plaintext
Thought process

All files are in place. Let me also check the .gitignore content.
````

````plaintext
Bash Tool: Check gitignore content
````

````plaintext
Thought process

Everything looks good. Let me now check the dispatch skill has complete content:
````

````plaintext
View: Verify dispatch skill has full cross-agent invocation patterns
````

````plaintext
Thought process

Good. Now let me do the final verification of the check_sync.py script and then package everything.
````

모든 파일이 올바르게 작성되어 있습니다. 최종 파일 트리를 확인하고 패키징합니다.

````plaintext
Bash Tool: Final file tree listing
````

````plaintext
Thought process: 검증 완료 후 캐시 제거 및 패키징 준비.

Good, everything is there. Now I need to clean up cache directories and package it. Let me create a tar.gz excluding caches.
````

캐시 디렉토리를 제외하고 깨끗하게 패키징합니다.

````plaintext
Bash Tool: Package boilerplate as tar.gz excluding caches
````

````plaintext
Thought process

Now let me verify what's actually in the archive.
````

````plaintext
Bash Tool: Verify archive contents
````

````plaintext
Thought process

39 files in the archive. All correct. Now let me copy to outputs.
````

39개 파일, 18KB. 이제 최종 전달합니다.

````plaintext
Bash Tool: Copy boilerplate folder and archive to outputs
````

````plaintext
Thought process

Let me present both the archive and the README for download.
````

````plaintext
Present File: /mnt/user-data/outputs/ddd-pbt-boilerplate.tar.gz, /mnt/user-data/outputs/ddd-pbt-boilerplate/README.md
````

boilerplate가 완성됐습니다. 검증 결과를 정리합니다.

**검증 통과 내역**:
- `pytest` — 21 tests passed (PBT 10개 + TDD 11개)
- `mypy` — 6 source files, no issues
- `ruff` — all checks passed
- `integrity-checker` — status: PASS (교차 참조 정합)

**파일 구성 (39개)**:

에이전트 설정 3개 — `AGENTS.md`(Codex Orchestrator, 원칙+판단예시), `CLAUDE.md`(Claude Code sub-agent), `GEMINI.md`(Gemini 검증 sub-agent)

도메인 문서 — `index.md`(지도), `glossary.md`, `docs/order/*.md`(개념별 서사); 카탈로그 `src/catalog/order.py`(구조)

구현 코드 4개 — `models.py`(Money VO + Batch Entity), `events.py`, `services.py`(allocate, cancel_order), `exceptions.py`

테스트 4개 — PBT 2개(Money round-trip/commutativity, Batch stateful machine/idempotence/SKU) + TDD 1개(Order 생성/취소/allocate 시나리오) + `conftest.py`(Hypothesis 3단계 프로파일 + 공유 strategy)

Skills 7개 — `domain-scout`, `property-extractor`, `integrity-checker`(+check_sync.py), `impact-tracer`, `test-router`, `doc-sync`, `dispatch`

Subagents 4개 — Claude Code용 `domain-explorer`, `code-scanner` + Codex용 `tdd-writer`, `code-reviewer`

인프라 3개 — `pyproject.toml`, `.gitignore`, `.claude/settings.json`(PostToolUse/Stop hooks)

`tar.gz`를 다운로드하여 새 프로젝트에 풀면, `pip install -e ".[dev]"` 한 번으로 바로 동작합니다.

> File: /mnt/user-data/outputs/ddd-pbt-boilerplate.tar.gz

> File: /mnt/user-data/outputs/ddd-pbt-boilerplate/README.md





---
Powered by [Claude Exporter](https://www.ai-chat-exporter.net)