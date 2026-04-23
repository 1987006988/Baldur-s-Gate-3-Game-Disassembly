from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    ".gitignore",
    "Makefile",
    ".codex/config.toml",
    ".agent/PLANS.md",
    ".agents/skills/bg3-research/SKILL.md",
    "scripts/check_repo.py",
    "docs/AGENTS.md",
    "docs/00_project/overview.md",
    "docs/00_project/repo_map.md",
    "docs/00_project/current_state.md",
    "docs/00_project/decision_log.md",
    "docs/00_project/next_step.md",
    "docs/00_project/source_index.md",
    "docs/01_methodology/deconstruction_framework.md",
    "docs/01_methodology/evidence_rules.md",
    "docs/01_methodology/module_template.md",
    "docs/02_sources/benchmark_projects.md",
    "docs/02_sources/bg3_official.md",
    "docs/02_sources/bg3_player_analysis.md",
    "docs/03_analysis/00_core_thesis.md",
    "docs/03_analysis/01_macro_structure.md",
    "docs/03_analysis/02_quests_and_choices.md",
    "docs/03_analysis/03_party_and_camp.md",
    "docs/03_analysis/04_combat_and_environment.md",
    "docs/03_analysis/05_implementation_validation.md",
    "templates/source_note.md",
    "templates/case_note.md",
]

ANALYSIS_FILES = [
    "docs/03_analysis/00_core_thesis.md",
    "docs/03_analysis/01_macro_structure.md",
    "docs/03_analysis/02_quests_and_choices.md",
    "docs/03_analysis/03_party_and_camp.md",
    "docs/03_analysis/04_combat_and_environment.md",
    "docs/03_analysis/05_implementation_validation.md",
]

SOURCE_INDEX_FILE = "docs/00_project/source_index.md"
CURRENT_STATE_FILE = "docs/00_project/current_state.md"
NEXT_STEP_FILE = "docs/00_project/next_step.md"

SOURCE_ID_RE = re.compile(r"\b(?:BG3-(?:OFF|PLY)-\d{3}|BMK-\d{3})\b")
BACKTICK_PATH_RE = re.compile(r"`([^`]+)`")
SECTION_RE = re.compile(r"^##\s+(.+?)\n(.*?)(?=^##\s+|\Z)", re.M | re.S)


def read_text(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def normalize_text(text: str) -> str:
    return re.sub(r"[\s`*_\-:：,，。；;（）()]+", "", text)


def parse_sections(text: str) -> dict[str, str]:
    return {title.strip(): body.strip() for title, body in SECTION_RE.findall(text)}


def parse_source_index(text: str) -> dict[str, dict[str, object]]:
    entries: dict[str, dict[str, object]] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        parts = [part.strip() for part in stripped.strip("|").split("|")]
        if len(parts) < 7:
            continue
        source_id = parts[0]
        if not SOURCE_ID_RE.fullmatch(source_id):
            continue
        where_used = BACKTICK_PATH_RE.findall(parts[5])
        entries[source_id] = {
            "title": parts[1],
            "type": parts[2],
            "priority": parts[3],
            "status": parts[4],
            "where_used": where_used,
            "notes": parts[6],
        }
    return entries


def collect_source_ids(text: str) -> set[str]:
    return set(SOURCE_ID_RE.findall(text))


def check_required_files(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"missing: {relative}")
            continue
        if path.is_file() and not path.read_text(encoding="utf-8").strip():
            errors.append(f"empty: {relative}")


def check_analysis_markers(warnings: list[str]) -> None:
    for relative in ANALYSIS_FILES:
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "Source IDs" not in text or "待验证问题" not in text:
            warnings.append(f"analysis lacks source or open-question marker: {relative}")


def check_source_ids(source_entries: dict[str, dict[str, object]], errors: list[str]) -> None:
    valid_ids = set(source_entries)
    for relative in ANALYSIS_FILES:
        text = read_text(relative)
        for source_id in sorted(collect_source_ids(text)):
            if source_id not in valid_ids:
                errors.append(f"unknown Source ID in analysis: {relative} -> {source_id}")


def check_where_used_paths(source_entries: dict[str, dict[str, object]], errors: list[str]) -> None:
    for source_id, entry in source_entries.items():
        for relative in entry["where_used"]:
            if not (ROOT / relative).exists():
                errors.append(f"missing Where used path: {source_id} -> {relative}")


def check_state_alignment(errors: list[str]) -> None:
    current_state = parse_sections(read_text(CURRENT_STATE_FILE))
    next_step = parse_sections(read_text(NEXT_STEP_FILE))

    current_phase = current_state.get("当前阶段", "")
    current_actions = current_state.get("接下来 1~3 个最优先动作", "")
    current_task = next_step.get("当前唯一主任务", "")

    if not current_task:
        errors.append("missing section: docs/00_project/next_step.md -> 当前唯一主任务")
        return

    haystack = f"{current_phase}\n{current_actions}"
    milestone_markers = set(re.findall(r"M\d+", current_task))
    path_markers = {
        item for item in BACKTICK_PATH_RE.findall(current_task) if item.endswith((".md", ".py"))
    }

    consistent = True
    if milestone_markers:
        consistent = milestone_markers.issubset(set(re.findall(r"M\d+", haystack)))
    if consistent and path_markers:
        consistent = any(marker in haystack for marker in path_markers)
    if consistent and not milestone_markers and not path_markers:
        consistent = normalize_text(current_task)[:12] in normalize_text(haystack)

    if not consistent:
        errors.append("state mismatch: current_state next actions do not align with next_step current task")


def check_placeholder_usage(source_entries: dict[str, dict[str, object]], errors: list[str]) -> None:
    placeholder_ids = {
        source_id for source_id, entry in source_entries.items() if entry["status"] == "to read"
    }
    if not placeholder_ids:
        return

    for relative in ANALYSIS_FILES:
        text = read_text(relative)
        used = sorted(collect_source_ids(text) & placeholder_ids)
        if used:
            errors.append(
                f"placeholder Source ID referenced in analysis: {relative} -> {', '.join(used)}"
            )


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    check_required_files(errors)
    if errors:
        print("CHECK FAILED")
        for item in errors:
            print(f"- {item}")
        return 1

    source_entries = parse_source_index(read_text(SOURCE_INDEX_FILE))
    if not source_entries:
        errors.append("failed to parse source index entries")
    else:
        check_source_ids(source_entries, errors)
        check_where_used_paths(source_entries, errors)
        check_placeholder_usage(source_entries, errors)

    check_analysis_markers(warnings)
    check_state_alignment(errors)

    if errors:
        print("CHECK FAILED")
        for item in errors:
            print(f"- {item}")
        if warnings:
            print("WARNINGS")
            for item in warnings:
                print(f"- {item}")
        return 1

    print("CHECK PASSED")
    if warnings:
        print("WARNINGS")
        for item in warnings:
            print(f"- {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
