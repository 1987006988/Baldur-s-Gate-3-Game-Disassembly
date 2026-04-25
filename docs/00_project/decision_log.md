# Decision Log

## 2026-04-25 | 将阶段 6 的第九个子单元固定为“first release package assembly / review sheet”

- 为什么改：五段 actual units 虽然已经闭合，但仓库仍缺一层统一的 assembly / review，无法稳定回答“这五段如何装成同一条发布链、先审什么、什么情况下才值得回写单段文件”。如果没有这一步，后续会话很容易借审阅之名回头重写 queue、误升 supporting bundle，或把 modding / Journal 文档越级写成 shipped content 实锤。
- 改动影响范围：`.agent/execplan_stage6_release_package_assembly_review.md`、`docs/00_project/stage6_release_package_assembly_review_sheet.md`、`docs/01_methodology/presentation_forms.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/00_project/deconstruction_master_execution_plan.md`、`docs/00_project/deconstruction_granular_codex_plan.md`、`docs/00_project/repo_map.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：下一步应执行这份 review sheet 的首轮一致性审阅，只在命中 writeback trigger 时回写对应单段承载文件；不要把 assembly / review 层继续膨胀成第二份导览稿，也不要借它回跳阶段 5。

## 2026-04-25 | 将阶段 6 首轮一致性审阅的首个局部 writeback 收束为“final evidence matrix keeps a standalone entry-page row”

- 为什么改：`ASSEMBLY-MAP-001`、`presentation_forms.md` 与 `repo_map.md` 都把 `入口页` 视为五段发布链中的独立装配位，但 `docs/00_project/stage6_final_section_release_units.md` 里的 `FINAL-ASSET-001` 行集只列了第一段、第二段、第三段与收尾段，等于把 `入口页` 并进了第一段，削弱了收尾段证据矩阵对前四段 actual units 的 traceback 完整性。
- 改动影响范围：`docs/00_project/stage6_final_section_release_units.md`、`docs/00_project/stage6_release_package_assembly_review_sheet.md`、`docs/01_methodology/presentation_forms.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`
- 后续注意事项：后续一致性审阅必须把“`入口页`、第一段、第二段、第三段”固定视为收尾段证据矩阵中的四个上游行位；如果没有新的 trigger，不要继续重写其它 actual units，也不要借这个修正回跳阶段 5。

## 2026-04-25 | 将阶段 6 的当前执行口径固定为“continue controlled review”，而不是“future first review”

- 为什么改：首轮一致性审阅已经完成并修正了 `FINAL-ASSET-001` 的独立 `入口页` 行，但 `deconstruction_display_overview.md`、`deconstruction_master_execution_plan.md`、`deconstruction_granular_codex_plan.md`、`presentation_forms.md` 与 `repo_map.md` 里仍保留“下一步执行首轮一致性审阅”的旧表述。如果不修，这些高优先级文件会继续把当前主任务描述成过去时点之前的动作，削弱阶段 6 的唯一主线。
- 改动影响范围：`docs/00_project/deconstruction_display_overview.md`、`docs/00_project/deconstruction_master_execution_plan.md`、`docs/00_project/deconstruction_granular_codex_plan.md`、`docs/01_methodology/presentation_forms.md`、`docs/00_project/repo_map.md`、`docs/00_project/stage6_release_package_assembly_review_sheet.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`
- 后续注意事项：后续阶段 6 继续推进时，应默认进入“受控一致性审阅（续轮）”；若未命中新 actual-unit trigger，就只更新审阅结论与状态同步，不回头重写任一 release unit，也不借口径漂移回跳阶段 5。

## 2026-04-25 | 将阶段 6 的第七个子单元固定为“third section first actual release units”

- 为什么改：第二段虽然已经有第一批实际发布单元，但第三段仍停留在 queue 层；如果不把“延迟反馈折叠”真正落成一组实际发布单元，阶段 6 会继续卡在“营地只存在于说明文字、没有真实发布物”的半成品状态。
- 改动影响范围：`.agent/execplan_stage6_third_section_actual_release_units.md`、`docs/00_project/stage6_third_section_release_units.md`、`docs/01_methodology/presentation_forms.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/00_project/repo_map.md`、`docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：第三段实际单元必须坚持“主折返层 + supporting-bundle 边界条”口径，不能把 `reflection / roster-state`、`dialogue accessibility maintenance` 或 late-game `ending feedback` 误写成第二条公开营地主干；下一步应直接切到“收尾段：证据分级”的首批实际发布单元，不要回头重写第三段 queue，也不要借“补发布”之名回跳阶段 5。

## 2026-04-25 | 将阶段 6 的第四个子单元固定为“first release package minimum config / excerpt queue / asset queue”

- 为什么改：`section skeleton` 虽然已经锁定，但仓库仍缺少一份能直接约束后续会话工作粒度的最小发布单元表；如果不把每一段最低需要的摘录 / 图 / 卡片 / 回溯路径写死，阶段 6 仍会停在“导览稿已经写好、发布包尚未成形”的半成品状态。
- 改动影响范围：`.agent/execplan_stage6_first_release_package_excerpt_asset_queue.md`、`docs/01_methodology/presentation_forms.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/00_project/repo_map.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：下一步不应再补展示原则，而应直接把入口页与第一段落成第一批实际 `excerpt card / asset spec / traceback card`；在没有更强官方来源前，也不得借“补发布包”之名回跳阶段 5、重开第二条对称主链。

## 2026-04-25 | 将阶段 6 的第六个子单元固定为“second section first actual release units”

- 为什么改：入口页与第一段虽然已经有第一批实际发布单元，但第二段仍停留在 queue 层；如果不把“局部行动到状态回流”真正落成一组实际发布单元，阶段 6 会继续卡在“只有开场有实物、中段仍是计划表”的半成品状态。
- 改动影响范围：`.agent/execplan_stage6_second_section_actual_release_units.md`、`docs/00_project/stage6_second_section_release_units.md`、`docs/01_methodology/presentation_forms.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/00_project/repo_map.md`、`docs/03_analysis/04_combat_and_environment.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：第二段实际单元必须坚持“章节接力双联卡”口径，不能把 `Grymforge` 与 `Minthara -> Moonrise Towers` 误写成同一条具体因果链；下一步应直接切到“第三段：延迟反馈折叠”的首批实际发布单元，不要回头重写第二段 queue，也不要借“补发布”之名回跳阶段 5。

## 2026-04-22 | 采用三层拆解作为仓库主方法

- 为什么改：普通剧情整理无法解释玩家自由感的形成机制，单纯功能罗列也无法解释沉浸与反馈。
- 改动影响范围：`README.md`、`docs/01_methodology/*`、`docs/03_analysis/*`
- 后续注意事项：所有模块都要覆盖体验层、系统层、实现验证层，避免只写其中一层。

## 2026-04-22 | 用状态文件承担长期记忆，而不是依赖会话上下文

- 为什么改：长期研究需要跨会话恢复上下文，聊天记录不稳定也不适合作为唯一记忆载体。
- 改动影响范围：`docs/00_project/current_state.md`、`next_step.md`、`repo_map.md`、`source_index.md`
- 后续注意事项：每次有意义的研究推进后都要同步状态文件。

