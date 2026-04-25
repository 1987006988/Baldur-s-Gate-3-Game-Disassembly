# ExecPlan: Quest Reactivity Cross-Act Readback Spine

## Goal

把阶段 5 / `Quest Reactivity` 的首个横向子单元固化为一条可复用的跨阶段状态回流主干：不把 `02_quests_and_choices.md` 扩成全任务表，而是把 `Grove / Goblin` 的处理矩阵、`Last Light / Moonrise / Gauntlet` 的中盘收束点组，以及 `Rivington -> Wyrm's Crossing -> Lower City -> 终局组织与收束压力` 的 late-game 压缩梯，压成同一条 `Act 1 -> Act 2 -> Act 3` 读回链。

## Why it matters

- 如果这一轮仍只按区域包逐块补写，阶段 5 就会退回“局部结论很多，但没有横向主干”的状态。
- 如果这一轮直接扩成全任务表，仓库会重新滑回旧的抽象模块跳转与剧情复述。
- 这条跨阶段主干是当前最稳的公开证据闭合链：`Act 1` 已有处理方式 / 时序 / 营地折返边界，`Act 2` 已有明确的跨 Act 读回落点，`Act 3` 已有高密度 quest bundle 的过滤、重排、并行承接与组织级压缩阶梯。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：进入阶段 5 / `Quest Reactivity`，优先把 `Grove / Goblin`、`Act 2` 收束点组与 `Act 3` 到终局组织的链条压成横向主干。
- 上游已完成并可直接复用：
  - `docs/02_sources/case_note_grove_goblin_resolution_matrix.md`
  - `docs/02_sources/case_note_last_light_moonrise_gauntlet_convergence.md`
  - `docs/02_sources/case_note_act3_density_and_resolution_load.md`
  - `docs/02_sources/case_note_rivington_entry_pressure.md`
  - `docs/02_sources/case_note_wyrms_crossing_bridge_and_gate_pack.md`
  - `docs/02_sources/case_note_lower_city_faction_resolution_pack.md`
  - `docs/02_sources/case_note_endgame_organization_compression.md`
- 本轮主回写模块：
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`
  - 如有必要最小回写 `docs/03_analysis/01_macro_structure.md`

## Inputs and evidence

- `BG3-OFF-004`：提供 `Grove / Goblin` 中 `knocked out` / `killed`、长休时序与 `journal wording` 边界。
- `BG3-OFF-008`：提供 `Grove / Goblin` 冲突下游的营地可达性与 `companion reaction` 边界。
- `BG3-OFF-002`：提供 `Moonrise Towers` 的跨 Act 读回、`Act II` / late-game `writing and flow`、`scripting` 与 ending feedback 锚点。
- `BG3-OFF-001`, `BG3-OFF-003`：提供阶段级城市节点与 `Swiss cheese` 多入口设计语言。
- `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`：提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，用于约束这一轮只写到公开可验证的层级。

## Milestones

1. 新建 `docs/02_sources/case_note_quest_reactivity_cross_act_readback_spine.md`
   - 只压一条最强主干：`Grove / Goblin -> Act 2 收束点组 -> Act 3 压缩梯`
   - 明确哪些链段已经足以升级为跨阶段主干，哪些仍只能停留在区域包层
2. 回写 `docs/03_analysis/02_quests_and_choices.md`
   - 新增一段跨阶段主干总结，不再只让 `Act 1`、`Act 2`、`Act 3` 分散停留在各自 supplement
   - 明确这条链解释的是“处理方式如何被反复读回”，不是“任务分支有多少”
3. 回写 `docs/03_analysis/05_implementation_validation.md`
   - 把 `objective / step` 与 `bundle / flow / ending feedback` 的边界写成分层矩阵
   - 明确 `Act 1`、`Act 2`、`Act 3` 三段各自可升级到哪一层
4. 同步状态文件与索引
   - 更新 `current_state.md`、`next_step.md`、`decision_log.md`
   - 如新增 `Where used`，同步 `source_index.md`
   - 运行 `python scripts/check_repo.py` 与 `make check`

## Validation

- `docs/03_analysis/02_quests_and_choices.md` 明确写出至少 1 条 `Act 1`、1 条 `Act 2`、1 条 `Act 3` 的跨阶段状态回流链。
- `docs/03_analysis/05_implementation_validation.md` 明确区分：
  - 哪些判断已足以写到 `objective / step`
  - 哪些判断目前只能停留在 `bundle / flow / ending feedback`
- `docs/00_project/current_state.md` 与 `docs/00_project/next_step.md` 能直接说明：阶段 5 已正式展开，且本轮完成的是首个跨阶段主干子单元。
- 不新增任何与该主干无关的区域包扩写、剧情摘要或无关来源侦察。

## Progress

- 2026-04-24：创建本计划，锁定阶段 5 / `Quest Reactivity` 的首个横向子单元为“跨阶段状态回流主干”。

## Decision Log

- 2026-04-24：决定阶段 5 先压最强的 `cross-act readback spine`，而不是回头补 `Act 1` / `Act 2` / `Act 3` 的全任务表。
- 2026-04-24：决定当前最稳的横向主干不以“某条任务完整 objective 表”呈现，而以“处理矩阵 -> 收束点组 -> 高密度压缩梯”呈现。

## Surprises & Discoveries

- 当前最稳的公开实锚仍集中在 `Minthara` 路径与 `Moonrise Towers` 的跨 Act 读回；这说明阶段 5 的首轮综合更适合压“读回主干”，而不是强行拼出一张假装完整的任务总表。
- `Act 3` 的公开边界已经足够支撑过滤、门槛化、并排承接与组织级压缩四层阶梯，但仍不足以反推每一层的私有 objective 编排。

## Outcomes & Retrospective

- 本子单元完成后，阶段 5 应继续停留在 `Quest Reactivity`，下一步优先补“上游入口 / 改道 / 门槛链”如何服务当前主干，而不是跳回无关模块或重新扩 `Act 3`。
