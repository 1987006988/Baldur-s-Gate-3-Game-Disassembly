# ExecPlan: Act 3 Total Framework

## Goal

把 `Act 3` 固化成首轮“高密度城市 + 高收束压力”框架包：不按 `Rivington`、`Wyrm's Crossing`、`Lower City` 先做地点导览，而是先用已完成的 `Act 2` 三个子单元作为上游，说明后期为什么会同时被玩家感知为“线太多、事太密”和“前史开始集中结算”。

## Why it matters

- 如果 `Act 3` 一上来就拆成城市地点列表，阶段 4 会立刻退化成景点导览，失去“反应性在高密度环境下如何承压”的总问题。
- 如果只写“终局快到了，所以压力更高”，又会把后期误写成单纯剧情加速，而看不见高密度城市、派系并行与前史读回如何叠在一起。
- 只有先把 `Act 3` 写成上位框架，后续 `Rivington`、`Wyrm's Crossing`、`Lower City` 与终局组织子块才不会彼此脱节。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：执行 `Act 3 总框架` 首轮框架包。
- 上游已完成：
  - `.agent/execplan_act2_total_framework.md`
  - `.agent/execplan_shadow_cursed_lands_region_pack.md`
  - `.agent/execplan_last_light_moonrise_gauntlet_convergence.md`
  - `docs/02_sources/case_note_act2_pressure_and_reactivity_frame.md`
  - `docs/02_sources/case_note_shadow_cursed_lands_pressure_loop.md`
  - `docs/02_sources/case_note_last_light_moonrise_gauntlet_convergence.md`
- 本轮优先回写模块是：
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- `BG3-OFF-001`：官方 About 页把 `the sprawling city of Baldur's Gate` 与 `shadow-cursed forests`、`Underdark` 并列呈现，说明 `Act 3` 对官方来说是差异化阶段节点，而不是“终局前剩余内容合集”。
- `BG3-OFF-002`：`Patch 7` 明确把新增 evil ending cinematics 写成 `depending on the choices you make` 的结果，同时继续集中修复 `writing and flow`、`scripting`、角色反应与长休 / 营地边界，说明后期结算并不是单一终局按钮，而是高密度状态读回区。
- `BG3-OFF-003`：Adam Smith 用 `Swiss cheese` 描述 BG3 的多入口结构，同时明确团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的结局与状态排列。
- `BG3-OFF-012`、`BG3-OFF-013`、`BG3-OFF-014`：提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，用来约束本轮只能写到“并行 quest bundle / 读回压力”这一级。

## Milestones

1. 新建 `docs/02_sources/case_note_act3_density_and_resolution_load.md`，把主问题锁定为“高密度与高收束压力如何在后期共同成立”，而不是城市地点综述。
2. 把“`Act 3` 是高密度城市中的反应性承压测试”最小回写到：
   - `docs/03_analysis/01_macro_structure.md`
   - `docs/03_analysis/02_quests_and_choices.md`
   - `docs/03_analysis/05_implementation_validation.md`
3. 同步 `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md`，并在检查通过后把下一唯一主任务切到 `Rivington`。

## Validation

- `case_note_act3_density_and_resolution_load.md` 已完成，并明确把 `Act 3` 锁定为“高密度城市 + 高收束压力”的框架包。
- `01_macro_structure.md` 能解释：`Act 3` 的关键变化不是“城市内容更多”，而是“多条并行线与终局读回同时进入同一阶段”。
- `02_quests_and_choices.md` 能解释：后期任务层不应被写成地点导览，而应被写成高密度并行线如何在更短窗口里被读取与压向结算。
- `05_implementation_validation.md` 新增 `Act 3` 的验证入口，并明确哪些判断仍只能停留在公开结构边界。
- `current_state.md` 与 `next_step.md` 已从 `Act 3 总框架` 切到 `Rivington`，且没有新增硬阻塞。

## Progress

- 2026-04-24：创建本计划，作为 `Act 3 总框架` 首轮框架包的执行记录。

## Decision Log

- 2026-04-24：决定先把 `Act 3` 写成“高密度城市 + 高收束压力”的上位框架，而不是提前拆 `Rivington`、`Wyrm's Crossing`、`Lower City`。
- 2026-04-24：决定继续复用 `BG3-OFF-001`、`BG3-OFF-002`、`BG3-OFF-003` 与公开 Journal 结构底座，不为追求“新来源”而跳出当前主线。

## Surprises & Discoveries

- 当前最稳的公开锚点并不是“某个 Act 3 地点介绍页”，而是“城市节点定位 + 选择驱动 ending feedback + 开发者承认后期状态排列密度更高”的交叉。
- 这意味着本轮更适合先压“后期承压方式”，而不是追求地点级信息密度。

## Outcomes & Retrospective

- 完成后应直接切到 `Rivington`，把 `Act 3 总框架` 作为上位边界继续往下压；不要回头把 `Act 3` 拆回城市百科或终局剧情提要。
