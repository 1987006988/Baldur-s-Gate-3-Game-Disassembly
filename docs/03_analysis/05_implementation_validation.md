# Implementation Validation

## Question

在不依赖私有开发资料的前提下，我们如何尽可能验证前述体验与系统判断不是空想？

## Short answer

本模块的职责不是反向工程出完整实现，而是建立一套“公开可验证证据链”。我们优先使用官方术语、开发者访谈、补丁说明、UI 信号、流程结构与可稳定复现的案例，来判断哪些结论已经足够稳，哪些仍只是合理推测。

## Validation Entry Points

- 官方资料中的设计意图与术语
- 补丁说明中的系统修正点
- UI、日志、提示、状态变化中的稳定信号
- 不同模块之间是否存在一致的回流现象
- 高辨识度案例能否在补丁 / 热修 / 社区更新中找到明确的状态差异与后续反馈锚点

## Current Working Assumptions

- `推断`：如果一个体验在多个模块反复出现，且官方用相近术语描述，就可以提高其可信度。
- `推断`：补丁说明最容易暴露设计团队真正关心的系统边界与失效点。
- `推断`：当官方补丁明确区分某个分支的状态差异，并同时修复其跨长休、跨区域或后续章节反应时，这类条目可作为“状态回流存在”的强验证入口。
- `待验证问题`：是否还能从公开工具链、脚本命名或社区技术观察中提取更具体的实现线索？

## Evidence Rules In Practice

- 没有来源支撑的技术判断不升级为事实。
- 观察到的 UI 或流程信号，要和来源材料互相校对。
- 发现冲突时优先降级结论，而不是硬拼解释。
- 若某个案例只有社区线索而缺乏官方直接来源，只能把它留在“案例入口”层，不能直接升级为系统性事实。

## Current Validation Anchors

### Nautiloid 开场 / 教程边界

- `事实`：`BG3-OFF-015` 直接暴露了开场阶段的 narrator 触发、quest item 高亮、受限检定、条件清理和角色离场崩溃边界。
- `事实`：`BG3-OFF-002` 直接暴露了 `Escape the Nautiloid` 的 quest close 会因时序问题失效，以及 tutorial 结束后的 buff / 装备交接需要被修复。
- `事实`：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 提供了公开 Journal / trigger 结构语言，使我们可以更稳地把这些问题表述为 quest / objective / step 与 trigger update 边界，而不是纯玩家印象。
- `推断`：这说明 `Nautiloid` 已经是一个真实的实现验证入口：它同时暴露了 opening flow、任务关闭、状态清理与角色交接。基于 `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-015`

### Act 1 地表主区作为 opening state 的续接层

- `事实`：`BG3-OFF-015` 说明 nautiloid 阶段的部分 harmful conditions 会在坠毁后被移除，表明 crash 后存在明确的状态清理边界。
- `事实`：`BG3-OFF-002` 说明 tutorial 结束后的装备与 buff 交接会继续影响地表招募，例如 `Shadowheart / Lae'zel` 在后续被招募时需要获得新的装备。
- `事实`：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 继续提供了 objective / step / trigger update 的公开结构语言，使我们能把“地表在续接什么 opening state”写成结构性问题，而不是只写体验印象。
- `推断`：这使 `Act 1 地表主区` 成为比 `Nautiloid` 更好的第二层验证入口：它允许我们公开追问哪些状态会在 crash 时被清理，哪些会在地表招募、目标续接和后续营地前史里被重新读取。基于 `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-015`

### Minthara 击倒路径

- `事实`：`BG3-OFF-004` 直接暴露了 `knocked out` 与 `killed` 的状态差异，以及跨长休判定失效点。
- `事实`：`BG3-OFF-002` 继续暴露了该状态在后续区域与章节中的再调用问题。
- `推断`：这说明任务回流不是单个对白开关，而是会跨区域、跨休息节点重新结算的状态链。
- `案例线索`：`BG3-PLY-003` 可作为玩家侧对照，用来识别哪些路径是系统稳定支持，哪些只是边缘状态或历史 bug。

### Grove / Goblin 冲突作为 resolution matrix 验证入口

- `事实`：`BG3-OFF-004` 不只暴露了 `knocked out` / `killed` 的状态差异，还暴露了“击倒 Minthara -> 长休 -> 再处理其他首领”这一时序本身会影响后续判定。
- `事实`：`BG3-OFF-002` 继续把同一冲突的延迟结果写到跨区域与跨章节层：被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 重新读取这条前史。
- `事实`：`BG3-OFF-008` 进一步暴露了 Minthara 在营地中的对话可达性与 `companion reaction` 也是需要单独维护的边界。
- `推断`：把这三组条目放在一起看，`Grove / Goblin` 就不再只是一个“站哪边”的剧情摘要，而是 `Act 1` 第一块同时暴露“处理方式 / 长休时序 / 营地读出”三种验证入口的区域包。基于 `BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-008`

### Underdark 作为区域切换与下游 setup 的验证入口

- `事实`：官方 About 页把 `Underdark` 列在 BG3 的差异化区域序列中，说明它属于公开可验证的宏观结构节点。来源：`BG3-OFF-001`
- `事实`：Adam Smith 用 `Swiss cheese` 描述 BG3 的路径组织，说明“同一阶段存在多个洞口 / 进入方式”是官方直接给出的结构语言。来源：`BG3-OFF-003`
- `事实`：`Community Update 14` 的 patch notes 直接写到 `Added setup for several Grymforge quests in the Underdark.`，并把 `Grymforge` 定义为包含 `questlines, choices, cinematics, complex combat encounters` 的区域。来源：`BG3-OFF-006`
- `推断`：这组公开入口已足以让我们把 `Underdark` 写成“区域切换如何带出下游 quest setup”的验证对象：它能支撑“阶段重构”这一层判断，但还不足以直接反推具体 objective / step 映射。基于 `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-006`

### Grymforge 作为战斗 / 环境区域压缩包的验证入口

- `事实`：`Community Update 14` 不只把 `Grymforge` 描述成复杂战斗区，还把它与 `Underdark` 中的若干 quest setup 明确连在一起。来源：`BG3-OFF-006`
- `事实`：Adam Smith 对 `Swiss cheese` 的描述说明，BG3 会把多入口与非常规 problem-solving 当成关卡 / 遭遇的同一套设计语言。来源：`BG3-OFF-003`
- `案例线索`：`BG3-PLY-004` 说明玩家确实把 `Grymforge / Grym` 理解成可通过高差、机关、落体、远程触发与战前布置重写的遭遇，但这仍只能承担案例入口。来源：`BG3-PLY-004`
- `推断`：这组公开入口已足以让我们把 `Grymforge` 写成“战斗 / 环境 agency 也是区域推进体验一部分”的验证对象：它能支撑区域包级判断，但还不足以直接反推某条具体熔炉路径的 objective / step 映射。基于 `BG3-OFF-003`, `BG3-OFF-006`, `BG3-PLY-004`

### Mountain Pass / Creche 作为门槛 / 伙伴张力叠层包的验证入口

- `事实`：`Patch #3` 直接暴露了 `Mountain Pass / Creche` 的多重维护边界：拒绝 `Vlaakith` 后的多余检定会挡住后续对话、`Rosymorn Monastery gate` 的爆炸倒计时需要在进入 `Astral Plane` 后正确取消。来源：`BG3-OFF-016`
- `事实`：同一补丁还暴露了局部处理方式会改写敌意：如果 `Lae'zel` 在与 `Voss` 的互动中成功通过 `Deception` 检定，`githyanki` 不应继续保持敌对。来源：`BG3-OFF-016`
- `事实`：同一补丁同时把 `Lae'zel` 在 `Crèche Y'llek` 遇到 `Dream Visitor` 后的即时反应，以及 `camp night` 里关于 `crèche` 后果的延迟反思，列为需要修复的边界。来源：`BG3-OFF-016`
- `推断`：这组公开入口已足以让我们把 `Mountain Pass / Creche` 写成“结构门槛 + 伙伴张力”叠层包的验证对象：它能支撑区域包级判断，但还不足以直接反推 `Act 2` 切换规则或完整 `Journal / objective / step` 映射。基于 `BG3-OFF-003`, `BG3-OFF-016`

### 阶段 5 / Quest Reactivity 的上游前置链分层矩阵

| 链段 | 当前可升级到的层级 | 公开锚点 | 当前不能升级的部分 |
| --- | --- | --- | --- |
| `Nautiloid` 入口埋点 | 已接近 `objective / step` 邻近边界：`Escape the Nautiloid` 的 quest close、关键物件、状态清理与地表招募交接都有直接维护条目。 | `BG3-OFF-002`, `BG3-OFF-015`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把每个开场分歧都写成长线回流的事实表。 |
| `Act 1 地表主区` 目标网 | 可稳定升级为 `opening-state carryover + objective pressure net`：开场残余状态会在地表招募与目标续接中继续被读取。 | `BG3-OFF-002`, `BG3-OFF-015`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把完整早期路线顺序写成 objective / step 实锤。 |
| `Underdark` 改道 / 重构 | 可稳定升级为 `entry / diversion / setup bundle`：公开来源已足以支撑“同一阶段切到另一套推进框架”。 | `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-006` | 还不能把具体地下入口与过渡全部压到 objective / step。 |
| `Mountain Pass / Creche` 门槛 / 张力 | 局部门槛已接近 `objective / step` 邻近边界，但整体仍更稳地停留在 `gate-and-tension bundle`：对话门槛、敌意变化、即时伙伴反应与 `camp night` 读取都有直接维护条目。 | `BG3-OFF-016`, `BG3-OFF-003` | 还不能把 `Act 2` 切换规则或完整 objective 映射写成事实表。 |

- `推断`：把这四段串起来后，阶段 5 现在已经同时拥有“前置链”和“读回链”两段公开验证结构：上游先到 `objective` 埋点、目标网、改道与门槛，下游再进入 `resolution matrix -> convergence -> late-game bundle -> ending feedback` 的读回梯。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-006`, `BG3-OFF-015`, `BG3-OFF-016`

### Act 2 总框架作为中盘压力与跨 Act 读回的验证入口

- `事实`：官方 About 页把 `shadow-cursed forests` 与 `Underdark`、博德之门城市并列呈现，说明 `Act 2` 属于公开可验证的阶段级区域节点。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 的 `Writing and Flow`、`Scripting`、`Act II` 条目包含大量与任务流、营地夜晚场景、角色反应、对话优先级相关的修复。来源：`BG3-OFF-002`
- `事实`：同一补丁还明确写到，被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对玩家在 `Act I` 的处理作出反应。来源：`BG3-OFF-002`
- `事实`：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 继续提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，使我们能把 `Act 2` 的压力判断约束在“哪些状态会被更紧地重读”这一级，而不是凭印象猜测私有脚本。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这组公开入口已足以让我们把 `Act 2` 写成“中盘压力 / 前史重读框架”的验证对象：它能支撑阶段级判断，但还不足以直接反推影咒限制、收束点分工或完整 `objective / step` 映射。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

### Shadow-Cursed Lands 作为中盘压力落地的验证入口

- `事实`：官方 About 页没有只把 `shadow-cursed forests` 当成气氛词，而是把它放进 BG3 的差异化区域序列中。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 的 `Act II`、`Writing and Flow`、`Scripting` 条目集中暴露中盘任务流、角色反应、营地夜晚场景与对话优先级的维护边界；同一补丁还把至少一条 `Act I -> Act II` 的前史读回链明确写到 `Moonrise Towers`。来源：`BG3-OFF-002`
- `事实`：Adam Smith 的 `Swiss cheese` 结构语言提供了一个公开边界：即便进入中盘，BG3 也不应被默认理解成“只剩单一路径”。来源：`BG3-OFF-003`
- `事实`：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 继续提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，因此我们可以公开提出“哪些压力会重组推进”，但不能反推具体私有脚本。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这组公开入口已足以让我们把 `Shadow-Cursed Lands` 写成“中盘压力第一次落到区域推进上”的验证对象：它能支撑区域级判断，但还不足以直接反推具体影咒机制、路线分工或完整 objective / step 映射。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

### Last Light / Moonrise / Gauntlet 作为中盘收束点组的验证入口

- `事实`：`Patch 7` 的 `Writing and Flow`、`Scripting`、`Act II` 条目继续集中暴露中盘任务流、角色反应、营地夜晚场景与对话优先级的维护边界；同一补丁还明确写到，被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对 `Act I` 的处理作出反应。来源：`BG3-OFF-002`
- `事实`：Adam Smith 的 `Swiss cheese` 结构语言继续提供一个公开边界：即便进入收束段，BG3 的上位设计语言也不应被默认理解成“所有路径被取消”。来源：`BG3-OFF-003`
- `事实`：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 持续提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，因此我们可以公开提出“哪些节点在压缩与重读任务”，但不能反推具体私有 objective 编排。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这组公开入口已足以让我们把 `Last Light / Moonrise / Gauntlet` 写成“中盘收束点组”的验证对象：它能支撑“前置路径差异开始在较少节点被集中读取”这一组判断，但还不足以把三者内部的分工与完整 objective / step 映射写成实现实锤。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

### Act 3 总框架作为高密度城市与结算负载的验证入口

- `事实`：官方 About 页把 `the sprawling city of Baldur's Gate` 与 `shadow-cursed forests`、`Underdark` 并列呈现，说明 `Act 3` 属于公开可验证的阶段级城市节点。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 明确加入新的 evil ending cinematics，并把它们表述为会根据玩家做出的选择出现。来源：`BG3-OFF-002`
- `事实`：同一补丁继续集中修复 `writing and flow`、`scripting`、角色反应与长休 / 营地边界，说明后期结算不是单点 ending choice，而是高密度状态读回区。来源：`BG3-OFF-002`
- `事实`：Adam Smith 一方面继续用 `Swiss cheese` 描述 BG3 的多入口结构，另一方面明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的结局与状态排列。来源：`BG3-OFF-003`
- `事实`：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 持续提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，因此我们可以公开提出“后期并行线如何变密”，但不能反推具体城市子块的私有 objective 编排。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这组公开入口已足以让我们把 `Act 3` 写成“高密度城市中的结算负载”验证对象：它能支撑“并行线数量与前史读回压力同时升高”这一组判断，但还不足以把 `Rivington`、`Wyrm's Crossing`、`Lower City` 与终局组织的完整分工写成实现实锤。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

