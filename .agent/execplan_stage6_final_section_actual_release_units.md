# ExecPlan: Stage-6 Final Section First Actual Release Units

## Goal

把阶段 6 的第八个子单元固定为“收尾段：证据分级”的首批实际发布单元：
- 不再停留在 `presentation_forms.md` 里的最低 queue，而是把收尾段真正落成 `1` 组可复用的 `excerpt card / asset spec / traceback card`
- 本轮只处理一个位置：`收尾段：证据分级`
- 这组单元必须把“事实 / 推断 / 待验证问题”压成同一张可发布矩阵，并反向回链前四段的正文锚点
- 不新增研究来源，不回跳阶段 5，也不重写入口页、第一段、第二段、第三段的既有 actual units

## Why It Matters

- 如果收尾段继续只停在 queue 层，阶段 6 就会停在“前四段都有实物、最后一段仍只是说明文字”的半成品状态
- 收尾段是整条展示链第一次把“哪些判断已经够稳、哪些仍只是当前最强解释、哪些必须继续留作开放问题”真正压成发布物；如果这一步做不好，前四段就很容易在对外表达时被误读成同等强度的事实块
- 这一步还负责验证仓库能否把 `05_implementation_validation.md` 从“研究层的验证页”翻译成“发布层的证据分级矩阵”，而不是把 Journal / Osiris 文档误写成 shipped content 的私有实现实锤

## Repository Context

- 当前唯一高优先级依据：
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/deconstruction_master_execution_plan.md`
  - `docs/00_project/deconstruction_granular_codex_plan.md`
- 直接上游子单元：
  - `.agent/execplan_stage6_third_section_actual_release_units.md`
  - `docs/00_project/stage6_third_section_release_units.md`
- 本子单元直接落地文件：
  - `.agent/execplan_stage6_final_section_actual_release_units.md`
  - `docs/00_project/stage6_final_section_release_units.md`
  - `docs/01_methodology/presentation_forms.md`
  - `docs/00_project/deconstruction_display_overview.md`
  - `docs/00_project/repo_map.md`
  - `docs/03_analysis/05_implementation_validation.md`
  - `docs/00_project/current_state.md`
  - `docs/00_project/next_step.md`
  - `docs/00_project/decision_log.md`

## Inputs and Evidence

- 收尾段的发布 queue 与约束：
  - `docs/01_methodology/presentation_forms.md`
- 当前最稳的证据分级正文：
  - `docs/03_analysis/05_implementation_validation.md`
- 已落成的前四段 actual units：
  - `docs/00_project/stage6_entry_first_section_release_units.md`
  - `docs/00_project/stage6_second_section_release_units.md`
  - `docs/00_project/stage6_third_section_release_units.md`

## Milestones

1. 新建本子单元 ExecPlan
   - 明确本轮只落收尾段，不并行返工前四段
2. 新建收尾段实际发布单元承载文件
   - 写出 `1` 组 `excerpt card / asset spec / traceback card`
3. 最小回写展示 / 导航层
   - 在 `presentation_forms.md`、`deconstruction_display_overview.md` 与 `repo_map.md` 标明收尾段已从 queue 进入 actual units
4. 最小回写正文与证据边界
   - 在 `05_implementation_validation.md` 锁定收尾段 release anchor
   - 在 `05_implementation_validation.md` 新增收尾段 actual units evidence lock
5. 同步状态
   - 更新 `current_state.md`
   - 更新 `next_step.md`
   - 更新 `decision_log.md`

## Validation

- 已新增 `.agent/execplan_stage6_final_section_actual_release_units.md`
- 已新增 `docs/00_project/stage6_final_section_release_units.md`
- `docs/00_project/stage6_final_section_release_units.md` 里已有：
  - `1` 组 `excerpt card`
  - `1` 份 `asset spec`
  - `1` 条 `traceback card`
- `05_implementation_validation.md` 已能提供：
  - `facts / inferences / open questions` 的正文锚点
  - 对前四段 actual units 的反向回链
  - modding / Journal 文档不可越级发布的边界
- `presentation_forms.md`、`deconstruction_display_overview.md` 与 `repo_map.md` 已明确收尾段承载文件与阶段 6 当前闭合状态
- `python scripts/check_repo.py` 与 `make check` 通过

## Progress

- 2026-04-25：创建本计划，确认第八子单元只做一组“证据分级 actual units”，职责是把前四段的发布物统一重新分到 `事实 / 推断 / 待验证问题` 三层，并保留开放问题，不把 `05_implementation_validation.md` 误写成技术导论或实现总表

## Decision Log

- 2026-04-25：决定把收尾段实际单元单独承载在 `docs/00_project/stage6_final_section_release_units.md`，避免继续把前四段承载页膨胀成混合汇总页
- 2026-04-25：决定收尾段实际单元采用“证据矩阵主卡 + 回链 trace card”的写法：主卡负责重分级，trace card 负责把分级结论回链到前四段与 `Source ID`；两者都不能抹平开放问题

## Surprises & Discoveries

- 收尾段当前缺的不是更多来源，而是一份能明确声明“前四段都已经有实物，但它们并不处于同一证据强度层”的发布模板
- `05_implementation_validation.md` 已经拥有足够稳的分级语言；真正需要补的是把这些分级语言压成一张不会误导读者把 modding 文档当 shipped content 实锤的发布矩阵

## Outcomes & Retrospective

- 本子单元完成后，阶段 6 的五段首批实际发布单元可视为在当前计划下闭合
- 若后续继续推进，不应再回头重写任一段 queue；应先整理一份首轮发布包总装配 / 审阅清单，再决定是否需要新的发布层动作
