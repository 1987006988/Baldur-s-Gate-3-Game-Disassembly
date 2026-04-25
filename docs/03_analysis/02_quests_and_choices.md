# Quests and Choices

## Question

BG3 的任务与选择系统，为什么会让玩家觉得自己的决定不仅被记录，而且会被后续世界重新解释和反馈？

## Short answer

当前判断是，BG3 的任务反应性并不只来自分支数量，而来自任务状态、区域推进、营地节奏与角色反应之间的回流。较稳的证据显示，某些非常规处理方式会在长休、区域切换甚至后续章节中被重新带回任务流；玩家感受到的“被回应”往往因此发生在选择之后的二次反馈，而不是当下弹出一个结果提示。这个判断现在已有一条较强主案例和一条较弱辅案例支撑，但仍需继续控制推断范围。

## Player-layer observations

- 玩家常把 BG3 的自由感描述为“很多处理方式都能被系统接住”。
- 真正增强印象的，不只是眼前选项，而是稍后出现的人物反应、任务走向变化、营地对话和区域后果。
- 玩家体验中的高价值瞬间通常是“我本以为这是旁门做法，但游戏承认了它”。
- 主案例显示，这种“被接住”的体验有时来自对非标准处置方式的后续承认，而不是只来自传统对话分支。
- 辅案例显示，反馈不一定发生在任务现场，也可能在营地 / 长休节点以更强烈但更间接的方式折返。

## System-layer explanation

- 任务并非孤立分支，而是与角色状态、营地节奏、区域顺序、战斗结局共同构成回流系统。
- 同一任务可能允许对话、潜入、战斗、绕路、延后处理等不同入口，这些入口再影响后续反馈方式。
- 因为反馈延迟且分散，玩家会把系统反应理解为“世界记住了我的做法”。
- `推断`：这里的“选择”不应只理解为对话选项或任务日志分支；至少在部分区域与遭遇中，战斗与环境本身也承担了选择系统的功能。玩家并不是先在叙事层做完决定、再进入战斗，而是在战斗中继续通过站位、机关、地形与开战方式改写任务推进体验。基于 `BG3-OFF-003`, `BG3-OFF-006`, `BG3-PLY-004`

## Supplement: Nautiloid 作为早期任务状态埋点

- `事实`：`Patch 7` 直接说明 `Escape the Nautiloid` 会以正式任务流的方式出错或关闭失败，而不是纯教程标签。`BG3-OFF-002`
- `事实`：`Patch 6` 直接说明开场阶段已经存在关键 quest item、受限检定、narrator 触发物与坠毁后的 harmful condition 清理。`BG3-OFF-015`
- `事实`：官方 Journal 文档把任务结构公开表述为 `Category → Quest → Objective → Step`，并将 scripting trigger updates 与 Journal 更新并列描述。`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这使 `Nautiloid` 更适合作为任务模块的“前置模板块”，说明 BG3 的任务 / 选择逻辑从一开始就在记录目标推进、关键物件和角色状态交接，而不是等到 Act I 地表才开始真正生效。基于 `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-015`
- `待验证问题`：当前还不能把 `Nautiloid` 的每个开场分歧都升级成后续会被持续回流的大选择；更稳的写法是，它首先证明了“早期状态埋点存在”，而不是“早期每个决定都长线回响”。

## Supplement: Act 1 地表主区作为“目标网”而不是单主线

- `事实`：`Patch 7` 说明 tutorial 结束后的装备交接会在地表招募时继续被读取，例如 `Shadowheart / Lae'zel` 在后续招募时需要获得新的装备。`BG3-OFF-002`
- `事实`：`Patch 6` 说明 opening 阶段的部分 harmful conditions 会在坠毁时被移除，表明 crash 不是无差别重置，而是带边界的状态清理。`BG3-OFF-015`
- `事实`：官方 Journal 文档持续把任务结构公开表述为 `Category → Quest → Objective → Step`，并把 trigger updates 视作 Journal 更新的配套实现入口。`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此 `Act 1 地表主区` 不适合被理解成“开场结束后的自由空窗”，而更像 opening state 的第一层续接区：一些状态被清掉，一些状态通过同伴回收、目标继续挂起与后续招募重新进入任务流。基于 `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-015`
- `推断`：玩家在地表感受到的“我可以先去做那个”，不是缺少任务结构，而是多个 objective pressure 被同时挂起，允许玩家选择先兑现哪一段 opening 前史。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `待验证问题`：现阶段还不宜把地表主区的完整早期路线顺序写成事实矩阵；更稳的口径是“目标网存在”，而不是“每条路线的优先级与回流都已被证实”。

## Supplement: Grove / Goblin 冲突作为“状态回流网”而不是派系二选一

- `事实`：`Hotfix #20` 明确区分了 Minthara 的 `knocked out` 与 `killed` 两类状态，并说明 `journal wording` 会据此区分。`BG3-OFF-004`
- `事实`：同一热修还直接暴露了“击倒 Minthara -> 长休 -> 再处理其他首领”这一时序会影响后续判定，否则不会出现专门的修复条目。`BG3-OFF-004`
- `事实`：`Patch 7` 明确写到 `Knocked Out Minthara will now always flee to Moonrise Towers.`，并会在 `Act II` 对 `Act I` 的击倒作出反应。`BG3-OFF-002`
- `事实`：`Hotfix #5` 直接把 Minthara 的营地对话可达性与 `companion reaction` 列为修复对象，说明这块的下游读出不只发生在任务现场。`BG3-OFF-008`
- `推断`：因此 `Grove / Goblin` 当前最稳的写法，不是“站 Grove 还是站 Goblin”的平面立场摘要，而是“处理方式 -> 即时状态 -> 长休 / 跨区域续接 -> 营地 / Act II 读出”的 resolution matrix。基于 `BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-008`
- `推断`：相较于 `Act 1 地表主区` 的“目标网”，`Grove / Goblin` 是 `Act 1` 第一块更清楚把“怎么处理冲突对象”写成后续状态差异的区域包。基于 `BG3-OFF-002`, `BG3-OFF-004`
- `待验证问题`：除 Minthara 外，这块还有哪些首领顺序或处理差异能用同等级别的公开来源压实，而不是只停留在玩家观察？

## Supplement: Grymforge / Grym 作为“战斗 / 环境也是选择系统”的补强案例