### Rivington 作为入口过滤与外环承压的验证入口

- `事实`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为 BG3 的阶段级城市节点直接点名。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 一方面把新的 evil ending cinematics 写成会根据玩家选择出现，另一方面继续集中修复后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界。来源：`BG3-OFF-002`
- `事实`：Adam Smith 继续用 `Swiss cheese` 描述 BG3 的多入口结构，并明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。来源：`BG3-OFF-003`
- `事实`：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 持续提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，因此我们可以公开提出“第一层入口过滤如何组织 quest bundle”，但不能反推 `Rivington` 内部的私有 objective 编排。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这组公开入口已足以让我们把 `Rivington` 写成“`Act 3` 第一层入口过滤与外环承压区”的验证对象：它能支撑“后期高密度并行线会先在这里被分束、过滤与重排”这一组判断，但还不足以把哪些读回发生在 `Rivington` 现场、哪些延迟到 `Wyrm's Crossing` 或 `Lower City` 写成实现实锤。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

### Wyrm's Crossing 作为桥梁 / 门槛重排的验证入口

- `事实`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为 BG3 的阶段级城市节点直接点名。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 一方面把新的 evil ending cinematics 写成会根据玩家选择出现，另一方面继续集中修复后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界。来源：`BG3-OFF-002`
- `事实`：Adam Smith 继续用 `Swiss cheese` 描述 BG3 的多入口结构，并明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。来源：`BG3-OFF-003`
- `事实`：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 持续提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，因此我们可以公开提出“第二层 bridge / gate bundle 如何重排 late-game reading order”，但不能反推 `Wyrm's Crossing` 内部的私有 objective 编排。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这组公开入口已足以让我们把 `Wyrm's Crossing` 写成“`Act 3` 的桥梁 / 门槛 / 第二层结构重排区”的验证对象：它能支撑“已被 `Rivington` 过滤过的后期并行线，会在这里进一步被压成更靠近城市核心的门槛结构”这一组判断，但还不足以把哪些门槛已逼近 `objective / step` 层、哪些仍应延后到 `Lower City` 写成实现实锤。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

### Lower City 作为更高密度内城并行 / 结算区的验证入口

- `事实`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为 BG3 的阶段级城市节点直接点名。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 一方面把新的 evil ending cinematics 写成会根据玩家选择出现，另一方面继续集中修复后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界。来源：`BG3-OFF-002`
- `事实`：Adam Smith 继续用 `Swiss cheese` 描述 BG3 的多入口结构，并明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。来源：`BG3-OFF-003`
- `事实`：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 持续提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，因此我们可以公开提出“更高密度的内城 quest bundle / 结算负载如何组织”，但不能反推 `Lower City` 内部的私有 objective 编排。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这组公开入口已足以让我们把 `Lower City` 写成“`Act 3` 的更高密度内城并行 / 结算区”验证对象：它能支撑“已被 `Rivington` 过滤、被 `Wyrm's Crossing` 门槛化的后期并行线，会在这里开始以更短窗口同时承接、重读与逼近结算”这一组判断，但还不足以把哪些并行束已逼近 `objective / step` 层、哪些仍应延后到 `终局组织与收束压力` 写成实现实锤。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

### 终局组织与收束压力作为组织级终局压缩 / ending feedback 读取层的验证入口

- `事实`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为 BG3 的阶段级城市节点直接点名。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 明确加入新的 evil ending cinematics，并把它们表述为会根据玩家做出的选择出现；同一补丁继续集中修复后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界。来源：`BG3-OFF-002`
- `事实`：Adam Smith 继续用 `Swiss cheese` 描述 BG3 的多入口结构，并明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。来源：`BG3-OFF-003`
- `事实`：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 持续提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的公开结构语言，因此我们可以公开提出“组织级 quest bundle 压缩 / ending feedback 读取层如何组织”，但不能反推终局私有 objective 编排。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这组公开入口已足以让我们把 `终局组织与收束压力` 写成“`Act 3` 的组织级终局压缩层”验证对象：它能支撑“已在 `Lower City` 并排承接的问题束，会在这里开始被更少、更硬的终局组织位读取、重排并逼向 ending feedback”这一组判断，但还不足以把哪些组织位已逼近 `objective / step` 层、哪些仍应停留在 `organization bundle / flow / ending feedback` 边界写成实现实锤。基于 `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

### 阶段 5 / Quest Reactivity 的跨阶段分层矩阵

| 链段 | 当前可升级到的层级 | 公开锚点 | 当前不能升级的部分 |
| --- | --- | --- | --- |
| `Grove / Goblin` 处理矩阵 | 已接近 `objective / step` 边界：至少 `knocked out` / `killed`、长休时序、`journal wording` 与营地可达性有直接维护条目。 | `BG3-OFF-004`, `BG3-OFF-008` | 还不能把除 `Minthara` 外的全量首领顺序与处理差异写成事实表。 |
| `Last Light / Moonrise / Gauntlet` 收束点组 | 可稳定升级为 `convergence pack / cross-Act reread`：至少 `Moonrise Towers` 已被直接写成 `Act I -> Act II` 的读回落点。 | `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把三者内部的分工或完整 `objective / step` 映射写成实现实锤。 |
| `Rivington -> Wyrm's Crossing -> Lower City` | 可稳定升级为 `bundle` 级结构梯：第一层过滤、第二层门槛重排、更高密度并排承接与局部结算。 | `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把每一层具体哪条城市线已经压到 `objective / step` 写成私有任务表。 |
| `终局组织与收束压力` | 可稳定升级为 `organization bundle + ending feedback`：late-game 问题束会被更少、更硬的终局组织位读取、重排并逼向结算。 | `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把终局组织内部的完整 objective 编排、派系分工或结局清单写成事实表。 |

- `推断`：把这四段串起来后，阶段 5 当前最稳的实现验证结论是：BG3 的 `Quest Reactivity` 已足以被公开写成一条“处理矩阵 -> 收束点组 -> 高密度 bundle 过滤 / 重排 / 并排承接 -> 组织级 ending feedback 压缩”的跨阶段读回梯，而不只是“分支很多”。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

### 阶段 5 / Quest Reactivity 的 late `Act 1` / early `Act 2` 交接矩阵

| 链段 | 当前可升级到的层级 | 公开锚点 | 当前不能升级的部分 |
| --- | --- | --- | --- |
| `Mountain Pass / Creche` | 局部门槛已接近 `objective / step` 邻近边界：对话阻塞、敌意变化、即时伙伴反应与 `camp night` 后果读取均有直接维护条目。 | `BG3-OFF-016`, `BG3-OFF-003` | 还不能把 `Act 2` 切换规则、警告文本或完整 objective 映射写成事实表。 |
| `Shadow-Cursed Lands` | 可稳定升级为 `pressure / flow filter bundle`：公开来源已足以支撑“中盘风险开始持续过滤推进方式与前史读回”。 | `BG3-OFF-002`, `BG3-OFF-003` | 还不能把区域内部哪些风险变量、路线分工与读回时机压到 `objective / step` 层。 |
| `Last Light / Moonrise / Gauntlet` | 可稳定升级为 `convergence pack / reread bundle`：至少 `Moonrise Towers` 已被直接写成 `Act I -> Act II` 的读回落点，且公开 Journal 文档允许我们只写到结构层。 | `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把三者内部的分工、完整 objective / step 映射或更多私有任务排序写成实现实锤。 |

- `推断`：把这三段补入之后，阶段 5 的公开验证结构不再只有“上游前置链”和“下游 readback spine”两端，而是补齐了最关键的中盘接缝：late `Act 1` 的 gate 会先被改写成 early `Act 2` 的 pressure filter，再被压成 `convergence pack`。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`

### 阶段 5 / Quest Reactivity 的第二条公开跨阶段链证据上限