## 2026-04-22 | 优先把“任务与选择”设为首个深挖模块

- 为什么改：它最直接承载 BG3 的高反应性印象，也最能检验三层拆解方法是否有效。
- 改动影响范围：`docs/00_project/current_state.md`、`next_step.md`、`docs/03_analysis/02_quests_and_choices.md`
- 后续注意事项：需要尽快补齐来源与案例，防止该模块停留在高层判断。

## 2026-04-22 | 新增项目级主路线图并将下一步切换为先写首份 ExecPlan

- 为什么改：仓库已有结构和模块骨架，但缺少项目级推进顺序、阶段出口条件和跑偏判定，容易让后续会话直接进入局部补写。
- 改动影响范围：`docs/00_project/master_roadmap.md`、`current_state.md`、`next_step.md`
- 后续注意事项：后续优先按照路线图推进，不要在没有 ExecPlan 的情况下直接展开大型模块深挖。

## 2026-04-22 | 明确展示层从属于研究层，并为任务与选择模块落首份 ExecPlan

- 为什么改：仓库接下来会进入证据底座建设阶段，需要先防止展示需求提前牵引研究结构；同时“任务与选择回流”已具备作为首个可执行计划对象的条件。
- 改动影响范围：`docs/01_methodology/presentation_forms.md`、`.agent/execplan_quests_and_choices.md`、`current_state.md`、`next_step.md`
- 后续注意事项：后续若制作任何展示物，必须回溯到研究文档与 Source ID；任务与选择模块的后续推进应优先依据 ExecPlan，而不是临时改主线。

## 2026-04-22 | 将任务与选择模块的首批来源从泛指集合收紧为 5 条具体来源

- 为什么改：ExecPlan 已进入执行阶段，需要先把“官方更新 / 开发者说明 / 社区案例”落成具体可追溯条目，否则后续案例筛选仍会停留在泛化口径。
- 改动影响范围：`docs/00_project/source_index.md`、`docs/02_sources/source_note_bg3_off_002_patch_7.md`、`docs/02_sources/source_note_bg3_off_003_xbox_podcast.md`、`docs/02_sources/source_note_bg3_off_004_hotfix_20.md`、`current_state.md`、`next_step.md`
- 后续注意事项：社区来源继续只作为案例线索使用；在没有官方或更强来源交叉支撑前，不要把社区讨论直接写成事实。

## 2026-04-22 | 先用两条案例骨架闭合 ExecPlan，再决定正文整合权重

- 为什么改：当前阶段的关键不是继续扩案例，而是先验证两条最小证据链能否闭合；同时需要承认两条案例的证据强度并不对称。
- 改动影响范围：`.agent/execplan_quests_and_choices.md`、`docs/02_sources/case_note_minthara_knockout_path.md`、`docs/02_sources/case_note_dark_urge_bard_event.md`、`current_state.md`、`next_step.md`
- 后续注意事项：Minthara 路径可作为当前主案例继续推进；Dark Urge bard 事件在获得更直接来源前，应优先作为辅案例或待验证耦合案例处理。

## 2026-04-22 | 用官方 Community Update #28 补强 Dark Urge bard 事件，并完成正文回写准备

- 为什么改：Milestone 4 的完成要求不仅是整理主辅案例边界，还要尽量为较弱案例找到更直接的官方支撑，降低正文回写时的悬空感。
- 改动影响范围：`docs/00_project/source_index.md`、`docs/02_sources/source_note_bg3_off_005_cu28_dark_urge_bard.md`、`docs/02_sources/case_note_dark_urge_bard_event.md`、`.agent/quests_and_choices_writeback_prep.md`、`current_state.md`、`next_step.md`
- 后续注意事项：即使补入 `BG3-OFF-005`，Dark Urge bard 事件仍应作为辅案例；正文整合时不要让它承担超过现有证据强度的结论。

## 2026-04-22 | 完成任务与选择模块首轮正文回写，并固定主辅案例权重

- 为什么改：准备区材料已经足够支撑首轮正文；继续停留在准备文件会增加维护成本，也无法检验研究结论是否真能落入分析模块。
- 改动影响范围：`docs/03_analysis/02_quests_and_choices.md`、`.agent/execplan_quests_and_choices.md`、`current_state.md`、`next_step.md`
- 后续注意事项：Minthara 路径可继续承担主案例；Dark Urge bard 事件在获得更多直接来源前，只能承担辅案例或营地耦合说明。

## 2026-04-22 | 对营地模块和实现验证模块做最小同步，而不重复扩写任务模块

- 为什么改：任务模块已经形成可追溯正文，如果耦合点仍只存在于一个模块内部，后续会导致跨模块理解断裂。
- 改动影响范围：`docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/source_index.md`、`current_state.md`、`next_step.md`
- 后续注意事项：这次同步只承接已确认的营地折返反馈与补丁验证入口，不代表相关模块已经完成深挖。

## 2026-04-22 | 先锁定 Grymforge / Grym 作为战斗 / 环境向补强方向，而不急于回写正文

- 为什么改：当前任务模块的结构偏差已经明确，但直接把一个证据层级还不够稳的战斗案例写入正文，风险高于收益；先把方向锁定并记录证据缺口更安全。
- 改动影响范围：`docs/02_sources/source_note_bg3_ply_004_grym_environment_case.md`、`docs/02_sources/case_note_grymforge_environment_resolution.md`、`docs/00_project/source_index.md`、`current_state.md`、`next_step.md`
- 后续注意事项：后续优先为 Grymforge / Grym 补更高层来源；在此之前，它应作为“补强方向”而不是正文既定案例。

## 2026-04-22 | 用官方 Grymforge 区域框架来源补强后，决定先深挖战斗模块再回流任务模块

- 为什么改：`BG3-OFF-006` 已足以证明 Grymforge 兼具任务、选择与复杂战斗遭遇，但仍不足以直接支撑某条具体环境解法进入任务模块正文。
- 改动影响范围：`docs/02_sources/source_note_bg3_off_006_cu14_grymforge.md`、`docs/02_sources/case_note_grymforge_environment_resolution.md`、`docs/00_project/source_index.md`、`current_state.md`、`next_step.md`
- 后续注意事项：Grymforge / Grym 现阶段应优先作为 `04_combat_and_environment` 的主深挖案例；是否回流到任务模块，取决于后续具体路径证据是否足够稳。

## 2026-04-22 | 先在战斗模块落稳 Grymforge / Grym 的高层判断，再决定回流范围

