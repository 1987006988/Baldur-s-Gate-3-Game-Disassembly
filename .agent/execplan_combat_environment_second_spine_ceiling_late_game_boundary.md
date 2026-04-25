# ExecPlan: Combat / Environment Second Spine Ceiling / Late-Game Boundary

## Goal

把阶段 5 / `Combat / Environment` 的第二子单元压成一份明确的 late-game boundary 计划：不把 `Shadow-Cursed Lands` 之后的 `Last Light / Moonrise / Gauntlet` 与 `Act 3` 城市子包重新摊成 encounter 列表，而是判断它们在当前公开来源下能否进入第二条 cross-stage combat spine；若不能，就把它们稳定降回 region-pack / supporting bundle 层。

## Why it matters

- 如果在首条 “early local agency -> regional pressure loop” 环境主干建立后继续硬追第二条对称 spine，仓库会把 late `Act 2` / `Act 3` 的收束、过滤、门槛与 ending feedback bundle 误写成同级环境锚点。
- 如果反过来因为 late-game 证据不够，就把这几块重新写回 encounter / 机关 / cheese 列表，阶段 5 / `Combat / Environment` 也会退回攻略化写法。
- 当前最需要的不是再发明新主干，而是给现有环境主干补一层“证据上限 / 边界锁定”，明确哪些 late-game 结论仍然有效、但只能停在 supporting bundle。

## Repository context

- 当前唯一主任务来自 `docs/00_project/next_step.md`：阶段 5 / `Combat / Environment` 的第二子单元，处理 second spine ceiling / late-game boundary。
- 上一子单元已完成：
  - `.agent/execplan_combat_environment_early_local_agency_to_pressure_loop.md`
  - `docs/02_sources/case_note_combat_environment_early_local_agency_to_pressure_loop.md`
- 本轮直接复用、但不重写的 late-game case notes：
  - `docs/02_sources/case_note_last_light_moonrise_gauntlet_convergence.md`
  - `docs/02_sources/case_note_act3_density_and_resolution_load.md`
  - `docs/02_sources/case_note_rivington_entry_pressure.md`
  - `docs/02_sources/case_note_wyrms_crossing_bridge_and_gate_pack.md`
  - `docs/02_sources/case_note_lower_city_faction_resolution_pack.md`
  - `docs/02_sources/case_note_endgame_organization_compression.md`
- 本轮主回写模块：
  - `docs/03_analysis/04_combat_and_environment.md`
  - `docs/03_analysis/05_implementation_validation.md`
- 本轮同步文件：
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
  - `docs/00_project/decision_log.md`

## Inputs and evidence

- `BG3-OFF-001`：提供 `shadow-cursed forests` 与 `the sprawling city of Baldur's Gate` 作为差异化阶段节点的公开区域定位。
- `BG3-OFF-002`：提供 late `Act 2` / `Act 3` 的 `Writing and Flow`、`Scripting`、`Act II`、ending cinematics 等公开维护边界，说明后期重点是 flow / reaction / ending feedback 的高密度读回。
- `BG3-OFF-003`：提供 `Swiss cheese` 多入口 / problem-solving 设计语言，并明确团队上线后继续补了大量 late-game dialogue / cinematics，说明后期是更高密度状态覆盖，而不是自动变成单一路线。
- `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`：提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，帮助判断哪些 late-game 结论只能停在 bundle 层。

## Milestones

1. 新建 `docs/02_sources/case_note_combat_environment_second_spine_ceiling_late_game_boundary.md`
   - 只处理 `Shadow-Cursed Lands` 之后的 late `Act 2` / `Act 3` 锚点
   - 为每个锚点给出“当前最稳职责 / 当前可升级层级 / 不能进入第二条环境主干的原因”
2. 回写 `docs/03_analysis/04_combat_and_environment.md`
   - 新增 second spine ceiling / late-game boundary 小节
   - 明确 late-game 结论依旧有效，但只能作为 supporting bundle，而不是第二条对称环境 spine
3. 回写 `docs/03_analysis/05_implementation_validation.md`
   - 新增对应的 late-game boundary 验证矩阵
   - 把“late-game 不是无效，而是公开证据层级不足”写清
4. 同步状态与决策
   - 更新 `current_state.md`、`next_step.md`、`decision_log.md`
   - 把下一唯一主任务从 `Combat / Environment` 切到剩余横向主干，而不是继续停在已锁定的 second spine ceiling 上
5. 运行 `python scripts/check_repo.py` 与 `make check`

## Validation

- `docs/03_analysis/04_combat_and_environment.md` 明确区分：
  - 第一条环境主干已经成立
  - `Last Light / Moonrise / Gauntlet` 与 `Act 3` 各包当前只能作为 supporting bundles
- `docs/03_analysis/05_implementation_validation.md` 明确给出：
  - 哪些 late-game 锚点最多只能升级到 `convergence`、`entry filter`、`bridge / gate`、`parallel resolution`、`organization / ending feedback` 层
  - 为什么它们暂不能进入第二条 cross-stage combat spine
- `docs/00_project/current_state.md` 与 `docs/00_project/next_step.md` 能直接说明：
  - `Combat / Environment` 的 second spine ceiling 已锁定
  - 除非出现更强 late-game 环境来源，否则不再继续追第二条对称 spine

## Progress

- 2026-04-25：创建本计划，锁定阶段 5 / `Combat / Environment` 第二子单元只处理 second spine ceiling / late-game boundary，不回退成 encounter 列表。

## Decision Log

- 2026-04-25：决定把 late `Act 2` / `Act 3` 的现有公开锚点统一视为 first spine 的 downstream supporting bundles，而不是继续追求第二条对称环境 spine。
- 2026-04-25：决定本子单元完成后，若无新增强环境来源，`Combat / Environment` 应在当前公开来源下暂时收口并切往剩余横向主干。

## Surprises & Discoveries

- late `Act 2` / `Act 3` 并非“没有战斗 / 环境作用”，而是当前公开来源更稳定地暴露了它们的 `flow / filter / gate / ending feedback` 职责，却没有暴露可与 `Grymforge` 或 `Shadow-Cursed Lands` 对称的成熟环境锚点。
- 因此 second spine ceiling 的核心不是“late-game 不重要”，而是“late-game 的重要性目前更稳地属于 supporting bundle，而不是第二条环境主干”。

## Outcomes & Retrospective

- 本子单元完成后，阶段 5 / `Combat / Environment` 的当前公开来源边界应被明确锁定：
  - 第一条环境主干保留为正式横向 spine
  - `Shadow-Cursed Lands` 之后的 late-game 锚点保留为 downstream supporting bundles
  - 后续只有在出现更强、直接点名 late-game combat / environment agency 的官方来源时，才重新打开第二条 spine 的判断