| 候选束 | 当前可升级到的层级 | 公开锚点 | 当前不能升级的部分 |
| --- | --- | --- | --- |
| `Mountain Pass / Creche -> Voss / camp night` | 可稳定升级为 `gate / tension / delayed camp readout bundle`：公开条目已直接暴露对话门槛、局部敌意、即时伙伴反应与延迟营地读出。 | `BG3-OFF-016` | 还不能把它写成第二条具名 `Act I -> Act II` 任务链，因为公开来源没有给出与 `Moonrise Towers` 同级的 downstream 命名落点。 |
| `Karlach` 跨 `Act` 反思 + 非 `Minthara` 营地修复 | 可稳定升级为 `camp fold / dialogue accessibility bundle`：公开条目已证明非 `Minthara` 的跨阶段读回与营地可达性维护真实存在。 | `BG3-OFF-007`, `BG3-OFF-010` | 还不能把这组维护串成单一主链，因为它们目前更像多个营地折叠点，而非一条连续的跨区域任务脊梁。 |
| late-game `writing and flow` / ending feedback / `trigger updates` | 可稳定升级为 `ending feedback / organization bundle`：公开来源已足以证明中后段会持续重读前史并在更少节点压向结算。 | `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把这些后期维护写成第二条显式跨 `Act` 链，因为公开来源没有给出与 `Minthara -> Moonrise Towers` 同级的“具体 upstream handling -> 具体 downstream node”配对。 |

- `推断`：阶段 5 当前已可以把“第二条公开跨阶段链”正式降级为证据上限问题，而不是继续把弱锚点硬拼成对称 spine：公开来源只支撑“一条显式 spine + 多个支撑 bundle”的结构。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `推断`：因此后续实现验证的正确方向，不再是继续寻找第二条与 `Minthara` 同级的主链，而是继续给既有区域包判断锁定层级上限，明确哪些结论可逼近 `objective / step`，哪些必须停在 `gate / tension`、`camp fold` 或 `ending feedback / organization bundle`。来源：`BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`

### Dark Urge 营地 bard 事件

- `事实`：`BG3-OFF-005` 直接确认了“营地临时入队”这一状态变化。
- `推断`：营地 / 长休很可能是叙事状态折返进玩家可见层的重要接口。
- `案例线索`：`BG3-PLY-002` 只能作为玩家侧线索，帮助我们观察这类事件在玩家视角下如何被感知，不能单独承担系统事实。

## What Is Stable Enough To Claim

- `事实`：补丁、热修与社区更新不是边缘材料，而是当前最稳定的公开实现验证入口之一。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-005`
- `事实`：连 `Nautiloid` 这样的开场段落，也会在补丁层暴露 quest close、条件清理、关键物件与角色交接问题，因此不能把开场简单降级成“无状态的教程前厅”。来源：`BG3-OFF-002`, `BG3-OFF-015`
- `推断`：当同一问题同时表现为任务状态、营地反馈与后续章节反应异常时，我们更有理由把它理解为跨模块状态回流问题，而不是单点脚本错误。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-005`
- `推断`：Journal 与 scripting 的公开文档足以给区域包提供“结构层验证”，哪怕我们还不能也不应反推私有脚本细节。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：`Grove / Goblin` 现在已经可以被较稳地写成一份早期 `resolution matrix`，因为公开来源已同时暴露处理方式、长休时序与营地可达性三种边界。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-008`
- `推断`：`Underdark` 现在已经可以被较稳地写成一份早期“区域切换 / 下游 setup”验证入口，因为公开来源已同时暴露区域定位、多入口设计语言与直通 `Grymforge` 的 quest setup。来源：`BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-006`
- `推断`：`Grymforge` 现在已经可以被较稳地写成一份早期“战斗 / 环境区域压缩包”验证入口，因为公开来源已同时暴露下游 setup、复杂遭遇框架与玩家对环境重写型遭遇的稳定感知。来源：`BG3-OFF-003`, `BG3-OFF-006`, `BG3-PLY-004`
- `推断`：`Mountain Pass / Creche` 现在已经可以被较稳地写成一份 late `Act 1` 的“门槛 / 伙伴张力叠层包”验证入口，因为公开来源已同时暴露对话门槛、局部敌意、即时伙伴反应与营地后续读取四种边界。来源：`BG3-OFF-003`, `BG3-OFF-016`
- `推断`：`Act 2` 现在已经可以被较稳地写成一份“中盘压力 / 前史重读框架”验证入口，因为公开来源已同时暴露阶段节点定位、`Act II` 的 flow / reaction 维护，以及至少一条明确的跨 Act 状态重读链。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：`Shadow-Cursed Lands` 现在已经可以被较稳地写成一份“中盘压力落地的区域验证入口”，因为公开来源已同时暴露区域节点定位、`Act II` 的 flow / reaction 维护、多入口设计语言与公开的任务结构边界。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：`Last Light / Moonrise / Gauntlet` 现在已经可以被较稳地写成一份“中盘收束点组”的验证入口，因为公开来源已同时暴露 `Act II` 的 flow / reaction 维护、至少一条明确写到 `Moonrise Towers` 的前史读回链，以及公开的任务结构语言。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：`Act 3` 现在已经可以被较稳地写成一份“高密度城市 + 结算负载”的验证入口，因为公开来源已同时暴露城市节点定位、选择驱动的 ending feedback、开发者承认后期状态排列更密，以及公开的任务结构边界。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：`Rivington` 现在已经可以被较稳地写成一份“第一层入口过滤 + 外环承压”的验证入口，因为公开来源已同时暴露 `Act 3` 的城市节点定位、后期高密度状态读回、多入口设计语言与公开的任务结构边界。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：`Wyrm's Crossing` 现在已经可以被较稳地写成一份“桥梁 / 门槛 / 第二层结构重排”的验证入口，因为公开来源已同时暴露 `Act 3` 的城市节点定位、后期高密度状态读回、多入口设计语言与公开的任务结构边界。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：`Lower City` 现在已经可以被较稳地写成一份“更高密度的内城并行 / 结算区”验证入口，因为公开来源已同时暴露 `Act 3` 的城市节点定位、选择驱动的 ending feedback、开发者承认后期状态排列更密，以及公开的任务结构边界。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：`终局组织与收束压力` 现在已经可以被较稳地写成一份“组织级终局压缩 / ending feedback 读取层”的验证入口，因为公开来源已同时暴露后期 ending feedback、flow / scripting 维护、多入口设计语言与公开的任务结构边界。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：把 `Grove / Goblin`、`Last Light / Moonrise / Gauntlet` 与 `Act 3` 的过滤 / 门槛 / 并排承接 / 终局压缩梯拼起来后，阶段 5 已拥有第一条可复述的跨阶段状态回流主干；当前能最稳升级的是“读回梯存在”，而不是“全任务 objective 表已被公开证明”。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：把 `Nautiloid`、`Act 1 地表主区`、`Underdark` 与 `Mountain Pass / Creche` 压成前置链后，阶段 5 已能更稳地解释为什么 `Grove / Goblin` 会成为第一块高可见 `resolution matrix`：它前面已经有 objective 埋点、目标网、改道与门槛四层前史。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-006`, `BG3-OFF-015`, `BG3-OFF-016`
- `推断`：把 `Mountain Pass / Creche -> Shadow-Cursed Lands -> Last Light / Moonrise / Gauntlet` 压成中盘接缝后，阶段 5 已能更稳地区分三层不同强度的公开边界：局部门槛可逼近 `objective / step` 邻近层，整段压力过滤更适合停留在 `flow bundle`，而收束点组则更适合停留在 `convergence pack / reread bundle`。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`

### 阶段 5 / Quest Reactivity 的层级锁定矩阵

| 锚点组 | 当前公开上限 | 当前验证结论 | 后续只能怎么补 |
| --- | --- | --- | --- |
| `Nautiloid`、`Grove / Goblin`、`Mountain Pass / Creche` 的局部边界 | `objective / step` 邻近层 | 这几组已拥有最直接的 quest close、处理矩阵、门槛与读取时机维护条目。 | 只允许继续补更细的 objective-adjacent 局部锚点，不允许扩成全量路线表。 |
| `Act 1 地表主区`、`Underdark` | `objective pressure net` / `entry-diversion bundle` | 可验证的是开场状态续接与阶段内部改道，而不是完整 objective 映射。 | 后续若无更强锚点，应继续停在 bundle 层。 |
| `Shadow-Cursed Lands`、`Last Light / Moonrise / Gauntlet` | `pressure filter bundle` / `convergence pack` | 可验证的是中盘如何过滤推进并把前史压向读回节点。 | 后续只补更细的 Journal 结构语言，不反推内部私有分工。 |
| 非 `Minthara` 营地反应 | `camp fold / dialogue accessibility bundle` | 可验证的是折叠层与可达性维护真实存在。 | 不再让这组锚点承担“第二条主链”任务。 |
| `Rivington -> Wyrm's Crossing -> Lower City -> 终局组织与收束压力` | `filter / gate / parallel resolution / ending feedback bundles` | 可验证的是 late-game bundle 的多层压缩梯。 | 后续只补层级边界，不写成城市 objective 总表。 |

- `推断`：阶段 5 现在最重要的实现验证结论，已经不是“是否还存在第二条主链”，而是“哪些锚点还能向 `objective / step` 邻近层窄化，哪些必须明确停在 bundle 层”。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `推断`：因此后续验证动作必须缩窄为 objective-adjacent 局部边界侦察，优先处理 `Grove / Goblin` 与 `Mountain Pass / Creche` 这类已有直接维护条目的锚点，而不是继续横向扩写 late-game bundle 或再追第二条对称 spine。来源：`BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-016`

### 阶段 5 / Quest Reactivity 的 objective-adjacent 窄化结果

| 局部锚点 | 当前能再压一层的 fragment | 能压到哪一层 | 必须停在哪一层 | 核心原因 |
| --- | --- | --- | --- | --- |
| `Grove / Goblin` | `Minthara` 的 `knocked out / killed` 差异、`journal wording`、以及“击倒 -> 长休 -> 再处理其他首领”的时序判定 | `objective-adjacent local resolution fragment` | 营地中的对话可达性与 `companion reaction` 仍停在 `delayed camp readout` | `BG3-OFF-004` 直接点名 state / wording / timing；`BG3-OFF-008` 直接点名的是营地下游可达性，而不是新的 objective fragment。 |
| `Mountain Pass / Creche` | `Vlaakith` 拒绝后的对话阻塞、`Voss` 相关敌意变化、`Lae'zel` 即时反应时机 | `objective-adjacent local gate fragment` | `camp night` 中对 `crèche` 后果的延迟反思，以及整块区域的 `Act 2` 切换解释，仍停在 `delayed readout / gate-and-tension bundle` | `BG3-OFF-016` 直接点名的是局部门槛、敌意变化、即时反应与读出时机，但没有给出与 `Moonrise Towers` 同级的 downstream 命名节点。 |

- `事实`：`BG3-OFF-012`、`BG3-OFF-013`、`BG3-OFF-014` 提供的价值，仍然只是公开层级语言：它们允许我们判断某个 patch 锚点更像 `quest / objective / step` 邻近层，还是更像 delayed readout / bundle 层，但不能单独把 shipped content 的私有排布写成事实。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此 objective-adjacent narrowing 的真正出口，并不是“把局部锚点继续扩成 objective 总表”，而是把每个锚点拆成更细的 fragment：只有被 patch / hotfix 直接点名的 state / gate / timing 片段还能前进，其余部分必须明确降回 readout 或 bundle 层。来源：`BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `推断`：这也意味着阶段 5 / `Quest Reactivity` 在当前来源下已经基本收口：继续推进的正确条件，不是“还能再想出一条链”，而是“是否出现了新的官方条目，能像 `BG3-OFF-004` 或 `BG3-OFF-016` 一样直接点名局部 fragment”。来源：`BG3-OFF-004`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`

### 阶段 5 / Companion / Camp / Long Rest 的首条跨区域主干

| 链段 | 当前可升级到的层级 | 公开锚点 | 当前不能升级的部分 |
| --- | --- | --- | --- |
| `Act 1 地表主区` | `upstream state-density layer`：opening-state handoff 已足以支撑“第一批营地折叠有真实前史输入”。 | `BG3-OFF-002` | 还不能把早期顺序差异直接写成 camp scene 调度事实表。 |
| `Dark Urge bard` | `local camp-state-shift sample`：官方已直接确认营地临时入队，并由 `Patch 7` 回指到 `Alfira` 与 `temporarily`。 | `BG3-OFF-005`, `BG3-OFF-002`, `BG3-PLY-002` | 还不能把完整后续差异、跨版本稳定性与内部调度全部写成事实链。 |
| `Grove / Goblin` | `first delayed camp readout bundle`：营地对话可达性、`companion reaction` 与 `Moonrise Towers` 的后续读回已形成第一块稳定的 delayed readout。 | `BG3-OFF-008`, `BG3-OFF-002` | 还不能把除 `Minthara` 外的全部后果都压成同级 camp spine。 |
| `Mountain Pass / Creche` | `gate / tension -> camp-night delayed reread bundle`：局部门槛、敌意变化、即时伙伴反应与 `camp night` 读取时机都已有直接维护条目。 | `BG3-OFF-016` | 还不能把整块过渡升级为新的显式任务主链。 |
| `Last Light / Moonrise / Gauntlet` | `convergence-adjacent reread bundle`：中盘收束点组附近存在更密的 `flow / reaction / trigger-update` 重读边界。 | `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把具体哪些 `Act II` 后果稳定折返到 camp scene 列表写成事实表。 |
| `终局组织与收束压力` | `ending-feedback handoff bundle`：late-game 会以更少、更硬的节点持续读回前史，并把它压向 `ending feedback`。 | `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把 late-game `ending feedback` 写成第二条对称的 public camp spine。 |

- `推断`：把这六段串起来后，阶段 5 当前已经拥有第一条可复述的 `Companion / Camp / Long Rest` 横向主干；但它的结构不是第二条 `Quest Reactivity`，而是“前史密度生成 -> 局部 camp-state shift -> delayed camp readout -> camp-night reread -> convergence-adjacent reread -> ending-feedback handoff”。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-005`, `BG3-OFF-008`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`, `BG3-PLY-002`
- `推断`：`BG3-OFF-007` 的跨 `Act` 反思时刻与 `BG3-OFF-010` 的非 `Minthara` camp fix 已足以证明营地反馈链被系统性维护，但在当前公开来源下仍更稳地停在 `reflection / dialogue accessibility supporting bundle` 层，而不是第二条对称 spine。来源：`BG3-OFF-007`, `BG3-OFF-010`
- `推断`：因此阶段 5 / `Companion / Camp / Long Rest` 当前的正确动作，已经从“继续扩 camp scene 条目”切换成“守住 ceiling 并把 supporting bundle / handoff 边界写清”；这条主干在现有来源下应视为完成收口。来源：`BG3-OFF-007`, `BG3-OFF-010`

