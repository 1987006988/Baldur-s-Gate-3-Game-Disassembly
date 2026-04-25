# ExecPlan: Last Light / Moonrise / Gauntlet Convergence Pack

## Goal

把 `Last Light / Moonrise / Gauntlet / 相关收束点` 固化成 `Act 2` 的首轮“中盘收束点组”：不按地点分别写导览，而是先用已完成的 `Act 2 总框架` 与 `Shadow-Cursed Lands` 区域包作上游，说明这些节点为何共同承担“多条前置路径被重新压缩、读取并推向后续结算”的职责；再把稳定结论最小回写到任务、营地、宏观结构与实现验证四层。

## Why it matters

- 如果把 `Last Light`、`Moonrise`、`Gauntlet` 各自拆成平行地点包，`Act 2` 会重新退化成地点目录与剧情高潮摘要。
- `Shadow-Cursed Lands` 已经证明中盘压力先落到“整段推进如何被风险重组”；本轮必须继续压实“这些压力最后在哪里被读回、压缩、改写后续顺序”。
- 只有先把这组节点写成同一块收束组织器，阶段 3 / `Act 2` 才算真正闭合，仓库也才能无歧义切到 `Act 3 总框架`。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：执行 `Last Light / Moonrise / Gauntlet / 相关收束点` 首轮收束包。
- 上游已完成：
  - `.agent/execplan_act2_total_framework.md`
  - `.agent/execplan_shadow_cursed_lands_region_pack.md`
  - `docs/02_sources/case_note_act2_pressure_and_reactivity_frame.md`
  - `docs/02_sources/case_note_shadow_cursed_lands_pressure_loop.md`
- 本轮优先回写模块是：
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/03_party_and_camp.md`
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- `BG3-OFF-001`：官方 About 页把 `shadow-cursed forests` 作为阶段级区域节点点名，给 `Act 2` 提供差异化阶段框架。
- `BG3-OFF-002`：`Patch 7` 的 `Writing and Flow`、`Scripting`、`Act II` 条目，以及 `Minthara -> Moonrise Towers -> Act II reaction` 链，直接暴露中盘收束点附近的 flow / reaction / cross-Act readback 维护边界。
- `BG3-OFF-003`：Adam Smith 的 `Swiss cheese` 结构语言，用来防止把收束误写成“只剩单一路线”。
- `BG3-OFF-012`、`BG3-OFF-013`、`BG3-OFF-014`：提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，用来约束“收束”只能写到公开可验证的任务组织层。
- 上游框架：`docs/02_sources/case_note_act2_pressure_and_reactivity_frame.md`、`docs/02_sources/case_note_shadow_cursed_lands_pressure_loop.md`

## Milestones

1. 新建 `docs/02_sources/case_note_last_light_moonrise_gauntlet_convergence.md`，把主问题锁定为“多条前置路径如何在这组节点被重新压缩与读取”，而不是地点导览。
2. 把“`Last Light / Moonrise / Gauntlet` 是 `Act 2` 的中盘收束点组”回写到：
   - `docs/03_analysis/02_quests_and_choices.md`
   - `docs/03_analysis/03_party_and_camp.md`
   - `docs/03_analysis/01_macro_structure.md`
   - `docs/03_analysis/05_implementation_validation.md`
3. 同步 `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md`，并在检查通过后把下一唯一主任务切到 `Act 3 总框架`。

## Validation

- `case_note_last_light_moonrise_gauntlet_convergence.md` 已完成，并明确把这一组节点锁定为“中盘收束点组”。
- `02_quests_and_choices.md` 与 `03_party_and_camp.md` 完成显著回写，能解释前置路径如何在这组节点被重新读回。
- `01_macro_structure.md` 能解释这组节点为何属于同一块中盘压缩器，而不是三个平行地点。
- `05_implementation_validation.md` 新增这一组节点的验证入口，但不把内部 objective / step 映射写成实现实锤。
- `current_state.md` 与 `next_step.md` 已把主线切到下一块 `Act 3 总框架`。

## Progress

- 2026-04-24：创建本计划，作为 `Last Light / Moonrise / Gauntlet / 相关收束点` 首轮收束包的执行记录。

## Decision Log

- 2026-04-24：决定先把 `Last Light / Moonrise / Gauntlet` 写成“中盘收束点组”，而不是分别拆成 `Last Light`、`Moonrise`、`Gauntlet` 三份地点笔记。
- 2026-04-24：决定继续复用 `BG3-OFF-001`、`BG3-OFF-002`、`BG3-OFF-003` 与 Journal 公开结构底座，不为追求“新来源”而打散当前主线。

## Surprises & Discoveries

- 当前最稳的公开锚点仍然不是某一篇直接讲 `Last Light` 或 `Gauntlet` 的官方介绍，而是“`Act II` flow / reaction 维护 + `Moonrise Towers` 前史读回 + Journal 结构语言”的交叉。
- 这意味着本轮更适合先压“收束关系”，而不是追求地点级事实密度。

## Outcomes & Retrospective

- 完成后应直接切到 `Act 3 总框架`，不要回头把 `Act 2` 收束点组继续拆成地点百科、剧情高潮提要或单个角色专章。
