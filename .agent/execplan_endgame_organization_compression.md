# ExecPlan: Endgame Organization and Resolution Pressure

## Goal

把 `终局组织与收束压力` 固化成 `Act 3` 的首轮“组织级终局压缩 / ending feedback 读取层”子单元：不把它写成 Boss 顺序表、终局剧情提要或结局百科，而是以前面已经完成的 `Act 3 总框架`、`Rivington`、`Wyrm's Crossing` 与 `Lower City` 为上游边界，说明后期为什么会从“更高密度的内城并行 / 结算负载”继续压到“更少、更硬的终局组织位与收束压力”。

## Why it matters

- 如果这一步退化成“最后都发生了什么”，阶段 4 会直接从区域包执行法滑回剧情复述，`Act 3` 前面刚建立的“入口过滤 -> 门槛重排 -> 内城并行 / 结算负载”三层结构也会断掉。
- `Lower City` 已经证明，后期问题束在城市核心会以更短窗口并排承接；`终局组织与收束压力` 现在必须继续说明，这些已被并排承接的问题束如何不再只是“很多事同时发生”，而开始被组织级终局位读取、压缩与逼向 ending feedback。
- 只有先把这一层写成“组织级压缩”，阶段 4 / `Act 3` 才算真正闭合；否则仓库只是在城市子块上停住，还没有回答 BG3 后期为什么会被感知成“事很多，而且每件事都在逼近终局”。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：执行 `终局组织与收束压力` 子单元。
- 上游已完成：
  - `.agent/execplan_act3_total_framework.md`
  - `.agent/execplan_rivington_region_pack.md`
  - `.agent/execplan_wyrms_crossing_region_pack.md`
  - `.agent/execplan_lower_city_region_pack.md`
  - `docs/02_sources/case_note_act3_density_and_resolution_load.md`
  - `docs/02_sources/case_note_rivington_entry_pressure.md`
  - `docs/02_sources/case_note_wyrms_crossing_bridge_and_gate_pack.md`
  - `docs/02_sources/case_note_lower_city_faction_resolution_pack.md`
- 本轮优先回写模块是：
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- `BG3-OFF-001`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为阶段级城市节点直接点名，说明后期不是“终局前剩余内容”的散装集合，而是一整块城市化阶段。
- `BG3-OFF-002`：`Patch 7` 一方面把新的 evil ending cinematics 写成会 `depending on the choices you make` 出现，另一方面继续集中修复后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界，说明终局读取不是单点按钮，而是高密度状态读回区。
- `BG3-OFF-003`：Adam Smith 继续用 `Swiss cheese` 描述 BG3 的多入口结构，并明确说团队上线后继续补了大量额外 dialogue / cinematics 去覆盖更高密度的状态与结局排列，说明后期不是“多入口失效”，而是“多入口进入更高读回负载”。
- `BG3-OFF-012`、`BG3-OFF-013`、`BG3-OFF-014`：提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，用来约束本轮只写到“组织级 quest bundle 压缩 / ending feedback 读取层”，而不假装掌握终局私有 objective 编排。

## Milestones

1. 新建 `docs/02_sources/case_note_endgame_organization_compression.md`，把主问题锁定为“终局组织如何承接 `Lower City` 已建立的高密度并行 / 结算负载，并继续压成组织级终局收束”，而不是终局剧情摘要。
2. 新建 `.agent/execplan_endgame_organization_compression.md`，固定这块的完成标准、写作边界与下游切换条件。
3. 把“`终局组织与收束压力` 是 `Act 3` 的组织级压缩层，而不是终局剧情提要”最小回写到：
   - `docs/03_analysis/01_macro_structure.md`
   - `docs/03_analysis/02_quests_and_choices.md`
   - `docs/03_analysis/05_implementation_validation.md`
4. 同步 `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md`，并在检查通过后把下一唯一主任务切到阶段 5 / `Quest Reactivity`。

## Validation

- `case_note_endgame_organization_compression.md` 已完成，并明确把 `终局组织与收束压力` 锁定为“组织级终局压缩 / ending feedback 读取层”，而不是 Boss 顺序表或结局百科。
- `01_macro_structure.md` 能解释：为什么 `Act 3` 在 `Lower City` 之后不只是继续增加密度，而是开始把已高密度并排承接的问题束压向更少、更硬的终局组织位。
- `02_quests_and_choices.md` 能解释：终局组织层的价值不在于补一份最终分支表，而在于把 late-game quest bundle 从“并排要处理”继续压成“必须被组织级收束位读取 / 重排 / 逼向 ending feedback”。
- `05_implementation_validation.md` 新增 `终局组织与收束压力` 的验证入口，并明确哪些判断仍只能停留在公开可验证的 `quest bundle / trigger updates / ending feedback / flow` 边界。
- `current_state.md` 与 `next_step.md` 已表明：阶段 4 / `Act 3` 首轮闭合完成，下一唯一主任务切到阶段 5 / `Quest Reactivity`。

## Progress

- 2026-04-24：创建本计划，作为 `终局组织与收束压力` 子单元的执行记录。

## Decision Log

- 2026-04-24：决定先把 `终局组织与收束压力` 写成“组织级终局压缩 / ending feedback 读取层”，而不是把终局组织、Boss 顺序与结局段落平均摊开。
- 2026-04-24：决定继续复用 `BG3-OFF-001`、`BG3-OFF-002`、`BG3-OFF-003` 与公开 Journal 结构底座，不为追求“新来源”而打断当前 `Act 3` 闭合。

## Surprises & Discoveries

- 当前最稳的公开锚点仍然不是某条直接点名终局组织细节的单条官方说明，而是“城市阶段定位 + ending feedback + 后期 flow / scripting 维护 + 多入口设计语言 + Journal 公开结构”的交叉。
- 这意味着本轮最适合先压“组织级压缩职责”，而不是追求终局地点级或 Boss 级事实密度。

## Outcomes & Retrospective

- 完成后应直接切到阶段 5 / `Quest Reactivity`，把 `Act 1` 到 `Act 3` 已跑通的区域包重新压成横向状态回流主干；不要回头把 `Act 3` 扩成城市百科或终局剧情摘要。