- `事实`：官方把 Grymforge 描述为同时包含 `questlines, choices, cinematics, complex combat encounters` 的区域，而不是纯战斗房间。`BG3-OFF-006`
- `事实`：开发者明确把 BG3 的关卡与遭遇组织成允许多入口、非常规 problem-solving 的 `Swiss cheese` 结构。`BG3-OFF-003`
- `推断`：把这两条来源合起来看，Grymforge / Grym 至少足以支撑一个高层判断：BG3 的“选择”并不只发生在对话前，而会延伸到遭遇内部；环境与战斗解法本身就是任务体验差异化的一部分。基于 `BG3-OFF-003`, `BG3-OFF-006`
- `待验证问题`：现阶段还不能把某条具体 Grym / 熔炉打法直接升级成任务模块事实，因为稳定证据仍停留在高层官方框架与社区案例入口之间；更细的路径判断应继续留在 `04_combat_and_environment.md` 深挖。基于 `BG3-PLY-004`

## Case 1: Minthara 击倒路径（主案例）

### 选择点

- `事实`：在哥布林相关流程中，玩家可以不直接击杀 Minthara，而是选择将其击倒。`BG3-OFF-004`

### 状态变化

- `事实`：官方热修明确区分了 Minthara 的 `knocked out` 与 `killed` 两类状态。`BG3-OFF-004`
- `事实`：官方热修明确写到，在“击倒 Minthara -> 长休 -> 再处理其他首领”的顺序下，游戏曾错误判断她是否已在 Act I 被击败，因此官方专门修复了这一判定。`BG3-OFF-004`
- `事实`：官方补丁明确写到，被击倒的 Minthara 会前往 Moonrise Towers。`BG3-OFF-002`
- `推断`：这说明该路径至少涉及跨长休、跨区域、跨 Act 的状态传递，而不是单点对话标记。基于 `BG3-OFF-002`, `BG3-OFF-004`

### 后续反馈

- `事实`：官方补丁明确写到，Minthara 会在 Act II 对玩家曾在 Act I 击倒她一事作出反应。`BG3-OFF-002`
- `推断`：这条路径之所以适合做主案例，不是因为它最常见，而是因为它已经显示出“非常规处理方式 -> 状态保留 -> 后续角色再解释”的完整回流轮廓。基于 `BG3-OFF-002`, `BG3-OFF-004`

### 当前可得结论

- `推断`：至少在这条支线上，BG3 的任务系统并不只是记录“完成/失败”，而会记录更细的处理方式，并在后续区域重新调用。基于 `BG3-OFF-002`, `BG3-OFF-004`

### 仍需保留的待验证问题

- `待验证问题`：这条路径从一开始就是完整支持路径，还是在后续更新中被逐步正规化？
- `待验证问题`：Minthara 的后续反应深度到底只是局部对白回应，还是会更深地影响任务/队伍状态？
- `待验证问题`：这条路径的代表性是否足以外推为 BG3 更普遍的任务设计原则？

## Case 2: Dark Urge 营地 bard 事件（辅案例）

### 选择点

- `事实`：在 Dark Urge 流程中，官方确认“某位 bard”会在营地暂时以可控制角色身份加入。`BG3-OFF-005`

### 状态变化

- `事实`：官方社区更新把这一变化放在 Dark Urge 语境中，并用 `TEMPORARILY` 标记其临时性。`BG3-OFF-005`
- `事实`：官方后续文案又强调“这不是新同伴路线，而是一个带后果预告的短暂状态”。`BG3-OFF-005`
- `事实`：玩家社区持续把这条事件当作一个与长休 / 营地节点相关的高辨识度后果事件来讨论，但这只能作为案例线索，不可直接外推为系统事实。`BG3-PLY-002`
- `推断`：这说明 BG3 的某些关键反馈会被故意放到营地 / 长休节点执行，而不是在任务现场立即结算。基于 `BG3-OFF-005`, `BG3-PLY-002`

### 后续反馈

- `事实`：现有官方来源可以直接确认“临时入队”与“强后果预告”，但还不能直接穷尽这条事件的后续差异分布。`BG3-OFF-005`
- `推断`：对任务模块而言，这条案例的价值不在于它有多稳定，而在于它提示我们：任务反馈可以通过营地事件折返，因而不应把“任务回应”狭义理解成任务日志或现场对白。基于 `BG3-OFF-005`, `BG3-PLY-002`

### 当前可得结论

- `推断`：这条事件更适合作为主案例的补充，说明 BG3 的反馈位置不仅会跨时间，也会跨场景，从任务现场转移到营地 / 长休。基于 `BG3-OFF-005`

### 仍需保留的待验证问题

- `待验证问题`：这条事件的触发条件、角色替换逻辑和后续差异，到底有哪些可稳定复核的分支？
- `待验证问题`：这条案例应继续留在任务与选择模块中，还是在后续更适合作为 `03_party_and_camp` 的耦合案例？
- `待验证问题`：如果后续找不到更细的直接来源，它是否应继续保留在首批正文案例中？

## Implementation-layer evidence / hypothesis

- 已有证据：
  - `BG3-OFF-002` 与 `BG3-OFF-004` 已足以证明，至少在 Minthara 路径上，官方明确维护了“击倒/击杀”的状态差异、跨长休判定和后续章节反应。
  - `BG3-OFF-005` 已足以证明，至少在 Dark Urge bard 事件上，官方明确承认了“营地临时入队”这一状态变化，并把它包装成带后果的短暂事件。
  - `BG3-OFF-002` 与 `BG3-OFF-015` 也已足以证明，连开场 `Nautiloid` 都存在正式 quest close、关键物件、检定限制与状态清理边界。
  - `BG3-OFF-003` 则提供了更高层的设计意图背景：团队有意识地保留多入口、非常规解法与高密度状态排列。
