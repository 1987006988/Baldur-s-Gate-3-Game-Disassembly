# ExecPlan: Lower City Region Pack

## Goal

把 `Lower City` 固化成 `Act 3` 的首轮“更高密度的内城并行 / 结算区”区域包：不把它写成内城景点导览、派系列表或支线总表，而是以前面已完成的 `Act 3 总框架`、`Rivington` 与 `Wyrm's Crossing` 为上位 / 上游边界，说明后期并行线为什么会在这里从“已被过滤、已被门槛化重排”继续压成更高密度的内城并行承接与局部结算负载。

## Why it matters

- 如果这一步退化成“内城里有什么内容”，阶段 4 会直接滑回城市百科，前面刚建立的“高密度承压 -> 第一层过滤 -> 第二层门槛重排”三段结构会断掉。
- `Wyrm's Crossing` 已经把后期并行线压成桥梁 / 门槛式第二层重排；`Lower City` 现在必须继续说明，这些已被重排的问题束如何在更靠近城市核心的位置变成更高密度的并行承接与局部结算区，而不是继续重复“过桥”或“过检查点”。
- 只有先把 `Lower City` 写成“更高密度的内城并行 / 结算区”，后续 `终局组织与收束压力` 才能被写成更进一步的终局压缩与组织层，而不是把所有后期功能都提前塞进 `Lower City`。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：执行 `Lower City` 首轮区域包。
- 上游已完成：
  - `.agent/execplan_act3_total_framework.md`
  - `.agent/execplan_rivington_region_pack.md`
  - `.agent/execplan_wyrms_crossing_region_pack.md`
  - `docs/02_sources/case_note_act3_density_and_resolution_load.md`
  - `docs/02_sources/case_note_rivington_entry_pressure.md`
  - `docs/02_sources/case_note_wyrms_crossing_bridge_and_gate_pack.md`
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`
- 本轮优先回写模块是：
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- `BG3-OFF-001`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为 BG3 的阶段级城市节点直接点名，说明 `Act 3` 对官方来说是差异化的城市阶段，而不是终局前剩余内容的泛称。
- `BG3-OFF-002`：`Patch 7` 一方面把新的 evil ending cinematics 写成会 `depending on the choices you make` 出现，另一方面继续集中修复后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界，说明后期不是单点结算，而是更高密度的状态读回区。
- `BG3-OFF-003`：Adam Smith 继续用 `Swiss cheese` 描述 BG3 的多入口结构，并明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。
- `BG3-OFF-012`、`BG3-OFF-013`、`BG3-OFF-014`：提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，用来约束本轮只写到“内城并行 quest bundle / 结算负载”的公开可验证层，而不假装掌握 `Lower City` 的私有 objective 编排。

## Milestones

1. 新建 `docs/02_sources/case_note_lower_city_faction_resolution_pack.md`，把主问题锁定为“`Lower City` 如何把已在 `Rivington` 被第一次过滤、在 `Wyrm's Crossing` 被第二层门槛化的问题束，继续压成更高密度的内城并行 / 结算区”，而不是内城地点导览或派系百科。
2. 把“`Lower City` 是 `Act 3` 更高密度的内城并行 / 结算区”回写到：
   - `docs/03_analysis/01_macro_structure.md`
   - `docs/03_analysis/02_quests_and_choices.md`
   - `docs/03_analysis/05_implementation_validation.md`
3. 同步 `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md`，并在检查通过后把下一唯一主任务切到 `终局组织与收束压力`。

## Validation

- `case_note_lower_city_faction_resolution_pack.md` 已完成，并明确把 `Lower City` 锁定为“更高密度的内城并行 / 结算区”，而不是内城景点导览、派系列表或终局总包。
- `01_macro_structure.md` 能解释：为什么 `Act 3` 的第三个城市子块不只是继续扩内容，而是把前两层过滤 / 门槛继续压成更靠近城市核心的并行与结算承压区。
- `02_quests_and_choices.md` 能解释：`Lower City` 的任务层价值不在于列出更多派系线，而在于这些 late-game quest bundle 开始以更短窗口同时要求承接、重读与局部结算。
- `05_implementation_validation.md` 新增 `Lower City` 的验证入口，并明确哪些判断仍只能停留在公开的 `quest bundle / trigger updates / ending feedback / flow` 边界。
- `current_state.md` 与 `next_step.md` 已从 `Lower City` 切到 `终局组织与收束压力`，且没有新增硬阻塞。

## Progress

- 2026-04-24：创建本计划，作为 `Lower City` 首轮区域包的执行记录。

## Decision Log

- 2026-04-24：决定先把 `Lower City` 写成“更高密度的内城并行 / 结算区”，而不是把内城各片区、派系线和局部事件平均摊开。
- 2026-04-24：决定继续复用 `BG3-OFF-001`、`BG3-OFF-002`、`BG3-OFF-003` 与公开 Journal 结构底座，不为了追求“新来源”而打断当前 `Act 3` 城市子块的连续推进。

## Surprises & Discoveries

- 当前最稳的公开锚点依然不是某条直接点名 `Lower City` 内部细节的官方条目，而是“城市阶段定位 + 选择驱动的 ending feedback + 开发者承认后期状态排列更密 + Journal 公开结构”的交叉。
- 这意味着本轮最适合先压“更高密度的内城并行 / 结算职责”，而不是追求具体地点级事实密度。

## Outcomes & Retrospective

- 完成后应直接切到 `终局组织与收束压力`，把 `Lower City` 作为已完成的高密度内城承压区继续往下压；不要回头把它扩成内城百科、派系列表或全支线总表。