- 为什么改：目前已经有足够来源支撑 Grymforge / Grym 在战斗模块中的高层成立，但仍不够把具体环境解法完整写成任务模块事实链。
- 改动影响范围：`docs/03_analysis/04_combat_and_environment.md`、`docs/00_project/source_index.md`、`current_state.md`、`next_step.md`
- 后续注意事项：回流到任务模块时，只能回流“环境与战斗也是一种选择系统”这一层的稳定判断；具体打法仍需继续筛稳。
## 2026-04-22 | 完成 Grymforge / Grym 的最小必要回流，并将主线切换到评估首份 ExecPlan 出口
- 为什么改：高层判断已经足够支持把“战斗 / 环境也是一种选择系统”补回任务模块；继续让同一 ExecPlan 占用主线，会把仓库重新拖回局部补证据而不是阶段切换。
- 改动影响范围：`docs/03_analysis/02_quests_and_choices.md`、`.agent/execplan_quests_and_choices.md`、`current_state.md`、`next_step.md`
- 后续注意事项：`Grymforge / Grym` 的具体路径补强仍保留在战斗模块；下一份 ExecPlan 应优先承接已经出现明确耦合入口但尚未形成案例推进机制的模块。
## 2026-04-22 | 结束任务模块的首轮主线，并把下一份 ExecPlan 切到营地模块
- 为什么改：`quests_and_choices` 已完成首轮正文、跨模块耦合与最小必要回流；继续延长同一计划的收益开始下降，而营地模块已经具备清晰切入口。
- 改动影响范围：`.agent/execplan_party_and_camp.md`、`current_state.md`、`next_step.md`
- 后续注意事项：`party_and_camp` 后续必须围绕“反馈折返点”推进，避免滑向同伴人物志或恋爱系统总整理。

## 2026-04-22 | 先锁定营地模块边界，再进入来源筛选
- 为什么改：`party_and_camp` 当前最大的风险不是缺材料，而是边界膨胀；先把问题归属、最小关系图和案例准入标准写死，比直接补资料更能保障后续会话稳定接力。
- 改动影响范围：`.agent/execplan_party_and_camp.md`、`current_state.md`、`next_step.md`
- 后续注意事项：Milestone 2 只筛与“反馈折返点”直接相关的来源，不要把同伴人物介绍或泛恋爱讨论混进首批来源池。

## 2026-04-23 | 将当前唯一主任务临时切换为“仓库整改”
- 为什么改：模块 3 明显落后于局部案例模块，集合式来源又被直接上升为正文证据；若继续沿旧主线推进，会放大仓库的上位解释缺口与来源不稳问题。
- 改动影响范围：`.agent/execplan_repo_rectification.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：这是临时纠偏，不是永久替换项目主路线图；整改结束后仍应回到主路线图定义的模块顺序。

## 2026-04-23 | 先用官方高层来源补强模块 3，并把 BG3-OFF-001 从占位条目压实
- 为什么改：`00_core_thesis.md` 与 `01_macro_structure.md` 之前直接引用 `BG3-OFF-001`、`BG3-PLY-001` 这类集合式来源，导致总论点与宏观结构无法作为可信入口。
- 改动影响范围：`docs/03_analysis/00_core_thesis.md`、`docs/03_analysis/01_macro_structure.md`、`docs/00_project/source_index.md`、`docs/02_sources/source_note_bg3_off_001_about_page.md`
- 后续注意事项：后续若继续处理占位来源，应优先清理仍留在顶层正文与实现验证层中的占位引用，而不是再次扩写局部案例。

## 2026-04-23 | 用具体案例来源替换实现验证层中的集合式玩家占位来源
- 为什么改：`05_implementation_validation.md` 仍直接列出 `BG3-PLY-001`，会让实现验证层继续把集合式玩家来源当成实际证据入口，削弱整改 `M2` 的目标。
- 改动影响范围：`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/source_index.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：集合式条目仍可保留在索引中作为来源池入口，但在被拆实前，不应再出现在顶层正文或实现验证层的 Source IDs 中。

## 2026-04-23 | 统一 Grymforge case 的主归属口径，并同步导航层描述
- 为什么改：仓库已经明确把 Grymforge / Grym 作为 `04_combat_and_environment` 的主案例，仅向 `02_quests_and_choices` 做最小必要回流；若来源工作文件与导航说明仍停留在旧口径，会让后续会话误判模块边界。
- 改动影响范围：`docs/02_sources/case_note_grymforge_environment_resolution.md`、`README.md`、`docs/00_project/repo_map.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：后续若新增案例工作文件，应在文件内明确主归属模块与次级回流模块，避免再次出现“案例先跑、归属后补”的问题。

## 2026-04-23 | 将整改成果沉入检查脚本，并恢复项目主线到 party_and_camp
- 为什么改：如果整改只停留在文档层，后续会话仍可能重新引入无效 Source ID、失效 Where used 或状态文件不同步的问题；同时整改完成后需要尽快回到主路线图，而不是让“整改”长期占用主线。
- 改动影响范围：`scripts/check_repo.py`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`.agent/execplan_repo_rectification.md`
- 后续注意事项：后续推进营地模块时，应继续依赖检查器约束来源与状态同步，避免再次出现“局部案例先跑、上位解释层滞后”的问题。

## 2026-04-23 | 重写 README 以修复 GitHub 上的中文乱码
- 为什么改：根目录 README 是新会话和 GitHub 审阅的总入口；若正文编码异常，会直接破坏仓库的可读性与上下文恢复能力。
- 改动影响范围：`README.md`
- 后续注意事项：后续若再重写仓库入口文件，需继续以 UTF-8 保存，并在推送前优先检查 GitHub 预览效果。

## 2026-04-23 | 营地模块首批来源优先用官方补丁 / 热修做事实锚点
- 为什么改：营地 / 长休反馈很容易滑向玩家印象或同伴剧情整理；先用补丁、热修和社区更新锁定“营地是反馈折返点”的事实锚点，能降低后续案例选择的漂移风险。
- 改动影响范围：`.agent/execplan_party_and_camp.md`、`docs/00_project/source_index.md`、`docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/05_implementation_validation.md`
- 后续注意事项：社区来源继续只作为案例线索使用；下一步进入 `Milestone 3` 时，应优先围绕已确认的官方锚点组织案例骨架，而不是先扩充更多来源池。

## 2026-04-23 | 营地模块首批案例采用“1 强案例 + 1 候补案例”结构

- 为什么改：当前来源强度不支持同时把多个营地案例都写成同等强度的正文论据；先锁定 `Dark Urge 营地 bard 事件` 为强案例、`Minthara 营地反应链` 为候补案例，更利于控制论证权重。
- 改动影响范围：`.agent/execplan_party_and_camp.md`、`docs/02_sources/case_note_dark_urge_bard_event.md`、`docs/02_sources/case_note_minthara_camp_reaction_chain.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：正文回写时不要把 `Minthara` 个案直接扩写成普遍规律，应优先把它当作营地反馈边界的暴露点。

## 2026-04-23 | 第三类营地反馈案例只做一次受控侦察，并据此收束正文策略

- 为什么改：营地模块在 `Milestone 4` 后出现了“直接扩写正文”与“继续补第三案例”之间的分叉；如果不先给第三案例设定准入标准，后续很容易重新滑回无上限补资料。
- 改动影响范围：`.agent/execplan_party_and_camp.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/source_index.md`、`docs/02_sources/source_note_bg3_off_009_hotfix_29_halsin_camp.md`、`docs/02_sources/case_note_halsin_rescue_camp_feedback.md`
- 后续注意事项：本轮已找到 `救出 Halsin 后的营地同伴对话恢复` 这一第三案例候选，但它不足以进入首轮正文；下一步应直接按现有“强案例 + 候补案例 + 系统型补丁锚点”结构扩写 `03_party_and_camp.md`。
## 2026-04-23 | 营地模块首轮正文采用“强案例 + 候补案例 + 系统型补丁锚点”结构