- 合理推断：
  - 任务系统内部至少在部分支线中存在较细的状态记录与条件判断，否则很难稳定支撑延迟反馈、区域切换后的再解释，以及营地节点的折返反馈。基于 `BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-005`
  - `Nautiloid` 说明“状态记录”并不是中后期案例才出现的复杂化结果，而是在开场就已经以更压缩的方式存在。基于 `BG3-OFF-002`, `BG3-OFF-015`
  - BG3 的高反应性体验并不只依赖对话树，而依赖任务状态、区域流转、营地节奏与角色反应共同构成的回流网络。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-004`, `BG3-OFF-005`
  - 在部分高复杂度区域里，任务系统与战斗系统并不是串联关系，而是交叠关系；玩家通过环境与遭遇内部做出的策略性处理，也会被体验为“另一种选择”。基于 `BG3-OFF-003`, `BG3-OFF-006`, `BG3-PLY-004`
- 待验证问题：
  - 哪些反馈是任务脚本直接驱动，哪些是通过同伴 / 营地 / 区域状态间接折返实现？
  - 现有较强证据是否主要集中在少数高辨识度分支，而非普遍规律？
  - Dark Urge bard 事件的直接官方支撑是否足以让它稳定留在本模块，而不是转移到 `03_party_and_camp`？
  - 如果后续为 Grymforge / Grym 补到更稳定的具体路径来源，哪些结论应继续留在战斗模块，哪些才值得升级为任务模块的常规论据？

### Region-pack conclusion: Grove / Goblin

- `推断`：`Grove / Goblin` 现在已经可以被写成一份早期 `resolution matrix`，因为公开来源已同时暴露处理方式、长休时序与营地可达性三种边界。基于 `BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-008`
- `待验证问题`：这份 `resolution matrix` 是否还能稳定扩展到 Minthara 以外的处理路径，而不是继续依赖单一高可见案例？

## Supplement: Underdark 作为“推进框架选择”而不只是地图切换

- `事实`：官方 About 页把 `Underdark` 作为 BG3 差异化区域之一并列呈现，而不是把它写成可忽略的边缘角落。基于 `BG3-OFF-001`
- `事实`：Adam Smith 用 `Swiss cheese` 描述 BG3 的路径与关卡组织，强调同一阶段允许玩家从不同洞口进入问题。基于 `BG3-OFF-003`
- `事实`：`Community Update 14` 的 patch notes 直接写到 `Added setup for several Grymforge quests in the Underdark.`，并把 `Grymforge` 继续定义为包含 `questlines, choices, cinematics, complex combat encounters` 的区域。基于 `BG3-OFF-006`
- `推断`：因此，进入 `Underdark` 当前更稳的写法不是“换一张地图继续探索”，而是把 `Act 1` 的任务推进从地表问题网与 `Grove / Goblin` 的处理矩阵，改写成另一套以地下穿行和下游区域推进为中心的阅读顺序。基于 `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-006`
- `推断`：这补强了任务模块的一个边界：BG3 的 reactivity 不只发生在“同一冲突怎么处理”，也发生在“同一阶段先兑现哪一套空间 / 任务框架”。基于 `BG3-OFF-003`, `BG3-OFF-006`
- `待验证问题`：`Underdark` 的哪些具体入口 / 过渡能稳定映射到 objective / step 变化，哪些更可能只是玩家体感上的顺序差异？

### Region-pack conclusion: Underdark

- `推断`：`Underdark` 现在已经可以被写成一份早期 `entry / progression pack`，因为公开来源已同时暴露差异化区域定位、多入口设计语言与直通 `Grymforge` 的下游 setup。基于 `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-006`
- `待验证问题`：这份 `entry / progression pack` 能否进一步稳定压到更细的 objective / step 层，而不是长期只停在结构性高层判断？

## Supplement: Grymforge 作为“遭遇内部也继续分化选择”的区域压缩包

- `事实`：`Community Update 14` 直接把 `Grymforge` 定义为包含 `questlines, choices, cinematics, complex combat encounters` 的区域，并说明它的若干 quest setup 已在 `Underdark` 提前铺设。基于 `BG3-OFF-006`
- `事实`：开发者对 BG3 使用 `Swiss cheese` 这一多入口 / 非常规 problem-solving 设计语言，不只适用于地图进入方式，也适用于玩家如何穿入具体遭遇。基于 `BG3-OFF-003`
- `推断`：因此，`Grymforge` 对任务模块当前最稳的补强，不是把某条著名熔炉打法硬写成任务事实，而是说明 `Underdark` 下游的区域推进会继续在遭遇内部分化：玩家处理复杂战斗 / 环境问题的方式，本身就是选择系统的一部分。基于 `BG3-OFF-003`, `BG3-OFF-006`, `BG3-PLY-004`
- `待验证问题`：现阶段还不能把具体熔炉机关路径升级成 objective / step 事实链；更细的路径判断仍应继续留在 `04_combat_and_environment.md` 与 `05_implementation_validation.md`。

### Region-pack conclusion: Grymforge

- `推断`：`Grymforge` 现在已经可以被写成 `Act 1` 第一块早期 `encounter bundle / combat-agency compression pack`，因为公开来源已同时暴露下游 setup、区域级 `choices + complex combat encounters` 框架，以及玩家如何把遭遇读成环境重写问题。基于 `BG3-OFF-003`, `BG3-OFF-006`, `BG3-PLY-004`
- `待验证问题`：这份区域包结论是否还能继续压到更细的 Journal / objective / step 层，而不是长期只停在“战斗 / 环境也是选择系统”的高层判断？

## Supplement: Mountain Pass / Creche 作为“权限测试 + 伙伴张力”的 late Act 1 gate

- `事实`：`Patch #3` 暴露了这块区域的多个任务 / 对话边界：拒绝 `Vlaakith` 后一个多余 skill check 可能阻塞后续对话启动；`Rosymorn Monastery gate` 的爆炸倒计时需要在进入 `Astral Plane` 后正确取消。基于 `BG3-OFF-016`
- `事实`：同一补丁还暴露了局部处理方式会改写敌意结果：如果 `Lae'zel` 在与 `Voss` 的互动中成功通过 `Deception` 检定，`githyanki` 不应继续保持敌对。基于 `BG3-OFF-016`
- `事实`：同一补丁把 `Lae'zel` 在 `Crèche Y'llek` 遇到 `Dream Visitor` 后的即时反应与 `camp night` 里关于 `crèche` 后果的延迟反思都列为需要修复的边界。基于 `BG3-OFF-016`
- `推断`：因此 `Mountain Pass / Creche` 对任务模块的最稳补强，不是提供一份完整分支表，而是说明 late `Act 1` 的选择开始同时表现为权限 / 对话门槛、局部敌意变化与伙伴反应压力。基于 `BG3-OFF-003`, `BG3-OFF-016`
- `待验证问题`：这块的哪些处理方式会进一步稳定映射到 `Journal / objective / step`，哪些更像区域现场与营地后续之间的混合读出？

## Upstream Lead-in Chain: 从 `Nautiloid` 到 `Mountain Pass / Creche` 的入口 / 改道 / 门槛链

