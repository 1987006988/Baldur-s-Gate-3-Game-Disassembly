# ExecPlan: Act 1 Surface Region Pack

## Goal

把 `Act 1 地表主区` 做成 `Nautiloid` 之后的第一块稳定区域包：先用 1 份 route-pack case note 压实“地表是问题网而不是景点串联”，再把其结论沉入宏观结构、任务回流、战斗 / 环境，并只给营地与实现验证补前序入口。

## Why it matters

- 这是 `Nautiloid` 模板之后，第一次检验 BG3 能否把“压缩样本”展开成稳定的 Act 级前场。
- 这一块如果写成景点导览或招募目录，后续 `Grove / Goblin`、`Camp`、`Underdark` 都会失去上游网络。
- 这一块做稳后，仓库就能把 `Grove / Goblin 冲突` 当作“状态回流网”的下游块，而不是重新从零解释 Act 1 为什么自由。

## Repository context

- 当前唯一主任务已切到 `Act 1 地表主区`。
- 上游已完成：
  - `.agent/execplan_nautiloid_region_pack.md`
  - `docs/02_sources/case_note_nautiloid_opening_state_and_multi_entry.md`
- 本轮需要同步回写的模块是：
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/04_combat_and_environment.md`
  - `docs/03_analysis/03_party_and_camp.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- 高层区域 / 产品定位：`BG3-OFF-001`
- 多入口 / 非常规 problem-solving 设计语言：`BG3-OFF-003`
- 开场到地表的状态交接与后续招募连续性：`BG3-OFF-002`, `BG3-OFF-015`
- Journal / trigger 的公开结构语言：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## Milestones

1. 锁定 `Act 1 地表主区` 的边界：只写 crash 后的 route pack 与前史密度，不展开 `Grove / Goblin` 的 resolution matrix。
2. 新建 `docs/02_sources/case_note_act1_surface_route_pack.md`。
3. 将“地表是问题网、不是景点串联”的稳定结论最小回写到 5 个分析模块。
4. 同步状态文件；若检查通过，则把下一唯一主任务切到 `Grove / Goblin 冲突`。

## Validation

- 至少 1 个 `Act 1 地表主区` case note 完成。
- 至少 `01_macro_structure.md`、`02_quests_and_choices.md`、`04_combat_and_environment.md` 完成最小必要回写。
- `03_party_and_camp.md` 只补“前序状态入口”，不重新扩写营地正文。
- `05_implementation_validation.md` 只新增验证入口与待验证问题，不升级具体脚本断言。
- `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md` 已同步。

## Progress

- 2026-04-24：创建本计划，作为 `Act 1 地表主区` 首轮区域包的执行记录。

## Decision Log

- 2026-04-24：本轮只做 1 个 `route pack` 主 case note，不额外拆第二个 `recruitment_and_discovery` note。
- 2026-04-24：现有官方来源已足以先把地表写成“opening state 的续接层 + 问题网”，但不足以把完整早期路线矩阵写成事实表。

## Outcomes & Retrospective

- 完成后若检查通过，应直接切到 `Grove / Goblin 冲突`，不要在 `Act 1 地表主区` 回退成景点补丁或招募目录。
