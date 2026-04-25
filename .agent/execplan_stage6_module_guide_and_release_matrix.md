# ExecPlan: Stage-6 Module Guide and Release Matrix

## Goal

把阶段 6 的第二个子单元固定为“模块职责 / 推荐展示形态 / 发布导览矩阵”：

- 不新增研究来源，不重开阶段 5 的任何横向主干。
- 把已经锁定的阅读顺序进一步压成每个模块在展示链里的明确职责。
- 把 `presentation_forms.md` 从轻量原则页升级为可直接执行的发布导览矩阵。
- 让 `repo_map.md` 与 `deconstruction_display_overview.md` 能直接回答“每个模块现在在发布链里做什么”。

## Why it matters

- 阶段 6 的首个子单元已经锁定了入口顺序，但仓库仍停留在“顺序对了、职责还偏口头”的状态。
- 如果不把模块职责与发布导览写死，后续会话仍可能把 `Quest`、`Combat`、`Camp` 当成三份并列工程，而不是同一展示链的不同段落。
- `presentation_forms.md` 当前只给出原则，还不能直接指导“先发什么、后发什么、每个模块该以什么形态出现”。

## Repository context

- 当前高优先级依据：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 上一子单元：
  - `.agent/execplan_stage6_display_entry_and_reading_order.md`
- 本子单元的直接目标文件：
  - `docs/01_methodology/presentation_forms.md`
  - `docs/00_project/repo_map.md`
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/03_analysis/00_core_thesis.md`
  - `docs/03_analysis/01_macro_structure.md`
  - `docs/03_analysis/03_party_and_camp.md`
  - `docs/03_analysis/05_implementation_validation.md`

## Inputs and evidence

- `README.md`
- `docs/00_project/current_state.md`
- `docs/00_project/next_step.md`
- `docs/00_project/source_index.md`
- `docs/03_analysis/00_core_thesis.md`
- `docs/03_analysis/01_macro_structure.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/04_combat_and_environment.md`
- `docs/03_analysis/05_implementation_validation.md`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-007`
- `BG3-OFF-010`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`

## Milestones

1. 新建本子单元 ExecPlan
   - 明确只处理展示职责、展示形态与发布导览。
   - 明确不新增研究链、不补新来源。
2. 重写 `docs/01_methodology/presentation_forms.md`
   - 把 6 个正式模块压成一张“阅读位序 / 模块职责 / 推荐展示形态 / 发布使用方式 / 交接关系”矩阵。
3. 更新导航文件
   - `docs/00_project/repo_map.md`
   - `docs/00_project/deconstruction_display_overview.md`
   - 让仓库入口能直接把矩阵翻译成发布导览。
4. 最小回写分析模块
   - 给 `00_core_thesis.md`、`01_macro_structure.md`、`03_party_and_camp.md`、`05_implementation_validation.md` 增加阶段 6 的展示职责 / handoff 说明。
5. 同步状态与决策
   - `docs/00_project/current_state.md`
   - `docs/00_project/next_step.md`
   - `docs/00_project/decision_log.md`
6. 运行校验
   - `python scripts/check_repo.py`
   - `make check`

## Validation

- 新增 `.agent/execplan_stage6_module_guide_and_release_matrix.md`
- `presentation_forms.md` 已不再只是原则页，而是可直接执行的模块职责 / 发布导览矩阵
- `repo_map.md` 与 `deconstruction_display_overview.md` 能用相同口径解释阶段 6 当前展示链
- 至少 2 个以上分析模块带有明确的阶段 6 展示职责 / handoff 说明
- `current_state.md` 与 `next_step.md` 明确表明阶段 6 已从“入口顺序锁定”推进到“模块导览矩阵完成”
- `python scripts/check_repo.py` 与 `make check` 通过

## Progress

- 2026-04-25：创建本计划，确认本轮只处理模块职责、展示形态与发布导览矩阵，不新增来源，不回跳阶段 5。

## Decision Log

- 2026-04-25：决定把 `presentation_forms.md` 从“轻量原则页”升级成“阶段 6 当前发布矩阵”，避免展示职责继续停留在口头约定。
- 2026-04-25：决定把 `Act 收束与终局压力` 继续保留为 `01_macro_structure.md`、`02_quests_and_choices.md` 与 `03_party_and_camp.md` 的联读结果，而不是为阶段 6 新开独立入口文件。

## Surprises & Discoveries

- 当前缺口已经不是“入口顺序错了”，而是“模块读完以后该去哪、该用什么形态发布”还没有被稳定写成仓库共识。
- 只改导航还不够；至少需要让部分分析模块自己声明在展示链中的职责，后续才不会重新漂回并列工程写法。

## Outcomes & Retrospective

- 本子单元完成后，阶段 6 的下一步应进入“实际发布导览稿 / section skeleton”层，而不是继续补矩阵定义。
- 在没有更强官方来源前，后续仍不得以“优化展示”为名回跳阶段 5 扩第二条对称 spine。