- 为什么改：当前证据强度不支持把营地模块直接写成同伴剧情总整理；先用 1 条较闭合的强案例、1 条边界暴露型候补案例和 1 组系统型补丁锚点，更能保持论证收束。
- 改动影响范围：`docs/03_analysis/03_party_and_camp.md`、`.agent/execplan_party_and_camp.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：若后续直接扩写正文，应优先补“第三类营地反馈案例”或继续控制 `Dark Urge` 与 `Minthara` 的论证权重，避免高辨识度特例吞掉模块解释力。

## 2026-04-23 | 完成营地模块的小范围证据补强后，停止继续做同类低收益迭代

- 为什么改：本轮已经用 `BG3-OFF-002` 补强了 `Dark Urge bard` 的官方 framing，并用 `BG3-OFF-010` 补出非 `Minthara` 的营地 reaction / 对话可达性平行锚点；继续围绕零散补丁 / 热修做同类侦察，收益开始明显下降。
- 改动影响范围：`docs/03_analysis/03_party_and_camp.md`、`docs/02_sources/source_note_bg3_off_002_patch_7.md`、`docs/02_sources/source_note_bg3_off_010_hotfix_3_camp_reactivity.md`、`.agent/execplan_party_and_camp.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：`party_and_camp` 后续只在出现更强官方来源时再做定点回补；`Halsin` 候选继续只留在 open questions，不升级为正文主案例。

## 2026-04-23 | 将项目总逻辑从“模块研究顺序”重排为“展示顺序 + 区域包执行顺序”双轨结构

- 为什么改：仓库原有研究底座已经足够稳，但项目级入口没有把“研究推进顺序”和“展示给人看的顺序”分开写清，导致局部模块推进时容易给人“为什么突然拆营地”的观感。
- 改动影响范围：`README.md`、`docs/00_project/overview.md`、`docs/00_project/repo_map.md`、`docs/00_project/master_roadmap.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/00_project/deconstruction_master_execution_plan.md`、`docs/00_project/deconstruction_granular_codex_plan.md`、`docs/00_project/source_index.md`、`docs/02_sources/benchmark_projects.md`、`docs/02_sources/bg3_official.md`
- 后续注意事项：后续执行必须按区域包 / Act 包推进，再把结论沉入分析模块；展示时必须按“宏观结构 → 局部行动 → 任务回流 → 营地折叠 → Act 收束 → 实现验证”的链条组织，不要再把营地作为独立平行模块突然推出。

## 2026-04-24 | 将外部交付中的总逻辑成果受控合并回主仓库

- 为什么改：`D:\download` 中已有一套更清晰的项目级总览、阶段计划和超细颗粒度执行脚本；直接吸收这些项目级成果，能在不重写既有研究正文的前提下，解决仓库入口、展示顺序和执行单元不一致的问题。
- 改动影响范围：`README.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/00_project/deconstruction_master_execution_plan.md`、`docs/00_project/deconstruction_granular_codex_plan.md`、`docs/00_project/master_roadmap.md`、`docs/00_project/repo_map.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`、`docs/02_sources/benchmark_projects.md`、`docs/02_sources/bg3_official.md`、`docs/02_sources/source_note_bmk_002_reverse_design_ff6.md`、`docs/02_sources/source_note_bmk_003_boss_keys.md`、`docs/02_sources/source_note_bg3_off_011_osiris_intro.md`、`docs/02_sources/source_note_bg3_off_012_journal_editor_overview.md`、`docs/02_sources/source_note_bg3_off_013_journal_structure_overview.md`、`docs/02_sources/source_note_bg3_off_014_add_quest_to_situation.md`
- 后续注意事项：继续以主仓库现有 `docs/03_analysis/*` 正文和案例积累为主，不要把区域包执行法误写成剧情目录；下一步直接执行 `Nautiloid 区域包`，不要回跳到营地模块做低收益补丁侦察。

## 2026-04-24 | 将 `Nautiloid` 固定为第一块模板区域包

- 为什么改：项目级文件虽然已经把执行单元改成“区域包 / Act 包”，但如果第一块区域包不真正跑通，仓库仍会停留在口号层。`Nautiloid` 体量最可控，也最能同时暴露多入口、早期战斗、队友收编、正式目标与状态清理。
- 改动影响范围：`.agent/execplan_nautiloid_region_pack.md`、`docs/02_sources/source_note_bg3_off_015_patch_6_nautiloid_tutorial.md`、`docs/02_sources/case_note_nautiloid_opening_state_and_multi_entry.md`、`docs/02_sources/source_note_bg3_off_002_patch_7.md`、`docs/03_analysis/00_core_thesis.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/04_combat_and_environment.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/source_index.md`
- 后续注意事项：`Nautiloid` 只证明“起点就有区域包逻辑”，不提前外推所有开场分歧都会长线回流；下一步应直接进入 `Act 1 地表主区`，继续按同样模板推进。

## 2026-04-24 | 将 `Act 1 地表主区` 首轮区域包收束为“route pack + 前史密度”口径

- 为什么改：`Act 1 地表主区` 最容易滑回景点导览或招募目录；现有官方来源已经足以证明它是 opening state 的续接层与第一块稳定问题网，但还不足以把完整早期路线矩阵写成事实表。
- 改动影响范围：`.agent/execplan_act1_surface_region_pack.md`、`docs/02_sources/case_note_act1_surface_route_pack.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/04_combat_and_environment.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/source_index.md`
- 后续注意事项：如果后续继续补 `Act 1 地表主区`，应优先补更聚焦的 `recruitment_and_discovery` 子 note 或更直接的官方地表来源，而不是回退成景点清单；当前区域包完成后，主线应切到 `Grove / Goblin 冲突`。

## 2026-04-24 | 将 `Grove / Goblin 冲突` 首轮区域包收束为“resolution matrix”口径

- 为什么改：这块最容易滑成派系立场总结、首领攻略或道德讨论；现有官方来源已经足以压实“处理方式 / 长休时序 / 营地折返”三种边界，但还不足以把全量首领顺序与结局写成事实表。
- 改动影响范围：`.agent/execplan_grove_goblin_region_pack.md`、`docs/02_sources/case_note_grove_goblin_resolution_matrix.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/source_index.md`
- 后续注意事项：如果后续继续补 `Grove / Goblin`，应优先补同级别的公开证据路径，而不是回退成派系剧情总表；当前区域包完成后，主线应切到 `Underdark`。

## 2026-04-24 | 将 `Underdark` 首轮区域包收束为“entry choice / stage reframing”口径

