# ExecPlan: Rivington Region Pack

## Goal

把 `Rivington` 固化成 `Act 3` 的首轮“入口过滤 + 外环承压”区域包：不把它写成进城前的缓冲前厅、零散支线前台或城市导览，而是先用已完成的 `Act 3 总框架` 作为上位边界，说明后期高密度并行线为什么需要先在这里被第一次分束、过滤与重排，再把稳定结论最小回写到宏观结构、任务与选择、实现验证模块。

## Why it matters

- 如果这一步写成“城市外围有什么内容”，阶段 4 会立刻退化成地点目录，`Act 3` 刚建立的“高密度城市 + 高收束压力”框架也会失焦。
- `Act 3 总框架` 已经说明后期不是“内容更多”这么简单，而是“并行线更密、前史读回更近、结算负载更重”；`Rivington` 现在必须把这层上位判断压到第一层城市子块。
- 只有先把 `Rivington` 写成“入口过滤包”，后续 `Wyrm's Crossing` 才能被写成桥梁 / 门槛 / 第二层重排区，`Lower City` 才不会被直接写成无差别的终局内容堆。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：执行 `Rivington` 首轮区域包。
- 上游已完成：
  - `.agent/execplan_act3_total_framework.md`
  - `docs/02_sources/case_note_act3_density_and_resolution_load.md`
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`
- 本轮优先回写模块是：
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- `BG3-OFF-001`：官方 About 页把 `the sprawling city of Baldur's Gate` 与 `shadow-cursed forests`、`Underdark` 并列呈现，说明 `Act 3` 对官方来说是差异化阶段节点，而不是终局前剩余内容合集。
- `BG3-OFF-002`：`Patch 7` 一方面继续集中暴露后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界，另一方面把新增 evil ending cinematics 写成 `depending on the choices you make` 的结果，说明后期不是单点结算，而是高密度状态读回区。
- `BG3-OFF-003`：Adam Smith 继续用 `Swiss cheese` 描述 BG3 的多入口结构，同时明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的结局与状态排列。
- `BG3-OFF-012`、`BG3-OFF-013`、`BG3-OFF-014`：提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，用来约束本轮只能写到“入口过滤 / quest bundle 重排”这一层，而不能提前写死 `Rivington` 内部的私有 objective 编排。

## Milestones

1. 新建 `docs/02_sources/case_note_rivington_entry_pressure.md`，把主问题锁定为“`Rivington` 如何作为 `Act 3` 的第一层入口过滤与外环承压区”，而不是地点导览。
2. 把“`Rivington` 是后期高密度并行线第一次被分束与重排的外环入口包”回写到：
   - `docs/03_analysis/01_macro_structure.md`
   - `docs/03_analysis/02_quests_and_choices.md`
   - `docs/03_analysis/05_implementation_validation.md`
3. 同步 `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md`，并在检查通过后把下一唯一主任务切到 `Wyrm's Crossing`。

## Validation

- `case_note_rivington_entry_pressure.md` 已完成，并明确把 `Rivington` 锁定为“入口过滤 + 外环承压”而不是进城前厅。
- `01_macro_structure.md` 能解释：`Act 3` 的第一层城市子块为什么不是单纯展开内容，而是先过滤密度、重排阅读顺序。
- `02_quests_and_choices.md` 能解释：`Rivington` 的价值不在于独立结算，而在于把后期并行 quest bundle 第一次压成“先碰哪些线、先承接哪些读回”的入口分束。
- `05_implementation_validation.md` 新增 `Rivington` 的验证入口，并明确哪些判断仍只能停留在公开的 `quest bundle / trigger updates` 边界。
- `current_state.md` 与 `next_step.md` 已从 `Rivington` 切到 `Wyrm's Crossing`，且没有新增硬阻塞。

## Progress

- 2026-04-24：创建本计划，作为 `Rivington` 首轮区域包的执行记录。

## Decision Log

- 2026-04-24：决定先把 `Rivington` 写成“入口过滤 + 外环承压”包，而不是把城市外围的地点、支线与过场平均摊开。
- 2026-04-24：决定继续复用 `BG3-OFF-001`、`BG3-OFF-002`、`BG3-OFF-003` 与公开 Journal 结构底座，不为追求新来源而打散当前主线。

## Surprises & Discoveries

- 当前最稳的公开锚点依然不是某条直接点名 `Rivington` 细节的官方条目，而是“城市节点定位 + 高密度状态读回 + 多入口设计语言 + Journal 公开结构”的交叉。
- 这意味着本轮最适合先压“入口过滤职责”，而不是追求地点级事实密度。

## Outcomes & Retrospective

- 完成后应直接切到 `Wyrm's Crossing`，把 `Rivington` 作为已完成的第一层过滤边界继续往下压；不要回头把它扩成城市外环百科、支线列表或剧情前厅摘要。
