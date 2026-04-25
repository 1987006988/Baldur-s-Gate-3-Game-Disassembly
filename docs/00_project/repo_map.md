# Repo Map

## 新会话从哪里开始

1. 先读 `README.md`，理解仓库目标、边界、双轨总逻辑与基本工作流。
2. 再读 `docs/00_project/deconstruction_display_overview.md`，先解决“项目到底按什么逻辑拆、为什么不是剧情复述”。
3. 再读 `docs/00_project/deconstruction_master_execution_plan.md`，理解阶段划分、依赖关系与完成标准。
4. 再读 `docs/00_project/deconstruction_granular_codex_plan.md`，确认每个区域包 / 跨阶段系统的实际执行脚本。
5. 再读 `docs/00_project/current_state.md`，确认当前阶段与最近变更。
6. 再读 `docs/00_project/next_step.md`，获取当前默认状态与是否真的需要重开维护 round。
7. 再读 `docs/00_project/source_index.md`，确认来源状态与可追溯入口。
8. 然后进入本轮相关模块、来源笔记或 ExecPlan。

## 关键文件作用

- `docs/00_project/overview.md`：项目总命题、范围与方法价值。
- `docs/00_project/deconstruction_display_overview.md`：面向读者 / 观众解释“这个项目到底怎么拆、为什么现在拆这一块”。
- `docs/00_project/deconstruction_master_execution_plan.md`：阶段划分、输入输出、依赖与暂停条件。
- `docs/00_project/deconstruction_granular_codex_plan.md`：操作级执行脚本，给 Codex 直接用。
- `docs/00_project/master_roadmap.md`：项目级主路线摘要，负责保持总线稳定。
- `docs/00_project/current_state.md`：单页状态看板。
- `docs/00_project/decision_log.md`：追加式决策历史。
- `docs/00_project/next_step.md`：本轮执行入口。
- `docs/00_project/source_index.md`：来源总索引与 Source ID 主表。

## 长期记忆核心

- `README.md`
- `docs/00_project/deconstruction_display_overview.md`
- `docs/00_project/deconstruction_master_execution_plan.md`
- `docs/00_project/deconstruction_granular_codex_plan.md`
- `docs/00_project/current_state.md`
- `docs/00_project/next_step.md`
- `docs/00_project/decision_log.md`
- `docs/00_project/source_index.md`

这些文件共同承担长期记忆；不要把关键上下文留在聊天记录里。

## 只想按当前展示入口阅读

如果目标不是推进执行，而是先看懂仓库当前最稳的对外结构，按这个顺序读：

1. `README.md`
2. `docs/00_project/deconstruction_display_overview.md`
3. `docs/03_analysis/00_core_thesis.md`
4. `docs/03_analysis/01_macro_structure.md`
5. `docs/03_analysis/04_combat_and_environment.md`
6. `docs/03_analysis/02_quests_and_choices.md`
7. `docs/03_analysis/03_party_and_camp.md`
8. `docs/03_analysis/05_implementation_validation.md`

`Act 收束与终局压力` 当前不作为单独入口文件，而是通过 `01_macro_structure.md`、`02_quests_and_choices.md` 与 `03_party_and_camp.md` 的联读进入。

## 阶段 6 当前模块导览

- `docs/03_analysis/00_core_thesis.md`：开场模块，先回答整条反应性链在解释什么。
- `docs/03_analysis/01_macro_structure.md`：导航模块，先把 Act / 区域 / 压力梯与阅读骨架排出来。
- `docs/03_analysis/04_combat_and_environment.md`：第一组证据模块，先让读者理解“我能这样试”的局部 agency。
- `docs/03_analysis/02_quests_and_choices.md`：第二组证据模块，把前面的尝试写回状态与后续读回。
- `docs/03_analysis/03_party_and_camp.md`：第三组证据模块，把分散状态折叠成营地 / 长休反馈。
- `docs/03_analysis/05_implementation_validation.md`：收尾模块，给整条链分级并保留证据边界。

## 阶段 6 当前发布导览

如果目标不是继续研究，而是把仓库压成一条对外导览，按这个顺序组织最稳：

1. `README.md` 与 `docs/00_project/deconstruction_display_overview.md`
   先说明项目边界、总逻辑与为什么当前按这条链读。
2. `docs/03_analysis/00_core_thesis.md` 与 `docs/03_analysis/01_macro_structure.md`
   先锁命题，再给导航骨架。
3. `docs/03_analysis/04_combat_and_environment.md` 与 `docs/03_analysis/02_quests_and_choices.md`
   先证明局部能动性，再解释状态如何被记录与读回。
4. `docs/03_analysis/03_party_and_camp.md`
   把前面的状态折成延迟反馈。
