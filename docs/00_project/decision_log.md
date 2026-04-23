# Decision Log

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
