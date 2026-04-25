# ExecPlan: Combat / Environment Early Local Agency to Regional Pressure Loop

## Goal

把阶段 5 / `Combat / Environment` 的首个横向子单元固化为一条可复用的跨阶段环境主干：不把 `04_combat_and_environment.md` 重新摊成 encounter 列表，而是把 `Nautiloid -> Act 1 地表主区 -> Grymforge -> Shadow-Cursed Lands` 压成同一条 “early local agency -> regional pressure loop” 脊梁。

## Why it matters

- 如果继续只让 `Grymforge` 单独承担战斗 / 环境模块，阶段 5 就不会真正形成横向主干。
- 如果反过来把每个区域包重新摊成打法、机关或 encounter 清单，仓库会退回攻略化写法，偏离“区域包 / 横向主干”方法。
- 当前公开来源已经足够把早期开场样本、地表常态化、成熟 encounter compression 与中盘区域压力循环压成一条结构链，但还不足以把 late `Act 2` / `Act 3` 的所有区域包都升级成第二条对称环境主干。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：阶段 5 已从 `Quest Reactivity` 切到 `Combat / Environment`，先建立第一份跨阶段 ExecPlan。
- 上游已完成并可直接复用：
  - `docs/02_sources/case_note_nautiloid_opening_state_and_multi_entry.md`
  - `docs/02_sources/case_note_act1_surface_route_pack.md`
  - `docs/02_sources/case_note_grymforge_environment_resolution.md`
  - `docs/02_sources/case_note_shadow_cursed_lands_pressure_loop.md`
- 本轮主回写模块：
  - `docs/03_analysis/04_combat_and_environment.md`
  - `docs/03_analysis/05_implementation_validation.md`
- 本轮同步文件：
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
  - `docs/00_project/decision_log.md`
  - `docs/00_project/source_index.md`

## Inputs and evidence

- `BG3-OFF-015`：提供 `Nautiloid` opening / tutorial 段的正式 flow、交互物、状态清理与 crash 后 handoff 边界。
- `BG3-OFF-002`：补足 `Nautiloid` 的 quest close / buff / equipment handoff，并提供 `Act II` 的 `writing and flow` / `scripting` 维护条目，支撑中盘压力循环仍属于被正式维护的 flow 问题。
- `BG3-OFF-003`：提供 `Swiss cheese` 多入口 / 非常规 problem-solving 设计语言，作为整条环境主干的高层统一口径。
- `BG3-OFF-006`：把 `Grymforge` 直接定义成包含 `choices` 与 `complex combat encounters` 的区域，并暴露 `Underdark -> Grymforge` 的 setup。
- `BG3-PLY-004`：仅作为 `Grymforge / Grym` 环境重写型遭遇的玩家案例入口，不升级为系统普遍事实。

## Milestones

1. 新建 `docs/02_sources/case_note_combat_environment_early_local_agency_to_pressure_loop.md`
   - 只压四段主干：`Nautiloid`、`Act 1 地表主区`、`Grymforge`、`Shadow-Cursed Lands`
   - 明确每段当前可升级到哪一层，以及为什么下一段不是简单重复上一段
2. 回写 `docs/03_analysis/04_combat_and_environment.md`
   - 新增阶段 5 的首条跨阶段环境主干小节
   - 写清这条 spine 当前为什么只稳到 `Shadow-Cursed Lands`
3. 回写 `docs/03_analysis/05_implementation_validation.md`
   - 新增对应分层矩阵
   - 明确哪些节点能进 cross-stage combat spine，哪些仍只能停在 region-pack / supporting bundle 层
4. 同步状态、决策与来源索引
   - 更新 `current_state.md`、`next_step.md`、`decision_log.md`
   - 为新 ExecPlan / case note 补齐 `source_index.md` 的 `Where used`
5. 运行 `python scripts/check_repo.py` 与 `make check`

## Validation

- `docs/03_analysis/04_combat_and_environment.md` 明确出现一条四段式 cross-stage spine，而不是回退成 encounter 列表。
- `docs/03_analysis/05_implementation_validation.md` 明确区分：
  - 哪些链段已足以进入第一条环境主干
  - 哪些 late `Act 2` / `Act 3` 锚点当前仍只能停在 region-pack 或 supporting bundle 层
- `docs/00_project/current_state.md` 与 `docs/00_project/next_step.md` 能直接说明：
  - `Quest Reactivity` 已收口
  - `Combat / Environment` 首条环境主干已完成首轮压实
  - 下一步要处理的是第二条环境主干的证据上限 / 边界，而不是回头补 encounter 清单

## Progress

- 2026-04-25：创建本计划，锁定阶段 5 / `Combat / Environment` 的首个横向子单元为 “early local agency -> regional pressure loop”。

## Decision Log

- 2026-04-25：决定阶段 5 的 `Combat / Environment` 先压“一条由开场样本到中盘区域压力循环”的主干，而不是继续把 `Grymforge` 当作孤立主案例。
- 2026-04-25：决定当前首条环境主干先停在 `Shadow-Cursed Lands`；late `Act 2` / `Act 3` 若无更强环境证据，不得被强拉成第二条对称 spine。

## Surprises & Discoveries

- `Combat / Environment` 比 `Quest Reactivity` 更早遇到“案例成熟度不均”的问题：`Grymforge` 已是成熟区域压缩包，但 `Nautiloid` 与 `Act 1 地表主区` 更像上游样本 / 常态化层。
- `Shadow-Cursed Lands` 的价值并不在于再给出一个著名战斗，而在于把玩家的战术 agency 从“局部遭遇重写”推进到“整段区域穿行如何在压力下保持多种推进方式”。

## Outcomes & Retrospective

- 本子单元完成后，阶段 5 / `Combat / Environment` 的下一步应优先处理“second public combat spine ceiling / late-game boundary”问题：评估 `Shadow-Cursed Lands` 之后的锚点能否进入第二条环境主干；若不能，就把它们明确降回 region-pack / supporting bundle 层。