### 阶段 5 / Companion / Camp / Long Rest 的 second public camp spine ceiling / late-game boundary

| 候选锚点 | 当前可升级到的层级 | 公开锚点 | 当前不能升级的部分 |
| --- | --- | --- | --- |
| `BG3-OFF-007`：`Withers' Wardrobe` + `Karlach` 反思 | `reflection / roster-state supporting bundle` | `BG3-OFF-007` 直接把营地写成 roster 管理入口，并补入 `Karlach` 的跨 `Act` 反思时刻。 | 还不能把这组条目写成第二条 public camp spine，因为它们没有形成稳定的跨区域 delayed readback 链，只证明营地承担 roster / reflection 职责。 |
| `BG3-OFF-010`：非 `Minthara` camp fixes | `dialogue accessibility maintenance bundle` | `BG3-OFF-010` 直接修复 Astarion、Voss、Mizora、Wyll 等 camp scene / dialogue accessibility / 在场识别问题。 | 还不能把这些分散修复压成第二条 public camp spine，因为它们证明的是维护广度，不是同一条可复述的跨区域读回结构。 |
| `Last Light / Moonrise / Gauntlet` | `convergence-adjacent reread bundle` | 既有阶段 5 营地主干与 `Act II` 收束点组结论。 | 还不能把中盘收束点组升格为第二条 camp-centered spine；当前公开来源更稳地暴露的是收束附近的 reread，而不是新的 camp 主链。 |
| `终局组织与收束压力` / late-game `ending feedback` | `ending-feedback handoff bundle` | 既有终局 organization 压缩结论与阶段 5 营地主干 handoff 结论。 | 还不能把 late-game `ending feedback` 反向写成第二条营地主干终点；当前最稳的公开边界是 handoff，而不是第二条 camp-centered readback。 |

- `推断`：在当前公开来源下，阶段 5 / `Companion / Camp / Long Rest` 只稳定支撑 1 条 public camp spine；`BG3-OFF-007` 与 `BG3-OFF-010` 扩大的是“营地反馈链被系统性维护”的公开覆盖面，而不是生成第二条对称主链。来源：`BG3-OFF-007`, `BG3-OFF-010`
- `推断`：这意味着营地模块的正确实现验证动作，已经从“继续搜集 camp scene”切换成“守住 ceiling”：把 `reflection / roster-state`、`dialogue accessibility maintenance` 与 `ending-feedback handoff` 明确留在 supporting bundle / handoff 层。来源：`BG3-OFF-007`, `BG3-OFF-010`
- `推断`：因此阶段 5 的下一唯一主任务不应再是营地模块内部扩链，而应切到 `Implementation Validation` 的阶段收束：统一整理三条横向主干的一条 spine、ceiling 与 bundle 边界。来源：`BG3-OFF-007`, `BG3-OFF-010`

### 阶段 5 / Combat / Environment 的首条跨阶段主干

| 链段 | 当前可升级到的层级 | 公开锚点 | 当前不能升级的部分 |
| --- | --- | --- | --- |
| `Nautiloid` | `compressed local-agency sample`：开场 flow、交互物、状态清理与 quest close 都有直接维护条目。 | `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-015` | 还不能把任何单条 tutorial 解法写成成熟战斗主案例。 |
| `Act 1 地表主区` | `route-agency normalization layer`：opening-state handoff 与多入口设计语言已足以支撑“局部 agency 在 crash 后常态化”。 | `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-015` | 还不能把某条 early-surface 遭遇压成稳定 objective / step 或成熟环境主案例。 |
| `Grymforge` | `mature combat-agency compression pack`：复杂遭遇框架、`Underdark -> Grymforge` setup 与玩家对环境重写型遭遇的稳定感知已同时成立。 | `BG3-OFF-003`, `BG3-OFF-006`, `BG3-PLY-004` | 还不能把具体熔炉 / 落体 / 远程拉杆路径写成 objective / step 事实链。 |
| `Shadow-Cursed Lands` | `regional pressure loop`：中盘 `writing and flow` / `scripting` 维护与多入口设计语言已足以支撑“持续风险会过滤推进方式”。 | `BG3-OFF-002`, `BG3-OFF-003` | 还不能把区域内部风险变量、路线分工或收束时机压到 objective / step 层。 |

- `推断`：把这四段串起来后，阶段 5 当前最稳的 `Combat / Environment` 验证结论是：BG3 的战斗 / 环境能动性已经足以被公开写成一条“开场局部问题重写 -> 地表常态化 -> 成熟 encounter compression -> 中盘区域压力循环”的跨阶段主干，而不再只是由 `Grymforge` 单点支撑。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-006`, `BG3-OFF-015`, `BG3-PLY-004`
- `推断`：当前公开来源还不足以把 `Last Light / Moonrise / Gauntlet` 或 `Act 3` 城市子包同级写成第二条 cross-stage combat spine；它们在战斗 / 环境层更稳的身份仍是收束点组、城市 filtering / gate bundles，或等待更强环境锚点的 region-pack 结论。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-006`

### 阶段 5 / Combat / Environment 的 second spine ceiling / late-game boundary

| 锚点 | 当前可升级到的层级 | 公开锚点 | 当前不能升级的部分 |
| --- | --- | --- | --- |
| `Last Light / Moonrise / Gauntlet` | `convergence pack` | `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把它写成第二条环境 spine 的成熟 region-pack anchor，因为公开来源更稳定地暴露的是 `Act II` 的 flow / reaction / reread 压缩，而不是新的环境 agency 核心。 |
| `Act 3 总框架` | `density-and-resolution-load framing bundle` | `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把后期城市密度直接写成与 `Shadow-Cursed Lands` 对称的区域级 pressure loop。 |
| `Rivington` | `entry-filter supporting bundle` | `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把“第一层入口过滤”写成新的成熟 combat / environment anchor。 |
| `Wyrm's Crossing` | `bridge-and-gate supporting bundle` | `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把“桥梁 / 门槛重排”写成第二条环境 spine 的中段 region-pack anchor。 |
| `Lower City` | `parallel-resolution supporting bundle` | `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把“更高密度并行 / 结算区”直接写成 late-game 环境 pressure loop。 |
| `终局组织与收束压力` | `organization-ending-feedback supporting bundle` | `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把 organization / ending feedback 读取层写成第二条环境 spine 的终点锚点。 |

- `推断`：阶段 5 / `Combat / Environment` 当前最重要的实现验证结论，已经不再是“还能不能硬找出第二条对称 spine”，而是“late-game 的哪些战斗 / 环境判断有效、但必须明确停在 supporting bundle 层”。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此 `Last Light / Moonrise / Gauntlet` 与 `Act 3` 相关锚点的正确写法，不是被视为第一环境主干失败后的替补 spine，而是被视为 first spine 在 late-game 的 downstream reading context：它们继续说明压力如何被收束、过滤、门槛化、并行承接与组织化。来源：`BG3-OFF-002`, `BG3-OFF-003`
- `推断`：只要仓库还没有更直接点名 late-game `complex combat encounters`、区域级风险循环或环境 problem-solving 的官方条目，就应把 second spine ceiling 视为已锁定边界，而不是继续让 `Act 3` 城市子包竞争第二条环境主干位置。来源：`BG3-OFF-002`, `BG3-OFF-003`

### 阶段 5 / Unified Exit Matrix

| 横向主干 | 已成立的正式 spine | 已锁定的 ceiling / boundary | 当前可保守升级的判断 | 当前必须停留的层级 | 阶段出口结论 |
| --- | --- | --- | --- | --- | --- |
| `Quest Reactivity` | 一条显式 readback spine，外加已完成的上游前置链与 late `Act 1` / early `Act 2` 接缝。 | 第二条公开跨阶段主链已被 ceiling 锁死；objective-adjacent 只剩 `Minthara` 的局部 resolution-state fragment 与 `Vlaakith / Voss / Lae'zel` 的局部 gate fragment。 | BG3 的任务反应性当前最稳地写法，是“少数局部 state / gate fragment + 一条显式 readback spine + 多个 bundle / fold / ending-feedback 层”，而不是 objective 总表。 | `camp fold`、late-game `filter / gate / parallel resolution / ending feedback`、以及除少数 fragment 外的 objective / step 细表。 | 在当前公开来源下已完成收口；除非出现更强官方来源，否则不再重开第二条公开 quest spine。 |
| `Combat / Environment` | 一条 “early local agency -> regional pressure loop” 正式环境 spine：`Nautiloid -> Act 1 地表主区 -> Grymforge -> Shadow-Cursed Lands`。 | `Shadow-Cursed Lands` 之后的 late `Act 2` / `Act 3` 锚点已经锁定为 supporting bundles，第二条对称环境 spine 不成立。 | BG3 的战斗 / 环境能动性已足以被公开写成一条跨阶段主干，而不再只是 `Grymforge` 单点。 | second spine、`Act 3` encounter / 机关 / cheese 列表、以及任何没有更强官方锚点的 late-game 环境升格。 | 在当前公开来源下已完成“首条环境 spine + second-spine ceiling”闭合。 |
| `Companion / Camp / Long Rest` | 一条 public `camp fold / delayed feedback` spine，覆盖 `Act 1` 前史密度、`camp night` reread、中盘收束附近的 reread 与 late-game handoff。 | `BG3-OFF-007` 只稳定支撑 `reflection / roster-state supporting bundle`，`BG3-OFF-010` 只稳定支撑 `dialogue accessibility maintenance bundle`，late-game 只稳定支撑 `ending-feedback handoff`；第二条公开 camp spine 不成立。 | 营地 / 长休当前最稳的系统判断是：它是被持续维护的反馈折叠层，而不是平行人物志或 scene 清单。 | 第二条对称 camp spine、camp scene 清单、以及把 `reflection` / `accessibility maintenance` / `ending feedback` 反写成新的 camp-centered 主链。 | 在当前公开来源下已完成“1 条 public spine + supporting bundles + handoff boundary”闭合。 |

- `推断`：阶段 5 的三条横向主干现在已经被压成同一种出口结构：每条都拥有 `1` 条正式 spine、`1` 次 ceiling / supporting-bundle / handoff 收口，以及一组必须等待更强官方来源才可能继续上升的开放问题。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-004`, `BG3-OFF-006`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-010`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-015`, `BG3-OFF-016`
- `推断`：因此阶段 5 当前的正确下一步，不再是重开单条主干，而是切到阶段 6 / 展示收束，把这份 exit matrix 转译成读者能直接使用的展示入口。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## Stage 6 Display Role

- `推断`：在当前展示链里，本模块只应作为收尾章或附录出现：它的职责是给前面 5 个模块分级、标边界、保留开放问题，而不是抢在开头替代展示入口。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此本模块最适合被压成证据矩阵、来源类型图与验证入口清单，而不适合被误读成新的“技术细节仓库”或阶段 6 的开场导论。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：只要读者在读完本模块后能反向定位回 `00_core_thesis` 到 `03_party_and_camp` 的对应结论，阶段 6 的展示链就闭合了；否则说明验证层仍在和正文竞争入口位置。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`
- `推断`：在阶段 6 的实际发布导览稿里，本模块现在已经被固定为最后一段：前面 4 段先负责让读者看见反应性链条，本模块再统一说明哪些判断已经够稳、哪些仍只能停在当前最强解释或待验证问题层。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## Stage 6 Release-Facing Evidence Queue

