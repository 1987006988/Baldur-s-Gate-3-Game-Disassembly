# Deconstruction Master Execution Plan

## 1. 文件职责

本文件负责把整个项目切成可执行阶段，明确：

- 每个阶段的目标是什么
- 这个阶段吃什么输入、产出什么输出
- 依赖关系是什么
- 完成定义是什么
- 对应哪些仓库文件
- 什么算跑偏
- 什么情况下必须暂停并重审计划

本文件不替代操作脚本。真正要落到“下一步先做什么、先写哪个 case note、先回写哪个模块”，请配合 `docs/00_project/deconstruction_granular_codex_plan.md` 使用。

## 2. 总原则

### 原则 A：研究顺序 ≠ 展示顺序

- 研究顺序按区域包 / Act 包推进，用来收证据与压边界。
- 展示顺序按玩家体验链条推进，用来解释 BG3 为什么强。

### 原则 B：区域包是执行单元，分析模块是沉淀容器

执行时不要在抽象模块之间来回跳。先做区域包，再把区域包里的稳定结论沉到：

- `01_macro_structure.md`
- `02_quests_and_choices.md`
- `03_party_and_camp.md`
- `04_combat_and_environment.md`
- `05_implementation_validation.md`

### 原则 C：实现验证层是横向校验层

官方补丁 / 热修、开发者访谈、Journal / Osiris / Modding 文档，不直接替代玩家体验分析；它们的作用是把结论升级、降级或改写边界。

## 3. 总阶段划分

- 阶段 0：总逻辑重审与导航重排
- 阶段 1：执行底座冻结
- 阶段 2：Act 1 区域包
- 阶段 3：Act 2 区域包
- 阶段 4：Act 3 区域包
- 阶段 5：横向综合与实现验证升级
- 阶段 6：展示收束与发布导览

---

## 阶段 0：总逻辑重审与导航重排

### 目标

先解决“这个项目到底按什么逻辑拆”“为什么现在做这一块”“为什么不会再突然拆营地”。

### 输入

- 现有仓库结构与分析模块
- `master_roadmap.md`
- `current_state.md`
- `next_step.md`
- `repo_map.md`

### 输出

- `deconstruction_display_overview.md`
- `deconstruction_master_execution_plan.md`
- `deconstruction_granular_codex_plan.md`
- 已同步的 `README.md`、`master_roadmap.md`、`repo_map.md`、`current_state.md`、`next_step.md`

### 依赖关系

无。它是后续所有阶段的前提。

### 完成定义

- 仓库里已经单独存在“展示逻辑说明”文件。
- 仓库里已经单独存在“阶段计划”与“操作脚本”。
- 当前状态文件能直接回答“为什么现在是这一块”。

### 对应文件

- `README.md`
- `docs/00_project/deconstruction_display_overview.md`
- `docs/00_project/deconstruction_master_execution_plan.md`
- `docs/00_project/deconstruction_granular_codex_plan.md`
- `docs/00_project/master_roadmap.md`
- `docs/00_project/repo_map.md`
- `docs/00_project/current_state.md`
- `docs/00_project/next_step.md`

### 什么算跑偏

- 只是额外多写了一份路线图，但没有解决“为什么现在拆这个”。
- 继续把研究顺序当展示顺序用。

### 必须暂停并重审的条件

- 新文件与旧路线图互相冲突。
- `current_state.md` 和 `next_step.md` 仍然不能解释当前主任务。

---

## 阶段 1：执行底座冻结

### 目标

把真正影响后续判断的外部底座补齐：

- Reverse Design / Boss Keys 等 benchmark 方法
- BG3 官方产品定位与开发者表述
- BG3 官方补丁 / 热修 / Community Update
- BG3 官方 Journal / Osiris / Modding 文档

### 输入

- 阶段 0 的新导航与计划文件
- 当前 `source_index.md`
- 已有官方来源与案例文件

### 输出

- 可复用的 benchmark source notes
- 可复用的 Journal / Osiris source notes
- 更新后的 `source_index.md`
- 更新后的 `benchmark_projects.md` 与 `bg3_official.md`

### 依赖关系

依赖阶段 0，因为要先知道这些来源将服务哪条总逻辑。

### 完成定义

- `source_index.md` 中已收录 benchmark 方法与官方 modding / journal / osiris 文档。
- 每类来源都至少有 1 条已蒸馏的 source note。
- 后续任何区域包都可以直接引用这组底座，而不必重新解释为什么要看这些资料。

### 对应文件

- `docs/00_project/source_index.md`
- `docs/02_sources/benchmark_projects.md`
- `docs/02_sources/bg3_official.md`
- `docs/02_sources/source_note_bmk_*.md`
- `docs/02_sources/source_note_bg3_off_011_*.md` 及后续同类文件

### 什么算跑偏

- 新增很多链接，却没有 source note。
- 把 modding 文档当成现成技术实锤，而不是验证入口。

### 必须暂停并重审的条件

