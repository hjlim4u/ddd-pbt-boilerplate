When work is complete, verify:
- `pytest tests/ -q`
- `mypy src/`
- `python .agents/skills/integrity-checker/scripts/check_sync.py`
Also confirm new rules are reflected in docs/ and src/catalog/, and corresponding tests exist.