# ExecPlan: Quest Reactivity Late Act 1 / Early Act 2 Transition Boundary

## Goal

把阶段 5 / `Quest Reactivity` 的第三个子单元固化为一组只服务既有主干的交接边界分层：不把 `Mountain Pass / Creche`、`Shadow-Cursed Lands`、`Last Light / Moonrise / Gauntlet` 重新摊成 late `Act 1` / `Act 2` 总表，而是只回答一件事：`Act 1` 的高压 gate 如何进入 `Act 2` 的 pressure filtering，再如何被压成 `convergence pack`。

## Why it matters

- 如果只停在“上游前置链 + readback spine”，阶段 5 仍会在 `Mountain Pass / Creche -> Act 2` 这一跳上留下明显空档，看起来像 `Act 2` 突然开始接管。
- 如果反过来把这一跳扩写成 `Act 2` 地点目录或 `Act 1` 总表，仓库会重新退回旧的模块跳转与剧情复述。
- 当前公开来源已经足以压出三层不同强度的边界：`gate`、`pressure filter`、`convergence pack`；这正好是下一步判断“哪些能逼近 `objective / step`，哪些仍只能停在 bundle 层”的最佳切口。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：在已完成的 `cross-act readback spine` 与 `upstream entry / diversion / gate chain` 基础上，补 late `Act 1` / early `Act 2` 的交接边界。
- 上游已完成并可直接复用：
  - `.agent/execplan_quest_reactivity_cross_act_readback_spine.md`
  - `.agent/execplan_quest_reactivity_upstream_entry_diversion_gate_chain.md`
  - `docs/02_sources/case_note_mountain_pass_creche_gate_and_party_tension.md`
  - `docs/02_sources/case_note_shadow_cursed_lands_pressure_loop.md`
  - `docs/02_sources/case_note_last_light_moonrise_gauntlet_convergence.md`
- 本轮主回写模块：
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`
  - 如有必要最小回写 `docs/03_analysis/01_macro_structure.md`

## Inputs and evidence

- `BG3-OFF-016`：直接暴露 `Mountain Pass / Creche` 的对话门槛、局部敌意、即时伙伴反应与 `camp night` 后果读取边界。
- `BG3-OFF-002`：直接暴露 `Act II` 的 `writing and flow` / `scripting` 维护，以及 `Minthara -> Moonrise Towers -> Act II reaction` 这条跨 Act 读回链。
- `BG3-OFF-003`：提供 `Swiss cheese` 设计语言，用于约束“进入压力阶段后，多入口并未消失，只是被重新过滤与压缩”。
- `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`：提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，用于明确本轮最多只能升级到哪一层。

## Milestones

1. 新建 `docs/02_sources/case_note_quest_reactivity_late_act1_early_act2_transition_boundary.md`
   - 只压一组三段交接：`Mountain Pass / Creche -> Shadow-Cursed Lands -> Last Light / Moonrise / Gauntlet`
   - 明确每段各自承担 `gate`、`pressure filter`、`convergence pack` 中的哪一层职责
2. 回写 `docs/03_analysis/02_quests_and_choices.md`
   - 新增一段交接边界总结
   - 明确这不是另一份 `Act 1` / `Act 2` 目录，而是现有主干中最关键的中盘接缝
3. 回写 `docs/03_analysis/05_implementation_validation.md`
   - 新增一张三段分层矩阵
   - 明确哪些判断已接近 `objective / step`，哪些仍只能停留在 `gate / pressure / convergence bundle`
4. 如有必要最小回写 `docs/03_analysis/01_macro_structure.md`
   - 只补一句 late `Act 1` 到 early `Act 2` 的结构接缝说明
5. 同步状态文件与索引
   - 更新 `current_state.md`、`next_step.md`、`decision_log.md`
   - 同步 `source_index.md` 的 `Where used`
   - 运行 `python scripts/check_repo.py` 与 `make check`

## Validation

- `docs/03_analysis/02_quests_and_choices.md` 明确写出：`Mountain Pass / Creche` 不是单独尾声块，而是通向 `Shadow-Cursed Lands` 的高压 gate；`Shadow-Cursed Lands` 不是泛化氛围块，而是 pressure filter；`Last Light / Moonrise / Gauntlet` 不是地点并列，而是 convergence pack。
- `docs/03_analysis/05_implementation_validation.md` 明确区分：
  - `Mountain Pass / Creche` 仅局部门槛接近 `objective / step`
  - `Shadow-Cursed Lands` 当前更稳地停留在 `pressure / flow bundle`
  - `Last Light / Moonrise / Gauntlet` 当前更稳地停留在 `convergence pack / reread bundle`
- `current_state.md` 与 `next_step.md` 能直接说明：阶段 5 已完成前三个子单元，且下一步不回跳无关模块。

## Progress

- 2026-04-24：创建本计划，锁定阶段 5 / `Quest Reactivity` 的第三个子单元为 late `Act 1` / early `Act 2` 交接边界分层。

## Decision Log

- 2026-04-24：决定这一轮不新增第二条 readback spine，也不重写 `Act 2` 总框架，而是先把最薄弱的交接缝压实。
- 2026-04-24：决定这组交接只写成 `gate -> pressure filter -> convergence pack` 三段，而不假装已掌握完整 objective 编排。

## Surprises & Discoveries

- `Mountain Pass / Creche` 与 `Shadow-Cursed Lands` 的差别不只是阶段先后，而是公开证据强度不同：前者已经有局部门槛与 reaction 边界，后者更像整段压力过滤器。
- `Last Light / Moonrise / Gauntlet` 的公开证据虽然仍高度依赖 `Moonrise Towers` 这类高可见锚点，但已经足够承担“把过滤后的前史压向较少读回节点”的职责。

## Outcomes & Retrospective

- 本子单元完成后，阶段 5 将不再只拥有“前置链”和“下游读回梯”两段，而会补齐二者之间最关键的中盘接缝。
- 下一步应继续停留在 `Quest Reactivity`，优先评估是否还能压出第二条不依赖 `Minthara -> Moonrise Towers` 的公开跨阶段链；若不能，应把原因压实到实现验证层。
