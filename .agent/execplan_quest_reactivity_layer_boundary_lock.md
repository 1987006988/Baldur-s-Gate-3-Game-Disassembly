# ExecPlan: Quest Reactivity Layer Boundary Lock

## Goal

把阶段 5 / `Quest Reactivity` 的第五个子单元固定为“层级收口 / 边界锁定”：

- 不再继续寻找与 `Minthara -> Moonrise Towers` 对称的第二条公开跨 Act 主链。
- 在已完成的上游前置链、中盘接缝、首条 `readback spine` 与“第二条公开链证据上限”判断基础上，明确哪些链段还能逼近 `objective / step`，哪些必须停在 `gate / tension`、`camp fold`、`ending feedback / organization bundle`。
- 把这套边界同步回 `02_quests_and_choices.md` 与 `05_implementation_validation.md`，让阶段 5 后续推进只剩“窄化验证”，而不再回退成全任务表或区域包复述。

## Why it matters

- 如果没有这一层边界锁定，阶段 5 会在“已有一条显式 spine”之后重新失控，不是被拉回第二条对称主链，就是被拉回全局 objective 表。
- 当前仓库已经拥有足够多的区域包结论；真正缺的不是更多“还有哪些例子”，而是“这些例子最多能被公开写到哪一层”。
- 这一子单元完成后，`Quest Reactivity` 的后续工作才会变成窄范围、可验证、可停手的收尾动作。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：继续停留在阶段 5 / `Quest Reactivity`，优先收口哪些结论还能逼近 `objective / step`，哪些必须明确停在 `gate / tension`、`camp fold` 与 `ending feedback / organization bundle`。
- 已完成且必须直接复用的四个子单元：
  - `.agent/execplan_quest_reactivity_cross_act_readback_spine.md`
  - `.agent/execplan_quest_reactivity_upstream_entry_diversion_gate_chain.md`
  - `.agent/execplan_quest_reactivity_late_act1_early_act2_transition_boundary.md`
  - `.agent/execplan_quest_reactivity_second_public_chain_ceiling.md`
- 本轮主回写模块：
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`
- 必须同步的状态文件：
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
  - `docs/00_project/decision_log.md`

## Inputs and evidence

- 区域包 / Act 包结论：
  - `docs/02_sources/case_note_grove_goblin_resolution_matrix.md`
  - `docs/02_sources/case_note_mountain_pass_creche_gate_and_party_tension.md`
  - `docs/02_sources/case_note_last_light_moonrise_gauntlet_convergence.md`
  - `docs/02_sources/case_note_endgame_organization_compression.md`
  - 以及阶段 5 已完成的四份横向 case note
- 官方来源：
  - `BG3-OFF-002`
  - `BG3-OFF-003`
  - `BG3-OFF-004`
  - `BG3-OFF-007`
  - `BG3-OFF-008`
  - `BG3-OFF-010`
  - `BG3-OFF-012`
  - `BG3-OFF-013`
  - `BG3-OFF-014`
  - `BG3-OFF-015`
  - `BG3-OFF-016`

## Milestones

1. 新建 `docs/02_sources/case_note_quest_reactivity_layer_boundary_lock.md`
   - 用一张“层级锁定矩阵”重排既有锚点。
   - 只回答“最多能写到哪一层”，不新增剧情包。
2. 回写 `docs/03_analysis/02_quests_and_choices.md`
   - 明确阶段 5 当前最接近 `objective / step` 的只剩少数局部锚点。
   - 明确为什么 `camp fold` 和 `ending feedback` 只能当支撑层，而不是第二条主链。
3. 回写 `docs/03_analysis/05_implementation_validation.md`
   - 写清“一条显式 spine + 多个支撑 bundle”之后的稳定层级分布。
   - 把后续验证动作压缩成“只补 objective-adjacent 窄锚点”。
4. 同步状态文件
   - 更新 `current_state.md`、`next_step.md`、`decision_log.md`
   - 如需要，再补 `source_index.md`
   - 运行 `python scripts/check_repo.py` 与 `make check`

## Validation

- `docs/02_sources/case_note_quest_reactivity_layer_boundary_lock.md` 已形成明确矩阵，至少区分：
  - `objective / step` 邻近层
  - `gate / tension` / `pressure filter` / `convergence pack`
  - `camp fold`
  - `ending feedback / organization bundle`
- `docs/03_analysis/02_quests_and_choices.md` 已明确写出：
  - 哪些链段还能继续向 `objective / step` 逼近
  - 为什么其余锚点必须停在 bundle 层
- `docs/03_analysis/05_implementation_validation.md` 已明确写出：
  - 阶段 5 的 ceiling 已从“是否存在第二条主链”切换成“如何锁定各锚点层级上限”
- `current_state.md` 与 `next_step.md` 能直接说明：
  - 阶段 5 的第五个子单元已完成
  - 下一步只剩 objective-adjacent 窄化验证，而不是继续扩主链

## Progress

- 2026-04-24：创建本计划，确认阶段 5 / `Quest Reactivity` 的下一子单元不是再补新链，而是把既有判断锁到公开可写的最高层级。

## Decision Log

- 2026-04-24：决定把阶段 5 的第五个子单元定义为“层级收口 / 边界锁定”，而不是继续扩写第二条公开跨 Act 主链。
- 2026-04-24：决定后续只允许“objective-adjacent”局部锚点继续升级；`camp fold` 与 `ending feedback / organization bundle` 不再参与主链竞争。

## Surprises & Discoveries

- 仓库现阶段最稀缺的不是案例数量，而是层级纪律：没有边界锁定时，越多已完成区域包越容易重新被误写成 objective 总表。
- `Quest Reactivity` 当前最稳的新增价值，已经从“找到更多链”转成“明确哪类锚点只能作为 supporting bundle 存在”。

## Outcomes & Retrospective

- 本子单元完成后，阶段 5 的下一步应收窄为“只补最接近 `objective / step` 的局部锚点”，优先考虑 `Grove / Goblin` 与 `Mountain Pass / Creche` 这类已有直接维护条目的窄边界。
- 如果后续没有更强官方来源，`Quest Reactivity` 不应继续横向扩链，而应准备切换到其余横向主干。
