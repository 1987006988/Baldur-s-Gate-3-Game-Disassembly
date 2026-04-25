# Next Step

## 当前唯一主任务

阶段 6 / `展示收束与发布导览` 已完成五段首批 actual units、首轮发布包总装配 / 审阅清单，以及截至 2026-04-26 的第三十二轮受控一致性审阅。首轮局部 trigger 与第十轮 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` traceback 修正都已保留。阶段 0 到阶段 6 的主任务现已全部结束。

当前默认状态不是“继续开 `round33`”，而是：

> 阶段 6 已闭合，仓库进入冻结后的条件触发维护态。

`docs/00_project/stage6_release_package_assembly_review_sheet.md` 现在是默认主动维护入口；`.agent/execplan_stage6_release_package_assembly_review_round32.md` 只保留为截至 2026-04-26 的最近一次维护记录。若没有新的实际 trigger，不要再把任何 `round*.md` 当成当前唯一主任务。

在未命中新 trigger 的情况下，当前没有新的默认 stage-6 执行子单元；本轮默认动作是按 `docs/01_methodology/stage6_freeze_maintenance_playbook.md` 先做 trigger 判定与 maintenance pass，再决定是否只停在 review-layer / 状态入口维护。

## 当前默认动作

1. 维持阶段 6 冻结维护态，不新增新的 review round。
2. 把 `round*.md` 视为维护记录链，而不是默认主动推进主线。
3. 先按 `docs/01_methodology/stage6_freeze_maintenance_playbook.md` 执行四步 maintenance pass；只有命中新 trigger 时，才先读 `review sheet`，再按需要读取最近一次维护记录并决定是否新增新的维护 addendum。

## 只有以下情况才允许重开 Stage 6 Review

1. 五段 actual units 之一发生正文级改动。
2. `entry / opening / camp / closing / final` 的 handoff 顺序发生变化。
3. evidence lock 或 benchmark traceback 出现回退、缺失、错链。
4. release package assembly map 被改动后需要重新校对。
5. 项目负责人明确要求对发布链做新一轮一致性审阅。

## 以下情况不应重开

1. 只是为了“再谨慎检查一轮”。
2. 没有新的正文改动，也没有新的 trigger。
3. 只是 latest addendum 文件名还可以继续递增。
4. 没有任何 evidence / assembly / handoff 层面的实质变化。

## 若未来确需重开，建议先读

- `README.md`
- `docs/00_project/current_state.md`
- `docs/00_project/deconstruction_master_execution_plan.md`
- `docs/00_project/stage6_release_package_assembly_review_sheet.md`
- `.agent/execplan_stage6_release_package_assembly_review_round32.md`
- `docs/03_analysis/05_implementation_validation.md`
- `docs/01_methodology/stage6_freeze_maintenance_playbook.md`

## 完成后必须更新

- `docs/00_project/current_state.md`
- `docs/00_project/next_step.md`
- `docs/00_project/decision_log.md`（如有新的决策变化）
- `docs/00_project/stage6_release_package_assembly_review_sheet.md` 与实际命中新 trigger 的承载文件（如有）
- `docs/01_methodology/stage6_freeze_maintenance_playbook.md`（如维护动作或判定顺序发生变化）
