---
name: dispatch
description: >
  다른 모델의 에이전트에게 작업을 위임할 때 사용.
  Claude Code 또는 Gemini CLI를 headless 모드로 호출한다.
---

## Claude Code 호출

1. `.task/context.md`에 관련 부분만 발췌한다.
2. `.task/prompt.md`에 프롬프트를 작성한다.
3. 호출:
   - 읽기 전용: claude -p "$(cat .task/prompt.md)" --allowedTools "Read,Bash(grep *)"
   - 파일 수정: claude -p "$(cat .task/prompt.md)" --allowedTools "Read,Edit,Write,Bash(pytest *)"

## Gemini CLI 호출

1. `.task/prompt.md`에 프롬프트를 작성한다. 파일 경로만 안내해도 된다.
2. 호출: gemini -p "$(cat .task/prompt.md)" --output-format json > .task/result.json

## 컨텍스트 발췌 원칙

- 먼저 `src/catalog/`의 `CATALOG`에서 관련 `doc_file`, `test_file`을 찾는다.
- Claude Code에게는 필요한 파일에서 관련 ID나 도메인 용어가 있는 부분만 발췌한다.
- Gemini에게는 파일 경로만 전달하고 직접 읽게 한다.

## 컨텍스트 발췌 예시

개념별 서사는 `docs/<scope>/*.md`에 있다. 제약 ID와 도메인 용어를 함께 grep한다.

```bash
# Batch 관련 (INV-01, POL-03 등)
grep -E "INV-01|POL-03|주문 취소" docs/order/batch.md > .task/context.md
grep -E "POL-03|주문 취소" docs/order/order.md >> .task/context.md
```

PowerShell 예시:

```powershell
Select-String -Path docs/order/batch.md -Pattern "INV-01|POL-03|주문 취소" -Context 0,8 |
  ForEach-Object { $_.ToString() } | Set-Content .task/context.md
```

## 규칙

- Claude Code에게는 발췌하여 전달한다.
- Gemini에게는 파일 경로만 전달한다.
- 경로는 `docs/index.md` Scope Registry와 카탈로그 메타데이터를 기준으로 찾는다.
- sub-agent에게 다른 sub-agent의 존재를 알리지 않는다.
- 작업 완료 후 `.task/` 디렉토리를 비운다: `rm -rf .task/*`
