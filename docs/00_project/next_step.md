# Next Step

## 当前唯一主任务

阶段 6 / 展示收束与发布导览现已完成五段首批 actual units、首轮发布包总装配 / 审阅清单，以及三十一轮受控一致性审阅。首轮修正了 `FINAL-ASSET-001` 遗漏独立 `入口页` 行的局部 trigger，第十轮补回了 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 的双重 traceback，而 2026-04-26 的第三十一轮继续确认该 traceback 未回退、五段 actual units 仍未命中新 trigger，并把续轮入口统一推进到 `review sheet + 最新 addendum（round31）`。若继续推进，当前唯一主任务仍是按 `docs/00_project/stage6_release_package_assembly_review_sheet.md` + `.agent/execplan_stage6_release_package_assembly_review_round31.md` 继续做受控一致性审阅，只检查五段 actual units 的顺序、handoff、evidence lock 与 traceback；只有再次命中 writeback trigger 时，才回写对应单段承载文件。不要回跳阶段 5，也不要回头重写任一已完成段落的 queue。

## 本轮建议先读

- `README.md`
- `docs/00_project/deconstruction_display_overview.md`
- `docs/01_methodology/presentation_forms.md`
- `docs/00_project/repo_map.md`
- `docs/00_project/current_state.md`
- `.agent/execplan_stage6_release_package_assembly_review.md`
- `.agent/execplan_stage6_release_package_assembly_review_round31.md`
- `docs/00_project/stage6_release_package_assembly_review_sheet.md`
- `docs/00_project/stage6_entry_first_section_release_units.md`
- `docs/00_project/stage6_second_section_release_units.md`
- `docs/00_project/stage6_third_section_release_units.md`
- `docs/00_project/stage6_final_section_release_units.md`
- `docs/03_analysis/05_implementation_validation.md`

## 完成标准

- 至少再完成 `1` 轮基于 review sheet 的受控一致性审阅，并在 `stage6_release_package_assembly_review_sheet.md` 写明当前结论
- 若再次命中 trigger，至少精确回写对应单段承载文件；若未命中 trigger，明确写清“无需新增回写”的依据
- 至少同步 review-level 支撑文件与 `current_state.md`、`next_step.md`，确保“assembly / review 已存在”与“现在执行的是继续受控审阅而不是回到旧基准 ExecPlan 的起始时点”之间没有口径冲突
- `current_state.md` 和 `next_step.md` 能清楚表明：阶段 6 已从“新建 assembly / review 层”切到“已完成三十一轮受控审阅，并以 review sheet + 最新 addendum 继续做受控复核”

## 完成后必须更新

- `docs/00_project/current_state.md`
- `docs/00_project/next_step.md`
- `docs/00_project/decision_log.md`（如有新的决策变化）
- 审阅时实际被更新的单段承载文件（如有）与 assembly / review 承载文件