- 为什么改：这块最容易滑成地下景观导览、支线列表或单纯地图切换；现有官方来源已经足以压实 `Underdark` 是 `Act 1` 内部的差异化区域、符合多入口设计语言，并且直接承担通向 `Grymforge` 的公开 setup，但还不足以把完整地下入口矩阵与 objective 变体写成事实表。
- 改动影响范围：`.agent/execplan_underdark_region_pack.md`、`docs/02_sources/case_note_underdark_entry_choice_pack.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：如果后续继续补 `Underdark`，应优先补更细的入口 / 过渡与 objective 映射，而不是回退成地下全区导览；当前区域包完成后，主线应切到 `Grymforge`。

## 2026-04-24 | 将 `Grymforge` 首轮区域包收束为“encounter bundle / combat-agency compression”口径

- 为什么改：这块最容易滑成单个 `Grym` Boss 战摘要、熔炉机关列表或版本敏感的打法 / cheese 合集；现有公开来源已经足以压实 `Underdark -> Grymforge` 的下游 setup、区域级 `choices + complex combat encounters` 框架，以及玩家如何把遭遇读成环境重写问题，但还不足以把具体熔炉路径写成 objective / step 事实链。
- 改动影响范围：`.agent/execplan_grymforge_region_pack.md`、`docs/02_sources/case_note_grymforge_environment_resolution.md`、`docs/03_analysis/04_combat_and_environment.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：如果后续继续补 `Grymforge`，应优先补更直接点名环境路径边界的公开来源，而不是继续扩玩家打法帖；当前区域包完成后，主线应切到 `Mountain Pass / Creche`。

## 2026-04-24 | 将 `Mountain Pass / Creche` 首轮区域包收束为“gate + party tension”口径

- 为什么改：这块最容易滑成 `Lae'zel` 剧情专章、`gith` lore 摘要或单纯的冲突复述；现有公开来源已经足以压实对话门槛、局部敌意、即时伙伴反应与 `camp night` 后果读取四种边界，但还不足以把 `Act 2` 切换规则和完整 objective 映射写成事实表。
- 改动影响范围：`.agent/execplan_mountain_pass_creche_region_pack.md`、`docs/02_sources/source_note_bg3_off_016_patch_3_creche_tension.md`、`docs/02_sources/case_note_mountain_pass_creche_gate_and_party_tension.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：如果后续继续补 `Mountain Pass / Creche`，应优先补更直接讨论阶段切换、门槛警告或 `Journal / objective / step` 边界的官方来源，而不是回退成剧情摘要；当前区域包完成后，主线应切到 `Act 2 总框架`。

## 2026-04-24 | 将 `Act 2 总框架` 首轮框架包收束为“pressure + re-read frame”口径

- 为什么改：`Act 2` 最容易滑成影咒气氛摘要或中盘剧情转折提要；现有公开来源已经足以压实官方区域定位、`Act II` 的 flow / reaction 维护与至少一条明确的跨 Act 前史读回，但还不足以把影咒限制、收束点分工或完整 objective 映射写成事实表。
- 改动影响范围：`.agent/execplan_act2_total_framework.md`、`docs/02_sources/case_note_act2_pressure_and_reactivity_frame.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：如果后续继续补 `Act 2`，应优先进入 `Shadow-Cursed Lands` 与后续收束点子块，把压力框架压到具体区域组织器，而不是回退成氛围、lore 或泛化“中盘更黑更难”的描述。

## 2026-04-24 | 将 `Shadow-Cursed Lands` 首轮区域包收束为“pressure loop / concrete pressure organizer”口径

- 为什么改：这块最容易滑成影咒景观 / 生存气氛摘要；现有公开来源已经足以压实官方区域定位、`Act II` flow / reaction 维护与多入口设计语言，但还不足以把具体影咒机制、路线分工或完整 objective 映射写成事实表。
- 改动影响范围：`.agent/execplan_shadow_cursed_lands_region_pack.md`、`docs/02_sources/case_note_shadow_cursed_lands_pressure_loop.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/04_combat_and_environment.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：如果后续继续补 `Shadow-Cursed Lands`，应优先把它与 `Last Light / Moonrise / Gauntlet` 的收束分工压实，而不是回退成影咒 lore、环境百科或局部机制清单；当前区域包完成后，主线应切到 `Last Light / Moonrise / Gauntlet / 相关收束点`。

## 2026-04-24 | 将 `Last Light / Moonrise / Gauntlet` 首轮收束包收束为“convergence pack / midgame compression”口径

- 为什么改：这组节点最容易被重新拆成 `Last Light`、`Moonrise`、`Gauntlet` 三份平行地点笔记，导致 `Act 2` 尾段退化成地点目录或剧情高潮提要；现有公开来源已经足以压实 `Act II` 的 flow / reaction 维护、至少一条明确的 `Moonrise Towers` 前史读回链，以及公开的 Journal 结构语言，但还不足以把三者内部的完整分工与 objective 映射写成事实表。
- 改动影响范围：`.agent/execplan_last_light_moonrise_gauntlet_convergence.md`、`docs/02_sources/case_note_last_light_moonrise_gauntlet_convergence.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：如果后续继续补这组节点，应优先补更直接点名 `Last Light`、`Moonrise`、`Gauntlet` 分工的官方条目，而不是回退成地点百科；当前收束包完成后，主线应切到 `Act 3 总框架`。

## 2026-04-24 | 将 `Act 3 总框架` 首轮框架包收束为“density + resolution load”口径

- 为什么改：`Act 3` 最容易滑成城市地点列表、派系百科或终局剧情提要；现有公开来源已经足以压实官方城市节点定位、选择驱动的 ending feedback、开发者承认后期状态排列更密，以及公开的 Journal 结构语言，但还不足以把各城市子块与终局组织的完整 objective 映射写成事实表。
- 改动影响范围：`.agent/execplan_act3_total_framework.md`、`docs/02_sources/case_note_act3_density_and_resolution_load.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：如果后续继续补 `Act 3`，应优先进入 `Rivington`，把“高密度城市 + 高收束压力”继续压到外环入口过滤层，而不是回退成城市景点导览或终局事件摘要。

## 2026-04-24 | 将 `Rivington` 首轮区域包收束为“entry filter + outer-ring pressure”口径

- 为什么改：`Rivington` 最容易滑成进城前的缓冲段、零散支线前厅或城市外围导览；现有公开来源已经足以压实 `Act 3` 的城市节点定位、后期高密度状态读回、多入口设计语言与公开 Journal 结构边界，但还不足以把 `Rivington` 内部具体 quest / objective 分工写成事实表。
- 改动影响范围：`.agent/execplan_rivington_region_pack.md`、`docs/02_sources/case_note_rivington_entry_pressure.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：如果后续继续补 `Act 3`，应优先进入 `Wyrm's Crossing`，把 `Rivington` 已完成的第一层过滤继续压成桥梁 / 门槛 / 第二层重排结构，而不是回头把 `Rivington` 扩成城市外环百科或地点目录。

## 2026-04-24 | 将 `Wyrm's Crossing` 首轮区域包收束为“bridge + gate + second-layer reordering”口径

