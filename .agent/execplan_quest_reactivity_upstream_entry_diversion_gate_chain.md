# ExecPlan: Quest Reactivity Upstream Entry / Diversion / Gate Chain

## Goal

把阶段 5 / `Quest Reactivity` 的第二个横向子单元固化为一条服务既有主干的上游前置链：不把 `Act 1` 重新扩成总表，而是把 `Nautiloid -> Act 1 地表主区 -> Underdark -> Mountain Pass / Creche` 压成“入口埋点 -> 目标网 -> 改道 / 重构 -> 门槛 / 张力”四段链，说明 `Grove / Goblin` 之前的区域包怎样为现有 `readback spine` 提供前史密度。

## Why it matters

- 如果阶段 5 只保留 `Grove / Goblin -> Act 2 -> Act 3` 的 readback spine，主干会显得从 `Act 1` 中段突然开始，容易让仓库重新被追问“那前面那些区域包为什么存在”。
- 如果这一轮反过来把 `Act 1` 全部重摊成总表，仓库会重新滑回旧的抽象模块跳转与剧情复述。
- 当前四个已完成的 `Act 1` 区域包，已经足以稳定承担四种不同职责：`Nautiloid` 提供入口埋点，地表主区提供目标网，`Underdark` 提供改道 / 重构，`Mountain Pass / Creche` 提供 late `Act 1` 的门槛 / 张力；它们正好能为现有 readback spine 补齐上游。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：在首条 `cross-act readback spine` 基础上，继续补 `Nautiloid`、`Act 1 地表主区`、`Underdark`、`Mountain Pass / Creche` 的“入口 / 改道 / 门槛”前置链。
- 上游已完成并可直接复用：
  - `docs/02_sources/case_note_nautiloid_opening_state_and_multi_entry.md`
  - `docs/02_sources/case_note_act1_surface_route_pack.md`
  - `docs/02_sources/case_note_underdark_entry_choice_pack.md`
  - `docs/02_sources/case_note_mountain_pass_creche_gate_and_party_tension.md`
- 本轮主回写模块：
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`
  - 如有必要最小回写 `docs/03_analysis/01_macro_structure.md`

## Inputs and evidence

- `BG3-OFF-015`：提供 `Nautiloid` 的 quest item、受限检定、状态清理与 tutorial 边界。
- `BG3-OFF-002`：提供 `Escape the Nautiloid` 的 quest close、坠毁后的状态续接与地表招募交接边界。
- `BG3-OFF-003`：提供 `Swiss cheese` 多入口 / problem-solving 设计语言。
- `BG3-OFF-001`：提供差异化区域节点的公开产品语言。
- `BG3-OFF-006`：提供 `Underdark -> Grymforge` 的公开 quest setup 与区域级 `choices / complex combat encounters` 框架。
- `BG3-OFF-016`：提供 `Mountain Pass / Creche` 的对话门槛、局部敌意、即时伙伴反应与 `camp night` 后果读取边界。
- `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`：提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，用于约束这一轮只写到可公开验证的层级。

## Milestones

1. 新建 `docs/02_sources/case_note_quest_reactivity_upstream_entry_diversion_gate_chain.md`
   - 只压一条上游前置链：`Nautiloid -> Act 1 地表主区 -> Underdark -> Mountain Pass / Creche`
   - 明确每一段各自承担入口、目标网、改道 / 重构、门槛 / 张力中的哪一种职责
2. 回写 `docs/03_analysis/02_quests_and_choices.md`
   - 新增一段上游前置链总结
   - 明确 `Grove / Goblin` 不是阶段 5 主干的任意起点，而是前四段之后第一块高可见 `resolution matrix`
3. 回写 `docs/03_analysis/05_implementation_validation.md`
   - 把四段前置链压成分层矩阵
   - 明确哪些段落已接近 `objective / step`，哪些仍只能停留在 `entry / diversion / gate bundle`
4. 如有必要最小回写 `docs/03_analysis/01_macro_structure.md`
   - 只补一句这条上游前置链如何服务既有 readback spine
5. 同步状态文件
   - 更新 `current_state.md`、`next_step.md`、`decision_log.md`
   - 运行 `python scripts/check_repo.py` 与 `make check`

## Validation

- `docs/03_analysis/02_quests_and_choices.md` 明确写出至少 1 条由四个 `Act 1` 区域包组成的上游前置链，并说明它如何服务现有 `cross-act readback spine`。
- `docs/03_analysis/05_implementation_validation.md` 明确区分：
  - 哪些前置链判断已足以写到 `objective / step` 邻近边界
  - 哪些前置链判断目前只能停留在 `entry / diversion / gate bundle`
- `docs/00_project/current_state.md` 与 `docs/00_project/next_step.md` 能直接说明：阶段 5 已完成前两个子单元，下一步进入 late `Act 1` / early `Act 2` 交接边界分层。
- 不新增任何与该前置链无关的新区域包扩写、剧情摘要或无关来源侦察。

## Progress

- 2026-04-24：创建本计划，锁定阶段 5 / `Quest Reactivity` 的第二个横向子单元为“上游入口 / 改道 / 门槛前置链”。

## Decision Log

- 2026-04-24：决定阶段 5 的第二个子单元不再新增第二条 readback spine，而是先给既有主干补齐 `Act 1` 上游前史。
- 2026-04-24：决定这条前置链只压到四段职责层，不把 `Act 1` 重新扩成完整 objective 表。

## Surprises & Discoveries

- `Act 1` 已完成的四个区域包并不是平铺补丁，它们正好对应四种前置职责：入口埋点、目标网、改道 / 重构、门槛 / 张力。
- 这说明阶段 5 不需要回头重写总逻辑，只要把既有区域包重新压成“上游前置链 + 下游 readback spine”的两段结构即可。

## Outcomes & Retrospective

- 本子单元完成后，阶段 5 应继续停留在 `Quest Reactivity`，下一步优先补 `Mountain Pass / Creche -> Shadow-Cursed Lands -> Last Light / Moonrise / Gauntlet` 的交接边界，继续判断哪些段落能升到 `objective / step`，哪些仍只能停留在 `bundle / flow`。
