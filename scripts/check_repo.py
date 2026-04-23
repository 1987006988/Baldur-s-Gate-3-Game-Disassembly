from pathlib import Path
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


def main() -> int:
    errors = []
    warnings = []

    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"missing: {relative}")
            continue
        if path.is_file():
            text = path.read_text(encoding="utf-8").strip()
            if not text:
                errors.append(f"empty: {relative}")

    for relative in ANALYSIS_FILES:
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "Source IDs" not in text and "待验证" not in text:
            warnings.append(f"analysis lacks source/hypothesis marker: {relative}")

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