- `事实`：`Nautiloid` 已经有公开可见的 quest close、关键物件、状态清理与地表招募交接边界，因此 `Quest Reactivity` 的入口不是从 `Grove / Goblin` 才突然开始。基于 `BG3-OFF-002`, `BG3-OFF-015`
- `事实`：`Act 1 地表主区` 继续把这些开场残余状态展开成多个同时挂起的 objective pressure；公开 Journal 文档持续给出 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的结构语言。基于 `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-015`
- `事实`：`Underdark` 既是官方直接点名的差异化区域，又公开承担通向 `Grymforge` 的 quest setup，因此它提供的不是单纯地图切换，而是一条会改写阶段阅读顺序的改道。基于 `BG3-OFF-001`, `BG3-OFF-003`, `BG3-OFF-006`
- `事实`：`Mountain Pass / Creche` 直接暴露了对话门槛、局部敌意、即时伙伴反应与 `camp night` 后果读取边界，说明进入中盘前的最后一段前史已经被压成高压 gate。基于 `BG3-OFF-016`
- `推断`：因此阶段 5 当前更稳的上游写法，不是把 `Act 1` 重新摊成总表，而是把它压成一条四段前置链：`Nautiloid` 负责入口埋点，地表主区负责目标网，`Underdark` 负责改道 / 重构，`Mountain Pass / Creche` 负责 late `Act 1` 的门槛 / 张力。基于 `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-006`, `BG3-OFF-015`, `BG3-OFF-016`
- `推断`：从这个角度看，`Grove / Goblin` 之所以适合作为现有主干的第一块高可见 `resolution matrix`，不是因为前面没有任务反应性，而是因为前四段已经先把 objective 压力、路线改写与高压门槛准备好了。基于 `BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-006`, `BG3-OFF-016`
- `待验证问题`：这条前置链里，`Nautiloid -> 地表主区` 与 `Mountain Pass / Creche -> Act 2` 哪些边界已经足以压到 `objective / step` 邻近层，哪些仍只能停留在 `entry / diversion / gate bundle`？

## Transition Boundary: 从 `Mountain Pass / Creche` 到 `Last Light / Moonrise / Gauntlet` 的 gate / pressure / convergence 接缝

- `事实`：`Mountain Pass / Creche` 已直接暴露对话门槛、局部敌意、即时伙伴反应与 `camp night` 后果读取边界，因此它不是 late `Act 1` 的普通尾声，而是通向中盘的高压 gate。来源：`BG3-OFF-016`
- `事实`：`Shadow-Cursed Lands` 与 `Act II` 的公开补丁条目持续暴露 `writing and flow`、`scripting`、角色反应与营地场景维护边界，说明中盘一开始就不是空白新盘，而是带着前史读回与风险过滤继续推进。来源：`BG3-OFF-002`
- `事实`：`Last Light / Moonrise / Gauntlet` 已拥有至少一条明确的跨 Act 读回锚点：被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对 `Act I` 的处理作出反应；公开 Journal 文档继续提供 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的结构语言。来源：`BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此这组 late `Act 1` / early `Act 2` 接缝当前最稳的写法，不是再拆一份 `Act 1` 总表或 `Act 2` 地点目录，而是把它压成三段连续功能：`Mountain Pass / Creche` 先把前史压成高压 gate，`Shadow-Cursed Lands` 再把多入口推进过滤进持续风险条件，`Last Light / Moonrise / Gauntlet` 最后把这些已被过滤的差异压向较少的读回节点。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `推断`：这也解释了为什么阶段 5 的第三子单元必须停在这条接缝上，而不是重新摊开中盘内容：当前最有价值的增量不是地点细节，而是明确 BG3 如何让“高压门槛”继续变成“压力过滤”，再变成“读回压缩”。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-016`
- `待验证问题`：当前最接近 `objective / step` 邻近层的仍主要是 `Mountain Pass / Creche` 的局部门槛；`Shadow-Cursed Lands` 与 `Last Light / Moonrise / Gauntlet` 哪些部分还能继续稳定压到更细的 Journal 层，仍需要更直接的公开锚点。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`

### Region-pack conclusion: Mountain Pass / Creche

- `推断`：`Mountain Pass / Creche` 现在已经可以被写成一份 late `Act 1` 的 `gate-and-tension pack`，因为公开来源已同时暴露对话门槛、局部敌意、即时伙伴反应与营地后续读取四种边界。基于 `BG3-OFF-003`, `BG3-OFF-016`
- `待验证问题`：这份区域包结论是否还能继续压到更细的 objective / step 层，而不是长期只停在“结构门槛 + 伙伴张力”的高层判断？

## Supplement: Shadow-Cursed Lands 作为中盘“压力条件下的推进入口”

- `事实`：官方 About 页把 `shadow-cursed forests` 作为 BG3 差异化区域之一直接点名。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 的 `Act II`、`Writing and Flow`、`Scripting` 条目集中修复中盘任务流、角色反应、营地夜晚场景与对话优先级；同一补丁还把被击倒的 Minthara 明确送往 `Moonrise Towers`，并在 `Act II` 重新读取 `Act I` 前史。来源：`BG3-OFF-002`
- `事实`：官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 结构。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此 `Shadow-Cursed Lands` 对任务模块当前最稳的价值，不是再补一组地点摘要，而是提供 `Act 2` 的第一个“压力条件下的推进入口”：中盘任务不再只是多目标同时展开，而开始更紧地与风险条件、前史读回和后续收束方向绑在一起。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：与 `Act 1 地表主区` 的“目标网”相比，这块区域更像把任务推进改写成“在持续压力下继续前进”的阅读方式；与后续 `Last Light / Moonrise / Gauntlet` 相比，它先负责组织推进，而不是完成收束。来源：`BG3-OFF-002`, `BG3-OFF-003`
- `待验证问题`：当前还不能把这块区域内部哪些压力会稳定映射到 objective / step、哪些主要停留在 flow / reaction / camp 边界写成事实表。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## Supplement: Last Light / Moonrise / Gauntlet 作为“中盘收束点组”而不是平行地点包

- `事实`：`Patch 7` 的 `Writing and Flow`、`Scripting`、`Act II` 条目集中暴露中盘任务流、角色反应、营地夜晚场景与对话优先级的维护边界；同一补丁还明确写到，被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对玩家曾在 `Act I` 的处理作出反应。来源：`BG3-OFF-002`
- `事实`：Adam Smith 用 `Swiss cheese` 描述 BG3 的多入口 / problem-solving 结构，说明中盘收束不应被直接理解成“前面所有入口都失效，只剩一条路”。来源：`BG3-OFF-003`
- `事实`：官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为公开的更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此 `Last Light / Moonrise / Gauntlet` 当前最稳的任务层写法，不是三个彼此平行的地点条目，而是同一块 `convergence pack`：前面被区域包拉开的处理差异与推进方向，在这里开始更集中地被读取、重排与压缩。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：与 `Shadow-Cursed Lands` 的“在压力中继续推进”不同，这组节点更像把任务阅读方式改写成“前史现在要被回答了”：玩家不只是继续往前走，而是在更少的节点里面对更多前置处理差异。来源：`BG3-OFF-002`, `BG3-OFF-003`
- `待验证问题`：除 `Minthara -> Moonrise Towers -> Act II reaction` 外，还有哪些同级别的公开读回链足以把“收束点组”继续压到更细的 objective / step 层，而不是停留在高层任务组织判断？

## Supplement: Act 3 作为“高密度并行线 + 结算负载”而不是城市地点导览

- `事实`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为 BG3 差异化区域之一直接点名。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 明确加入新的 evil ending cinematics，并把它们表述为会根据玩家做出的选择出现。来源：`BG3-OFF-002`
- `事实`：Adam Smith 一方面继续用 `Swiss cheese` 描述 BG3 的多入口 / problem-solving 结构，另一方面明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。来源：`BG3-OFF-003`
- `事实`：官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为公开更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此 `Act 3` 当前最稳的任务层写法，不是“进入城市后有更多支线”，而是“更多并行 quest bundle 被挤进同一阶段，同时更靠近 ending feedback 与状态结算”。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：与 `Last Light / Moonrise / Gauntlet` 的 `convergence pack` 不同，`Act 3` 并没有继续把任务压到更少节点；它更像在已经接近终局的前提下，把多条派系线、城市线与前史读回重新同时展开，所以玩家才会一起感到“线索暴增”和“每条线都更像收束线”。来源：`BG3-OFF-002`, `BG3-OFF-003`
- `推断`：`Swiss cheese` 式多入口在这里并没有失效，而是进入更高负载状态：入口依旧很多，但每个入口都更可能连向派系重排、前史重读或结局反馈。来源：`BG3-OFF-002`, `BG3-OFF-003`

## Supplement: Rivington 作为“并行 quest bundle 的第一层过滤包”

- `事实`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为 BG3 差异化区域之一直接点名。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 明确加入新的 evil ending cinematics，并把它们表述为会根据玩家做出的选择出现；同一补丁继续集中修复后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界。来源：`BG3-OFF-002`
- `事实`：Adam Smith 一方面继续用 `Swiss cheese` 描述 BG3 的多入口 / problem-solving 结构，另一方面明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。来源：`BG3-OFF-003`
- `事实`：官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为公开更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此 `Rivington` 当前最稳的任务层写法，不是“进入城市前先摆出几条零散支线”，而是“后期更高密度的并行 quest bundle 第一次在这里被过滤成可进入的初始阅读顺序”。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：与 `Last Light / Moonrise / Gauntlet` 的 `convergence pack` 不同，`Rivington` 的价值不在于把前史立即压向较少节点，而在于让玩家先决定要从哪一束后期问题切入；它更像 late-game bundle 的第一次分束，而不是第一次结算。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `待验证问题`：哪些 `Act 3` 并行线更适合先被压成 `Rivington` 的入口过滤包，哪些已经足以被理解成更接近 `Wyrm's Crossing`、`Lower City` 或终局组织的后续重排与结算束，目前仍缺更直接的公开来源。