- 为什么改：`Wyrm's Crossing` 最容易滑成过桥路线、检查点清单或桥头地点导览；现有公开来源已经足以压实 `Act 3` 的城市节点定位、后期高密度状态读回、多入口设计语言与公开 Journal 结构边界，但还不足以把 `Wyrm's Crossing` 内部具体 quest / objective 分工写成事实表。
- 改动影响范围：`.agent/execplan_wyrms_crossing_region_pack.md`、`docs/02_sources/case_note_wyrms_crossing_bridge_and_gate_pack.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：如果后续继续补 `Act 3`，应优先进入 `Lower City`，把 `Wyrm's Crossing` 已完成的第二层门槛 / 重排继续压成更高密度的内城并行 / 结算区，而不是回头把它扩成桥头百科、检查点列表或过桥剧情摘要。

## 2026-04-24 | 将 `Lower City` 首轮区域包收束为“higher-density inner-city parallel / resolution”口径

- 为什么改：`Lower City` 最容易滑成内城景点导览、派系列表或全支线总表；现有公开来源已经足以压实 `Act 3` 的城市节点定位、选择驱动的 ending feedback、开发者承认后期状态排列更密，以及公开 Journal 结构边界，但还不足以把 `Lower City` 内部具体 quest / objective 分工写成事实表。
- 改动影响范围：`.agent/execplan_lower_city_region_pack.md`、`docs/02_sources/case_note_lower_city_faction_resolution_pack.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：如果后续继续补 `Act 3`，应优先进入 `终局组织与收束压力`，把 `Lower City` 已建立的高密度并行 / 结算负载继续压成组织级终局收束，而不是回头把 `Lower City` 扩成内城百科、派系总表或泛化终局剧情摘要。

## 2026-04-24 | 将 `终局组织与收束压力` 首轮子单元收束为“organization-level compression / ending-feedback pressure”口径

- 为什么改：这块最容易滑成 Boss 顺序表、终局剧情提要或结局百科；现有公开来源已经足以压实 `Act 3` 的 ending feedback、后期 flow / reaction 维护、多入口设计语言与公开 Journal 结构边界，但还不足以把终局组织内部的完整 objective / step 分工写成事实表。
- 改动影响范围：`.agent/execplan_endgame_organization_compression.md`、`docs/02_sources/case_note_endgame_organization_compression.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：阶段 4 / `Act 3` 首轮闭合后，主线应切到阶段 5 / `Quest Reactivity`；不要回头把 `Act 3` 扩成城市百科、终局剧情摘要或全任务总表。

## 2026-04-24 | 将阶段 5 / `Quest Reactivity` 的首个子单元收束为“cross-act readback spine”口径

- 为什么改：阶段 5 最容易滑成全任务表、区域包复述，或重新回到旧的抽象模块跳转；现有公开来源已经足以把 `Grove / Goblin` 的处理矩阵、`Act 2` 的收束点组与 `Act 3` 的过滤 / 门槛 / 并排承接 / 组织级压缩压成同一条跨阶段主干，但还不足以把整条链写成完整 objective 表。
- 改动影响范围：`.agent/execplan_quest_reactivity_cross_act_readback_spine.md`、`docs/02_sources/case_note_quest_reactivity_cross_act_readback_spine.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：阶段 5 下一子单元应继续补“入口 / 改道 / 门槛”前置链，服务当前 readback spine；不要回头扩 `Act 3` 城市子包，也不要把 `Quest Reactivity` 写成全任务百科。

## 2026-04-24 | 将阶段 5 / `Quest Reactivity` 的第二个子单元收束为“upstream entry / diversion / gate chain”口径

- 为什么改：如果只保留 `Grove / Goblin -> Act 2 -> Act 3` 的 readback spine，阶段 5 会显得从 `Act 1` 中段突然开始；但若反过来把 `Act 1` 重新摊成总表，又会退回旧的区域包复述。现有公开来源已经足以把 `Nautiloid -> Act 1 地表主区 -> Underdark -> Mountain Pass / Creche` 压成服务既有主干的上游前置链，但还不足以把这四段写成完整 objective 表。
- 改动影响范围：`.agent/execplan_quest_reactivity_upstream_entry_diversion_gate_chain.md`、`docs/02_sources/case_note_quest_reactivity_upstream_entry_diversion_gate_chain.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`
- 后续注意事项：阶段 5 下一子单元应优先补 `Mountain Pass / Creche -> Shadow-Cursed Lands -> Last Light / Moonrise / Gauntlet` 的交接边界，继续判断哪些已足以升级到 `objective / step`，哪些仍只能停留在 `gate / pressure / convergence bundle`；不要回头把 `Act 1` 扩成总表，也不要跳回无关模块。

## 2026-04-24 | 将阶段 5 / `Quest Reactivity` 的第三个子单元收束为“late Act 1 / early Act 2 transition boundary”口径

- 为什么改：如果只有“上游前置链 + 下游 readback spine”，阶段 5 在 `Mountain Pass / Creche -> Act 2` 这条最关键接缝上仍然是空的；但若直接把这段扩写成 `Act 2` 地点目录或章节总表，又会退回旧的区域包复述。现有公开来源已经足以把 `Mountain Pass / Creche -> Shadow-Cursed Lands -> Last Light / Moonrise / Gauntlet` 压成 `gate -> pressure filter -> convergence pack` 三段边界，但还不足以把整段写成完整 objective 表。
- 改动影响范围：`.agent/execplan_quest_reactivity_late_act1_early_act2_transition_boundary.md`、`docs/02_sources/case_note_quest_reactivity_late_act1_early_act2_transition_boundary.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：阶段 5 下一子单元应优先评估是否还能压出第二条不依赖 `Minthara -> Moonrise Towers` 的公开跨阶段链；若不能，要把证据上限明确压回实现验证层，而不是继续假装仓库已拥有全局 objective 表。

## 2026-04-24 | 将阶段 5 / `Quest Reactivity` 的第四个子单元收束为“second public chain ceiling”口径

- 为什么改：继续追求与 `Minthara -> Moonrise Towers` 对称的第二条公开跨 Act 主链，会逼仓库把 `Mountain Pass / Creche`、营地反应修复与 late-game ending feedback 这几类弱锚点误升成同级 spine；现有公开来源已经足以证明这些支撑束存在，但还不足以把它们写成第二条具名的 `upstream handling -> downstream node -> cross-Act reaction` 链。
- 改动影响范围：`.agent/execplan_quest_reactivity_second_public_chain_ceiling.md`、`docs/02_sources/case_note_quest_reactivity_second_public_chain_ceiling.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`
- 后续注意事项：阶段 5 后续应继续做“层级收口”，把既有判断分别压稳到 `objective / step` 邻近层、`gate / tension`、`camp fold`、`ending feedback / organization bundle`，不要再以“必须找出第二条对称主链”为前提推进。

## 2026-04-24 | 将阶段 5 / `Quest Reactivity` 的第五个子单元收束为“layer boundary lock”口径

