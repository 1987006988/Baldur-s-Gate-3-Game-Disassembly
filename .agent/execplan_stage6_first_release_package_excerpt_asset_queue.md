# ExecPlan: Stage-6 First Release Package Minimum Config / Excerpt Asset Queue

## Goal

把阶段 6 的第四个子单元固定为“首轮发布包最低配置 / excerpt queue / asset queue”：

- 不新增研究来源，不回跳阶段 5 的任何横向主干。
- 把既有 `section skeleton` 继续压成每一段的最小发布单元：必须摘录什么、至少需要哪张图、要准备哪类卡片、从哪份正文与 `Source ID` 回溯。
- 让后续会话直接回答“下一步补哪张卡、哪张图、哪条摘录”，而不是再讨论阅读顺序、模块职责或展示原则。

## Why It Matters

- 阶段 6 的前三个子单元已经解决了“先读谁”“谁负责什么”“导览稿怎么一段一段讲”，但还没有解决“首轮发布包最少要带什么”。
- 如果这一步不落地，仓库仍会停在“导览骨架已经写好、实际发布包仍然是空壳”的半成品状态。
- 如果不把 excerpt / asset / card / traceback 四类最小单元写死，后续会话很容易再回到无上限补图、补摘录，或者借“补展示”之名回跳阶段 5。

## Repository Context

- 当前唯一高优先级依据：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 已完成的直接上游子单元：
  - `.agent/execplan_stage6_display_entry_and_reading_order.md`
  - `.agent/execplan_stage6_module_guide_and_release_matrix.md`
  - `.agent/execplan_stage6_release_walkthrough_section_skeleton.md`
- 本子单元直接落地文件：
  - `docs/01_methodology/presentation_forms.md`
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/repo_map.md`
  - `docs/03_analysis/05_implementation_validation.md`
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
- `docs/03_analysis/05_implementation_validation.md`
- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-006`
- `BG3-OFF-007`
- `BG3-OFF-008`
- `BG3-OFF-010`
- `BG3-OFF-011`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-015`
- `BG3-OFF-016`

## Milestones

1. 新建本子单元 ExecPlan
   - 明确本轮只处理“首轮发布包最低配置 / excerpt queue / asset queue”。
   - 明确不新增来源、不回跳阶段 5。
2. 更新 `docs/01_methodology/presentation_forms.md`
   - 把 5 段发布导览稿继续压成统一的最小发布清单。
   - 为每一段写清 excerpt queue、asset queue、card queue 与 traceback path。
3. 更新导航层文件
   - 在 `docs/00_project/deconstruction_display_overview.md` 说明第四子单元现在固定了什么。
   - 在 `docs/00_project/repo_map.md` 明确最低发布包清单现在放在哪里、下一步该补哪一层。
4. 最小回写正文证据层
   - 在 `docs/03_analysis/05_implementation_validation.md` 增加面向发布的 evidence queue，说明每段当前最稳的公开证据入口与不能越级摘录的边界。
5. 同步项目状态
   - 更新 `docs/00_project/current_state.md`
   - 更新 `docs/00_project/next_step.md`
   - 更新 `docs/00_project/decision_log.md`
6. 运行校验
   - `python scripts/check_repo.py`
   - `make check`

## Validation

- 新增 `.agent/execplan_stage6_first_release_package_excerpt_asset_queue.md`
- `docs/01_methodology/presentation_forms.md` 已不再只停留在 `section skeleton`，而是能直接回答每段至少需要什么摘录 / 图 / 卡片 / 回溯路径。
- `docs/00_project/deconstruction_display_overview.md` 与 `docs/00_project/repo_map.md` 已明确第四子单元的产物位置与使用方式。
- `docs/03_analysis/05_implementation_validation.md` 已新增 release-facing evidence queue，而不是只停留在阶段出口原则。
- `docs/00_project/current_state.md` 与 `docs/00_project/next_step.md` 已从“section skeleton”切换到“最低发布配置已锁定，下一步进入首批实际卡片 / 资产规格”。
- `python scripts/check_repo.py` 与 `make check` 通过。

## Progress

- 2026-04-25：创建本计划，确认本轮只把阶段 6 的导览骨架继续压成“首轮发布包最低配置 / excerpt queue / asset queue”，不新增来源，不重开阶段 5。

## Decision Log

- 2026-04-25：决定把阶段 6 的第四个子单元集中落在 `presentation_forms.md`，由它承担最小发布包清单的单一真源，而不是把 excerpt / asset 要求分散写进多个导航文件。
- 2026-04-25：决定只在 `05_implementation_validation.md` 增加面向发布的 evidence queue，不再额外新开一份“展示证据总表”文件，避免研究层与展示层再次分叉。

## Surprises & Discoveries

- 当前真正缺的不是更多展示原则，而是一个能约束后续会话工作粒度的最小发布单元表。
- 发布层当前最大的风险不是内容不够，而是容易一次想做太多替代摘录、替代图和替代卡片，反而让首轮发布包迟迟不能闭合。

## Outcomes & Retrospective

- 本子单元完成后，阶段 6 的下一步应切到“首批实际 excerpt card / asset spec / traceback card”，优先入口页与第一段，而不是继续补原则。
- 在没有更强官方来源前，后续仍不得借“补发布包”之名回跳阶段 5、重开第二条对称 `Quest` / `Combat` / `Camp` spine。
