"""카탈로그·코드·테스트·문서 정합성 자동 검증. Hooks에서 자동 실행 가능.

정본: src/catalog/ (Python 객체)
구현: src/domain/ (docstring의 ID 참조)
테스트: tests/ (docstring의 ID 참조)
서사: docs/<scope>/*.md (YAML frontmatter로 catalog과 교차 검증)
"""

import json
import re
import sys
from pathlib import Path


def extract_ids(text: str, prefix: str) -> set[str]:
    return set(re.findall(rf"{prefix}-\d+", text))


def parse_frontmatter(text: str) -> dict | None:
    """YAML frontmatter를 파싱한다. --- 로 감싸진 블록."""
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    fm: dict[str, object] = {}
    for line in match.group(1).strip().splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        # [a, b, c] 형식의 리스트 파싱
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip() for v in value[1:-1].split(",") if v.strip()]
            fm[key] = items
        else:
            fm[key] = value
    return fm


def read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(project_root: Path | None = None) -> dict:
    root = project_root or Path.cwd()

    results: dict = {
        "status": "PASS",
        "catalog_errors": [],
        "missing_tests": [],
        "orphan_ids": [],
        "unconstrained_code": [],
        "doc_errors": [],
    }

    # ── 카탈로그 로드 ────────────────────────────────────────
    sys.path.insert(0, str(root))
    try:
        from src.catalog import CATALOG  # noqa: PLC0415
    except Exception as e:
        results["status"] = "ERROR"
        results["catalog_errors"].append(f"Cannot import CATALOG: {e}")
        return results

    catalog_constraint_ids = {c.id for c in CATALOG.constraints}
    catalog_model_ids = {m.id for m in CATALOG.models}
    catalog_property_ids = {p.id for p in CATALOG.properties}
    catalog_event_ids = {e.id for e in CATALOG.events}

    # ── Check 1: 카탈로그 내부 참조 정합성 ──────────────────
    for model in CATALOG.models:
        doc_path = root / model.doc_file
        if not doc_path.exists():
            results["doc_errors"].append(
                f"{model.id}.doc_file → missing file: {model.doc_file}"
            )
        for cid in model.constraints:
            if cid not in catalog_constraint_ids:
                results["catalog_errors"].append(
                    f"{model.id}.constraints → {cid} not defined in catalog"
                )
        for pid in model.properties:
            if pid not in catalog_property_ids:
                results["catalog_errors"].append(
                    f"{model.id}.properties → {pid} not defined in catalog"
                )
        for eid in model.events:
            if eid not in catalog_event_ids:
                results["catalog_errors"].append(
                    f"{model.id}.events → {eid} not defined in catalog"
                )
        for did in model.depends_on:
            if did not in catalog_model_ids:
                results["catalog_errors"].append(
                    f"{model.id}.depends_on → {did} not defined in catalog"
                )

    for constraint in CATALOG.constraints:
        for mid in constraint.applies_to:
            if mid not in catalog_model_ids:
                results["catalog_errors"].append(
                    f"{constraint.id}.applies_to → {mid} not defined in catalog"
                )
        for pid in constraint.properties:
            if pid not in catalog_property_ids:
                results["catalog_errors"].append(
                    f"{constraint.id}.properties → {pid} not defined in catalog"
                )

    for prop in CATALOG.properties:
        for cid in prop.source:
            if cid not in catalog_constraint_ids:
                results["catalog_errors"].append(
                    f"{prop.id}.source → {cid} not defined in catalog"
                )
        for mid in prop.models:
            if mid not in catalog_model_ids:
                results["catalog_errors"].append(
                    f"{prop.id}.models → {mid} not defined in catalog"
                )

    for event in CATALOG.events:
        for mid in event.related_models:
            if mid not in catalog_model_ids:
                results["catalog_errors"].append(
                    f"{event.id}.related_models → {mid} not defined in catalog"
                )

    # ── Check 2: 카탈로그 ↔ 제약사항 양방향 일관성 ──────────
    # 제약사항이 연결한 property가 역으로 그 제약사항을 source로 가리키는지 확인
    for constraint in CATALOG.constraints:
        for pid in constraint.properties:
            prop = next((p for p in CATALOG.properties if p.id == pid), None)
            if prop is not None and constraint.id not in prop.source:
                results["catalog_errors"].append(
                    f"{constraint.id} → {pid}: property.source does not include {constraint.id}"
                )

    # ── Check 3: Property test_file 존재 여부 ───────────────
    for prop in CATALOG.properties:
        test_path = root / prop.test_file
        if not test_path.exists():
            results["missing_tests"].append(
                f"{prop.id} — test file missing: {prop.test_file}"
            )

    # ── Check 4: 제약사항 → 테스트 추적성 ───────────────────
    tests_dir = root / "tests"
    test_ids: set[str] = set()
    if tests_dir.exists():
        for f in sorted(tests_dir.rglob("test_*.py")):
            content = read_utf8(f)
            test_ids |= extract_ids(content, "INV")
            test_ids |= extract_ids(content, "POL")
            test_ids |= extract_ids(content, "FMT")
            test_ids |= extract_ids(content, "P")

    for cid in sorted(catalog_constraint_ids - test_ids):
        results["missing_tests"].append(f"{cid} — no test references this ID")

    # ── Check 5: 코드 ID → 카탈로그 역방향 검증 ────────────
    src_dir = root / "src" / "domain"
    code_ids: set[str] = set()
    if src_dir.exists():
        for f in src_dir.rglob("*.py"):
            content = read_utf8(f)
            code_ids |= extract_ids(content, "INV")
            code_ids |= extract_ids(content, "POL")
            code_ids |= extract_ids(content, "FMT")

    for cid in sorted(code_ids - catalog_constraint_ids):
        results["unconstrained_code"].append(
            f"{cid} — referenced in code but not in catalog"
        )

    # ── Check 6: 고아 Property (어떤 Constraint도 참조 안 함) ─
    linked_prop_ids = {pid for c in CATALOG.constraints for pid in c.properties}
    for pid in sorted(catalog_property_ids - linked_prop_ids):
        results["orphan_ids"].append(
            f"{pid} — in catalog but no constraint references it"
        )

    # ── Check 7: docs/<scope>/*.md frontmatter ↔ catalog 일치 ─
    for model in CATALOG.models:
        md_file = root / model.doc_file
        if not md_file.exists():
            continue

        content = read_utf8(md_file)
        fm = parse_frontmatter(content)
        if fm is None:
            results["doc_errors"].append(
                f"{model.doc_file} — YAML frontmatter 없음"
            )
            continue

        model_id = fm.get("model_id", "")
        if model_id != model.id:
            results["doc_errors"].append(
                f"{model.doc_file}.model_id: frontmatter={model_id!r} != catalog={model.id!r}"
            )

        scope = fm.get("scope", "")
        if scope != model.scope:
            results["doc_errors"].append(
                f"{model.doc_file}.scope: frontmatter={scope!r} != catalog={model.scope!r}"
            )

        for field, catalog_val in [
            ("constraints", model.constraints),
            ("properties", model.properties),
            ("events", model.events),
            ("depends_on", model.depends_on),
        ]:
            doc_val = tuple(fm.get(field, []))
            if doc_val != catalog_val:
                results["doc_errors"].append(
                    f"{model.doc_file}.{field}: "
                    f"frontmatter={list(doc_val)} != "
                    f"catalog={list(catalog_val)}"
                )

    # ── Check 8: glossary.md ↔ catalog glossary 일치 ─────────
    glossary_path = root / "docs" / "glossary.md"
    if glossary_path.exists() and hasattr(CATALOG, "glossary"):
        glossary_text = read_utf8(glossary_path)
        catalog_glossary_ids = {g.id for g in CATALOG.glossary}

        doc_glossary_ids = set(re.findall(r"\[G-\d+\]", glossary_text))
        doc_glossary_ids = {gid.strip("[]") for gid in doc_glossary_ids}

        for gid in sorted(catalog_glossary_ids - doc_glossary_ids):
            results["doc_errors"].append(
                f"glossary.md — missing term ID: {gid}"
            )
        for gid in sorted(doc_glossary_ids - catalog_glossary_ids):
            results["doc_errors"].append(
                f"glossary.md — unknown term ID: {gid}"
            )

    if any([
        results["catalog_errors"],
        results["missing_tests"],
        results["orphan_ids"],
        results["unconstrained_code"],
        results["doc_errors"],
    ]):
        results["status"] = "ISSUES_FOUND"

    return results


if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    result = check(root)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    sys.exit(0 if result["status"] == "PASS" else 1)
