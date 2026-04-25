# Master Roadmap

## 作用

本文件是《博德之门3》研究仓库的项目级主路线摘要。它不替代 ExecPlan，也不替代操作级计划；它的职责是稳定回答四个问题：

1. 这个项目到底按什么总逻辑拆。
2. 研究顺序和展示顺序为什么不同。
3. 哪些旧判断保留，哪些地方已经纠偏。
4. 当前主线处在哪个阶段，为什么现在默认不是继续开新 round。

详细阶段定义见 `docs/00_project/deconstruction_master_execution_plan.md`；操作级执行脚本见 `docs/00_project/deconstruction_granular_codex_plan.md`。

## 保留的东西

以下基础判断保留，不推翻重来：

- 三层拆解方法继续作为总方法底座。
- `docs/03_analysis/00_core_thesis.md` 到 `05_implementation_validation.md` 这组分析模块继续保留，作为长期分析骨架。
- 来源纪律、事实 / 推断 / 待验证问题分层、Source ID 管线、状态文件与决策日志继续保留。
- 现有 `quests_and_choices`、`party_and_camp`、`combat_and_environment` 的已得结论继续有效，只是它们现在要被重新放回更清楚的总逻辑里。

## 纠偏后的核心判断

### 1. 模块顺序不是展示顺序

过去的项目更接近“研究模块顺序”，对内部推进有价值，但对外会造成“为什么突然从任务跳到营地”的观感。现在明确区分：

- 展示顺序：按玩家体验链条组织。
- 研究顺序：按区域包 / Act 包收证据，再回写多个模块。

### 2. 区域包是研究执行单元，不是剧情复述目录

Nautiloid、Act 1 地表、Grove / Goblin、Underdark、Grymforge、Creche、Act 2、Act 3 等，都不是为了按剧情复述，而是为了把一个阶段里同时发生的空间组织、任务状态、战斗解法、营地反馈和实现验证入口收束成一个可执行包。

### 3. 营地 / 长休是反馈折叠层，不能孤立出现

营地不应作为“突然单开的一章”。它在总逻辑中的位置必须晚于：

- 区域行动
- 任务状态变化
- 战斗 / 环境造成的局部结果

它负责把这些分散状态在休整节点重新呈现为同伴反应、对话可达性、关系推进和后续解释。

## 项目的两条顺序

### 展示顺序

1. 总命题与高反应性解释
2. 宏观结构与区域包
3. 局部行动层：战斗 / 环境 / 多入口
4. 任务与 Journal 状态回流
5. 同伴 / 营地 / 长休反馈折叠
6. Act 收束与终局压力
7. 实现验证

### 研究顺序

1. 冻结总逻辑与方法边界
2. 建立外部 benchmark 与官方验证底座
3. 按区域包推进 Act 1
4. 按区域包推进 Act 2
5. 按区域包推进 Act 3
6. 横向整合 Quest Reactivity / Camp / Combat / Implementation Validation
7. 展示收束与发布包装配

## 阶段摘要

### 阶段 0：总逻辑重审与仓库导航重排

目标：先解决“到底按什么逻辑拆”以及“为什么现在拆这个”。

### 阶段 1：执行底座冻结

目标：把 benchmark 方法、官方 modding / Journal / Osiris 文档纳入来源底座，并冻结区域包执行法。

### 阶段 2：Act 1 证据包

目标：拿 `Nautiloid` 到 `Mountain Pass / Creche` 做第一轮完整证明，验证“区域包写法”是否能稳定回写多个模块。

### 阶段 3：Act 2 证据包

目标：验证中盘如何把区域压力、营地反馈和任务收束叠在一起。

### 阶段 4：Act 3 证据包

目标：验证 BG3 在高密度城市、多派系并行与终局收束下，反应性如何扩张与变形。

### 阶段 5：综合与展示收束

目标：把前面分散的区域包材料重新压成适合阅读与展示的总链条，并完成三条横向主干的出口收口。

### 阶段 6：发布包装配与一致性审阅层

目标：把已闭合的五段 actual units 装配成首批发布包，并用受控 review 只处理真正值得回写的装配级冲突。

现状态：

- 首批发布包已闭合。
- 首轮局部 writeback 与第十轮 traceback 修正都已完成。
- 截至 2026-04-26 的最新维护确认是 `round32`。
- 阶段 6 现在处于“冻结后的条件触发维护态”，而不是默认继续开 `round33` 的主动推进态。
- 冻结维护态的默认维护动作也已被压成 `docs/01_methodology/stage6_freeze_maintenance_playbook.md`，后续应先按 playbook 判定 trigger，而不是先考虑新 round。

## 当前状态：冻结 / 维护态

当前主线不再是 `Nautiloid 区域包`，也不再是“继续多做一轮 stage 6 审阅”。当前仓库的稳定状态是：

- 阶段 0 到阶段 5 的研究与展示主线已经闭合。
- 阶段 6 的首批发布包装配链已经闭合。
- `stage6_release_package_assembly_review_sheet.md` 与 `docs/01_methodology/stage6_freeze_maintenance_playbook.md` 现在共同承担维护工具角色。
- 在没有新 trigger 的情况下，默认动作是先按 playbook 完成 no-trigger maintenance，而不是新增新的 stage 6 review round。

## 何时重开 Stage 6 Review

只有出现以下任一情况，才值得重新打开新的 stage 6 review round：

1. 五段 actual units 之一发生正文级改动。
2. `entry / opening / camp / closing / final` 的 handoff 顺序发生变化。
3. evidence lock 或 benchmark traceback 出现回退、缺失、错链。
4. release package assembly map 被改动后，需要重新校对。
5. 项目负责人明确要求对发布链做新一轮一致性审阅。

## 什么不算需要重开

以下情况不应触发新 round：

1. 只是为了“再谨慎检查一轮”。
2. 没有新的正文改动，也没有新的 trigger。
3. 只是 latest addendum 文件名看起来还可以继续递增。
4. 没有任何 evidence / assembly / handoff 层面的实质变化。

## 什么算跑偏

- 又重新按剧情复述写长文。
- 又把营地、任务、战斗拆成互不解释的平行模块。
- 收了很多来源，但没有形成区域包级别的 case note 与回写。
- 直接把 Osiris / Journal 文档当成现成技术实锤，而不是实现验证入口。
- 在没有新 trigger 的情况下，把 stage 6 review-loop 自己维持成默认主线。