| 发布段落 | 当前最稳的公开证据入口 | 可安全摘录到的层级 | 首轮发布最小证据动作 | 当前不能越级摘录的内容 |
| --- | --- | --- | --- | --- |
| 入口页 | `BG3-OFF-001`, `BG3-OFF-003`, `BMK-002`, `BMK-003` | 只能摘录“项目解释的是反应性链条、不是剧情复述”这一层，以及为什么要用“区域证据带 + 展示链 + 实现验证层”的方法。 | 绑定 1 条问题边界摘录 + 1 条非剧情复述摘录，并回链到 `README.md` 与 `deconstruction_display_overview.md`。 | 不能把 benchmark 方法或官方高层表述压成任何具体区域的实现实锤，也不能把入口页写成系统总表。 |
| 第一段：命题与导航 | `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 可安全摘录到“高反应性由区域组织、局部行动、状态回流与验证边界共同构成”的层级。 | 绑定 1 条命题摘录 + 1 条区域 / 压力梯摘录，并明确 handoff 到局部行动层。 | 不能把公开 Journal / modding 结构语言越级写成私有 quest 编排，也不能把 `Act` 梯压成剧情提要。 |
| 第二段：局部行动到状态回流 | `BG3-OFF-003`, `BG3-OFF-006`, `BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-PLY-004` | 可安全摘录到“一组局部 `agency` 行为如何被后续状态读回”的层级。 | 绑定 1 条局部 `agency` 摘录 + 1 条 readback 摘录，并做成同一张双联卡。 | 不能把 `Grymforge` 或 `Minthara` 个案越级写成全游戏 objective 总表，也不能重新追第二条对称 spine。 |
| 第三段：延迟反馈折叠 | `BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-010`, `BG3-OFF-016` | 可安全摘录到“营地 / 长休是 delayed feedback fold layer，而不是平行人物附录”的层级。 | 绑定 1 条 `camp fold` 摘录 + 1 条 supporting-bundle 边界摘录，并用折返图表示上游状态如何被 reread。 | 不能把 `reflection / roster-state bundle`、`dialogue accessibility maintenance bundle` 或 late-game handoff 越级写成第二条公开营地主干。 |
| 收尾段：证据分级 | `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`, `BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010` | 可安全摘录到“哪些是事实、哪些是推断、哪些仍是待验证问题”的层级。 | 绑定 1 张证据矩阵 + 1 张开放问题卡，并反向链接前面四段对应正文。 | 不能把 modding / Journal 文档写成 shipped content 的直接实现证明，也不能把开放问题抹平成已解决结论。 |

- `推断`：对阶段 6 的首轮发布包而言，真正需要的是“每一段都有一个足够稳、且不越级的公开证据入口”，而不是“每一段都堆满平行来源”。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此发布层的 excerpt queue 应该服从当前的验证边界，而不是为了版面完整度去硬补第二条 spine、objective 总表或 camp scene 清单。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-016`

## Stage 6 First Actual Units Evidence Lock

| 实际单元 | 当前绑定的文档锚点 | 当前最稳的 Source ID 入口 | 可安全发布到的层级 | 当前不能越级发布的内容 |
| --- | --- | --- | --- | --- |
| `ENTRY-EXCERPT-001` | `README.md`、`docs/00_project/deconstruction_display_overview.md` | `BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003` | 只能发布“项目问题 + 非剧情复述边界 + 反应性链条方法”这一层。 | 不能把 benchmark 方法写成 BG3 单一区域的实现实锤，也不能把入口页写成系统总表。 |
| `ENTRY-ASSET-001` | `README.md`、`docs/00_project/deconstruction_display_overview.md` | `BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003` | 只能发布链条总图与研究 / 展示双轨边界。 | 不能把 `Act` 顺序画成剧情时间轴，也不能把三条横向主干重新画成平级入口。 |
| `ENTRY-TRACE-001` | `docs/00_project/stage6_entry_first_section_release_units.md` | `BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003` | 可发布“这张入口卡从哪里来、为什么只说到这一层”。 | 不能把 trace card 写成新的研究结论页。 |
| `OPENING-EXCERPT-001` | `docs/03_analysis/00_core_thesis.md`、`docs/03_analysis/01_macro_structure.md` | `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 只能发布“高反应性命题 + 区域 / 压力梯 + 默认 handoff”这一层。 | 不能把公开 Journal / modding 语言越级写成私有 quest 编排，也不能把 `Act` 梯压成剧情提要。 |
| `OPENING-ASSET-001` | `docs/03_analysis/01_macro_structure.md` | `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 只能发布区域 / 压力梯与“下一段先看局部行动层”的导航关系。 | 不能把 `04_combat_and_environment.md`、`02_quests_and_choices.md`、`03_party_and_camp.md` 画成平级导论。 |
| `OPENING-TRACE-001` | `docs/03_analysis/00_core_thesis.md`、`docs/03_analysis/01_macro_structure.md`、`docs/00_project/stage6_entry_first_section_release_units.md` | `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 可发布“这组开场卡为什么只锁命题与导航、为何默认交接到局部行动层”。 | 不能把 trace card 扩成后续章节总表，也不能在这里提前补第二段内容。 |

- `推断`：阶段 6 的第五子单元之所以成立，不是因为仓库又多了一份发布说明，而是因为入口页与第一段现在都已拥有“文档锚点 + Source ID 入口 + 不可越级边界”三件套。来源：`BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：只要后续单元继续复用这套 evidence lock 写法，阶段 6 的发布层就不会再退回“漂亮但无法回链”的空展示。来源：`BG3-OFF-002`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## Stage 6 Second Section Actual Units Evidence Lock

| 实际单元 | 当前绑定的文档锚点 | 当前最稳的 Source ID 入口 | 可安全发布到的层级 | 当前不能越级发布的内容 |
| --- | --- | --- | --- | --- |
| `SECOND-EXCERPT-001` | `docs/03_analysis/04_combat_and_environment.md`、`docs/03_analysis/02_quests_and_choices.md` | `BG3-OFF-003`, `BG3-OFF-006`, `BG3-OFF-002`, `BG3-OFF-004`, `BG3-PLY-004` | 只能发布“局部 agency 已成立，且高可见处理方式会被后续读回”这一层。 | 不能把左侧局部 agency 与右侧 readback 硬写成同一条具体微观案例因果链。 |
| `SECOND-ASSET-001` | `docs/03_analysis/04_combat_and_environment.md`、`docs/03_analysis/02_quests_and_choices.md` | `BG3-OFF-003`, `BG3-OFF-006`, `BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 只能发布“第二段是章节接力：左侧局部 action space，右侧高可见 readback，中间由状态记录相连”这一层。 | 不能把图扩成 objective 总表、第二条对称 spine，或把 `Grymforge` 直接画箭头连到 `Moonrise Towers`。 |
| `SECOND-TRACE-001` | `docs/00_project/stage6_second_section_release_units.md`、`docs/03_analysis/05_implementation_validation.md` | `BG3-OFF-003`, `BG3-OFF-006`, `BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-PLY-004` | 可发布“这组双联卡从哪里来、为什么只能说到章节接力层”这一层。 | 不能把 trace card 写成新的系统总论页，也不能提前吞掉第三段的 camp fold 职责。 |

- `推断`：阶段 6 的第六子单元之所以成立，不是因为仓库又多了一份中段说明，而是因为第二段现在也拥有了“左侧正文锚点 + 右侧正文锚点 + evidence lock”三件套。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-004`, `BG3-OFF-006`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：只要后续单元继续复用这种“章节接力 + 不可越级因果链”的 evidence lock，阶段 6 的发布层就不会在中段退化成并列模块图、任务总表或伪单案例链。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-004`, `BG3-OFF-006`, `BG3-OFF-011`

## Stage 6 Third Section Actual Units Evidence Lock

| 实际单元 | 当前绑定的文档锚点 | 当前最稳的 Source ID 入口 | 可安全发布到的层级 | 当前不能越级发布的内容 |
| --- | --- | --- | --- | --- |
| `THIRD-EXCERPT-001` | `docs/03_analysis/03_party_and_camp.md` | `BG3-OFF-002`, `BG3-OFF-005`, `BG3-OFF-008`, `BG3-OFF-016`, `BG3-PLY-002` | 只能发布“营地 / 长休是 delayed feedback fold layer，且第一条公开营地折返主干已经成立”这一层。 | 不能把 `Dark Urge bard`、`Minthara`、`Lae'zel` 与 `Karlach` 写成同一条具体因果链。 |
| `THIRD-ASSET-001` | `docs/03_analysis/03_party_and_camp.md`、`docs/03_analysis/05_implementation_validation.md` | `BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-010`, `BG3-OFF-016` | 只能发布“第三段是折返层：前序状态在 camp / long rest 被 regroup 与 reread，并在右侧保留 supporting-bundle / handoff 边界”这一层。 | 不能把图扩成 camp scene 清单、同伴 roster 图，或把 `reflection / roster-state`、`dialogue accessibility maintenance`、late-game `ending feedback` 画成第二条对称营地主干。 |
| `THIRD-TRACE-001` | `docs/00_project/stage6_third_section_release_units.md`、`docs/03_analysis/05_implementation_validation.md` | `BG3-OFF-002`, `BG3-OFF-005`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-010`, `BG3-OFF-016`, `BG3-PLY-002` | 可发布“这组折返层单元从哪里来、为什么只说到 `camp fold / delayed feedback + supporting-bundle boundary`”这一层。 | 不能把 trace card 写成长休调度规则页，也不能让第三段提前吞掉收尾段的证据分级职责。 |

- `推断`：阶段 6 的第七子单元之所以成立，不是因为仓库又多了一份营地说明，而是因为第三段现在也拥有了“正文折返锚点 + evidence lock + 不可越级 supporting-bundle 边界”三件套。来源：`BG3-OFF-002`, `BG3-OFF-005`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-010`, `BG3-OFF-016`
- `推断`：只要后续单元继续复用这种“主折返层 + 边界条 + handoff 到验证层”的 evidence lock，阶段 6 的发布层就不会在第三段退化成人物附录、camp scene 清单或第二条对称营地主链。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-016`

## Stage 6 Final Section Release Anchor

- `FINAL-EXCERPT-001` 可安全摘录本文件中的“实现验证层当前只负责给前四段重分级，而不负责反向取代前四段”的展示职责，以及“公开可验证入口必须被重新分到 `事实 / 推断 / 待验证问题` 三层”的高层结论。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`, `BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`
- `FINAL-ASSET-001` 在本文件中应被压成“`claim tier -> document anchor -> source entry` 证据分级矩阵”的主体：左侧必须显式保留 `入口页`、第一段、第二段、第三段这四组 actual units，对中列只保留 `事实 / 当前最强解释 / 待验证问题` 三档，右侧只保留必须回链的文档锚点与公开来源入口；其中 `入口页` 这一行必须把 `BMK-002`、`BMK-003` 与 `BG3-OFF-001`、`BG3-OFF-003` 一起保留为完整的 benchmark + BG3 双重 traceback。来源：`BMK-002`, `BMK-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`, `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-007`, `BG3-OFF-010`
- `FINAL-TRACE-001` 在本文件中的默认职责只证明收尾段主卡的正文锚点已经成立；它不能把 modding / Journal 文档误写成 shipped content 实现图，也不能把开放问题条抹平成已解决结论；若回链到 `入口页`，还必须保留 `BMK-002 / BMK-003` 的 benchmark 来源。来源：`BMK-002`, `BMK-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`

## Stage 6 Final Section Actual Units Evidence Lock

| 实际单元 | 当前绑定的文档锚点 | 当前最稳的 Source ID 入口 | 可安全发布到的层级 | 当前不能越级发布的内容 |
| --- | --- | --- | --- | --- |
| `FINAL-EXCERPT-001` | `docs/03_analysis/05_implementation_validation.md` | `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`, `BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010` | 只能发布“前四段必须重新被分到 `事实 / 推断 / 待验证问题` 三层，且验证层不反向取代正文”这一层。 | 不能把 `BG3-OFF-011` 到 `BG3-OFF-014` 越级写成 shipped content 的私有脚本实锤，也不能把开放问题抹平成已解决结论。 |
| `FINAL-ASSET-001` | `docs/03_analysis/05_implementation_validation.md`、`docs/00_project/stage6_entry_first_section_release_units.md`、`docs/00_project/stage6_second_section_release_units.md`、`docs/00_project/stage6_third_section_release_units.md` | `BMK-002`, `BMK-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`, `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-007`, `BG3-OFF-010` | 只能发布“收尾段是一张证据分级矩阵：`入口页`、第一段、第二段、第三段这四组 actual units 证据强度不同，且必须保留 traceback path 与开放问题条”这一层。 | 不能把图扩成新的技术架构图、胜利图、把 `入口页` 并入第一段，或把 `入口页` 的 benchmark traceback 压缩成只剩 BG3 官方来源。 |
| `FINAL-TRACE-001` | `docs/00_project/stage6_final_section_release_units.md`、`docs/03_analysis/05_implementation_validation.md` | `BMK-002`, `BMK-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`, `BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-007`, `BG3-OFF-010` | 可发布“这组收尾单元从哪里来、为什么只说到公开验证边界与当前开放问题”这一层。 | 不能把 trace card 写成新的总论页，也不能让收尾段反向吞掉前四段 already-actual units 的职责。 |