## Supplement: Wyrm's Crossing 作为“桥梁 / 门槛后的第二层 quest bundle 重排包”

- `事实`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为 BG3 的阶段级城市节点直接点名；官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为公开更新入口。来源：`BG3-OFF-001`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：`Patch 7` 一方面把新的 evil ending cinematics 写成会 `depending on the choices you make` 出现，另一方面继续集中修复后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界。来源：`BG3-OFF-002`
- `事实`：Adam Smith 继续用 `Swiss cheese` 描述 BG3 的多入口结构，并明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。来源：`BG3-OFF-003`
- `推断`：因此 `Wyrm's Crossing` 当前最稳的任务层写法，不是“桥头继续摆出更多内容”，而是“已被 `Rivington` 过滤过的 late-game quest bundle，在这里进一步被压成带门槛感的第二层阅读顺序”。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：与 `Rivington` 的“先决定从哪一束问题切入”不同，`Wyrm's Crossing` 更像在追问“哪些问题已经变成必须跨过的桥梁 / 门槛”；它因此更接近 late-game bundle 的第二次压缩与重排，而不是单纯过桥。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `待验证问题`：哪些 `Wyrm's Crossing` 级别的任务重排已经足以稳定压到 `objective / step` 层，哪些目前仍更适合停留在“第二层 bundle 重排”这一公开边界？

## Supplement: Lower City 作为“更高密度的内城 quest bundle / 结算负载区”

- `事实`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为 BG3 的阶段级城市节点直接点名。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 明确加入新的 evil ending cinematics，并把它们表述为会根据玩家做出的选择出现；同一补丁继续集中修复后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界。来源：`BG3-OFF-002`
- `事实`：Adam Smith 一方面继续用 `Swiss cheese` 描述 BG3 的多入口 / problem-solving 结构，另一方面明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。来源：`BG3-OFF-003`
- `事实`：官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为公开更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此 `Lower City` 当前最稳的任务层写法，不是“内城里有更多派系线与支线”，而是“已在 `Rivington` 被过滤、在 `Wyrm's Crossing` 被门槛化的 late-game quest bundle，在这里开始以更短窗口同时要求承接、并排处理与逼近结算”。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：与 `Wyrm's Crossing` 的“哪些问题已经变成必须跨过的桥梁 / 门槛”不同，`Lower City` 更像在追问“哪些已跨过门槛的问题束现在必须开始并排被处理”；它因此更接近更高密度的内城并行与局部结算负载，而不是再次扮演门槛本身。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `待验证问题`：哪些 `Lower City` 级别的任务重排已经足以稳定压到 `objective / step` 层，哪些目前仍更适合停留在“高密度 quest bundle + ending feedback”这一公开边界？

## Supplement: 终局组织与收束压力作为“组织级 quest bundle 压缩 / ending feedback 读取层”

