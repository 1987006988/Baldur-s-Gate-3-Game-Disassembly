# Current State

## 当前阶段

仓库初始化完成，项目级主路线图与第二份 ExecPlan 已建立；`quests_and_choices` 首轮目标已基本封口，`party_and_camp` 的 Milestone 1 也已完成，当前进入首批来源筛选阶段。

## 已完成模块

- 仓库结构与协作规则
- 三层拆解方法与证据规则
- 展示形式方法文件 `presentation_forms.md`
- 来源索引骨架与初始来源分组
- 核心分析模块初始骨架
- 轻量检查脚本
- 项目级主路线图 `master_roadmap.md`
- 首份 ExecPlan `.agent/execplan_quests_and_choices.md`
- 首批 5 条任务与选择候选来源筛出，其中 3 条已完成来源笔记
- 已确认 2 个首批案例，并写出最小证据链骨架准备文件
- 已补入 `BG3-OFF-005` 并形成正文回写前准备清单
- `docs/03_analysis/02_quests_and_choices.md` 已完成首轮基于案例的正文回写
- `docs/03_analysis/03_party_and_camp.md` 与 `docs/03_analysis/05_implementation_validation.md` 已完成与任务模块的最小同步
- 已锁定 `Grymforge / Grym 环境解法路径` 作为战斗 / 环境向补强方向
- 已补入 `BG3-OFF-006`，确认 Grymforge 兼具任务、选择与复杂战斗遭遇的高层官方框架
- `docs/03_analysis/04_combat_and_environment.md` 已完成一轮基于 Grymforge / Grym 的案例回写
- 已将 Grymforge / Grym 的最小必要高层判断回流到 `docs/03_analysis/02_quests_and_choices.md`，明确“战斗 / 环境也可构成选择系统”
- 已创建第二份 ExecPlan `.agent/execplan_party_and_camp.md`，正式把“营地 / 长休是任务反馈折返点”提升为下一阶段主线

## 进行中模块

- 模块 2：来源体系与证据管线，尚未从索引骨架进入稳定蒸馏
- 模块 5：同伴、营地与长休循环，已完成边界锁定，等待首批来源与案例入口筛选
- 模块 6：战斗、构筑与环境战术，已完成首轮 Grymforge / Grym 深挖，后续可继续补强具体路径证据

## 阻塞点

- 暂无硬阻塞；当前风险主要是 `party_and_camp` 很容易滑向同伴剧情整理，因此后续执行必须持续坚持“反馈折返点”边界。
- Grymforge / Grym 虽已完成高层回流，但具体路径证据仍不足以支撑更强版本的任务模块论证。

## 最近一次重要变更

- 2026-04-22：创建 `.agent/execplan_party_and_camp.md`，正式把 `03_party_and_camp` 设为下一阶段主线模块。
- 2026-04-22：完成 `.agent/execplan_party_and_camp.md` 的 Milestone 1，明确营地模块优先研究“反馈折返点”，并写清问题归属与案例准入标准。
- 2026-04-22：完成 Grymforge / Grym 的最小必要回流，把“战斗 / 环境也是一种选择系统”补入 `02_quests_and_choices.md`，当前首份 ExecPlan 已接近首轮出口。
- 2026-04-22：完成仓库初始化，确定三层拆解方法、状态文件机制、来源索引机制和分析骨架。
- 2026-04-22：新增 `docs/00_project/master_roadmap.md`，明确 7 个项目模块、推荐顺序、阶段出口条件和跑偏判定规则。
- 2026-04-22：新增 `docs/01_methodology/presentation_forms.md`，明确研究文档是 source of truth，展示层只能从研究层压缩转述。
- 2026-04-22：新增 `.agent/execplan_quests_and_choices.md`，为“任务与选择回流”模块建立第一份可执行计划。
- 2026-04-22：完成首批 5 条来源筛选，补全 `source_index.md`，并为 3 条关键官方 / 开发者来源写出来源笔记。
- 2026-04-22：确认“Minthara 击倒路径”与“Dark Urge 营地 bard 事件”为首批两大案例，并写入案例骨架准备文件。
- 2026-04-22：补入 `BG3-OFF-005` 并完成 `.agent/quests_and_choices_writeback_prep.md`，明确主辅案例关系与正文回写边界。
- 2026-04-22：完成 `docs/03_analysis/02_quests_and_choices.md` 首轮正文回写，明确主案例、辅案例、事实边界与待验证问题。
- 2026-04-22：完成 `03_party_and_camp` 与 `05_implementation_validation` 的最小同步，使营地折返反馈与补丁验证入口不再只停留在任务模块内部。
- 2026-04-22：锁定 `Grymforge / Grym 环境解法路径` 作为下一条“战斗 / 环境绕解”补强方向，并写入来源索引与案例准备文件。
- 2026-04-22：补入 `BG3-OFF-006`，并把 Grymforge / Grym 的当前建议落点改为“先深挖 `04_combat_and_environment`，再反向支撑任务模块”。
- 2026-04-22：完成 `04_combat_and_environment` 的首轮 Grymforge / Grym 深挖，明确战斗模块中可成立的高层判断与仍需保留的待验证问题。

## 接下来 1~3 个最优先动作

1. 按 `.agent/execplan_party_and_camp.md` 执行 Milestone 2，筛出首批 3 到 5 条与营地 / 长休反馈相关的来源，并补齐索引状态。
2. 基于这些来源，确定 1 条强案例方向和 1 条候补案例方向，为 Milestone 3 做准备。
3. 继续为 Grymforge / Grym 补更具体的执行路径来源，但作为战斗模块补强，而不是当前主线。
