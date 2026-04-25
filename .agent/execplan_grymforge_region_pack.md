# ExecPlan: Grymforge Region Pack

## Goal

把 `Grymforge` 固化成 `Underdark` 下游的第一份“encounter bundle / combat-agency compression pack”区域包：复用现有 `Grymforge / Grym` case note，明确这块应写成“区域包把任务、空间、环境与复杂遭遇压到同一处”的验证点，而不是单个 Boss 战摘要或打法清单；再把稳定结论最小回写到战斗、任务与实现验证三个模块。

## Why it matters

- 这块是 `Underdark` 阶段重构之后的第一次高密度压缩，如果写稳，仓库就能证明 `Act 1` 的自由推进不只体现在入口与处理顺序，也体现在区域内部如何把战斗 / 环境变成真正的解法空间。
- 如果把 `Grymforge` 写成单个 `Grym` 攻略、机关清单或 cheese 合集，`Underdark -> Grymforge` 这条区域包链就会断成“突然开始讲打法”。
- 这块做稳后，`04_combat_and_environment.md` 会第一次拥有一份明确的区域包结论，`02_quests_and_choices.md` 也能更稳地补上“战斗 / 环境也是选择系统”的区域级回流。

## Repository context

- 当前唯一主任务已切到 `Grymforge`。
- 上游已完成：
  - `.agent/execplan_underdark_region_pack.md`
  - `docs/02_sources/case_note_underdark_entry_choice_pack.md`
- 当前可复用的下游材料：
  - `docs/02_sources/case_note_grymforge_environment_resolution.md`
  - `docs/02_sources/source_note_bg3_off_003_xbox_podcast.md`
  - `docs/02_sources/source_note_bg3_off_006_cu14_grymforge.md`
  - `docs/02_sources/source_note_bg3_ply_004_grym_environment_case.md`
- 本轮需要同步回写的模块是：
  - `docs/03_analysis/04_combat_and_environment.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- 多入口 / 非常规 problem-solving 设计语言：`BG3-OFF-003`
- `Underdark -> Grymforge` 的公开 setup 与复杂遭遇框架：`BG3-OFF-006`
- 玩家如何把 `Grymforge / Grym` 理解成环境重写型遭遇：`BG3-PLY-004`

## Milestones

1. 先锁定 `Grymforge` 的边界：只写区域框架、环境解法空间与最小必要的任务回流，不扩成 Boss 攻略或 cheese 清单。
2. 更新 `docs/02_sources/case_note_grymforge_environment_resolution.md`，把现有“战斗 / 环境主案例”收束成“区域包结论 + 待验证边界”。
3. 把“`Grymforge` 是 `Act 1` 第一块高密度的 `encounter bundle / combat-agency compression pack`”的稳定结论回写到：
   - `docs/03_analysis/04_combat_and_environment.md`
   - `docs/03_analysis/02_quests_and_choices.md`
   - `docs/03_analysis/05_implementation_validation.md`
4. 同步状态文件；若检查通过，则把下一唯一主任务切到 `Mountain Pass / Creche`。

## Validation

- 至少 1 份 `Grymforge` case note 完成显著更新。
- `04_combat_and_environment.md` 完成显著回写，明确 `Grymforge` 不是单个 Boss 战，而是区域包式战术问题。
- `02_quests_and_choices.md` 至少完成 1 段稳定回写，说明 `Grymforge` 如何把“环境 / 战斗也是选择系统”压成区域级结论。
- `05_implementation_validation.md` 新增 `Grymforge` 验证入口，但不升级任何私有触发器或 objective / step 断言。
- `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md` 已同步。

## Progress

- 2026-04-24：创建本计划，作为 `Grymforge` 首轮区域包的执行记录。

## Decision Log

- 2026-04-24：本轮不再新建第二份 `Grymforge encounter bundle` case note，而是优先收紧现有 `case_note_grymforge_environment_resolution.md`。
- 2026-04-24：当前更稳的口径是把 `Grymforge` 写成 `Underdark` 下游的“战斗 / 环境高密度压缩区”，而不是把 `Grym` 单独升级成整块区域的同义词。
- 2026-04-24：现有公开来源足以压实高层区域包结论，但还不足以把具体熔炉机关路径写成 objective / step 事实链。

## Outcomes & Retrospective

- 完成后若检查通过，应直接切到 `Mountain Pass / Creche`，不要继续围绕 `Grymforge` 扩打法、扩玩家帖或补整区导览。
