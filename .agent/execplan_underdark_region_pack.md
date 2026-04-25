# ExecPlan: Underdark Region Pack

## Goal

把 `Underdark` 做成 `Act 1` 内部第一块明确的“问题框架重构”区域包：先用 1 份 `entry choice pack` case note 说明“进入地下”本身就会改写阅读顺序与下游推送关系，再把稳定结论最小回写到宏观结构、任务与选择、实现验证三个模块。

## Why it matters

- 这一块要证明：BG3 的自由推进不只来自 `Grove / Goblin` 这种“同一冲突的不同处理方式”，也来自同一阶段内部可以切换到完全不同的空间 / 问题框架。
- 如果把 `Underdark` 写成地下景观导览或支线列表，`Act 1 地表主区` 的问题网与 `Grove / Goblin` 的状态回流网就会断在这里，无法自然推到 `Grymforge`。
- 这块做稳后，仓库就能把 `Grymforge` 读成 `Underdark` 的下游高密度区域，而不是再次从零解释“为什么突然开始拆复杂战斗遭遇”。

## Repository context

- 当前唯一主任务已切到 `Underdark`。
- 上游已完成：
  - `.agent/execplan_act1_surface_region_pack.md`
  - `.agent/execplan_grove_goblin_region_pack.md`
  - `docs/02_sources/case_note_act1_surface_route_pack.md`
  - `docs/02_sources/case_note_grove_goblin_resolution_matrix.md`
- 下游已存在可衔接案例：
  - `docs/02_sources/case_note_grymforge_environment_resolution.md`
- 本轮需要同步回写的模块是：
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- 高层区域 / 产品定位：`BG3-OFF-001`
- 多入口 / 非常规 problem-solving 设计语言：`BG3-OFF-003`
- `Underdark -> Grymforge` 的官方公开桥接：`BG3-OFF-006`

## Milestones

1. 锁定 `Underdark` 的边界：只写入口选择、阶段重构与对 `Grymforge` 的推送关系，不扩成地下全区内容清单。
2. 新建 `docs/02_sources/case_note_underdark_entry_choice_pack.md`。
3. 把“`Underdark` 是 `Act 1` 内部的问题框架重构，而不是单纯新地图”的稳定结论回写到：
   - `docs/03_analysis/01_macro_structure.md`
   - `docs/03_analysis/02_quests_and_choices.md`
   - `docs/03_analysis/05_implementation_validation.md`
4. 同步状态文件；若检查通过，则把下一唯一主任务切到 `Grymforge`。

## Validation

- 至少 1 份 `Underdark` case note 完成。
- `01_macro_structure.md` 完成显著回写，明确 `Underdark` 是 `Act 1` 内部的阶段重构块。
- `02_quests_and_choices.md` 至少完成 1 段稳定回写，说明“推进框架选择”也是任务反应性的一部分。
- `05_implementation_validation.md` 只新增结构性验证入口与待验证问题，不升级私有实现断言。
- `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md` 已同步。

## Progress

- 2026-04-24：创建本计划，作为 `Underdark` 首轮区域包的执行记录。

## Decision Log

- 2026-04-24：本轮只做 1 份 `entry choice pack` case note，不拆第二份 `underdark_to_grymforge_progression` note。
- 2026-04-24：当前更稳的口径是把 `Underdark` 写成“并行路径 + 功能性转场”的复合块，而不是在“替代入口 / 纯并行区 / 纯转场”三者中硬选一个。
- 2026-04-24：现有公开来源已足以压实“阶段重构”与“通向 Grymforge 的下游设置”，但还不足以把完整地下入口矩阵和 objective 变体写成事实表。

## Outcomes & Retrospective

- 完成后若检查通过，应直接切到 `Grymforge`，不要继续围绕 `Underdark` 扩景观、扩支线或补整区导览。