- benchmark 方法和项目总逻辑无法对齐。
- 官方文档与当前“区域包执行法”明显冲突。

---

## 阶段 2：Act 1 区域包

### 目标

把“区域包执行法”真正跑起来，并用 Act 1 证明：

- 宏观结构
- 战斗 / 环境
- 任务回流
- 营地折叠
- 实现验证

可以被同一轮区域包稳定回写。

### 子阶段

1. `Nautiloid`
2. `Act 1 地表主区`
3. `Grove / Goblin 冲突`
4. `Underdark`
5. `Grymforge`
6. `Mountain Pass / Creche`

### 输入

- 阶段 1 的来源底座
- 现有 `01_macro_structure.md`、`02_quests_and_choices.md`、`04_combat_and_environment.md`
- 已有营地与实现验证模块

### 输出

- 每个区域包至少 1 个区域 case note
- 需要时补新的官方 source note 与玩家 case note
- 对至少 3 个分析模块的回写
- 当前最强解释与待验证问题边界更新

### 依赖关系

依赖阶段 1，否则会边做区域包边临时补方法底座。

### 完成定义

- Act 1 六个区域包都完成首轮证据包。
- 至少能明确解释：Act 1 如何把多入口推进、任务回流、战斗环境和营地反馈连起来。
- `Nautiloid` 已成为可复用模板，而不是一次性例外。

### 对应文件

- `docs/03_analysis/01_macro_structure.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/04_combat_and_environment.md`
- `docs/03_analysis/05_implementation_validation.md`
- 相关 `docs/02_sources/*`

### 什么算跑偏

- 把 Act 1 写成剧情目录。
- 每个区域包只回写一个模块，导致其余模块继续悬空。
- 又重新围绕单一局部补丁做低收益侦察。

### 必须暂停并重审的条件

- 某个区域包连续两轮仍无法解释“它对总链条贡献了什么”。
- 多个区域包重复同一批结论，却没有新增边界或反例。

---

## 阶段 3：Act 2 区域包

### 目标

检验 BG3 中盘的“压力结构 + 阵营收束 + 营地折返 + 任务推进”如何叠在一起。

### 子阶段

1. `Act 2 总框架`
2. `Shadow-Cursed Lands`
3. `Last Light / Moonrise / Gauntlet / 收束点`

### 输入

- 阶段 2 的 Act 1 区域包模板
- 已更新的 `current_state.md`、`next_step.md`
- 官方 patch / community update / Journal / Osiris 线索

### 输出

- Act 2 的区域包 case notes
- 对任务、营地、实现验证模块的显著回写
- 对宏观结构“阶段性收束”判断的升级或降级

### 依赖关系

依赖阶段 2，因为 Act 2 需要以 Act 1 形成的区域包模板为基础。

### 完成定义

- 已能解释 BG3 如何在中盘把区域压力与反馈链密度显著提高。
- 已能解释 `Last Light / Moonrise / Gauntlet` 为什么是结构收束点，而不是纯剧情高潮。

### 对应文件

- 同阶段 2，但 `03_party_and_camp.md` 与 `05_implementation_validation.md` 权重更高。

### 什么算跑偏

- 把 Act 2 只写成阴影诅咒背景说明。
- 只抓高潮剧情，不写状态与系统收束。

### 必须暂停并重审的条件

- Act 2 材料无法稳定回到总链条，而一直停在叙事氛围描述。

---

## 阶段 4：Act 3 区域包

### 目标

检验 BG3 在高密度城市、派系并行、终局组织和多线程收束下，反应性如何维持、失真或被压缩。

### 子阶段

1. `Act 3 总框架`
2. `Rivington`
3. `Wyrm’s Crossing`
4. `Lower City`
5. `终局组织与收束压力`

### 输入

- 阶段 2 与阶段 3 的区域包写法
- 官方资料与社区案例的后期补充

### 输出

- Act 3 区域包 case notes
- 对宏观结构、任务回流与终局压力的系统判断
- 对“反应性在高密度内容下的边界”做出更稳判断

### 依赖关系

依赖阶段 3，因为 Act 3 只有放在前两阶段链条之后，才能看出哪些东西被维持，哪些东西被压缩。

### 完成定义

- 已能解释 BG3 后期为什么常被玩家同时感知为“极高密度”和“高收束压力”。
- 已能把 Act 3 的派系与城市结构放回总逻辑，而不是单纯列城市地点。

### 对应文件

- `01_macro_structure.md`
- `02_quests_and_choices.md`
- `03_party_and_camp.md`
- `05_implementation_validation.md`

### 什么算跑偏

- 变成城市地点导览。
- 只写终局，不写前面状态如何被压缩结算。

### 必须暂停并重审的条件

- Act 3 的区域包开始明显脱离前面阶段的比较框架。

---

## 阶段 5：横向综合与实现验证升级

### 目标

把前面所有区域包重新压成三条横向主干：