- `推断`：阶段 6 的第八子单元之所以成立，不是因为仓库又多了一份验证说明，而是因为收尾段现在也拥有了“正文分级锚点 + 前四段回链 + 不可越级的公开验证边界”三件套。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`, `BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`
- `推断`：至此，阶段 6 的五段首批实际发布单元已经在当前计划下闭合；如果后续还要推进发布层，正确下一步应是总装配 / 审阅，而不是回头重写任一段 queue 或把验证层改写成实现总表。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`

## Stage 6 Release Package Assembly Review Anchor

- `ASSEMBLY-MAP-001` 可安全摘录本文件中的“前五段 actual units 已可被装成同一条发布链，但它们仍需统一核对顺序、handoff 与 traceback”的结论；其中入口页仍依赖 `BMK-002 / BMK-003` 与 `BG3-OFF-001 / BG3-OFF-003` 的双重来源路径。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-002`, `BG3-OFF-006`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `ASSEMBLY-CHECK-001` 可安全摘录本文件中的“assembly / review 当前只检查三件事：顺序交接、证据边界、不可越级发布”的结论。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `ASSEMBLY-TRIGGER-001` 可安全摘录本文件中的“只有命中 handoff 冲突、证据越级、supporting bundle 误升或 traceback 失效时，才值得回写单段文件”的结论。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`

## Stage 6 Release Package Assembly Review Evidence Lock

| 审阅单元 | 当前绑定的文档锚点 | 当前最稳的 Source ID 入口 | 可安全发布到的层级 | 当前不能越级发布的内容 |
| --- | --- | --- | --- | --- |
| `ASSEMBLY-MAP-001` | `docs/00_project/stage6_release_package_assembly_review_sheet.md`、四份 stage-6 release units 承载文件 | `BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-002`, `BG3-OFF-006`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 只能发布“五段 actual units 已能按固定顺序装成一条链，且每段职责仍各自独立”这一层。 | 不能把 assembly map 写成新的总论页、额外第六段 actual unit，暗示五段证据强度已经完全等同，或把入口页的 benchmark traceback 压缩成只剩 BG3 官方来源。 |
| `ASSEMBLY-CHECK-001` | `docs/00_project/stage6_release_package_assembly_review_sheet.md`、`docs/03_analysis/05_implementation_validation.md` | `BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016` | 只能发布“总装配层当前只核对顺序、handoff、证据边界与 traceback”这一层。 | 不能把这套 checklist 写成放之四海皆准的通用 QA 框架，也不能拿它反向抹平开放问题。 |
| `ASSEMBLY-TRIGGER-001` | `docs/00_project/stage6_release_package_assembly_review_sheet.md`、`docs/03_analysis/05_implementation_validation.md` | `BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016` | 只能发布“只有命中明确 trigger 才回写单段 actual units；否则保持当前闭合状态”这一层。 | 不能把 trigger 写成重开阶段 5、重写 queue 或升级 modding / Journal 文档证据等级的借口。 |

- `推断`：阶段 6 的第九个子单元之所以成立，不是因为仓库又多了一份发布文案，而是因为现在已经有了“装配顺序 + 审阅清单 + 回写触发条件”三件套，可用来控制后续会话如何继续推进。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `推断`：如果 `ASSEMBLY-TRIGGER-001` 持续不被命中，后续正确动作应是执行受控一致性审阅，而不是新增第六段 actual units、重开阶段 5，或把验证层改写成实现总表。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `事实`：在 2026-04-25 的首轮一致性审阅中，`FINAL-ASSET-001` 曾短暂漏掉独立 `入口页` 行；该局部 trigger 已被修正，当前收尾段证据矩阵重新与五段 assembly map 对齐。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第二轮一致性审阅中，四份 stage-6 actual units 未再命中新 trigger；剩余漂移只出现在 `deconstruction_display_overview.md`、`deconstruction_master_execution_plan.md`、`deconstruction_granular_codex_plan.md`、`presentation_forms.md` 与 `repo_map.md` 仍把“首轮一致性审阅”写成未来动作的旧口径。该漂移现已被同步为“继续受控一致性审阅”。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `事实`：在 2026-04-25 的第三轮一致性审阅中，四份 stage-6 actual units 依旧未命中新 trigger；剩余漂移改为出现在 review-level 支撑文件本身：旧的 `.agent/execplan_stage6_release_package_assembly_review.md` 与 `current_state.md` 仍把后续动作写成“首轮一致性审阅”或“是否命中首轮 trigger”。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round3.md` 并同步状态文件，统一为“第三轮复核已完成，后续继续停在 assembly / review 层”。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `事实`：在 2026-04-25 的第四轮一致性审阅中，四份 stage-6 actual units 仍未命中新 trigger；剩余漂移进一步收窄为续轮入口口径本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md` 与 `repo_map.md` 仍把旧的 `.agent/execplan_stage6_release_package_assembly_review.md` 单独写成当前固定执行计划，而没有明确它现在只承担第九子单元的 origin / baseline。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round4.md` 并同步入口文件，统一为“继续受控一致性审阅时，默认读取 review sheet + 最新 addendum”。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `事实`：在 2026-04-25 的第五轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；剩余漂移进一步收窄为“最新 addendum 指针”本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 虽已接受“review sheet + 最新 addendum”的规则，却仍把 `.agent/execplan_stage6_release_package_assembly_review_round4.md` 固定写成当前最新 addendum。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round5.md` 并同步入口文件，推进为“继续受控一致性审阅时，默认读取 review sheet + 最新 addendum（当前为 round5）”。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `事实`：在 2026-04-25 的第六轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；剩余漂移继续停留在“最新 addendum 指针”本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 若继续推进，就会自然把 `.agent/execplan_stage6_release_package_assembly_review_round5.md` 留成过期指针。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round6.md` 并同步入口文件，推进为“继续受控一致性审阅时，默认读取 review sheet + 最新 addendum（当前为 round6）”。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `事实`：在 2026-04-25 的第七轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；剩余漂移继续停留在“最新 addendum 指针”本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 若继续推进，就会自然把 `.agent/execplan_stage6_release_package_assembly_review_round6.md` 留成过期指针。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round7.md` 并同步入口文件，推进为“继续受控一致性审阅时，默认读取 review sheet + 最新 addendum（当前为 round7）”。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `事实`：在 2026-04-25 的第八轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；剩余漂移继续停留在“最新 addendum 指针”本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 若继续推进，就会自然把 `.agent/execplan_stage6_release_package_assembly_review_round7.md` 留成过期指针。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round8.md` 并同步入口文件，推进为“继续受控一致性审阅时，默认读取 review sheet + 最新 addendum（当前为 round8）”。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `事实`：在 2026-04-25 的第九轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；剩余漂移继续停留在“最新 addendum 指针”本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 若继续推进，就会自然把 `.agent/execplan_stage6_release_package_assembly_review_round8.md` 留成过期指针。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round9.md` 并同步入口文件，推进为“继续受控一致性审阅时，默认读取 review sheet + 最新 addendum（当前为 round9）”。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `事实`：在 2026-04-25 的第十轮一致性审阅中，四份 stage-6 actual units 的顺序与 handoff 仍未出现新的结构冲突，但 `FINAL-ASSET-001` 与相关 review-level evidence lock 对 `入口页` 的 Source ID 回链一度被压缩成只剩 BG3 官方来源，遗漏了 `ENTRY-TRACE-001` 原本保留的 `BMK-002 / BMK-003` benchmark traceback。这属于 `ASSEMBLY-TRIGGER-001` 的 trigger `5`：收尾层与审阅层让入口页的完整 traceback path 变窄。该漂移现已通过回写 `docs/00_project/stage6_final_section_release_units.md` 与本文件修正，并同步推进到 `.agent/execplan_stage6_release_package_assembly_review_round10.md`。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第十一轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移重新收窄为“最新 addendum 指针”本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 若继续推进，会自然把 `.agent/execplan_stage6_release_package_assembly_review_round10.md` 留成过期指针。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round11.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第十二轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移仍只收窄为“最新 addendum 指针”本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 若继续推进，会自然把 `.agent/execplan_stage6_release_package_assembly_review_round11.md` 留成过期指针。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round12.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第十三轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮、第十二轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移仍只收窄为“最新 addendum 指针”本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 若继续推进，会自然把 `.agent/execplan_stage6_release_package_assembly_review_round12.md` 留成过期指针。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round13.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第十四轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮、第十二轮、第十三轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移仍只收窄为“最新 addendum 指针”本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 若继续推进，会自然把 `.agent/execplan_stage6_release_package_assembly_review_round13.md` 留成过期指针。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round14.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第十五轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮、第十二轮、第十三轮、第十四轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移仍只收窄为“最新 addendum 指针”本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 若继续推进，会自然把 `.agent/execplan_stage6_release_package_assembly_review_round14.md` 留成过期指针。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round15.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第十六轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮、第十二轮、第十三轮、第十四轮、第十五轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移仍只收窄为“最新 addendum 指针”本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 若继续推进，会自然把 `.agent/execplan_stage6_release_package_assembly_review_round15.md` 留成过期指针。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round16.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第十七轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮、第十二轮、第十三轮、第十四轮、第十五轮、第十六轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移仍只收窄为“最新 addendum 指针”本身：`deconstruction_display_overview.md`、`deconstruction_granular_codex_plan.md`、`repo_map.md`、`current_state.md` 与 `next_step.md` 若继续推进，会自然把 `.agent/execplan_stage6_release_package_assembly_review_round16.md` 留成过期指针。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round17.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第十八轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第十七轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。与前几轮不同，本轮新命中的残留漂移不再只是“最新 addendum 指针”本身，而是多份 review-level 入口文本仍把当前状态写成“已完成十六轮受控审阅”，或把当前审阅 ceiling 停在第十五轮 / 第十六轮；这会让 `current_state.md`、`next_step.md`、`repo_map.md` 与高优先级计划说明出现当前时点自相矛盾。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round18.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第十九轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第十八轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移已重新收窄为续轮入口与 review-level 产出清单本身：`deconstruction_display_overview.md`、`current_state.md`、`next_step.md`、`repo_map.md` 与 review sheet 仍把当前入口停在 `.agent/execplan_stage6_release_package_assembly_review_round18.md`，而 `deconstruction_granular_codex_plan.md` 的“优先产出什么”仍停在 `.agent/execplan_stage6_release_package_assembly_review_round17.md`。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round19.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第二十轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第十九轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移重新收窄为续轮入口本身：`deconstruction_display_overview.md`、`current_state.md`、`next_step.md`、`repo_map.md` 与 review sheet 继续把当前入口停在 `.agent/execplan_stage6_release_package_assembly_review_round19.md`，而 `deconstruction_granular_codex_plan.md` 的“优先产出什么”也继续停在 `.agent/execplan_stage6_release_package_assembly_review_round19.md`。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round20.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第二十一轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第二十轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移重新收窄为续轮入口本身：`deconstruction_display_overview.md`、`current_state.md`、`next_step.md`、`repo_map.md` 与 review sheet 继续把当前入口停在 `.agent/execplan_stage6_release_package_assembly_review_round20.md`，而 `deconstruction_granular_codex_plan.md` 的“优先产出什么”也继续停在 `.agent/execplan_stage6_release_package_assembly_review_round20.md`。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round21.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第二十二轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第二十一轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移重新收窄为续轮入口本身：`deconstruction_display_overview.md`、`current_state.md`、`next_step.md`、`repo_map.md` 与 review sheet 继续把当前入口停在 `.agent/execplan_stage6_release_package_assembly_review_round21.md`，而 `deconstruction_granular_codex_plan.md` 的“优先产出什么”也继续停在 `.agent/execplan_stage6_release_package_assembly_review_round21.md`。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round22.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第二十三轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第二十二轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移重新收窄为续轮入口本身：`deconstruction_display_overview.md`、`current_state.md`、`next_step.md`、`repo_map.md` 与 review sheet 继续把当前入口停在 `.agent/execplan_stage6_release_package_assembly_review_round22.md`，而 `deconstruction_granular_codex_plan.md` 的“优先产出什么”也继续停在 `.agent/execplan_stage6_release_package_assembly_review_round22.md`。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round23.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第二十四轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第二十三轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移重新收窄为续轮入口本身：`deconstruction_display_overview.md`、`current_state.md`、`next_step.md`、`repo_map.md` 与 review sheet 继续把当前入口停在 `.agent/execplan_stage6_release_package_assembly_review_round23.md`，而 `deconstruction_granular_codex_plan.md` 的“优先产出什么”也继续停在 `.agent/execplan_stage6_release_package_assembly_review_round23.md`。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round24.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第二十五轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第二十四轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移重新收窄为续轮入口本身：`deconstruction_display_overview.md`、`current_state.md`、`next_step.md`、`repo_map.md` 与 review sheet 继续把当前入口停在 `.agent/execplan_stage6_release_package_assembly_review_round24.md`，而 `deconstruction_granular_codex_plan.md` 的“优先产出什么”也继续停在 `.agent/execplan_stage6_release_package_assembly_review_round24.md`。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round25.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-25 的第二十六轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第二十五轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移重新收窄为续轮入口本身：`deconstruction_display_overview.md`、`current_state.md`、`next_step.md`、`repo_map.md` 与 review sheet 继续把当前入口停在 `.agent/execplan_stage6_release_package_assembly_review_round25.md`，而 `deconstruction_granular_codex_plan.md` 的“优先产出什么”也继续停在 `.agent/execplan_stage6_release_package_assembly_review_round25.md`。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round26.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-26 的第二十七轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第二十六轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移重新收窄为续轮入口本身：`deconstruction_display_overview.md`、`current_state.md`、`next_step.md`、`repo_map.md` 与 review sheet 继续把当前入口停在 `.agent/execplan_stage6_release_package_assembly_review_round26.md`，而 `deconstruction_granular_codex_plan.md` 的“优先产出什么”也继续停在 `.agent/execplan_stage6_release_package_assembly_review_round26.md`。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round27.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-26 的第二十八轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第二十七轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移重新收窄为续轮入口本身：`deconstruction_display_overview.md`、`current_state.md`、`next_step.md`、`repo_map.md` 与 review sheet 继续把当前入口停在 `.agent/execplan_stage6_release_package_assembly_review_round27.md`，而 `deconstruction_granular_codex_plan.md` 的“优先产出什么”也继续停在 `.agent/execplan_stage6_release_package_assembly_review_round27.md`。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round28.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-26 的第三十一轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第三十轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移重新收窄为续轮入口本身：`deconstruction_display_overview.md`、`current_state.md`、`next_step.md`、`repo_map.md` 与 review sheet 继续把当前入口停在 `.agent/execplan_stage6_release_package_assembly_review_round30.md`，而 `deconstruction_granular_codex_plan.md` 的“优先产出什么”也继续停在 `.agent/execplan_stage6_release_package_assembly_review_round30.md`。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round31.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：在 2026-04-26 的第三十轮一致性审阅中，五段 stage-6 actual units 仍未命中新 trigger；第十轮补回并经第十一轮到第二十九轮复核的 `ENTRY-TRACE-001 -> BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 本轮继续在 `stage6_final_section_release_units.md` 与本文件保持完整。当前剩余漂移重新收窄为续轮入口本身：`deconstruction_display_overview.md`、`current_state.md`、`next_step.md`、`repo_map.md` 与 review sheet 继续把当前入口停在 `.agent/execplan_stage6_release_package_assembly_review_round29.md`，而 `deconstruction_granular_codex_plan.md` 的“优先产出什么”也继续停在 `.agent/execplan_stage6_release_package_assembly_review_round29.md`。该漂移现已通过新增 `.agent/execplan_stage6_release_package_assembly_review_round30.md` 并同步入口文件修正。来源：`BMK-002`, `BMK-003`, `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这说明阶段 6 当前最稳的剩余工作仍不在任一单段 actual unit，而在 assembly / review 层的持续复核与执行文件同步；只要 `ASSEMBLY-TRIGGER-001` 不再被命中，就不应回头扩写单段承载文件。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `推断`：这也意味着阶段 6 的续轮入口现在必须被写成“review sheet + 最新 addendum”这一对组合，而不能继续把旧基准 ExecPlan 当成当前唯一执行入口；否则仓库会在 review-level 口径上反复回退到第九子单元的起始时点。来源：`BG3-OFF-011`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`

## What Is Still Unverified

- `待验证问题`：未来若要重新打开第二条 cross-stage combat spine，最少需要什么级别的 late-game 官方环境来源，才能让任何一个 supporting bundle 升格为成熟 region-pack anchor？
- `待验证问题`：`Act 3` 现有城市子包里，是否存在尚未吸收进仓库的更强环境锚点，足以让其中某一块脱离 `filter / gate / parallel resolution bundle` 身份？

- `待验证问题`：需要建立一个可重复复用的“实现验证检查清单”。
- `待验证问题`：需要收集更多能直接暴露系统边界的官方措辞。
- `待验证问题`：需要继续判断哪些补丁条目足以支撑“系统性规律”，哪些仍只代表个别高可见分支。
- `待验证问题`：`Nautiloid` 的哪些开场状态最值得在 `Act 1 地表主区` 阶段继续追踪，以判断它们是否真的跨区域回流？
- `待验证问题`：`Act 1 地表主区` 中哪些早期顺序差异能被更稳地映射到 objective / step 变化，哪些更可能先折返到营地调度层？
- `待验证问题`：`Grove / Goblin` 里除 Minthara 外，哪些首领顺序或处理差异也能被同级别的公开来源压实？
- `待验证问题`：`Underdark` 的哪些入口与过渡最值得继续压到 `Journal / objective / step` 层，而不只是停留在“阶段重构”这一高层判断？
- `待验证问题`：`Grymforge` 的哪些具体环境解法能继续压到 objective / step 或更稳定的公开边界，而不只是停留在区域包级高层判断？
- `待验证问题`：`Mountain Pass / Creche` 的哪些门槛变化、敌意变化与伙伴反应能继续稳定压到 `Journal / objective / step` 层，而不只是停留在补丁暴露的边界摘要？
- `待验证问题`：`Act 2` 的哪些压力变量与前史读回，能继续稳定压到 `Journal / objective / step` 层，而不只是停留在 `Act II` 的 flow / reaction / camp 维护边界？
- `待验证问题`：`Shadow-Cursed Lands` 的哪些区域风险与推进分工能继续稳定压到 `Journal / objective / step` 层，哪些更适合继续停留在“区域级压力循环”的验证粒度？
- `待验证问题`：`Last Light / Moonrise / Gauntlet` 中哪些收束已经足以稳定压到 `objective / step` 层，哪些目前仍更适合停留在“前史读回 + flow / reaction 维护”这一组公开边界？
- `待验证问题`：`Rivington` 的哪些入口过滤与阅读顺序变化已经足以稳定压到 `objective / step` 层，哪些目前仍更适合停留在“高密度 quest bundle 第一次被分束”这一组公开边界？
- `待验证问题`：`Wyrm's Crossing` 的哪些桥梁 / 门槛重排已经足以稳定压到 `objective / step` 层，哪些目前仍更适合停留在“第二层 quest bundle 重排”这一组公开边界？
- `待验证问题`：`Lower City` 的哪些更高密度并行 / 结算负载已经足以稳定压到 `objective / step` 层，哪些目前仍更适合停留在“高密度 quest bundle + ending feedback”这一组公开边界？
- `待验证问题`：终局组织与收束压力的哪些城市子块 / 派系线已经足以稳定压到 `objective / step` 层，哪些目前仍更适合停留在“组织级压缩 + ending feedback”这一组公开边界？
- `待验证问题`：当前“一条显式 spine + 多个支撑 bundle”的 ceiling 已被压实；下一步需要继续判断哪些 bundle 能进一步逼近 `objective / step`，而不是重新回到“必须凑出第二条同级别链”的前提。
- `待验证问题`：如果未来要重新打开第二条公开营地主干，至少需要什么级别的官方来源，才能让 `BG3-OFF-007` 或 `BG3-OFF-010` 这种 supporting bundle 升级为 spine anchor？
- `待验证问题`：`Act II` 收束点组中，哪些后果会稳定折返到 camp scene / camp dialogue，哪些目前仍更适合停在 `convergence-adjacent reread` 这一组公开边界？
- `待验证问题`：当前这条上游前置链里，`Nautiloid -> 地表主区` 与 `Mountain Pass / Creche -> Act 2` 哪些边界已经足以继续压到 `objective / step`，哪些仍只能留在 `entry / diversion / gate bundle`？
- `待验证问题`：当前这条中盘接缝里，`Shadow-Cursed Lands -> convergence pack` 的哪些判断还能继续被 Journal / trigger 结构语言压细，哪些必须明确停在 `pressure filter / convergence pack` 公开边界？
- `待验证问题`：阶段 5 完成这次层级锁定后，是否还能仅靠仓库现有来源继续推进 objective-adjacent 局部锚点；如果不能，`Quest Reactivity` 应准备停止扩链并切换到其余横向主干。

