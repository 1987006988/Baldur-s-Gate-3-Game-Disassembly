# Stage 6 Release Package Assembly Review Sheet

## Scope

本文只承载阶段 6 第九个子单元之后的总装配 / 审阅层：

- `五段 actual units 的 assembly map`
- `统一 review checklist`
- `受控 writeback trigger`
- `冻结后的条件触发维护规则`

这里不重写五段正文，也不替代 `presentation_forms.md`。它只回答一件事：

> 入口页、第一段、第二段、第三段、收尾段，当前如何被装成同一条发布链；以及什么情况下才值得重开维护 round？

## Assembly Map | `ASSEMBLY-MAP-001`

| 发布位置 | 当前单元 | 承载文件 | 必须保留的职责 | 默认 handoff | 若冲突，优先回写到 |
| --- | --- | --- | --- | --- | --- |
| 入口页 | `ENTRY-EXCERPT-001` / `ENTRY-ASSET-001` / `ENTRY-TRACE-001` | `docs/00_project/stage6_entry_first_section_release_units.md` | 只立项目问题、非剧情复述边界与链条总图，不展开案例。 | `OPENING-EXCERPT-001` | `docs/00_project/stage6_entry_first_section_release_units.md` |
| 第一段：命题与导航 | `OPENING-EXCERPT-001` / `OPENING-ASSET-001` / `OPENING-TRACE-001` | `docs/00_project/stage6_entry_first_section_release_units.md` | 只锁命题、区域 / 压力梯与“为什么先看局部行动层”。 | `SECOND-EXCERPT-001` | `docs/00_project/stage6_entry_first_section_release_units.md` |
| 第二段：局部行动到状态回流 | `SECOND-EXCERPT-001` / `SECOND-ASSET-001` / `SECOND-TRACE-001` | `docs/00_project/stage6_second_section_release_units.md` | 只展示章节接力：左侧局部 agency，右侧高可见 readback。 | `THIRD-EXCERPT-001` | `docs/00_project/stage6_second_section_release_units.md` |
| 第三段：延迟反馈折叠 | `THIRD-EXCERPT-001` / `THIRD-ASSET-001` / `THIRD-TRACE-001` | `docs/00_project/stage6_third_section_release_units.md` | 只展示 `camp fold / delayed feedback` 与 supporting-bundle 边界。 | `FINAL-EXCERPT-001` | `docs/00_project/stage6_third_section_release_units.md` |
| 收尾段：证据分级 | `FINAL-EXCERPT-001` / `FINAL-ASSET-001` / `FINAL-TRACE-001` | `docs/00_project/stage6_final_section_release_units.md` | 只负责重分级与回链，不替代前四段正文。 | 结束 | `docs/00_project/stage6_final_section_release_units.md` |

## Review Checklist | `ASSEMBLY-CHECK-001`

### A. 顺序与交接

- [x] 入口页只解释项目问题与边界，未提前吞掉第一段命题职责。
- [x] 第一段明确 handoff 到局部行动层，而不是直接跳到任务表或营地页。
- [x] 第二段保留了对第三段的 handoff，没有把 camp fold 提前吞掉。
- [x] 第三段明确 handoff 到 `05_implementation_validation.md`，没有提前完成证据分级。
- [x] 收尾段只做回链与重分级，没有反向取代前四段。

### B. 证据强度与 traceback

- [x] 五段都保留了文档锚点与 `Source ID` traceback path。
- [x] 五段没有把 `BG3-OFF-011` 到 `BG3-OFF-014` 越级写成 shipped content 私有脚本实锤。
- [x] 第二段、第三段、收尾段都保留了“当前不能越级发布什么”的边界条。
- [x] 当前总装配层可以安全回答“哪一段负责什么、从哪里回链、哪里必须停在当前最强解释”。

## Historical Maintenance Summary | `ASSEMBLY-HISTORY-001`

这里只保留仍会影响当前维护判断的关键节点；完整维护记录继续留在 `.agent/execplan_stage6_release_package_assembly_review_round*.md`。

- `2026-04-25A`：
  - 首轮一致性审阅命中局部 trigger，发现 `FINAL-ASSET-001` 把 `入口页` 并入第一段。
  - 已精确回写 `docs/00_project/stage6_final_section_release_units.md`、`presentation_forms.md` 与 `05_implementation_validation.md`，恢复收尾段证据矩阵中的独立 `入口页` 行。
- `2026-04-25J`：
  - 第十轮一致性审阅命中 `ASSEMBLY-TRIGGER-001` 的 trigger `5`。
  - 已补回 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback，并在 `docs/00_project/stage6_final_section_release_units.md` 与 `docs/03_analysis/05_implementation_validation.md` 保持完整。
- `2026-04-25K` 到 `2026-04-26F`：
  - 第十一轮到第三十二轮未再命中新 actual-unit 级 trigger。
  - 这段维护主要在清理 review-level 入口文件的 addendum 指针漂移，而不是新增五段正文改动。
- `2026-04-26G`：
  - 本轮将“latest addendum 指针同步”从主动维护逻辑中剥离。
  - `review sheet` 现在是唯一主动维护入口；`round*.md` 退回维护记录链，`round32` 只保留为截至 2026-04-26 的最近一次维护快照。