5. `docs/03_analysis/05_implementation_validation.md`
   最后收口证据等级，不倒置成开场导论。

## 阶段 6 当前发布骨架在哪里

- `docs/00_project/deconstruction_display_overview.md`
  负责解释为什么要这样排，以及当前 5 段导览稿各自讲什么、依赖哪几份正文、默认交给下一段什么。
- `docs/01_methodology/presentation_forms.md`
  负责把这 5 段继续压成可执行的 `section skeleton` 与“首轮发布最低配置”。
- `.agent/execplan_stage6_release_walkthrough_section_skeleton.md`
  负责记录本轮为什么做这一步、完成标准是什么、下一步该继续补哪一层发布组织。

如果下一次会话要继续推进阶段 6，不应再重写“先读谁”；应直接在这三处基础上继续补“每一段最低需要哪些摘录 / 图 / 卡片 / 回溯路径”。

## 阶段 6 当前最低发布包在哪里

- `.agent/execplan_stage6_first_release_package_excerpt_asset_queue.md`
  负责记录第四个子单元为什么存在、完成标准是什么，以及为什么这一步不能回跳阶段 5。
- `docs/01_methodology/presentation_forms.md`
  现在是最低发布包的单一真源：每一段需要哪些 excerpt、asset、card 与 traceback，都以这里为准。
- `docs/03_analysis/05_implementation_validation.md`
  现在补有 release-facing evidence queue，用来回答“这段可以安全摘录到哪一层、哪些内容不能越级发布”。

如果下一次会话继续推进阶段 6，不应再补新的展示原则；应直接把这里定义好的最低发布包，落成首批实际 excerpt card / asset spec / traceback card，优先入口页与第一段。

## 阶段 6 当前首批实际发布单元在哪里

- `.agent/execplan_stage6_first_actual_release_units_entry_and_first_section.md`
  负责记录第五个子单元为什么存在、完成标准是什么，以及为什么这一步仍不能回跳阶段 5。
- `docs/00_project/stage6_entry_first_section_release_units.md`
  现在是入口页与第一段首批实际发布单元的承载文件：已落成的 `excerpt card`、`asset spec` 与 `traceback card` 都以这里为准。
- `docs/03_analysis/00_core_thesis.md`
  负责提供第一段命题侧的 release anchor。
- `docs/03_analysis/01_macro_structure.md`
  负责提供第一段导航侧的 release anchor。
- `docs/03_analysis/05_implementation_validation.md`
  负责锁定这两组实际单元的证据边界与不可越级摘录范围。

如果下一次会话继续推进阶段 6，不应回头重写入口页与第一段的 queue；应直接切到“第二段：局部行动到状态回流”的首批实际发布单元。

## 阶段 6 当前第二段实际发布单元在哪里

- `.agent/execplan_stage6_second_section_actual_release_units.md`
  负责记录第六个子单元为什么存在、完成标准是什么，以及为什么这一步不能伪造单一案例因果链。
- `docs/00_project/stage6_second_section_release_units.md`
  现在是第二段首批实际发布单元的承载文件：已落成的 `excerpt card`、`asset spec` 与 `traceback card` 都以这里为准。
- `docs/03_analysis/04_combat_and_environment.md`
  负责提供第二段左侧“局部 agency”锚点。
- `docs/03_analysis/02_quests_and_choices.md`
  负责提供第二段右侧“状态读回”锚点。
- `docs/03_analysis/05_implementation_validation.md`
  负责锁定这组双联单元的证据边界与不可越级摘录范围。

如果下一次会话继续推进阶段 6，不应回头重写第二段的 queue；应直接切到“第三段：延迟反馈折叠”的首批实际发布单元。

## 阶段 6 当前第三段实际发布单元在哪里

- `.agent/execplan_stage6_third_section_actual_release_units.md`
  负责记录第七个子单元为什么存在、完成标准是什么，以及为什么这一步不能把营地写回人物附录或第二条对称营地主干。
- `docs/00_project/stage6_third_section_release_units.md`
  现在是第三段首批实际发布单元的承载文件：已落成的 `excerpt card`、`asset spec` 与 `traceback card` 都以这里为准。
- `docs/03_analysis/03_party_and_camp.md`
  负责提供第三段的 `camp fold / delayed feedback` 正文锚点。
- `docs/03_analysis/05_implementation_validation.md`
  负责锁定这组折返层单元的证据边界与不可越级摘录范围。

如果下一次会话继续推进阶段 6，不应回头重写第三段的 queue；应直接切到“收尾段：证据分级”的首批实际发布单元。

## 阶段 6 当前收尾段实际发布单元在哪里

