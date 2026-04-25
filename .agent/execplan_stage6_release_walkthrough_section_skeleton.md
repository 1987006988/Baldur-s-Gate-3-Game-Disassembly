# ExecPlan: Stage-6 Release Walkthrough Section Skeleton

## Goal

把阶段 6 的第三个子单元固定为“实际发布导览稿 / section skeleton”：

- 不新增研究来源，不重开阶段 5 的任何横向主干。
- 把已经锁定的阅读顺序与模块职责矩阵，继续压成一份可直接复用的发布导览骨架。
- 让仓库不只知道“先读谁、每个模块负责什么”，还知道“导览稿第一段到最后一段各自讲什么、依赖哪几份正文、默认交给下一段什么”。

## Why It Matters

- 阶段 6 的前两个子单元已经解决了“顺序”和“职责”，但还没有解决“实际怎么讲、怎么排、每段怎么交接”。
- 如果这一层不落成，仓库仍会停在“展示原则齐了、发布组织未落地”的半成品状态。
- 后续会话也仍可能借“优化展示”之名回跳阶段 5，重新把 `Quest`、`Combat`、`Camp` 当成并列工程补写。

## Repository Context

- 当前唯一高优先级依据：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 直接承接的上两个子单元：
  - `.agent/execplan_stage6_display_entry_and_reading_order.md`
  - `.agent/execplan_stage6_module_guide_and_release_matrix.md`
- 本子单元直接目标文件：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/01_methodology/presentation_forms.md`
  - `docs/00_project/repo_map.md`
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
  - `docs/00_project/decision_log.md`

## Inputs And Evidence

- `README.md`
- `docs/00_project/current_state.md`
- `docs/00_project/next_step.md`
- `docs/00_project/source_index.md`
- `docs/00_project/deconstruction_display_overview.md`
- `docs/01_methodology/presentation_forms.md`
- `docs/00_project/repo_map.md`
- `docs/03_analysis/00_core_thesis.md`
- `docs/03_analysis/01_macro_structure.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/04_combat_and_environment.md`
- `docs/03_analysis/05_implementation_validation.md`
- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-007`
- `BG3-OFF-010`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`

## Milestones

1. 新建本子单元 ExecPlan
   - 明确本轮只处理发布导览稿 / section skeleton。
   - 明确不新增来源、不回跳阶段 5。
2. 更新 `docs/00_project/deconstruction_display_overview.md`
   - 把“顺序解释 + 模块职责”压成一份可直接复用的导览稿骨架。
   - 明确每一段的目的、依赖模块与默认 handoff。
3. 更新 `docs/01_methodology/presentation_forms.md`
   - 把方法矩阵继续压成可执行的 section skeleton 与首轮发布最低配置。
4. 最小同步导航文件
   - 更新 `docs/00_project/repo_map.md`
   - 确保入口层、矩阵层与导览稿层口径一致。
5. 同步项目状态
   - 更新 `docs/00_project/current_state.md`
   - 更新 `docs/00_project/next_step.md`
   - 更新 `docs/00_project/decision_log.md`
6. 运行校验
   - `python scripts/check_repo.py`
   - `make check`

## Validation

- 新增 `.agent/execplan_stage6_release_walkthrough_section_skeleton.md`
- `docs/00_project/deconstruction_display_overview.md` 已不只解释顺序，而是提供可直接复用的 section skeleton
- `docs/01_methodology/presentation_forms.md` 已不只停在模块矩阵，而是写清首轮发布最低配置
- `docs/00_project/repo_map.md` 能直接告诉后续会话“发布导览骨架在哪里、下一步该补什么”
- `docs/00_project/current_state.md` 与 `docs/00_project/next_step.md` 明确表明阶段 6 已完成第三个子单元
- `python scripts/check_repo.py` 与 `make check` 通过

## Progress

- 2026-04-25：创建本计划，确认本轮只把阶段 6 的“顺序 + 职责”继续压成实际发布导览稿 / section skeleton；不新增研究来源，不回跳阶段 5。

## Decision Log

- 2026-04-25：决定把阶段 6 的第三个子单元落在现有文件上，优先更新 `deconstruction_display_overview.md` 与 `presentation_forms.md`，而不是另开新的项目级展示主文件。
- 2026-04-25：决定把 `Act 收束与终局压力` 继续保留为跨 `01_macro_structure.md`、`02_quests_and_choices.md` 与 `03_party_and_camp.md` 的联读段，而不把 section skeleton 扭回单独终局章。

## Surprises & Discoveries

- 当前最大缺口已经不是“先读谁”，而是“导览稿每一段到底该拿哪份正文、讲到哪一层、交给下一段什么”。
- 真正缺的不是更多展示原则，而是一份能直接约束后续会话的发布骨架。

## Outcomes & Retrospective

- 本子单元完成后，阶段 6 的下一步应切到“首轮发布包 / excerpt queue / asset queue”，也就是为每一段锁定最低必需的图、卡、摘录与回溯路径。
- 在没有更强官方来源前，后续不应再借“补展示”之名重开阶段 5 的第二条对称主链。
