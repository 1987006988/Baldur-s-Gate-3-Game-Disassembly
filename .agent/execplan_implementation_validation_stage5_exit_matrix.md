# ExecPlan: Implementation Validation Stage-5 Exit Matrix

## Goal

把阶段 5 的当前唯一主任务固定为“统一阶段出口矩阵”，而不是继续重开任何单条横向主干：

- 把 `Quest Reactivity`、`Combat / Environment`、`Companion / Camp / Long Rest` 三条主干统一压成同一种出口结构
- 明确每条主干各自已经成立的 spine、已经锁定的 ceiling / supporting-bundle / handoff 边界
- 把这些结论回写到 `docs/03_analysis/05_implementation_validation.md`
- 只对 `02_quests_and_choices.md`、`03_party_and_camp.md`、`04_combat_and_environment.md` 做最小出口同步
- 同步 `current_state.md`、`next_step.md`、`decision_log.md`，并把下一唯一主任务切到阶段 6 / 展示收束

## Why it matters

- 如果不做这一层统一出口，后续会话仍会把三条主干分别当成“还没收完”的开放工程，继续重开第二条对称 spine、重追 camp scene，或回跳 `Act 3` 已完成子包。
- 如果只在 `05_implementation_validation.md` 里抽象总结，而不把“各主干当前到底停在哪一层”写成矩阵，仓库会继续停在零散 ceiling 结论，无法形成清楚的阶段出口。
- 阶段 5 的真正完成定义，不是“三条主干都各写了一轮”，而是“三条主干都已经被压成统一的证据分级口径”。

## Repository context

- 当前高优先级依据：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 当前直接相关的既有子单元：
  - `.agent/execplan_quest_reactivity_objective_adjacent_narrowing.md`
  - `.agent/execplan_combat_environment_second_spine_ceiling_late_game_boundary.md`
  - `.agent/execplan_companion_camp_second_public_spine_ceiling_late_game_boundary.md`
- 当前直接相关的既有 case notes：
  - `docs/02_sources/case_note_quest_reactivity_objective_adjacent_narrowing.md`
  - `docs/02_sources/case_note_combat_environment_second_spine_ceiling_late_game_boundary.md`
  - `docs/02_sources/case_note_companion_camp_second_public_spine_ceiling_late_game_boundary.md`

## Inputs and evidence

- `docs/03_analysis/05_implementation_validation.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/04_combat_and_environment.md`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-004`
- `BG3-OFF-006`
- `BG3-OFF-007`
- `BG3-OFF-008`
- `BG3-OFF-010`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-015`
- `BG3-OFF-016`

## Milestones

1. 新建阶段 5 统一收束 case note
   - 只回答三条主干现在各自的 spine / ceiling / bundle / handoff 边界
   - 不新增任何新主链，也不补新来源
2. 回写 `docs/03_analysis/05_implementation_validation.md`
   - 新增统一的 stage-5 exit matrix
   - 明确哪些判断可保守写成事实 / 当前最强解释，哪些必须停在 bundle / handoff 层
3. 最小回写 `docs/03_analysis/02_quests_and_choices.md`
   - 写清 `Quest Reactivity` 已完成收口，不再继续追第二条公开跨阶段主链
4. 最小回写 `docs/03_analysis/03_party_and_camp.md`
   - 写清营地模块当前只稳定支撑 `1` 条 public camp spine
5. 最小回写 `docs/03_analysis/04_combat_and_environment.md`
   - 写清环境模块当前只稳定支撑 `1` 条正式环境 spine
6. 同步状态与决策
   - `docs/00_project/current_state.md`
   - `docs/00_project/next_step.md`
   - `docs/00_project/decision_log.md`
7. 运行校验
   - `python scripts/check_repo.py`
   - `make check`

## Validation

- 新增 `docs/02_sources/case_note_implementation_validation_stage5_exit_matrix.md`
- `docs/03_analysis/05_implementation_validation.md` 新增统一 stage-5 exit matrix
- `docs/03_analysis/02_quests_and_choices.md`、`03_party_and_camp.md`、`04_combat_and_environment.md` 都明确写出各自主干的当前出口
- `current_state.md` 与 `next_step.md` 能直接说明：
  - 阶段 5 已从“分别建主干”切到“统一验证出口”
  - 当前公开来源下，三条主干都已完成“1 条 spine + 1 次 ceiling / boundary 收口”
  - 下一唯一主任务应切到阶段 6 / 展示收束，而不是继续回跳阶段 5

## Progress

- 2026-04-25：创建本计划，确认本轮不再扩任何单条横向主干，只处理阶段 5 的统一出口矩阵。

## Decision Log

- 2026-04-25：决定把阶段 5 的完成定义从“分别补完三条主干”升级为“把三条主干压成统一的 exit matrix”。
- 2026-04-25：决定在没有更强官方来源前，不再重开第二条对称 `Quest` / `Combat` / `Camp` spine。

## Surprises & Discoveries

- 当前最缺的不是新证据，而是把已有 ceiling 结论统一成同一种出口语法。
- 三条主干虽然内容不同，但现在都已经能被压成同一种结构：
  - `1` 条正式 spine
  - `1` 次 ceiling / supporting-bundle / handoff 收口
  - 只剩“若未来出现更强官方来源，哪些 bundle 可能再上升”这一类待验证问题

## Outcomes & Retrospective

- 本子单元完成后，阶段 5 应视为在当前公开来源下完成闭合。
- 后续若没有更强官方来源，继续留在阶段 5 的收益将低于切换到阶段 6 / 展示收束。