- `.agent/execplan_stage6_final_section_actual_release_units.md`
  负责记录第八个子单元为什么存在、完成标准是什么，以及为什么这一步不能把验证层误写成 shipped content 的实现总表。
- `docs/00_project/stage6_final_section_release_units.md`
  现在是收尾段首批实际发布单元的承载文件：已落成的 `excerpt card`、`asset spec` 与 `traceback card` 都以这里为准。
- `docs/03_analysis/05_implementation_validation.md`
  负责提供收尾段的 `facts / inferences / open questions` 正文锚点，并锁定前四段 actual units 的 evidence lock。
- `docs/00_project/stage6_entry_first_section_release_units.md`、`docs/00_project/stage6_second_section_release_units.md`、`docs/00_project/stage6_third_section_release_units.md`
  负责提供收尾段必须反向回链的前四段实际单元。

如果下一次会话继续推进阶段 6，不应回头重写任一段 queue；当前五段首批实际发布单元已经闭合，如需继续推进，应先做首轮发布包总装配 / 审阅清单。

## 阶段 6 当前总装配 / 审阅层在哪里

- `.agent/execplan_stage6_release_package_assembly_review.md`
  负责记录第九个子单元为什么存在、完成标准是什么，以及为什么这一步不能借审阅之名回跳阶段 5；它现在保留为总装配层的基准说明，而不是当前主动主线。
- `.agent/execplan_stage6_release_package_assembly_review_round1.md` 到 `.agent/execplan_stage6_release_package_assembly_review_round31.md`
  负责保留历史维护记录；它们现在属于维护记录 / 归档链，不再承担当前默认推进主干。
- `.agent/execplan_stage6_release_package_assembly_review_round32.md`
  负责记录截至 2026-04-26 的最近一次维护确认；它的定位是“最新维护记录”，不是“当前默认下一轮主任务”。
- `docs/00_project/stage6_release_package_assembly_review_sheet.md`
  现在是阶段 6 总装配 / 审阅层的承载文件：五段 actual units 的 `assembly map`、`review checklist`、`writeback trigger` 与维护态规则都以这里为准。
- `docs/01_methodology/stage6_freeze_maintenance_playbook.md`
  现在是阶段 6 冻结维护态的操作清单：默认阅读顺序、四步 maintenance pass、允许写回范围与禁止动作都以这里为准。
- `docs/03_analysis/05_implementation_validation.md`
  负责给 assembly / review 层提供 release anchor 与 evidence lock，判断哪些冲突真的值得回写，哪些应保持当前边界。

如果下一次会话涉及阶段 6，不应默认新增 `round33`，也不应回头重写 queue。当前三十二轮审阅里，除首轮的 `FINAL-ASSET-001` 独立 `入口页` 行问题与第十轮补回 `BMK-002 / BMK-003` benchmark traceback 外，未再打开新的 actual-unit 级硬阻塞；因此阶段 6 现已进入冻结后的条件触发维护态。正确默认动作是先按 `docs/01_methodology/stage6_freeze_maintenance_playbook.md` 做 trigger 判定与 maintenance pass；只有出现五段 actual units 正文改动、handoff 顺序变化、evidence lock / benchmark traceback 回退、assembly map 改动，或项目负责人明确要求复核发布链时，才重开 `review sheet + round32` 这组维护入口。

## 分析正文

- `docs/03_analysis/00_core_thesis.md`：总论点与当前最强解释版本。
- `docs/03_analysis/01_macro_structure.md`：Act / 区域 / 入口 / 推进结构。
- `docs/03_analysis/02_quests_and_choices.md`：任务、分支、回流与反馈。
- `docs/03_analysis/03_party_and_camp.md`：同伴、营地、长休与反馈折返点。
- `docs/03_analysis/04_combat_and_environment.md`：战斗、构筑、环境战术与多解法空间。
- `docs/03_analysis/05_implementation_validation.md`：公开可验证证据链与实现层判断。

## 来源层

- `docs/02_sources/*.md` 既包括来源类型导航页，也包括来源笔记与案例工作文件。
- 来源导航页用于说明“该类来源怎么整理”。
- 来源笔记用于把具体 Source ID 压实成事实、推断、限制与可用位置。
- 案例工作文件用于在回写正文前保存最小证据链、归属判断与未决问题。
- 区域包执行时，应优先在来源层形成“官方锚点 + 案例线索 + 实现验证入口”的三件套，再回写正文。

## 模板和工具

- `templates/source_note.md`：单个来源读书卡模板。
- `templates/case_note.md`：单个案例拆解模板。
- `scripts/check_repo.py`：结构与内容完整性检查。
- `Makefile`：统一命令入口。
