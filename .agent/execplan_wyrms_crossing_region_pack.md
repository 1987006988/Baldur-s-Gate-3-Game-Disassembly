# ExecPlan: Wyrm's Crossing Region Pack

## Goal

把 `Wyrm's Crossing` 固化成 `Act 3` 的首轮“桥梁 / 门槛 / 第二层结构重排”区域包：不把它写成单纯的过桥路线、检查点列表或通道段，而是以前面已完成的 `Act 3 总框架` 与 `Rivington` 为上位 / 上游边界，说明后期高密度并行线为什么会在这里从“第一层入口过滤”进一步压成“带门槛的第二层重排”。

## Why it matters

- 如果这一步退化成“桥上有什么内容”，阶段 4 会再次滑回城市导览，`Rivington` 刚建立的“第一层过滤”与 `Act 3` 的“高密度承压框架”都会失去连续性。
- `Rivington` 已经证明后期并行线会先被分束；`Wyrm's Crossing` 现在必须进一步说明，这些已被分束的问题如何在更靠近城市核心的位置被加上桥梁 / 门槛压力，并重新组织阅读顺序。
- 只有先把 `Wyrm's Crossing` 写成“第二层重排包”，后续 `Lower City` 才能被写成更高密度的内城并行 / 结算区，而不是继续重复“入口过滤”或“桥头门槛”。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：执行 `Wyrm's Crossing` 首轮区域包。
- 上游已完成：
  - `.agent/execplan_act3_total_framework.md`
  - `.agent/execplan_rivington_region_pack.md`
  - `docs/02_sources/case_note_act3_density_and_resolution_load.md`
  - `docs/02_sources/case_note_rivington_entry_pressure.md`
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`
- 本轮优先回写模块是：
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- `BG3-OFF-001`：官方 About 页把 `the sprawling city of Baldur's Gate` 与其他阶段级区域并列呈现，说明 `Act 3` 对官方来说是差异化城市阶段，而不是终局前剩余内容的泛称。
- `BG3-OFF-002`：`Patch 7` 一方面继续集中修复后期 `writing and flow`、`scripting`、角色反应与长休 / 营地边界，另一方面把新的 evil ending cinematics 写成会 `depending on the choices you make` 出现，说明后期不是单点结算，而是更密的状态读回区。
- `BG3-OFF-003`：Adam Smith 继续用 `Swiss cheese` 描述 BG3 的多入口结构，并明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。
- `BG3-OFF-012`、`BG3-OFF-013`、`BG3-OFF-014`：提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，用来约束本轮只能写到“桥梁 / 门槛如何重排 late-game quest bundle”这一层，而不能提前假装掌握 `Wyrm's Crossing` 的私有 objective 编排。

## Milestones

1. 新建 `docs/02_sources/case_note_wyrms_crossing_bridge_and_gate_pack.md`，把主问题锁定为“`Wyrm's Crossing` 如何把 `Rivington` 已完成的第一层过滤继续压成桥梁 / 门槛 / 第二层结构重排包”，而不是桥头地点导览。
2. 把“`Wyrm's Crossing` 是后期并行线由入口过滤走向带门槛重排的第二层结构节点”回写到：
   - `docs/03_analysis/01_macro_structure.md`
   - `docs/03_analysis/02_quests_and_choices.md`
   - `docs/03_analysis/05_implementation_validation.md`
3. 同步 `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md`，并在检查通过后把下一唯一主任务切到 `Lower City`。

## Validation

- `case_note_wyrms_crossing_bridge_and_gate_pack.md` 已完成，并明确把 `Wyrm's Crossing` 锁定为“桥梁 / 门槛 / 第二层结构重排”，而不是过桥路线或桥头内容清单。
- `01_macro_structure.md` 能解释：为什么 `Act 3` 的第二个城市子块不只是继续展开内容，而是开始把已被过滤的并行线压到更靠近城市核心的门槛结构上。
- `02_quests_and_choices.md` 能解释：`Wyrm's Crossing` 的任务层价值不在于马上结算，而在于把 late-game quest bundle 进一步改写成“哪些读回已变成必须跨过的门槛、哪些仍被留待后续内城处理”。
- `05_implementation_validation.md` 新增 `Wyrm's Crossing` 的验证入口，并明确哪些判断仍只停留在公开可验证的 `quest bundle / trigger updates / flow` 边界。
- `current_state.md` 与 `next_step.md` 已从 `Wyrm's Crossing` 切到 `Lower City`，且没有新增硬阻塞。

## Progress

- 2026-04-24：创建本计划，作为 `Wyrm's Crossing` 首轮区域包的执行记录。

## Decision Log

- 2026-04-24：决定先把 `Wyrm's Crossing` 写成“桥梁 / 门槛 / 第二层结构重排”包，而不是把桥头地点、检查点与派系线平均摊开。
- 2026-04-24：决定继续复用 `BG3-OFF-001`、`BG3-OFF-002`、`BG3-OFF-003` 与公开 Journal 结构底座，不为追求新来源而打断当前 `Act 3` 城市子块的连续推进。

## Surprises & Discoveries

- 当前最稳的公开锚点依然不是某条直接点名 `Wyrm's Crossing` 内部 quest 细节的官方条目，而是“城市阶段定位 + 后期 flow / reaction 维护 + 多入口设计语言 + Journal 公开结构”的交叉。
- 这意味着本轮最适合先压“第二层门槛 / 重排职责”，而不是追求地点级事实密度。

## Outcomes & Retrospective

- 完成后应直接切到 `Lower City`，把 `Wyrm's Crossing` 作为已完成的桥梁 / 门槛节点继续往下压；不要回头把它扩成桥头百科、检查点列表或过桥剧情摘要。