- 为什么改：在已有“前置链 + 中盘接缝 + readback spine + second public chain ceiling”之后，仓库最容易再次失控成两种方向：要么把少数 objective-adjacent 局部锚点误扩成全局 objective 表，要么把 `camp fold` / late-game ending feedback 再次拉回“第二条对称主链”。现有公开来源已经足以把这些锚点重新分层，但还不足以支撑更大的跨阶段扩写。
- 改动影响范围：`.agent/execplan_quest_reactivity_layer_boundary_lock.md`、`docs/02_sources/case_note_quest_reactivity_layer_boundary_lock.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`
- 后续注意事项：阶段 5 下一子单元只允许处理 objective-adjacent 局部锚点，优先 `Grove / Goblin` 与 `Mountain Pass / Creche`；不要再扩 late-game bundle，也不要再让 `camp fold` 竞争第二条主链位置。

## 2026-04-24 | 将阶段 5 / `Quest Reactivity` 的第六个子单元收束为“objective-adjacent narrowing”口径

- 为什么改：仅有“层级锁定”还不够，它仍停留在“哪些区域包整体更接近 `objective / step`”的粗层级；但若继续扩链，又会再次把少数 patch / hotfix 锚点误写成 objective 总表。现有公开来源已经足以把 `Grove / Goblin` 与 `Mountain Pass / Creche` 各自再压到一层局部 fragment 边界，但还不足以支撑更大的 `Quest Reactivity` 扩写。
- 改动影响范围：`.agent/execplan_quest_reactivity_objective_adjacent_narrowing.md`、`docs/02_sources/case_note_quest_reactivity_objective_adjacent_narrowing.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：`Quest Reactivity` 在当前公开来源下应视为已收口；除非出现更强官方来源，否则不要继续扩 objective-adjacent 锚点，也不要再让 `camp fold` 或 late-game bundle 竞争主链位置。下一唯一主任务应切到阶段 5 / `Combat / Environment` 的跨阶段主干。

## 2026-04-25 | 将阶段 5 / `Combat / Environment` 的首个子单元收束为“early local agency -> regional pressure loop”口径

- 为什么改：如果继续只让 `Grymforge` 单独承担战斗 / 环境模块，阶段 5 就不会形成真正的横向主干；但如果反过来把所有区域包重新摊成 encounter / 机关 / cheese 列表，仓库又会退回攻略化写法。现有公开来源已经足以把 `Nautiloid -> Act 1 地表主区 -> Grymforge -> Shadow-Cursed Lands` 压成同一条环境 spine，但还不足以把 late `Act 2` / `Act 3` 强拉成第二条对称主干。
- 改动影响范围：`.agent/execplan_combat_environment_early_local_agency_to_pressure_loop.md`、`docs/02_sources/case_note_combat_environment_early_local_agency_to_pressure_loop.md`、`docs/03_analysis/04_combat_and_environment.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：阶段 5 下一子单元应优先处理 second spine ceiling / late-game boundary，判断 `Shadow-Cursed Lands` 之后的锚点能否进入第二条环境主干；若不能，就明确把它们降回 region-pack / supporting bundle 层，不要回头扩 `Act 3` 城市子包，也不要把它们摊成 encounter 列表。

## 2026-04-25 | 将阶段 5 / `Combat / Environment` 的第二个子单元收束为“second spine ceiling / late-game boundary”口径

- 为什么改：如果在首条 “early local agency -> regional pressure loop” 环境主干建立后继续硬追第二条对称 spine，仓库会把 late `Act 2` / `Act 3` 的收束、过滤、门槛、并行承接与 ending feedback bundle 误升成同级环境锚点；但如果因为证据不够就把这些区域包重新摊回 encounter / 机关 / cheese 列表，又会让阶段 5 退回攻略化写法。
- 改动影响范围：`.agent/execplan_combat_environment_second_spine_ceiling_late_game_boundary.md`、`docs/02_sources/case_note_combat_environment_second_spine_ceiling_late_game_boundary.md`、`docs/03_analysis/04_combat_and_environment.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`
- 后续注意事项：在没有更强、直接点名 late-game combat / environment agency 的官方来源前，不要重新打开第二条对称环境 spine；后续唯一主任务应切向剩余横向主干，而不是继续围绕 `Act 3` 已完成子包做重复扩写。

## 2026-04-25 | 将阶段 5 / `Companion / Camp / Long Rest` 的首个子单元收束为“cross-region camp fold / delayed feedback spine”口径

- 为什么改：如果继续让营地模块停在“强案例 + 候补案例 + 系统型补丁锚点”的并列结构，阶段 5 就还没有形成真正的横向主干；但如果反过来把 `Act 2` 收束点组、late-game `ending feedback` 与零散 camp fix 都误写成对称主链，仓库又会把弱锚点升格成新的 `objective` spine。
- 改动影响范围：`.agent/execplan_companion_camp_cross_region_fold_spine.md`、`docs/02_sources/case_note_companion_camp_cross_region_fold_spine.md`、`docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`
- 后续注意事项：下一子单元应优先测试 second public camp spine ceiling / late-game boundary；在没有更强官方来源前，不要把 `Karlach` 反思、非 `Minthara` camp fix 或 late-game `ending feedback` 强拉成第二条对称营地主干，也不要把营地模块重新摊成人物志或 camp scene 清单。

## 2026-04-25 | 将阶段 5 / `Companion / Camp / Long Rest` 的第二个子单元收束为“second public camp spine ceiling / late-game boundary”口径

- 为什么改：如果在首条 `camp fold / delayed feedback` 主干建立后继续硬追第二条对称营地主干，仓库会把 `BG3-OFF-007` 的跨 `Act` 反思、`BG3-OFF-010` 的非 `Minthara` camp fix 与 late-game `ending feedback` 误升成同级 spine；但如果不做 ceiling 动作，后续会话又会不断回到 camp scene 清单和人物志式扩写。
- 改动影响范围：`.agent/execplan_companion_camp_second_public_spine_ceiling_late_game_boundary.md`、`docs/02_sources/case_note_companion_camp_second_public_spine_ceiling_late_game_boundary.md`、`docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`、`docs/00_project/source_index.md`
- 后续注意事项：在没有更强、能稳定串起多区域 camp reread 的官方来源前，不要重新打开第二条公开营地主干；阶段 5 的下一唯一主任务应切到 `Implementation Validation` 的统一收束子单元，而不是继续补 camp scene、同伴人物条目或 late-game 营地摘录。

## 2026-04-25 | 将阶段 5 的完成定义统一收束为“stage-5 exit matrix”，并把下一唯一主任务切到阶段 6

