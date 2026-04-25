# ExecPlan Addendum: Stage-6 Release Package Assembly Review Round 4

## Goal

为阶段 6 的第四轮受控一致性审阅提供一份最新续轮覆盖说明，明确：

- 本轮仍未命中新 actual-unit trigger
- 剩余漂移已不在单段 actual units，也不在高优先级总计划口径，而在“续轮入口仍把旧基准 ExecPlan 当成当前唯一执行计划”
- 后续继续推进时，应以 `stage6_release_package_assembly_review_sheet.md` + 最新 addendum 作为当前入口；原 `.agent/execplan_stage6_release_package_assembly_review.md` 只保留第九子单元基准说明

## Why It Matters

- 第三轮之后，`next_step.md` 已开始把 addendum 纳入建议阅读，但 `deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md` 与 `repo_map.md` 仍把旧的 `.agent/execplan_stage6_release_package_assembly_review.md` 写成“当前固定执行计划”。
- 这不会触发单段 actual units 回写，但会让下一轮入口重新落回旧基准时点，削弱“续轮只做 assembly / review 复核”的当前主线。

## Inputs and Evidence

- `docs/00_project/stage6_release_package_assembly_review_sheet.md`
- `.agent/execplan_stage6_release_package_assembly_review.md`
- `.agent/execplan_stage6_release_package_assembly_review_round3.md`
- `docs/00_project/deconstruction_display_overview.md`
- `docs/00_project/deconstruction_granular_codex_plan.md`
- `docs/00_project/repo_map.md`
- `docs/00_project/current_state.md`
- `docs/00_project/next_step.md`
- `docs/03_analysis/05_implementation_validation.md`

## Round-4 Findings

1. 四份 stage-6 actual units 的顺序、handoff、evidence lock 与 traceback 继续与 `ASSEMBLY-MAP-001` 对齐。
2. `ASSEMBLY-TRIGGER-001` 本轮仍未被命中，因此不存在 actual-unit 级 writeback 理由。
3. 剩余漂移现在只出现在续轮入口本身：部分高优先级 stage-6 入口文档仍把旧的 `.agent/execplan_stage6_release_package_assembly_review.md` 写成当前固定执行计划，而没有明确它现在只承担第九子单元基准说明；这会让后续会话误把旧基准口径当作当前执行口径。

## Required Writeback

- 更新 `docs/00_project/deconstruction_display_overview.md`，把“当前执行计划”改写为“review sheet + 最新 addendum”，并把旧基准 ExecPlan 降回 origin / baseline。
- 更新 `docs/00_project/deconstruction_granular_codex_plan.md` 与 `docs/00_project/repo_map.md`，把续轮入口统一写成“基准说明 + 最新覆盖说明”。
- 更新 `docs/00_project/stage6_release_package_assembly_review_sheet.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md` 与 `docs/00_project/decision_log.md`，写死第四轮审阅结论。
- 不回写任一 stage-6 actual units 承载文件。

## Validation

- review sheet 中存在 `ASSEMBLY-REVIEW-2026-04-25D`
- `deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md` 与 `repo_map.md` 不再把旧基准 ExecPlan 单独写成当前唯一执行入口
- `current_state.md` 与 `next_step.md` 已明确：阶段 6 已完成四轮受控一致性审阅，后续续轮默认读取 review sheet 与最新 addendum
- `python scripts/check_repo.py` 与 `make check` 通过

## Current Outcome

- 阶段 6 当前仍是 `no hard blocker`
- 后续默认继续按 review sheet 做受控一致性审阅（续轮）
- 只要 `ASSEMBLY-TRIGGER-001` 继续不被命中，就不回写单段 actual units；只同步 review-level 支撑文件与续轮入口口径
