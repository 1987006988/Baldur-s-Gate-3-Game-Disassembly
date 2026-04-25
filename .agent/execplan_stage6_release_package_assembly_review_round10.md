# ExecPlan Addendum: Stage-6 Release Package Assembly Review Round 10

## Goal

为阶段 6 的第十轮受控一致性审阅提供一份最新续轮覆盖说明，明确：
- 本轮首次命中的是 `ASSEMBLY-TRIGGER-001` 的 trigger `5`
- 命中的不是顺序 / handoff 冲突，而是 `入口页` 在收尾层与 review-level evidence lock 中的 traceback path 被压窄
- `ENTRY-TRACE-001` 原本保留的 `BMK-002 / BMK-003` benchmark 回链，必须与 `BG3-OFF-001 / BG3-OFF-003` 一起继续留在 `FINAL-ASSET-001`、`FINAL-TRACE-001` 与 `ASSEMBLY-MAP-001` 的 source-entry 层
- 后续继续推进时，仍以 `stage6_release_package_assembly_review_sheet.md` + 最新 addendum 作为当前入口；`.agent/execplan_stage6_release_package_assembly_review.md` 继续只保留第九子单元基准说明

## Why It Matters

- 前九轮审阅的剩余漂移主要是“最新 addendum 指针”本身；本轮第一次出现需要精确回写 actual-unit / analysis 锚点的真实 trigger
- 这个 trigger 不大，但性质明确：如果收尾层把 `入口页` 的 benchmark 来源压缩成只剩 BG3 官方来源，那么发布包虽然还保留了“入口页”这一行，却丢掉了“为什么入口页可以用这套方法成立”的完整 traceback
- 若不修，仓库会在收尾层默认把 `BMK-002 / BMK-003` 当成只存在于前置方法层、而不是仍对 `入口页` 的 release evidence 生效

## Inputs and Evidence

- `docs/00_project/stage6_release_package_assembly_review_sheet.md`
- `.agent/execplan_stage6_release_package_assembly_review.md`
- `.agent/execplan_stage6_release_package_assembly_review_round9.md`
- `docs/00_project/stage6_entry_first_section_release_units.md`
- `docs/00_project/stage6_final_section_release_units.md`
- `docs/03_analysis/05_implementation_validation.md`
- `docs/00_project/deconstruction_display_overview.md`
- `docs/00_project/deconstruction_granular_codex_plan.md`
- `docs/00_project/repo_map.md`
- `docs/00_project/current_state.md`
- `docs/00_project/next_step.md`
- `docs/00_project/source_index.md`

## Round-10 Findings

1. 五段 stage-6 actual units 的顺序、handoff 与职责边界继续与 `ASSEMBLY-MAP-001` 对齐。
2. 本轮命中 `ASSEMBLY-TRIGGER-001` 的 trigger `5`：
   - `ENTRY-TRACE-001` 明确保留 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003`
   - 但 `FINAL-ASSET-001`、`FINAL-TRACE-001` 与 `ASSEMBLY-MAP-001` 在收尾层 / review-level 的 source-entry 层一度只剩 BG3 官方来源
   - 这会让 `入口页` 的 traceback path 从“benchmark 方法 + BG3 官方高层锚点”被压缩成“只有 BG3 官方高层锚点”
3. 该问题不要求重写前四段 actual units，也不要求回跳阶段 5；只需要精确回写收尾层与验证层，把 `入口页` 的 benchmark traceback 补回。

## Required Writeback

- 回写 `docs/00_project/stage6_final_section_release_units.md`：
  - 在 `FINAL-ASSET-001` 中明确 `入口页` 这一行必须保留 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003`
  - 在 `FINAL-TRACE-001` 中补回 `BMK-002 / BMK-003`
- 回写 `docs/03_analysis/05_implementation_validation.md`：
  - 在阶段 6 收尾段 evidence lock 中补回 `BMK-002 / BMK-003`
  - 在 assembly review anchor / evidence lock 中补回 `入口页` 的 benchmark traceback
  - 记录第十轮审阅命中的 traceback-path trigger 及其修复
- 更新 `docs/00_project/stage6_release_package_assembly_review_sheet.md`，写明第十轮审阅结论
- 更新 `docs/00_project/deconstruction_display_overview.md`、`docs/00_project/deconstruction_granular_codex_plan.md`、`docs/00_project/repo_map.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`，把当前入口推进到 `round10`

## Validation

- review sheet 中存在 `ASSEMBLY-REVIEW-2026-04-25J`
- `stage6_final_section_release_units.md` 与 `05_implementation_validation.md` 已重新保留 `入口页` 的 `BMK-002 / BMK-003` benchmark traceback
- `deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 已把当前最新 addendum 推进到 `.agent/execplan_stage6_release_package_assembly_review_round10.md`
- `python scripts/check_repo.py` 与 `make check` 通过

## Current Outcome

- 阶段 6 当前仍是 `no hard blocker`
- 当前最新 addendum 已推进到 `round10`
- 后续默认继续按 `review sheet + 最新 addendum` 执行受控一致性审阅
- 只要不再命中 `ASSEMBLY-TRIGGER-001`，就不继续回写其它单段 actual units；只同步 review-level 入口与状态文件