- `事实`：官方 About 页把 `the sprawling city of Baldur's Gate` 作为 BG3 的阶段级城市节点直接点名。来源：`BG3-OFF-001`
- `事实`：`Patch 7` 明确加入新的 evil ending cinematics，并把它们表述为会根据玩家做出的选择出现；同一补丁继续集中修复后期的 `writing and flow`、`scripting`、角色反应与长休 / 营地边界。来源：`BG3-OFF-002`
- `事实`：Adam Smith 一方面继续用 `Swiss cheese` 描述 BG3 的多入口 / problem-solving 结构，另一方面明确说团队上线后继续补了大量额外 dialogue / cinematics，去覆盖更高密度的状态与结局排列。来源：`BG3-OFF-003`
- `事实`：官方 Journal 文档持续把任务公开表述为 `Category -> Quest -> Objective -> Step`，并把 `trigger updates` 作为公开更新入口。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此 `终局组织与收束压力` 当前最稳的任务层写法，不是“终于把剩余支线收尾”，而是“已在 `Lower City` 并排承接的 late-game quest bundle，在这里开始被更少、更硬的终局组织位读取、重排并逼向 ending feedback”。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：与 `Lower City` 的“哪些问题束现在必须开始并排被处理”不同，这一层更像在追问“哪些已并排处理的问题束现在必须被组织级收束位读回”；它因此更接近 quest bundle 的组织级压缩，而不是继续扩写城市并行本身。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这也说明后期任务层并不是越靠近终局越只剩一条线；更稳的理解是，多入口依旧存在，但每个入口都更容易被接到组织级读回与 ending feedback，因此玩家会同时感到“还能切入”和“已经在被收束”。来源：`BG3-OFF-002`, `BG3-OFF-003`
- `待验证问题`：哪些终局组织级任务重排已经足以稳定压到 `objective / step` 层，哪些目前仍更适合停留在“organization bundle + ending feedback”这一公开边界？

## Cross-Act Spine: 从 `Grove / Goblin` 到终局组织的状态回流链

- `事实`：`Grove / Goblin` 这一块已经同时暴露了处理方式差异、长休时序与营地下游可达性；其中 `knocked out` / `killed`、`journal wording`、长休顺序与 `companion reaction` 都有公开补丁 / 热修锚点。来源：`BG3-OFF-004`, `BG3-OFF-008`
- `事实`：`Patch 7` 继续把这条 `Act 1` 差异明确写回 `Act 2`：被击倒的 Minthara 会前往 `Moonrise Towers`，并在 `Act II` 对 `Act I` 的处理作出反应。来源：`BG3-OFF-002`
- `事实`：`Act 3` 的公开锚点并没有把后期写成“单一终局分支”，而是同时暴露城市阶段节点、更多 ending feedback、late-game `writing and flow` / `scripting` 维护，以及 `Category -> Quest -> Objective -> Step` 与 `trigger updates` 的结构语言。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此阶段 5 当前最稳的 `Quest Reactivity` 主干，不是把三幕内容抄成全任务表，而是把既有区域包压成同一条读回梯：`Grove / Goblin` 先把处理方式写成 `resolution matrix`，`Last Light / Moonrise / Gauntlet` 再把这些前史压向较少的收束点，`Rivington -> Wyrm's Crossing -> Lower City -> 终局组织与收束压力` 则把已被收束过的问题束重新过滤、门槛化、并排承接，并最终压向组织级 ending feedback。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这条主干当前最重要的增量，是证明 BG3 的任务反应性并不等于“分支很多”，而等于“同一处理方式会在跨长休、跨区域、跨 Act 的多个节点被反复读回”。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-008`
- `待验证问题`：当前最接近 `objective / step` 层的公开实锚，仍集中在 `Grove / Goblin -> Moonrise Towers` 这条链；`Act 3` 大部分 late-game 重排目前仍更适合停留在 `bundle / flow / ending feedback` 边界，而不是被写成私有 objective 表。来源：`BG3-OFF-002`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## Phase 5 Ceiling: 第二条公开跨阶段链为何暂不能成立

- `事实`：`Patch #3` 对 `Mountain Pass / Creche` 的公开暴露，已经足以证明 late `Act 1` 存在对话门槛、局部敌意变化、即时伙伴反应与 `camp night` 后果读取；但这些条目仍停在 `gate + tension + delayed camp readout` 这一组边界，并没有像 `Minthara -> Moonrise Towers` 那样把一个具体前史处理直接写到 `Act II` 的命名落点。来源：`BG3-OFF-016`
- `事实`：`Patch #2` 与 `Hotfix #3` 继续暴露 `Karlach` 的跨 `Act` 反思，以及 `Astarion`、`Voss`、`Mizora`、`Wyll` 等人的营地反应 / 对话可达性维护；它们证明“非 `Minthara` 的跨阶段读回确实存在”，但目前仍更像 `camp fold / dialogue accessibility bundle`，而不是一条具名的跨区域、跨 `Act` 任务链。来源：`BG3-OFF-007`, `BG3-OFF-010`
- `事实`：`Patch 7`、开发者访谈与公开 Journal 文档共同支持另一层更高阶判断：`Act 2` / `Act 3` 存在持续的 `writing and flow`、`scripting`、ending feedback 与 `trigger updates` 维护语言，因此中后段确实会继续重读前史；但除 `Minthara -> Moonrise Towers` 外，公开来源尚未给出第二条同级别的“具体 upstream handling -> 具体 downstream node -> 明确跨 Act 反应”链。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此阶段 5 的第四个子单元当前应收束为“second public chain ceiling”而不是“第二条对称 readback spine”：公开来源已足以证明存在若干支撑束，但它们更适合分别停留在 `gate / tension pack`、`camp fold bundle` 与 `ending feedback / organization bundle`，不能被强行升级成与 `Minthara` 案例同级的第二条主链。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `推断`：这一步反而让阶段 5 的主干更稳，因为仓库现在可以明确区分“唯一公开显式 spine”与“多个公开支撑 bundle”，而不必为了追求对称性回退成全任务表或把弱锚点过度升级。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-016`

## Phase 5 Boundary Lock: 哪些锚点还能继续逼近 `objective / step`

| 锚点组 | 当前最稳层级 | 为什么能写到这里 | 为什么必须停在这里 |
| --- | --- | --- | --- |
| `Nautiloid`、`Grove / Goblin`、`Mountain Pass / Creche` 的局部边界 | `objective / step` 邻近层 | 这几组都已有直接维护条目，能同时暴露 quest close、处理矩阵、门槛变化、敌意变化、即时反应与长休读取。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-015`, `BG3-OFF-016` | 仍缺足够公开锚点把全量开场分歧、首领顺序或 `Act 2` 切换规则写成事实表。 |
| `Act 1 地表主区`、`Underdark` | `objective pressure net` / `entry-diversion bundle` | 这两块已足以解释早期问题网如何续接开场状态，以及同一阶段内部如何被改道。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-006`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-015` | 公开来源仍不足以把完整早期路线顺序与地下入口矩阵压成 objective 表。 |
| `Shadow-Cursed Lands`、`Last Light / Moonrise / Gauntlet` | `pressure filter bundle` / `convergence pack` | 中盘公开锚点已足以证明高压过滤与前史读回落点存在。来源：`BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016` | 还不能把中盘内部风险变量、地点分工与完整 objective / step 映射写成事实表。 |
| 非 `Minthara` 营地反应与跨 Act 反思 | `camp fold / dialogue accessibility bundle` | `Karlach` 与多名角色的营地 scene / dialogue accessibility 都被单独维护。来源：`BG3-OFF-007`, `BG3-OFF-010` | 这些锚点分散在不同角色线，不能组成第二条具名跨区域主链。 |
| `Rivington -> Wyrm's Crossing -> Lower City -> 终局组织与收束压力` | late-game `filter / gate / parallel resolution / ending feedback bundles` | 公开来源已足以证明后期是高密度 bundle 的过滤、门槛化、并排承接与组织级结算。来源：`BG3-OFF-001`, `BG3-OFF-002`, `BG3-OFF-003`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` | 还不能把城市子块与终局组织内部的私有 objective / step 编排写成事实表。 |

- `推断`：因此阶段 5 现在最稳的写法，不是“继续追第二条主链”，而是承认只有少数局部锚点接近 `objective / step`；其余绝大多数结论都必须明确停在 bundle 层。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-010`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `推断`：这也解释了为什么当前仍不能把 `Quest Reactivity` 升级成全局 objective 表：仓库现在已有一条显式 spine，但更多是在管理“哪些状态会被继续读回、过滤、门槛化、折叠和结算”，而不是公开掌握了每条 shipped quest 的私有 step 排布。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

