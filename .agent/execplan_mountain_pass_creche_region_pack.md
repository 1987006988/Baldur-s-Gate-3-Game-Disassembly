# ExecPlan: Mountain Pass / Creche Region Pack

## Goal

把 `Mountain Pass / Creche` 固化为 `Act 1` 后段的第一块“gate + party tension”区域包：先补 1 条直接点名 `Creche` 的官方来源，再新建聚焦于结构门槛、阵营 / 权威压力与 `Lae'zel` 相关即时 / 延迟反应的 case note，最后把稳定结论最小回写到宏观结构、营地 / 同伴、任务与实现验证模块。

## Why it matters

- 这是 `Act 1` 最容易被误写成剧情冲突复述的一块；如果不先锁定口径，仓库很容易从区域包推进退回角色专章或剧情摘要。
- `Underdark` 与 `Grymforge` 已经证明 late `Act 1` 不是简单尾声，但它们更偏向“阶段重构”与“遭遇压缩”；`Mountain Pass / Creche` 则要回答进入中盘前的高压门槛如何与伙伴张力叠在一起。
- 做稳这一块后，仓库就能顺利切到 `Act 2 总框架`，而不是继续滞留在 `Act 1` 尾部补零散细节。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：执行 `Mountain Pass / Creche` 首轮区域包。
- 上游已完成：
  - `.agent/execplan_underdark_region_pack.md`
  - `.agent/execplan_grymforge_region_pack.md`
  - `docs/02_sources/case_note_underdark_entry_choice_pack.md`
  - `docs/02_sources/case_note_grymforge_environment_resolution.md`
- 本轮需要优先回写的模块是：
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/03_party_and_camp.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- 多入口 / 非常规 problem-solving 的高层设计语言：`BG3-OFF-003`
- `Mountain Pass / Creche` 相关的对话门槛、敌意状态、即时伙伴反应与 `camp night` 后果读取边界：`BG3-OFF-016`

## Milestones

1. 新建 `docs/02_sources/source_note_bg3_off_016_patch_3_creche_tension.md`，把 `Patch #3` 中与 `Mountain Pass / Creche` 直接相关的边界压成可引用事实。
2. 新建 `docs/02_sources/case_note_mountain_pass_creche_gate_and_party_tension.md`，只记录：区域门槛、冲突 / 权威对象、伙伴反应、后续影响。
3. 把“`Mountain Pass / Creche` 是 late `Act 1` 的高压门槛包，而不是剧情冲突摘要”的稳定结论回写到：
   - `docs/03_analysis/01_macro_structure.md`
   - `docs/03_analysis/03_party_and_camp.md`
   - 必要时的 `docs/03_analysis/02_quests_and_choices.md`
   - `docs/03_analysis/05_implementation_validation.md`
4. 同步 `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md`；若检查通过，则把下一唯一主任务切到 `Act 2 总框架`。

## Validation

- 至少 1 条新的官方来源 `BG3-OFF-016` 已进入 `source_index.md` 并生成 source note。
- `Mountain Pass / Creche` case note 已完成，并明确把主问题锁定为“结构门槛 + 伙伴张力”。
- `01_macro_structure.md` 完成显著回写，能够解释这块为何是 `Act 1` 后段的高压入口。
- `03_party_and_camp.md` 至少完成 1 处前置压力回写，说明这块如何给 `camp night` 与伙伴反应提供上游状态。
- `05_implementation_validation.md` 新增 `Mountain Pass / Creche` 验证入口，但不把 `Act 2` 切换规则写死。
- `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md` 已同步。

## Progress

- 2026-04-24：创建本计划，作为 `Mountain Pass / Creche` 首轮区域包的执行记录。

## Decision Log

- 2026-04-24：决定这轮先把 `Mountain Pass / Creche` 写成“gate + party tension”包，而不是平均铺开结构门槛与伙伴张力两个方向。
- 2026-04-24：决定优先补 `Patch #3` 这一条直接点名 `Creche` 的官方来源，而不再只靠 `BG3-OFF-001` 与 `BG3-OFF-003` 的高层语言硬推。

## Surprises & Discoveries

- `Patch #3` 暴露的不是单一剧情 bug，而是一整组边界：`Vlaakith` 对话门槛、`Voss` 敌意变化、`Lae'zel` 即时反应与 `camp night` 读取时机，正好对应这块区域包最需要的四个面向。

## Outcomes & Retrospective

- 完成后应直接切到 `Act 2 总框架`，不要继续围绕 `Mountain Pass / Creche` 扩剧情细节、补 `gith` lore 或追单条角色争执。