- Quest Reactivity
- Companion / Camp / Long Rest
- Combat / Environment

并用 Journal / Osiris / patch / hotfix / developer explanation 对核心判断做一次升级、降级或分层。

### 输入

- 阶段 2~4 的区域包产出
- 官方 Journal / Osiris 文档
- 开发者说明与补丁文档

### 输出

- 升级后的 `05_implementation_validation.md`
- 重新校正的 `00_core_thesis.md`
- 需要时回写三个横向主干模块

### 依赖关系

必须依赖阶段 2~4。没有区域包素材，横向综合只会变成空洞二次概括。

### 完成定义

- 每条核心判断都已被分成：可写成事实、当前最强解释、必须待验证。
- 已能清楚说明哪些结论来自玩家体验，哪些被公开实现结构进一步支撑。

### 对应文件

- `docs/03_analysis/00_core_thesis.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/04_combat_and_environment.md`
- `docs/03_analysis/05_implementation_validation.md`

### 什么算跑偏

- 把 Implementation Validation 写成技术细节仓库。
- 为了“技术感”而升级没有证据的实现断言。

### 必须暂停并重审的条件

- Journal / Osiris 文档与既有系统判断持续冲突。
- 横向整合后发现区域包逻辑本身需要重写。

---

## 阶段 6：展示收束与发布导览

### 目标

把已经完成的研究内容压成适合人看、适合演示、适合持续维护的展示入口，而不扭曲研究边界。

### 输入

- 阶段 0~5 的全部沉淀
- `presentation_forms.md`

### 输出

- 清晰的阅读 / 展示顺序
- 需要时补图、卡片、流程图、结构图的说明稿
- 一份首轮发布包总装配 / 审阅清单
- 更新后的 `deconstruction_display_overview.md`

### 依赖关系

必须依赖前 0~5 阶段。展示收束永远在研究收束之后。

### 完成定义

- 仓库负责人一眼就能看懂项目按什么逻辑拆。
- 读者不会再问“为什么突然拆营地”。
- Codex 可以沿粒度计划继续补下一块，不需要再问总逻辑。
- 五段 actual units 已能被一份 assembly / review sheet 统一装配与审阅，而不必回头重写 queue。
- 首批发布包闭合后，阶段 6 能明确切入“冻结后的条件触发维护态”，而不是默认无限继续 addendum 续轮。
- 冻结维护态现在还有独立 playbook，因此后续会话即使进入 stage 6，也应先做 trigger 判定，而不是默认把维护理解成新一轮审阅。

### 对应文件

- `docs/00_project/deconstruction_display_overview.md`
- `docs/01_methodology/presentation_forms.md`
- `docs/01_methodology/stage6_freeze_maintenance_playbook.md`
- `docs/00_project/stage6_release_package_assembly_review_sheet.md`
- `README.md`
- `repo_map.md`

### 什么算跑偏

- 先做展示物，再补研究依据。
- 为了展示好看，把待验证问题写没了。

### 必须暂停并重审的条件

- 展示入口与研究现状开始冲突。

## 4. 当前阶段定位

本轮已完成：

- 阶段 0：总逻辑重审与导航重排
- 阶段 1：执行底座冻结的首轮搭桥（benchmark + Journal / Osiris 来源已经入索引）
- 阶段 2：Act 1 六个区域包首轮闭合
- 阶段 3：Act 2 首轮闭合
- 阶段 4：Act 3 首轮闭合
- 阶段 5：横向综合与实现验证升级已闭合
- 阶段 6：展示入口、section skeleton、最低发布包、五段 actual units、首轮 assembly / review 清单、截至 2026-04-26 的 `round32` 维护确认，以及冻结维护态 playbook 都已落地；当前维护入口也已进一步收口为 review sheet + playbook 这一组默认判定工具

当前默认阶段定位是：

> 阶段 6 已闭合，仓库进入“冻结后的条件触发维护态”。`stage6_release_package_assembly_review_sheet.md` 是默认主动维护入口，`docs/01_methodology/stage6_freeze_maintenance_playbook.md` 是默认维护动作清单，历史 round addendum 只保留为维护记录链；只有命中新 trigger、出现正文级改动 / handoff 变化 / evidence traceback 回退 / assembly map 改动，或项目负责人明确要求复核发布链时，才重开新的 review round。

以下情况不应再单独推动新 round：

- 只是为了“再谨慎检查一轮”
- 没有新的正文改动，也没有新的 trigger
- 只是想把 latest addendum 文件名继续递增

## 5. 什么情况下必须暂停并重审整份计划

出现以下任一情况，不要硬推进，先停下来重审：

1. 区域包写法明显退化成剧情复述。
2. 模块又重新和区域包脱钩，开始抽象跳转。
3. 营地再次脱离前序状态单独扩写。
4. 官方 Journal / Osiris / patch 资料系统性反驳当前总链条。
5. 新增资料太多，但 `current_state.md` 和 `next_step.md` 仍无法说清当前主线。