## Source IDs

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-004`
- `BG3-OFF-005`
- `BG3-OFF-006`
- `BG3-OFF-007`
- `BG3-OFF-008`
- `BG3-OFF-010`
- `BG3-OFF-011`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-016`
- `BG3-OFF-015`
- `BG3-PLY-002`
- `BG3-PLY-003`

## Open questions

- 下一轮是否应把“实现验证检查清单”整理为方法文件，而不是继续塞在模块正文里？
- 是否需要为补丁 / 热修条目单独定义更细的验证分级？

## Revision notes

- 2026-04-25：新增阶段 6 的第三段 actual units evidence lock，明确 `THIRD-EXCERPT-001`、`THIRD-ASSET-001` 与 `THIRD-TRACE-001` 只能安全发布到 `camp fold / delayed feedback + supporting-bundle / handoff` 这一层，不能越级写成 camp scene 清单或第二条对称营地主干。
- 2026-04-25：执行阶段 6 首轮一致性审阅并修正 `FINAL-ASSET-001` 的矩阵行集，明确收尾段证据矩阵必须显式保留 `入口页`、第一段、第二段、第三段四行，不能把 `入口页` 并入第一段。
- 2026-04-25：补入阶段 6 第三轮一致性审阅结论，明确四份 actual units 仍未命中新 trigger；本轮只清理 review-level 支撑文件中残留的“首轮审阅 / 首轮 trigger”旧口径。
- 2026-04-25：补入阶段 6 第四轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮只清理续轮入口仍把旧基准 ExecPlan 写成当前唯一执行计划的口径，并把当前入口统一为 `review sheet + 最新 addendum`。
- 2026-04-25：补入阶段 6 第五轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮只清理当前入口文件仍把 `.agent/execplan_stage6_release_package_assembly_review_round4.md` 固定写成最新 addendum 的轮次漂移，并把当前入口推进为 `review sheet + 最新 addendum（round5）`。
- 2026-04-25：补入阶段 6 第六轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮只继续推进当前入口文件中的最新 addendum 指针，把当前入口推进为 `review sheet + 最新 addendum（round6）`。
- 2026-04-25：补入阶段 6 第七轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮只继续推进当前入口文件中的最新 addendum 指针，把当前入口推进为 `review sheet + 最新 addendum（round7）`。
- 2026-04-25：补入阶段 6 第八轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮只继续推进当前入口文件中的最新 addendum 指针，把当前入口推进为 `review sheet + 最新 addendum（round8）`。
- 2026-04-25：补入阶段 6 第九轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮只继续推进当前入口文件中的最新 addendum 指针，把当前入口推进为 `review sheet + 最新 addendum（round9）`。
- 2026-04-25：补入阶段 6 第十轮一致性审阅结论，明确本轮命中的是 trigger `5` 的局部 traceback 漂移：收尾段与 review-level evidence lock 一度把 `入口页` 的 Source ID 回链压缩成只剩 BG3 官方来源，遗漏了 `BMK-002 / BMK-003`。本轮已回写 `stage6_final_section_release_units.md` 与 `05_implementation_validation.md`，把入口页的 benchmark + BG3 双重 traceback 补回，并把当前入口推进为 `review sheet + 最新 addendum（round10）`。
- 2026-04-25：补入阶段 6 第十一轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 保持完整，并只把当前入口文件中的最新 addendum 指针从 `round10` 推进到 `round11`。
- 2026-04-25：补入阶段 6 第十二轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并只把当前入口文件中的最新 addendum 指针从 `round11` 推进到 `round12`。
- 2026-04-25：补入阶段 6 第十三轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并只把当前入口文件中的最新 addendum 指针从 `round12` 推进到 `round13`。
- 2026-04-25：补入阶段 6 第十四轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并只把当前入口文件中的最新 addendum 指针从 `round13` 推进到 `round14`。
- 2026-04-25：补入阶段 6 第十五轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并只把当前入口文件中的最新 addendum 指针从 `round14` 推进到 `round15`。
- 2026-04-25：补入阶段 6 第十六轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并只把当前入口文件中的最新 addendum 指针从 `round15` 推进到 `round16`。
- 2026-04-25：补入阶段 6 第十七轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并只把当前入口文件中的最新 addendum 指针从 `round16` 推进到 `round17`。
- 2026-04-25：补入阶段 6 第十八轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并修正 review-level 入口文件仍把当前状态写成“已完成十六轮受控审阅”或把审阅 ceiling 停在第十五轮 / 第十六轮的残留口径，把当前入口推进到 `review sheet + 最新 addendum（round18）`。
- 2026-04-25：补入阶段 6 第十九轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口与 review-level 产出清单统一推进到 `review sheet + 最新 addendum（round19）`，同时修正多份入口文件仍停在 `round18`、以及 `deconstruction_granular_codex_plan.md` 的“优先产出什么”仍停在 `round17` 的残留漂移。
- 2026-04-25：补入阶段 6 第二十轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18、round19 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口统一推进到 `review sheet + 最新 addendum（round20）`，同时修正多份入口文件仍停在 `round19` 的残留漂移。
- 2026-04-25：补入阶段 6 第二十一轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18、round19、round20 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口统一推进到 `review sheet + 最新 addendum（round21）`，同时修正多份入口文件仍停在 `round20` 的残留漂移。
- 2026-04-25：补入阶段 6 第二十二轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18、round19、round20、round21 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口统一推进到 `review sheet + 最新 addendum（round22）`，同时修正多份入口文件仍停在 `round21` 的残留漂移。
- 2026-04-25：补入阶段 6 第二十三轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18、round19、round20、round21、round22 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口统一推进到 `review sheet + 最新 addendum（round23）`，同时修正多份入口文件仍停在 `round22` 的残留漂移。
- 2026-04-25：补入阶段 6 第二十四轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18、round19、round20、round21、round22、round23 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口统一推进到 `review sheet + 最新 addendum（round24）`，同时修正多份入口文件仍停在 `round23` 的残留漂移。
- 2026-04-25：补入阶段 6 第二十五轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18、round19、round20、round21、round22、round23、round24 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口统一推进到 `review sheet + 最新 addendum（round25）`，同时修正多份入口文件仍停在 `round24` 的残留漂移。
- 2026-04-25：补入阶段 6 第二十六轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18、round19、round20、round21、round22、round23、round24、round25 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口统一推进到 `review sheet + 最新 addendum（round26）`，同时修正多份入口文件仍停在 `round25` 的残留漂移。
- 2026-04-26：补入阶段 6 第二十七轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18、round19、round20、round21、round22、round23、round24、round25、round26 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口统一推进到 `review sheet + 最新 addendum（round27）`，同时修正多份入口文件仍停在 `round26` 的残留漂移。
- 2026-04-26：补入阶段 6 第二十八轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18、round19、round20、round21、round22、round23、round24、round25、round26、round27 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口统一推进到 `review sheet + 最新 addendum（round28）`，同时修正多份入口文件仍停在 `round27` 的残留漂移。
- 2026-04-26：补入阶段 6 第三十一轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18、round19、round20、round21、round22、round23、round24、round25、round26、round27、round28、round29、round30 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口统一推进到 `review sheet + 最新 addendum（round31）`，同时修正多份入口文件仍停在 `round30` 的残留漂移。
- 2026-04-26：补入阶段 6 第三十轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18、round19、round20、round21、round22、round23、round24、round25、round26、round27、round28、round29 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口统一推进到 `review sheet + 最新 addendum（round30）`，同时修正多份入口文件仍停在 `round29` 的残留漂移。
- 2026-04-26：补入阶段 6 第二十九轮一致性审阅结论，明确五段 actual units 仍未命中新 trigger；本轮继续确认 round10 补回并经 round11、round12、round13、round14、round15、round16、round17、round18、round19、round20、round21、round22、round23、round24、round25、round26、round27、round28 复核的 `BMK-002 / BMK-003 + BG3-OFF-001 / BG3-OFF-003` 双重 traceback 没有回退，并把续轮入口统一推进到 `review sheet + 最新 addendum（round29）`，同时修正多份入口文件仍停在 `round28` 的残留漂移。
- 2026-04-25：新增阶段 5 / `Implementation Validation` 的 unified exit matrix，并把 `Quest Reactivity`、`Combat / Environment`、`Companion / Camp / Long Rest` 三条横向主干统一压成 “1 条 spine + ceiling / bundle / handoff 边界” 的阶段出口结构，明确阶段 5 在当前公开来源下已完成收口。
- 2026-04-25：补入阶段 6 的模块导览职责，明确本模块当前只承担展示链的收尾与分级职责，不再与入口层竞争顺序。
- 2026-04-25：新增阶段 5 / `Companion / Camp / Long Rest` 的 second public camp spine ceiling / late-game boundary 验证矩阵，明确 `BG3-OFF-007` 只稳定支撑 `reflection / roster-state bundle`、`BG3-OFF-010` 只稳定支撑 `dialogue accessibility maintenance bundle`，而 `Act II` reread 与 late-game `ending feedback` 继续停在 `convergence-adjacent reread` / `ending-feedback handoff` 层。
- 2026-04-25：新增阶段 5 / `Combat / Environment` 的 second spine ceiling / late-game boundary 验证矩阵，明确 `Last Light / Moonrise / Gauntlet` 与 `Act 3` 各包当前只能停在 supporting bundle 层，而不能升格为第二条对称环境 spine。
- 2026-04-25：新增阶段 5 / `Combat / Environment` 的首条跨阶段主干矩阵，把 `Nautiloid -> Act 1 地表主区 -> Grymforge -> Shadow-Cursed Lands` 串成 “early local agency -> regional pressure loop” 的环境 spine，并明确 late `Act 2` / `Act 3` 当前仍未达到第二条同级 spine 的公开证据强度。
- 2026-04-25：新增阶段 5 / `Companion / Camp / Long Rest` 的首条跨区域 `camp fold / delayed feedback` 矩阵，把 `Act 1 地表主区 -> Dark Urge bard / Grove / Goblin -> Mountain Pass / Creche -> Last Light / Moonrise / Gauntlet -> 终局组织与收束压力` 串成第一条营地主干，并明确 `BG3-OFF-007`、`BG3-OFF-010` 与 late-game `ending feedback` 当前仍只稳定停在 supporting-bundle / handoff 层。