- 为什么改：三条横向主干都已经各自完成了“首条 spine + ceiling / supporting-bundle / handoff 边界”，如果继续按单条主干推进，仓库只会反复重开第二条对称链或回跳已完成区域包；真正缺的是把这些结论统一压成同一种阶段出口语法。
- 改动影响范围：`.agent/execplan_implementation_validation_stage5_exit_matrix.md`、`docs/02_sources/case_note_implementation_validation_stage5_exit_matrix.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/03_analysis/02_quests_and_choices.md`、`docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/04_combat_and_environment.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：在没有更强官方来源前，不再重新打开第二条对称 `Quest` / `Combat` / `Camp` spine；后续唯一主任务应进入阶段 6 / 展示收束，把这份 unified exit matrix 转译成对外展示入口。

## 2026-04-25 | 将阶段 6 的首个子单元固定为“display entry + reading order lock”

- 为什么改：阶段 5 虽然已经闭合，但仓库入口层仍容易看起来像三条横向主干并列收口；如果不先把 unified exit matrix 翻译成同一条阅读链，后续会话仍可能把 `Quest`、`Combat`、`Camp` 当成三份并列未完工工程继续扩写。
- 改动影响范围：`.agent/execplan_stage6_display_entry_and_reading_order.md`、`README.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/00_project/repo_map.md`、`docs/03_analysis/00_core_thesis.md`、`docs/03_analysis/01_macro_structure.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/source_index.md`
- 后续注意事项：当前展示入口顺序已锁定为“总命题 -> 宏观结构 -> 局部行动 -> 任务回流 -> 营地折叠 -> 实现验证”；下一步应继续压模块职责 / 展示形态 / 发布导览矩阵，不要借展示之名回跳阶段 5。

## 2026-04-25 | 将阶段 6 的第二个子单元固定为“module guide + release matrix”

- 为什么改：入口顺序虽然已经锁定，但仓库仍停留在“知道先读谁、不知道每个模块在发布链里负责什么”的状态；如果不把展示职责与推荐形态写死，后续会话仍可能把 `Quest`、`Combat`、`Camp` 当成并列工程继续扩写。
- 改动影响范围：`.agent/execplan_stage6_module_guide_and_release_matrix.md`、`docs/01_methodology/presentation_forms.md`、`docs/00_project/repo_map.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/03_analysis/00_core_thesis.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：当前 6 模块链已经拥有稳定的职责矩阵；下一步应继续把它压成实际发布导览稿 / section skeleton，而不是继续定义展示原则，也不要借此回跳阶段 5。

## 2026-04-25 | 将阶段 6 的第三个子单元固定为“release walkthrough / section skeleton”

- 为什么改：模块职责矩阵虽然已经锁定，但仓库仍缺一份能直接回答“导览稿第一段到最后一段分别讲什么、依赖哪几份正文、默认交给下一段什么”的实际骨架；如果这一步不做，后续会话仍会重复讨论展示原则，或者借“补展示”之名回跳阶段 5。
- 改动影响范围：`.agent/execplan_stage6_release_walkthrough_section_skeleton.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/01_methodology/presentation_forms.md`、`docs/00_project/repo_map.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`
- 后续注意事项：当前仓库已经拥有稳定的发布导览稿 / section skeleton；下一步不应再重写“先读谁”或“谁负责什么”，而应继续压“首轮发布包最低配置 / excerpt queue / asset queue”，同时保持阶段 5 的三条横向主干继续收口，不得回跳。
## 2026-04-25 | 将阶段 6 的第五个子单元固定为“entry page + opening section first actual release units”

- 为什么改：仅有“最低发布配置 / excerpt queue / asset queue”还不足以证明阶段 6 已进入真正的发布物生产；如果不先把入口页与第一段落成第一批实际 `excerpt card / asset spec / traceback card`，仓库仍会停在“规则完备、实物缺席”的半成品状态。
- 改动影响范围：`.agent/execplan_stage6_first_actual_release_units_entry_and_first_section.md`、`docs/00_project/stage6_entry_first_section_release_units.md`、`docs/01_methodology/presentation_forms.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/00_project/repo_map.md`、`docs/03_analysis/00_core_thesis.md`、`docs/03_analysis/01_macro_structure.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：下一步应直接切到“第二段：局部行动到状态回流”的首批实际发布单元；不要回头重写入口页 / 第一段的 queue，也不要借“继续补发布”之名回跳阶段 5。

## 2026-04-25 | 将阶段 6 的续轮入口固定为“review sheet + 最新 addendum”，而不是旧基准 ExecPlan 单独承担当前执行口径

- 为什么改：第三轮之后，`next_step.md` 已开始把 addendum 纳入建议阅读，但 `deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md` 与 `repo_map.md` 仍把旧的 `.agent/execplan_stage6_release_package_assembly_review.md` 单独写成当前固定执行计划。这样不会触发单段 actual units 回写，却会让下一轮入口继续落回第九子单元的 origin / baseline 时点，削弱“续轮只做 assembly / review 复核”的当前主线。
- 改动影响范围：`.agent/execplan_stage6_release_package_assembly_review_round4.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/00_project/deconstruction_granular_codex_plan.md`、`docs/00_project/repo_map.md`、`docs/00_project/stage6_release_package_assembly_review_sheet.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`、`docs/00_project/decision_log.md`
- 后续注意事项：后续阶段 6 继续推进时，应默认读取 `stage6_release_package_assembly_review_sheet.md` 与最新 addendum；原 `.agent/execplan_stage6_release_package_assembly_review.md` 只保留第九子单元的基准说明。只要没有新的 `ASSEMBLY-TRIGGER-001` 命中，就不回写单段 actual units。

## 2026-04-25 | 将阶段 6 的第八个子单元固定为“final section first actual release units”，并把首轮发布包视为已闭合

- 为什么改：第三段虽然已经有第一批实际发布单元，但收尾段仍停留在 queue 层；如果不把“证据分级”真正落成一组实际发布单元，阶段 6 会继续卡在“前四段有实物、最后一段仍是说明文字”的半成品状态。
- 改动影响范围：`.agent/execplan_stage6_final_section_actual_release_units.md`、`docs/00_project/stage6_final_section_release_units.md`、`docs/01_methodology/presentation_forms.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/00_project/repo_map.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：收尾段实际单元必须坚持“证据分级矩阵 + 回链 trace card”口径，不能把 `BG3-OFF-011` 到 `BG3-OFF-014` 越级写成 shipped content 实锤，也不能把开放问题抹平；当前五段 actual units 已在现有计划下闭合，下一步若继续推进，应先做总装配 / 审阅层，而不是回头重写 queue 或回跳阶段 5。
## 2026-04-25 | 将阶段 6 的第九个子单元固定为“first release package assembly / review sheet”

- 为什么改：五段 actual units 虽然已经闭合，但仓库仍缺一层统一的 assembly / review，无法稳定回答“这五段如何装成同一条发布链、先审什么、什么情况下才值得回写单段文件”。如果没有这一步，后续会话很容易借审阅之名回头重写 queue、误升 supporting bundle，或把 modding / Journal 文档越级写成 shipped content 实锤。
- 改动影响范围：`.agent/execplan_stage6_release_package_assembly_review.md`、`docs/00_project/stage6_release_package_assembly_review_sheet.md`、`docs/01_methodology/presentation_forms.md`、`docs/00_project/deconstruction_display_overview.md`、`docs/00_project/deconstruction_master_execution_plan.md`、`docs/00_project/deconstruction_granular_codex_plan.md`、`docs/00_project/repo_map.md`、`docs/03_analysis/05_implementation_validation.md`、`docs/00_project/current_state.md`、`docs/00_project/next_step.md`
- 后续注意事项：下一步应执行这份 review sheet 的首轮一致性审阅，只在命中 writeback trigger 时回写对应单段承载文件；不要把 assembly / review 层继续膨胀成第二份导览稿，也不要借它回跳阶段 5。