## Objective-Adjacent Narrowing: 只剩两个局部 fragment

- `事实`：`BG3-OFF-012`、`BG3-OFF-013`、`BG3-OFF-014` 只给了我们公开可验证的 `Category / Quest / Objective / Step` 与 `trigger update` 结构语言；要把某段判断继续压到 objective-adjacent 层，仍需要 patch / hotfix 直接点名局部 state、gate 或 timing fragment。来源：`BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：`Grove / Goblin` 里，`BG3-OFF-004` 直接点名了 `Minthara` 的 `knocked out / killed` 差异、`journal wording` 与“击倒 -> 长休 -> 再处理其他首领”的时序判定；`BG3-OFF-008` 则直接点名了营地中的对话可达性与 `companion reaction`。来源：`BG3-OFF-004`, `BG3-OFF-008`
- `推断`：因此 `Grove / Goblin` 当前只能把 `Minthara` 的局部 resolution-state fragment 再压一层：`knocked out / killed`、journal wording 与长休时序已足够 objective-adjacent；但营地里的对话可达性与 `companion reaction` 仍更稳地停在 delayed camp readout，而不是新的 objective fragment。来源：`BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `事实`：`Mountain Pass / Creche` 里，`BG3-OFF-016` 直接点名了 `Vlaakith` 拒绝后的对话阻塞、`Voss` 相关敌意变化、`Lae'zel` 的即时反应时机，以及 `camp night` 中对 `crèche` 后果的延迟反思。来源：`BG3-OFF-016`
- `推断`：因此 `Mountain Pass / Creche` 当前只能把局部门槛 / 敌意 / 即时反应再压一层：`Vlaakith / Voss / Lae'zel` 这组 local gate fragment 已足够 objective-adjacent；但 `camp night` 依旧只是 delayed readout，整块区域也仍不能被升级成 late `Act 1 -> Act 2` 的 objective map。来源：`BG3-OFF-016`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：这一步做完后，阶段 5 / `Quest Reactivity` 的正确收口口径就更清楚了：仓库拥有的不是“越来越细的 objective 总表”，而是“少数 local state / gate fragment + 一条显式 readback spine + 多个 bundle / fold / ending-feedback 层”。因此 `camp fold`、late-game bundle 与城市压缩层不再承担继续扩主链的任务。来源：`BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`, `BG3-OFF-016`
- `待验证问题`：若后续仍要继续推进 `Quest Reactivity`，优先级只应放在“是否还能找到非 `Minthara` 的同级局部 resolution fragment”与“是否还能找到 `Mountain Pass / Creche` 更直接的 act-transition gate 文本”，而不是继续横向扩 late-game bundle。来源：`BG3-OFF-004`, `BG3-OFF-016`

## 阶段 5 / Quest Reactivity 当前出口

- `推断`：当前公开来源下，`Quest Reactivity` 已完成统一收口：正式 spine 仍是既有 readback spine，而不是继续追第二条对称公开跨阶段主链。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：还能继续逼近 `objective / step` 的，只剩 `Minthara` 的局部 resolution-state fragment，与 `Vlaakith / Voss / Lae'zel` 的局部 gate fragment；它们之外的 `camp fold`、late-game `filter / gate / ending feedback` 都应继续停在 bundle / handoff 层。来源：`BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-016`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此本模块后续若没有更强官方来源，不应再扩 objective 总表、第二条公开主链或 late-game bundle，而应把阶段 5 视为已完成，并把下一步切向展示收束。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-008`, `BG3-OFF-016`

## Stage 6 Display Role

- `推断`：在当前展示链里，本模块承担的是“第二段右侧证据模块”职责：接住 `04_combat_and_environment.md` 已经建立的局部 agency，再把处理方式如何被状态记录、长休续接与跨区域读回压实给读者。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `推断`：因此本模块最适合被压成 `resolution matrix`、readback 梯与接力图右半边，而不适合重新滑回任务百科、地点总表或 objective 总表。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-008`
- `推断`：当前默认 handoff 必须是 `03_party_and_camp.md`；如果第二段在这里直接跳向实现验证，就会把“状态后来如何被营地 / 长休折返感知”提前吞掉。来源：`BG3-OFF-002`, `BG3-OFF-007`, `BG3-OFF-008`, `BG3-OFF-010`

## Stage 6 Release Anchor

