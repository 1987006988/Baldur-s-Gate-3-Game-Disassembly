# ExecPlan: Nautiloid Region Pack

## Goal

把 `Nautiloid` 做成新执行法的第一块模板区域包：先用最小 case note 锁定边界、来源与可写结论，再把它分别沉入宏观结构、任务回流、战斗 / 环境、实现验证四个模块。

## Why it matters

- 这是仓库第一次按“区域包”而不是“抽象模块”推进。
- `Nautiloid` 体量最可控，却同时暴露多入口、早期战斗、队友收编、初始任务状态与第一批系统清理。
- 如果这一块能跑通，后续 `Act 1 地表主区` 就能沿同样路径执行，而不会退回剧情复述。

## Repository context

- 项目级入口已把当前唯一主任务切到 `Nautiloid 区域包`。
- 当前需要同步回写的模块是：
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/04_combat_and_environment.md`
  - `docs/03_analysis/05_implementation_validation.md`
- `docs/03_analysis/00_core_thesis.md` 只做最小必要同步。

## Inputs and evidence

- 现有高层来源：`BG3-OFF-001`, `BG3-OFF-003`
- 开场 / 教程 / 任务关闭与状态清理入口：`BG3-OFF-002`
- 新增最小官方来源入口：`BG3-OFF-015`
- 实现验证底座：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## Milestones

1. 锁定 `Nautiloid` 的研究边界与首批来源。
2. 新建 `case_note_nautiloid_opening_state_and_multi_entry.md`。
3. 将可稳写结论最小回写到四个分析模块。
4. 同步状态文件，并确认下一步切到 `Act 1 地表主区`。

## Validation

- 至少 1 个 `Nautiloid` case note 完成。
- 至少 4 个分析模块得到最小必要回写。
- 技术判断继续留在 `05_implementation_validation.md` 的验证入口与待验证问题。
- `current_state.md`、`next_step.md`、`decision_log.md`、`source_index.md` 已同步。

## Progress

- 2026-04-24：创建本计划，作为 `Nautiloid 区域包` 首轮证据包的执行记录。

## Decision Log

- 2026-04-24：本轮只做 1 个主 case note，不额外扩写第二个 `early_party_recruitment` note。
- 2026-04-24：`Nautiloid` 先作为“多入口 + 早期状态埋点”的模板块回写，不提前把海滩后的回流链写死。

## Outcomes & Retrospective

- 完成后应直接切到 `Act 1 地表主区`，不要回跳到营地或其他旧模块做同类补料。