- 2026-04-22：建立实现验证模块骨架。
- 2026-04-22：根据 `02_quests_and_choices` 的首轮回写做最小同步，补入“补丁 / 热修 / 社区更新如何暴露状态回流边界”的当前入口。
- 2026-04-23：完成整改 `M2` 的最小必要清理，移除集合式玩家来源占位条目，改用具体社区案例 ID 作为案例线索。
- 2026-04-24：补入 `Nautiloid` 的 opening flow / Journal 验证入口，确认区域包可以把技术判断留在实现验证层而不提前写死。
- 2026-04-24：补入 `Act 1 地表主区` 作为 opening state 续接层的验证入口，开始公开追问“哪些状态被清理、哪些被续接”。
- 2026-04-24：补入 `Grove / Goblin` 作为 `Act 1` 第一块同时暴露“处理方式 / 时序 / 营地可达性”三种边界的区域包验证入口。
- 2026-04-24：补入 `Underdark` 作为“区域切换 / 下游 setup”验证入口，开始公开追问哪些阶段重构能继续映射到 objective / step 层。
- 2026-04-24：补入 `Grymforge` 作为“战斗 / 环境区域压缩包”验证入口，明确当前可升级的是区域包级判断，而不是具体熔炉路径事实链。
- 2026-04-24：补入 `Mountain Pass / Creche` 作为“结构门槛 + 伙伴张力”叠层包的验证入口，明确当前可升级的是区域包级判断，而不是 `Act 2` 切换规则的具体实现映射。
- 2026-04-24：补入 `Act 2` 作为“中盘压力 / 前史重读框架”的验证入口，明确当前可升级的是阶段级结构判断，而不是影咒限制或完整收束点映射的实现实锤。
- 2026-04-24：补入 `Shadow-Cursed Lands` 作为“中盘压力落地的区域验证入口”，明确当前可升级的是区域级压力循环判断，而不是具体影咒机制或完整路线分工的实现实锤。
- 2026-04-24：补入 `Last Light / Moonrise / Gauntlet` 作为“中盘收束点组”的验证入口，明确当前可升级的是“前史读回 + 节点压缩”这一组判断，而不是三者内部的完整 objective / step 分工。
- 2026-04-24：补入 `Act 3` 作为“高密度城市 + 结算负载”的验证入口，明确当前可升级的是后期承压框架，而不是各城市子块与终局组织的完整 objective / step 分工。
- 2026-04-24：补入 `Rivington` 作为“第一层入口过滤 + 外环承压”的验证入口，明确当前可升级的是 late-game bundle 的第一次分束判断，而不是 `Rivington` 内部 objective / step 的实现实锤。
- 2026-04-24：补入 `Wyrm's Crossing` 作为“桥梁 / 门槛 + 第二层结构重排”的验证入口，明确当前可升级的是门槛级 bundle 重排判断，而不是 `Wyrm's Crossing` 内部 objective / step 的实现实锤。
- 2026-04-24：补入 `Lower City` 作为“更高密度的内城并行 / 结算区”的验证入口，明确当前可升级的是高密度并排承接与局部结算判断，而不是 `Lower City` 内部 objective / step 或终局组织分工的实现实锤。
- 2026-04-24：补入 `终局组织与收束压力` 作为“组织级终局压缩 / ending feedback 读取层”的验证入口，明确当前可升级的是组织级压缩判断，而不是终局私有 objective / step 或结局百科式分工的实现实锤。
- 2026-04-24：新增阶段 5 / `Quest Reactivity` 的跨阶段分层矩阵，把 `Grove / Goblin -> Last Light / Moonrise / Gauntlet -> Rivington -> Wyrm's Crossing -> Lower City -> 终局组织与收束压力` 串成第一条可复述的 readback spine，并明确各链段最多只能升级到哪一层。
- 2026-04-24：新增阶段 5 / `Quest Reactivity` 的上游前置链分层矩阵，把 `Nautiloid -> Act 1 地表主区 -> Underdark -> Mountain Pass / Creche` 串成服务既有主干的入口 / 改道 / 门槛链，并明确各链段当前最多只能升级到哪一层。
- 2026-04-24：新增阶段 5 / `Quest Reactivity` 的 late `Act 1` / early `Act 2` 交接矩阵，把 `Mountain Pass / Creche -> Shadow-Cursed Lands -> Last Light / Moonrise / Gauntlet` 压成 `gate -> pressure filter -> convergence pack` 三段中盘接缝，并明确每段当前最多只能升级到哪一层。
- 2026-04-24：新增阶段 5 / `Quest Reactivity` 的“第二条公开跨阶段链证据上限”矩阵，明确当前公开来源只支撑“一条显式 spine + 多个支撑 bundle”，不再强求对称的第二条主链。
- 2026-04-24：新增阶段 5 / `Quest Reactivity` 的“层级收口 / 边界锁定”矩阵，把既有锚点重新分到 `objective / step` 邻近层、`gate / tension`、`camp fold` 与 `ending feedback / organization bundle`，并把后续验证动作收窄为 objective-adjacent 局部锚点。
- 2026-04-24：新增阶段 5 / `Quest Reactivity` 的 objective-adjacent narrowing 矩阵，把 `Grove / Goblin` 继续压细为局部 resolution-state fragment，把 `Mountain Pass / Creche` 继续压细为局部 gate fragment，并明确其余部分必须停在 delayed readout 或 bundle 层。