- `SECOND-EXCERPT-001` 可安全摘录本文件中“处理方式 -> 即时状态 -> 长休 / 跨区域续接 -> 营地 / Act II 读出”的 `Grove / Goblin` 高层结论，以及 `Minthara -> Moonrise Towers -> Act II reaction` 这一条当前最稳的高可见 readback。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-008`
- `SECOND-ASSET-001` 在本文件中应被压成“`resolution matrix -> long-rest timing -> cross-region reread`”的右侧接力梯，而不是全游戏 objective / step 图。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`
- `SECOND-TRACE-001` 在本文件中的默认职责只能证明第二段右侧的高可见 readback 已成立；它不能把 `Grymforge` 与 `Minthara` 硬写成同一条具体因果链，也不能借此重新打开第二条对称 spine。来源：`BG3-OFF-002`, `BG3-OFF-004`, `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014`

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
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-016`
- `BG3-OFF-015`
- `BG3-PLY-002`
- `BG3-PLY-003`
- `BG3-PLY-004`

## Open questions

- 需要继续判断 Minthara 路径是代表性主案例，还是带明显后期正规化痕迹的特殊高可见案例。
- 需要为 Dark Urge bard 事件补更细的直接来源，否则它应继续作为辅案例而非主论证。
- 需要补一个更偏“空间 / 战斗绕解”的案例，避免任务与选择模块只剩叙事与营地反馈方向。
- 需要继续压实哪些支撑束可逼近 `objective / step`，哪些必须明确停在 `gate / tension`、`camp fold` 或 `ending feedback` 边界，而不是继续强行寻找“第二条对称主链”。
- 需要继续补官方对“reactivity”或等价概念的更直接表述，以支撑更高层总结。

## Revision notes

- 2026-04-25：新增阶段 5 / `Quest Reactivity` 当前出口小节，明确本模块在当前公开来源下已完成“单显式 spine + objective-adjacent 局部 fragment + bundle / handoff 边界”收口，不再继续追第二条公开跨阶段主链。

- 2026-04-22：设为仓库当前唯一主任务，等待首轮证据链补强。
- 2026-04-22：依据案例骨架与回写准备清单完成首轮正文回写；以 Minthara 击倒路径为主案例，Dark Urge bard 事件为辅案例。
- 2026-04-22：从 `04_combat_and_environment` 回流最小必要结论，补入“战斗 / 环境也是一种选择系统”的高层判断，但继续把具体 Grymforge / Grym 路径留在战斗模块验证。
- 2026-04-24：补入 `Nautiloid` 作为开场任务状态埋点的最小必要回写，但不把它升级成与 Minthara 同等级的后果主案例。
- 2026-04-24：补入 `Act 1 地表主区` 作为 opening state 续接层与“目标网”的最小必要回写，避免把地表误写成无结构自由漫游。
- 2026-04-24：补入 `Grove / Goblin` 作为 `Act 1` 第一块“状态回流网”区域包，明确这块更适合写成 `resolution matrix`，而不是派系二选一摘要。
- 2026-04-24：补入 `Underdark` 作为 `Act 1` 内部的“推进框架选择”区域包，明确任务反应性不只来自处理方式，也来自阶段内阅读顺序的改写。
- 2026-04-24：补入 `Grymforge` 作为 `Underdark` 下游的“遭遇内部继续分化选择”的区域压缩包，只把高层区域包结论回流到任务模块。
- 2026-04-24：补入 `Shadow-Cursed Lands` 作为 `Act 2` 的第一个“压力条件下的推进入口”，明确中盘任务反应性开始更紧地依附风险条件、前史读回与后续收束方向。
- 2026-04-24：补入 `Last Light / Moonrise / Gauntlet` 作为 `Act 2` 的“中盘收束点组”，明确这些节点更适合被写成前史读回与任务压缩的共同落点，而不是三个平行地点包。
- 2026-04-24：补入 `Act 3` 作为“高密度并行线 + 结算负载”的后期框架，明确这阶段应先被写成并行 quest bundle 与 ending feedback 同时增密，而不是城市地点导览。
- 2026-04-24：补入 `Wyrm's Crossing` 作为“桥梁 / 门槛后的第二层 quest bundle 重排包”，明确它承接 `Rivington` 的第一层过滤，但还不应被写成内城结算核。
- 2026-04-24：补入 `Lower City` 作为“更高密度的内城 quest bundle / 结算负载区”，明确它承接前两层过滤 / 门槛结构，把 late-game bundle 压到更短窗口内的并排承接与局部结算，而不是内城支线总表。
- 2026-04-24：补入 `终局组织与收束压力` 作为“组织级 quest bundle 压缩 / ending feedback 读取层”，明确它承接 `Lower City` 已并排承接的问题束，把它们继续压向更少、更硬的终局组织位与 ending feedback，而不是终局剧情提要或结局百科。
- 2026-04-24：新增“`Grove / Goblin -> Last Light / Moonrise / Gauntlet -> Rivington -> Wyrm's Crossing -> Lower City -> 终局组织与收束压力`”这条跨阶段状态回流主干，明确阶段 5 的首个任务不是补全任务表，而是先压实一条可复述的 readback spine。
- 2026-04-24：新增“`Nautiloid -> Act 1 地表主区 -> Underdark -> Mountain Pass / Creche`”这条上游前置链，明确阶段 5 的第二个任务不是重写 `Act 1` 总表，而是给既有 readback spine 补齐入口 / 改道 / 门槛前史。
- 2026-04-24：新增“`Mountain Pass / Creche -> Shadow-Cursed Lands -> Last Light / Moonrise / Gauntlet`”这条 late `Act 1` / early `Act 2` 交接接缝，明确阶段 5 的第三个任务不是重写 `Act 2` 地点目录，而是把 gate、pressure filter 与 convergence pack 三层职责压实到同一条中盘接缝里。
- 2026-04-24：新增“第二条公开跨阶段链证据上限”结论，明确除 `Minthara -> Moonrise Towers` 外，当前公开来源最多只能再压出 `gate / tension`、`camp fold` 与 `ending feedback` 三类支撑 bundle，暂不能安全升级为第二条对称主链。
- 2026-04-24：新增 objective-adjacent narrowing 结论，明确 `Grove / Goblin` 只剩 `Minthara` 的局部 resolution-state fragment 能继续逼近 `objective / step`，`Mountain Pass / Creche` 只剩局部门槛 / 敌意 / 即时反应 fragment 能继续逼近 `objective / step`；`camp readout`、`camp fold` 与 late-game bundle 不再承担继续扩主链的任务。
