# ExecPlan: Stage-6 Freeze Maintenance Stabilization

## Goal

把阶段 6 的维护入口从“`latest addendum` 指针随轮次漂移”收口成稳定的冻结维护态：

- `docs/00_project/stage6_release_package_assembly_review_sheet.md` 成为唯一主动维护入口
- `.agent/execplan_stage6_release_package_assembly_review_round*.md` 退回维护记录链
- 不再因为“当前最新 round 文件名又变了”而自然诱发 `round33`

## Why It Matters

- 当前高优先级计划已经明确：阶段 6 已闭合，默认动作不是继续开新 round，而是维持条件触发维护态
- 但 round11 到 round32 的 review-level 漂移修正，仍把“latest addendum 指针同步”写成一种可重复的动作模板
- 如果不把这层再压一次，后续会话即使没有新 trigger，也仍会被文件口径牵引回“再做一轮 addendum”

## Repository Context

- 唯一高优先级依据：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 直接相关维护入口：
  - `docs/00_project/stage6_release_package_assembly_review_sheet.md`
  - `.agent/execplan_stage6_release_package_assembly_review.md`
  - `.agent/execplan_stage6_release_package_assembly_review_round32.md`
- 直接相关正文与状态文件：
  - `docs/03_analysis/05_implementation_validation.md`
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
  - `docs/00_project/decision_log.md`

## Inputs and Evidence

- 阶段 6 首批发布包已经闭合
- 第十轮局部 trigger 修复已把 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 补回
- 第十一轮到第三十二轮没有新的 actual-unit 级 trigger
- 当前剩余问题不在单段 release units，而在 review-level 入口仍容易把“最新 round 文件名”误读成主动主线

## Milestones

1. 新建 freeze-maintenance stabilization ExecPlan
   - 只描述本轮收口目标，不重开阶段 5 或单段 actual-unit 改写
2. 收口 review sheet
   - 保留 `assembly map`、`review checklist`、`writeback trigger`
   - 只保留关键历史审阅节点与冻结维护规则
   - 不再把 round11 到 round32 的指针递增写成持续主线
3. 回写 implementation validation
   - 把“pointer drift 只是 review-level 维护噪音，不是新 trigger”写进正文
4. 同步高优先级入口与状态文件
   - `deconstruction_display_overview.md`
   - `deconstruction_master_execution_plan.md`
   - `deconstruction_granular_codex_plan.md`
   - `current_state.md`
   - `next_step.md`
   - `decision_log.md`

## Validation

- `stage6_release_package_assembly_review_sheet.md` 不再要求默认读取“review sheet + latest addendum”才算进入维护态
- `05_implementation_validation.md` 已把 round10 修复、round11-32 无新 trigger、以及冻结维护入口稳定化写成统一证据段
- `deconstruction_granular_codex_plan.md` 不再把“冻结维护态稳定化”写成当前待执行子单元，而是改写为默认维护态规则
- `deconstruction_display_overview.md`、`deconstruction_master_execution_plan.md`、`deconstruction_granular_codex_plan.md`、`current_state.md`、`next_step.md` 的当前口径一致：
  - review sheet 是主动入口
  - round32 只是截至 2026-04-26 的最近一次维护记录
  - 没有新 trigger 就不应新开 round
- `python scripts/check_repo.py` 与 `make check` 通过

## Progress

- 2026-04-26：创建本计划，锁定当前唯一可推进子单元为“冻结维护态稳定化”，不新增新的 stage-6 review round。
- 2026-04-26：完成高优先级计划 / 状态 / 实现验证同步，把 `deconstruction_granular_codex_plan.md` 的当前动作改写为“默认维护态”，并把 `current_state.md`、`05_implementation_validation.md` 中 round11-32 的逐轮指针漂移叙述压缩回维护记录链。

## Decision Log

- 2026-04-26：决定把阶段 6 的主动入口进一步收口为 review sheet 本身，而不是继续依赖“latest addendum 指针”。
- 2026-04-26：决定保留 `round*.md` 作为维护记录链，但不再让它们通过文件名递增驱动默认主线。

## Outcomes & Retrospective

- 本子单元完成后，阶段 6 的默认动作将从“继续同步最新 round 文件名”改成“只维持冻结维护规则”
- 若未来再次命中新 trigger，应先从 review sheet 读取重开条件，再按需要补新的维护记录，而不是因为入口口径落后就自动续轮
- round11-32 的逐轮漂移细节现在继续保留在 `review sheet` 与 `round*.md` 维护记录链中；状态页与实现验证页只保留仍会影响后续判断的维护结论
