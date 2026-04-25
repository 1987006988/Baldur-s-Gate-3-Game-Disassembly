# ExecPlan Addendum: Stage-6 Release Package Assembly Review Round 3

## Goal

为阶段 6 第三轮受控一致性审阅提供一份无歧义的续轮覆盖说明，明确：

- 当前不是等待“首轮一致性审阅”，而是已经完成三轮 review
- 本轮仍未命中新 actual-unit trigger
- 剩余工作只停在 assembly / review 层与其支撑文件，不回写五段 actual units

## Why It Matters

- 旧的 `.agent/execplan_stage6_release_package_assembly_review.md` 仍保留乱码与“首轮审阅”旧口径，容易把当前主线拉回过去时点。
- 第三轮审阅没有发现 actual-unit 级问题；如果继续沿用旧口径，后续会话最容易误把 review-level 漂移当成重写 release unit 的理由。

## Inputs and Evidence

- `docs/00_project/stage6_release_package_assembly_review_sheet.md`
- `docs/03_analysis/05_implementation_validation.md`
- `docs/00_project/current_state.md`
- `docs/00_project/next_step.md`
- `docs/00_project/stage6_entry_first_section_release_units.md`
- `docs/00_project/stage6_second_section_release_units.md`
- `docs/00_project/stage6_third_section_release_units.md`
- `docs/00_project/stage6_final_section_release_units.md`

## Round-3 Findings

1. 四份 stage-6 actual units 的顺序、handoff、evidence lock 与 traceback 继续和 `ASSEMBLY-MAP-001` 对齐。
2. `ASSEMBLY-TRIGGER-001` 本轮未被命中，因此不存在 actual-unit 级 writeback 理由。
3. 剩余漂移只出现在 review-level 支撑文件：旧 ExecPlan 与 `current_state.md` 仍把动作写成“首轮审阅 / 首轮 trigger”。

## Required Writeback

- 更新 `docs/00_project/stage6_release_package_assembly_review_sheet.md`，补入第三轮审阅记录。
- 更新 `docs/03_analysis/05_implementation_validation.md`，补入第三轮审阅事实与推断。
- 更新 `docs/00_project/current_state.md` 与 `docs/00_project/next_step.md`，把当前主线写死为“已完成三轮审阅，继续做续轮复核”。
- 不回写任何 stage-6 actual units 承载文件。

## Validation

- review sheet 中存在 `ASSEMBLY-REVIEW-2026-04-25C`
- `05_implementation_validation.md` 已记录第三轮审阅事实
- `current_state.md` 与 `next_step.md` 不再把当前动作写成首轮审阅
- `python scripts/check_repo.py` 与 `make check` 通过

## Current Outcome

- 阶段 6 当前仍是 `no hard blocker`
- 后续默认继续按 review sheet 做受控一致性审阅（续轮）
- 只有再次命中 `ASSEMBLY-TRIGGER-001`，才允许回写单段 actual units