## Writeback Triggers | `ASSEMBLY-TRIGGER-001`

只有命中以下任一条件，才允许回写单段 actual units 承载文件：

1. handoff 顺序与 `presentation_forms.md`、`repo_map.md` 或 `deconstruction_display_overview.md` 冲突。
2. 某一段把下一段的职责提前吞掉，例如第二段提前吃掉第三段的 camp fold，或第三段提前吃掉收尾段的证据分级。
3. 某一段把 supporting bundle / handoff 误升成第二条对称 spine。
4. 某一段把 `BG3-OFF-011` 到 `BG3-OFF-014` 或其它公开 modding / Journal 文档越级写成 shipped content 实锤。
5. 某一段失去 traceback path，导致无法回链到正文或 `Source ID`。

如果以上条件都未命中：

- 保持五段 actual units 原文件不动。
- 不自动新增新的 review round。
- 不因为 `latest addendum` 文件名还可以继续递增，就把维护记录重新抬成主线。
- 优先维持冻结态与维护规则说明，而不是重写 release unit。

## Freeze Maintenance Status | `ASSEMBLY-MAINT-2026-04-26G`

- 阶段 6 的首批发布包已经闭合。
- `docs/00_project/stage6_release_package_assembly_review_sheet.md` 现在是默认主动维护入口。
- `.agent/execplan_stage6_release_package_assembly_review_round*.md` 全部保留为维护记录链：
  - `round1` 到 `round31` 是历史维护 / 归档记录
  - `round32` 是截至 2026-04-26 的最近一次维护记录
  - 它们都不是当前默认唯一主任务
- 只有出现以下情况之一，才允许重开新的 stage 6 review round：
  1. 五段 actual units 之一发生正文级改动
  2. `entry / opening / camp / closing / final` 的 handoff 顺序发生变化
  3. evidence lock 或 benchmark traceback 出现回退、缺失、错链
  4. release package assembly map 被改动后需要重新校对
  5. 项目负责人明确要求对发布链做新一轮一致性审阅
- 以下情况不应触发新 round：
  1. 只是为了“再谨慎检查一轮”
  2. 没有新的正文改动，也没有新的 trigger
  3. 只是 latest addendum 文件名还可以继续递增
  4. 没有任何 evidence / assembly / handoff 层面的实质变化

## Maintenance Pass | `ASSEMBLY-MAINT-CHECK-001`

- 默认先按 `docs/01_methodology/stage6_freeze_maintenance_playbook.md` 执行冻结维护态检查，而不是直接重开新的 round。
- `Pass 1` 先判定是否命中 `ASSEMBLY-TRIGGER-001`。
- `Pass 2` 只在 review-layer / 状态入口范围内检查口径是否退回“latest addendum 指针”或“默认 round33”。
- `Pass 3` 只复核两类仍会影响后续判断的 evidence lock：
  - `FINAL-ASSET-001` 是否继续保留独立 `入口页` 行
  - `ENTRY-TRACE-001` 是否继续保留 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback
- 若以上检查都未命中 trigger，本轮默认只允许更新 review-layer / 状态文件，不允许回写五段 actual units。

## Reopen Reading Order

只有在确实命中新 trigger 时，才按以下顺序重开：

1. `README.md`
2. `docs/00_project/current_state.md`
3. `docs/00_project/deconstruction_master_execution_plan.md`
4. `docs/00_project/stage6_release_package_assembly_review_sheet.md`
5. `.agent/execplan_stage6_release_package_assembly_review_round32.md`
6. `docs/03_analysis/05_implementation_validation.md`

## First-Pass Verdict

- 当前状态：`no hard blocker`
- 当前最稳结论：阶段 6 已从“五段 actual units 闭合”推进到“存在统一 assembly / review 层，并已完成必要维护纠偏”。首轮 `FINAL-ASSET-001` 的独立 `入口页` 行问题与第十轮 `ENTRY-TRACE-001` benchmark traceback 问题都已修正并保持有效。
- 当前默认动作：维持阶段 6 冻结维护态，不自动新增 `round33`；若未来再次命中新 trigger，再从本 review sheet 重开维护判断，并按需要读取最近一次维护记录。

## Files In Play

- `.agent/execplan_stage6_release_package_assembly_review.md`
- `.agent/execplan_stage6_release_package_assembly_review_round32.md`
- `.agent/execplan_stage6_freeze_maintenance_stabilization.md`
- `.agent/execplan_stage6_freeze_maintenance_playbook.md`
- `docs/01_methodology/presentation_forms.md`
- `docs/01_methodology/stage6_freeze_maintenance_playbook.md`
- `docs/00_project/deconstruction_display_overview.md`
- `docs/00_project/deconstruction_master_execution_plan.md`
- `docs/00_project/deconstruction_granular_codex_plan.md`
- `docs/00_project/repo_map.md`
- `docs/03_analysis/05_implementation_validation.md`
- `docs/00_project/stage6_entry_first_section_release_units.md`
- `docs/00_project/stage6_second_section_release_units.md`
- `docs/00_project/stage6_third_section_release_units.md`
- `docs/00_project/stage6_final_section_release_units.md`
