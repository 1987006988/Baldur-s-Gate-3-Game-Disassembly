# ExecPlan: Quest Reactivity Objective-Adjacent Narrowing

## Goal

把阶段 5 / `Quest Reactivity` 的第六个子单元固定为“objective-adjacent 窄化验证”：

- 不再继续扩新的跨阶段主链，也不再回头重写区域包总表。
- 只处理当前仍最接近 `objective / step` 的两个局部锚点：`Grove / Goblin` 与 `Mountain Pass / Creche`。
- 明确这两个锚点里，究竟哪些局部 fragment 还能再压一层，哪些部分必须明确停在 `camp readout`、`gate-and-tension bundle` 或其他 delayed readout 边界。
- 把这层更细的边界回写到 `docs/03_analysis/02_quests_and_choices.md` 与 `docs/03_analysis/05_implementation_validation.md`，并同步状态文件与决策记录。

## Why it matters

- 如果“层级锁定”之后不继续做这一步，仓库仍会停在“只有少数锚点接近 `objective / step`”的泛化口径，无法回答“到底是哪几个局部 fragment 接近到什么程度”。
- 如果反过来把这一步做成新的扩链动作，仓库又会重新退回两种旧问题：要么误把少数局部 patch 锚点扩成 objective 总表，要么把 `camp fold` / late-game bundle 再次拉回“第二条主链”。
- 这一步完成后，`Quest Reactivity` 在当前公开来源条件下就能真正收口：不是因为结论少，而是因为边界已经足够细，继续推进的收益会明显低于切换到下一个横向主干。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：完成“objective-adjacent 窄化验证”，优先处理 `Grove / Goblin` 的处理矩阵与 `Mountain Pass / Creche` 的局部门槛。
- 已完成且必须直接复用的阶段 5 子单元：
  - `.agent/execplan_quest_reactivity_cross_act_readback_spine.md`
  - `.agent/execplan_quest_reactivity_upstream_entry_diversion_gate_chain.md`
  - `.agent/execplan_quest_reactivity_late_act1_early_act2_transition_boundary.md`
  - `.agent/execplan_quest_reactivity_second_public_chain_ceiling.md`
  - `.agent/execplan_quest_reactivity_layer_boundary_lock.md`
- 本轮主回写模块：
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`
- 必须同步的状态文件：
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
  - `docs/00_project/decision_log.md`
  - `docs/00_project/source_index.md`

## Inputs and evidence

- `docs/02_sources/case_note_grove_goblin_resolution_matrix.md`
- `docs/02_sources/case_note_mountain_pass_creche_gate_and_party_tension.md`
- `docs/02_sources/case_note_quest_reactivity_layer_boundary_lock.md`
- `docs/02_sources/source_note_bg3_off_004_hotfix_20.md`
- `docs/02_sources/source_note_bg3_off_008_hotfix_5_minthara_camp.md`
- `docs/02_sources/source_note_bg3_off_012_journal_editor_overview.md`
- `docs/02_sources/source_note_bg3_off_013_journal_structure_overview.md`
- `docs/02_sources/source_note_bg3_off_014_add_quest_to_situation.md`
- `docs/02_sources/source_note_bg3_off_016_patch_3_creche_tension.md`

## Milestones

1. 新建 `docs/02_sources/case_note_quest_reactivity_objective_adjacent_narrowing.md`
   - 只回答两个问题：
     - `Grove / Goblin` 里哪些 fragment 真正接近 `objective / step`
     - `Mountain Pass / Creche` 里哪些 fragment 真正接近 `objective / step`
   - 不新增新区域、不扩第二条主链、不追新来源。
2. 回写 `docs/03_analysis/02_quests_and_choices.md`
   - 明确 `Grove / Goblin` 当前只能把 `Minthara` 的局部处理矩阵压到 objective-adjacent 层。
   - 明确 `Mountain Pass / Creche` 当前只能把局部门槛 / 敌意 / 即时反应压到 objective-adjacent 层，`camp night` 仍是 delayed readout。
   - 明确 `camp fold` 与 late-game bundle 不再承担继续扩主链的任务。
3. 回写 `docs/03_analysis/05_implementation_validation.md`
   - 新增一张 objective-adjacent narrowing 矩阵。
   - 把“还能再压一层”和“必须就此停手”明确分开。
4. 同步状态与决策
   - 更新 `current_state.md`、`next_step.md`、`decision_log.md`
   - 更新 `source_index.md` 的 `Where used`
   - 运行 `python scripts/check_repo.py` 与 `make check`

## Validation

- `docs/02_sources/case_note_quest_reactivity_objective_adjacent_narrowing.md` 已明确区分：
  - `Grove / Goblin` 的 objective-adjacent 局部 fragment
  - `Grove / Goblin` 必须停在 delayed camp readout 的部分
  - `Mountain Pass / Creche` 的 objective-adjacent 局部门槛 fragment
  - `Mountain Pass / Creche` 必须停在 delayed camp readout / gate-and-tension bundle 的部分
- `docs/03_analysis/02_quests_and_choices.md` 已明确写出：
  - 哪些 fragment 还能再压一层
  - 为什么其余部分不能再升级成 objective 总表
- `docs/03_analysis/05_implementation_validation.md` 已明确写出：
  - `BG3-OFF-012` / `013` / `014` 只提供公开层级语言
  - 真正能继续前进的只有被 patch / hotfix 直接点名的局部 state / gate fragment
- `current_state.md` 与 `next_step.md` 能直接说明：
  - 阶段 5 / `Quest Reactivity` 的第六个子单元已完成
  - 在当前来源下该主干已收口
  - 下一主任务应切到其他横向主干，而不是继续扩写 `Quest Reactivity`

## Progress

- 2026-04-24：创建本计划，确认阶段 5 / `Quest Reactivity` 的第六个子单元不再扩链，只做 objective-adjacent 窄化验证。

## Decision Log

- 2026-04-24：决定把 `Grove / Goblin` 与 `Mountain Pass / Creche` 的后续推进收窄为“局部 fragment 级别”的边界判断，而不是继续把整个区域包往 objective 总表方向推进。
- 2026-04-24：决定把 `camp readout`、`camp fold` 与 late-game bundle 明确降回 supporting layer，不再允许它们继续竞争第二条主链位置。

## Surprises & Discoveries

- 当前真正缺的不是更多 case，而是更细的“哪一小段已经被公开条目直接点名，哪一小段只是下游读出”的纪律。
- `Grove / Goblin` 与 `Mountain Pass / Creche` 看似都接近 `objective / step`，但它们接近的其实不是同一种东西：前者更接近局部 resolution-state fragment，后者更接近局部 gate fragment。

## Outcomes & Retrospective

- 本子单元完成后，阶段 5 / `Quest Reactivity` 在当前公开来源下应视为已完成收口：后续只有出现更强官方来源时，才值得重新打开 objective-adjacent 侦察。
- 下一主任务不应继续停留在 `Quest Reactivity`，而应切到其余横向主干，优先考虑 `Combat / Environment` 的跨阶段压缩。
