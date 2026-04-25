# ExecPlan: Stage-6 Release Package Assembly Review

## Goal

把阶段 6 从“五段 actual units 已各自落成”推进到“已有一份可直接驱动装配与审阅的总装配层”：

- 新建 `1` 份只服务 assembly / review 的汇总清单，而不是再补第六段 actual units
- 把入口页、第一段、第二段、第三段、收尾段压进同一份可执行 review sheet
- 明确哪些检查只在总装配层做，哪些情况才允许回写单段承载文件
- 不回跳阶段 5，不重写任一段 queue，也不把五段正文重新复制一遍

## Why It Matters

- 如果没有总装配 / 审阅层，阶段 6 会继续停在“每段都有实物，但没有统一装配规则”的半成品状态。
- 五段 actual units 当前已经闭合；下一步最稳的工作不再是补单段，而是确认它们在顺序、handoff、证据强度与 traceback 上能否作为同一条发布链工作。
- 这一步还负责把“何时才值得回写单段文件”写死，避免后续会话借审阅之名回头重写 queue、误升 supporting bundle，或把 modding / Journal 文档写成 shipped content 实锤。

## Repository Context

- 当前唯一高优先级依据：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 直接输入文件：
  - `docs/01_methodology/presentation_forms.md`
  - `docs/00_project/repo_map.md`
  - `docs/03_analysis/05_implementation_validation.md`
  - `docs/00_project/stage6_entry_first_section_release_units.md`
  - `docs/00_project/stage6_second_section_release_units.md`
  - `docs/00_project/stage6_third_section_release_units.md`
  - `docs/00_project/stage6_final_section_release_units.md`
- 本子单元直接落地文件：
  - `.agent/execplan_stage6_release_package_assembly_review.md`
  - `docs/00_project/stage6_release_package_assembly_review_sheet.md`
  - `docs/01_methodology/presentation_forms.md`
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
  - `docs/00_project/repo_map.md`
  - `docs/03_analysis/05_implementation_validation.md`
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
  - `docs/00_project/decision_log.md`

## Inputs and Evidence

- 已闭合的五段 actual units：
  - `docs/00_project/stage6_entry_first_section_release_units.md`
  - `docs/00_project/stage6_second_section_release_units.md`
  - `docs/00_project/stage6_third_section_release_units.md`
  - `docs/00_project/stage6_final_section_release_units.md`
- 当前展示层唯一真源：
  - `docs/01_methodology/presentation_forms.md`
- 当前最稳的证据边界：
  - `docs/03_analysis/05_implementation_validation.md`

## Milestones

1. 新建总装配 / 审阅 ExecPlan
   - 只定义 assembly / review 层职责，不并行新增新的 actual units
2. 新建汇总承载文件
   - 至少写出 `assembly map`、`review checklist`、`writeback trigger` 三块
3. 回写展示方法与导航层
   - 在 `presentation_forms.md`、`deconstruction_display_overview.md`、`repo_map.md` 中固定新承载文件与下一步动作
4. 回写总计划与验证层
   - 把 assembly / review 写回高优先级总计划文件
   - 在 `05_implementation_validation.md` 新增 assembly / review anchor 与 evidence lock
5. 同步状态
   - 更新 `current_state.md`
   - 更新 `next_step.md`
   - 更新 `decision_log.md`

## Validation

- 已新增 `.agent/execplan_stage6_release_package_assembly_review.md`
- 已新增 `docs/00_project/stage6_release_package_assembly_review_sheet.md`
- `docs/00_project/stage6_release_package_assembly_review_sheet.md` 至少包含：
  - `ASSEMBLY-MAP-001`
  - `ASSEMBLY-CHECK-001`
  - `ASSEMBLY-TRIGGER-001`
- `presentation_forms.md`、`deconstruction_display_overview.md`、`deconstruction_master_execution_plan.md`、`deconstruction_granular_codex_plan.md` 与 `repo_map.md` 已写明：阶段 6 的下一步是 assembly / review，而不是重写 queue
- `05_implementation_validation.md` 已能为 assembly / review 提供 release anchor 与 evidence lock
- `python scripts/check_repo.py` 与 `make check` 通过

## Progress

- 2026-04-25：创建本计划，确认当前子单元只做“总装配 / 审阅层”，不新增新段落，不重开阶段 5，也不回头重写任一已落成 actual unit。

## Decision Log

- 2026-04-25：决定把 assembly / review 单独承载在 `docs/00_project/stage6_release_package_assembly_review_sheet.md`，而不是继续向任一段 actual units 文件塞汇总信息。
- 2026-04-25：决定 assembly / review 层只承担三件事：装配顺序、审阅清单、回写触发条件；它不负责生成新的 release unit，也不负责替代五段原始承载文件。

## Surprises & Discoveries

- 当前最缺的不是更多发布文案，而是一份能把五段 actual units 的职责边界放在同一张表里核对的汇总层。
- `05_implementation_validation.md` 已经拥有足够稳的 release-facing evidence lock；真正需要补的是一份使用这些锁来判断“要不要回写单段”的装配清单。

## Outcomes & Retrospective

- 本子单元完成后，阶段 6 不再只是“五段都做出来了”，而是“已经有一份总装配 / 审阅层可驱动后续一致性检查”。
- 若后续继续推进，优先动作应是执行这份 review sheet 的首轮一致性审阅；只有命中 writeback trigger 时，才回写单段承载文件。
