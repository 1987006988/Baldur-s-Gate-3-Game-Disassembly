# Case Note

## Case name

Mountain Pass / Creche：结构门槛与伙伴张力包

## Related module

`docs/03_analysis/01_macro_structure.md`

次级回流模块：
- `docs/03_analysis/03_party_and_camp.md`
- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/05_implementation_validation.md`

## Question

`Mountain Pass / Creche` 能否被写成 `Act 1` 后段的“结构门槛 + 伙伴张力”叠层包：进入与处理它既是在过一个高压区域门槛，也是在承受 `Lae'zel / githyanki / Vlaakith / Voss` 相关的即时与延迟反应？

## Research boundary

- 本 note 只处理 `Mountain Pass / Creche` 作为 late `Act 1` gate-and-tension pack 的价值，不扩成完整剧情复述、派系年表或 `gith` 背景整理。
- 本 note 不把 `Lae'zel` 单独写成角色专章；这里只保留她与区域门槛直接耦合的反应与后续读取边界。
- 本 note 不提前写死 `Act 2` 切换规则；与阶段切换直接相关的技术判断继续留在实现验证层。

## First-pass source set

- `BG3-OFF-003`
- `BG3-OFF-016`

## Gate / tension pack

| 维度 | 当前能写成事实的部分 | 当前最稳判断 | 仍待验证 |
| --- | --- | --- | --- |
| 区域门槛 | `Patch #3` 暴露了两个直接与门槛/情境切换相关的维护点：拒绝 `Vlaakith` 后的多余检定会错误阻塞后续对话；`Rosymorn Monastery gate` 的爆炸倒计时需要在进入 `Astral Plane` 后正确取消。来源：`BG3-OFF-016` | 这块不是普通过道，而是带明确情境门槛与阶段压力的区域包。 | 这些门槛与 `Act 2` 进入规则的具体映射，目前还不能公开写死。 |
| 伙伴张力 | `Patch #3` 直接修复了 `Lae'zel` 在 `Crèche Y'llek` 遇到 `Dream Visitor` 后的即时反应，以及 `Avatar Lae'zel` 在 `camp night` 中过早反思 `crèche` 后果的问题。来源：`BG3-OFF-016` | 这说明伙伴反应并不是区域之后才附带发生，而是与局部门槛事件和营地后续读取一起被维护。 | 哪些反应只属于 `Lae'zel` 这一条线，哪些能代表更广义的“区域后果折返到营地”，还需继续筛。 |
| 处理方式 / 局部敌意 | `Patch #3` 明确写到：如果 `Lae'zel` 在与 `Voss` 的互动中成功通过 `Deception` 检定，`githyanki` 不应继续保持敌对。来源：`BG3-OFF-016` | 这块的选择不是抽象立场表达，而会改写局部敌意与后续通过方式。 | 这类敌意变化会向后传播到多大范围，目前还缺更直接的公开来源。 |
| 结构语言 | Adam Smith 用 `Swiss cheese` 描述 BG3 的场景 / 路径组织，强调同一目标存在多个洞口与进入方式。来源：`BG3-OFF-003` | 把 `Mountain Pass / Creche` 写成“高压门槛包”并不违背 BG3 的多入口逻辑；它更像 late `Act 1` 对这套逻辑的收紧与加压。 | 这块内部的多入口具体如何组织，还没有足够公开材料压成事实表。 |

## What can be written as facts

- `事实`：Adam Smith 在 Xbox Podcast 中把 BG3 的场景 / 路径结构比作 `Swiss cheese`，强调同一目标存在多个进入方式。来源：`BG3-OFF-003`
- `事实`：`Patch #3` 修复了拒绝 `Vlaakith` 后一个会阻塞后续对话启动的多余 skill check。来源：`BG3-OFF-016`
- `事实`：`Patch #3` 修复了 `Lae'zel` 在 `Crèche Y'llek` 遇到 `Dream Visitor` 后的反应时机，使其会在对话结束后立即触发。来源：`BG3-OFF-016`
- `事实`：`Patch #3` 修复了 `Rosymorn Monastery gate` 的爆炸倒计时，使其在进入 `Astral Plane` 后会被正确取消。来源：`BG3-OFF-016`
- `事实`：`Patch #3` 明确写到，如果 `Lae'zel` 在与 `Voss` 的互动中成功通过 `Deception` 检定，`githyanki` 不应继续保持敌对。来源：`BG3-OFF-016`
- `事实`：`Patch #3` 还修复了 `Avatar Lae'zel` 在 `camp night` 中过早反思 `crèche` 后果的问题；在真正访问 `zaith'isk` 之前，这段反思不应提前发生。来源：`BG3-OFF-016`

## What can only be written as inferences

- `推断`：`Mountain Pass / Creche` 当前最稳的写法不是单一同伴剧情专章，而是 `Act 1` 后段的高压门槛包：区域门槛、权威谈判、局部敌意、即时伙伴反应与营地后续读取在同一块里被同时维护。基于 `BG3-OFF-003`, `BG3-OFF-016`
- `推断`：相较于 `Underdark` 的“阶段重构”与 `Grymforge` 的“遭遇压缩”，这块更像 late `Act 1` 对自由推进结构的一次加压测试：问题不再只是“从哪进 / 怎么解”，而变成“你能不能过门槛、如何处理阵营权威、以及同伴如何立即与延迟回应”。基于 `BG3-OFF-003`, `BG3-OFF-016`
- `推断`：这也是它更适合先回写到 `01_macro_structure.md` 与 `03_party_and_camp.md` 的原因：公开来源首先暴露的是结构门槛与反应边界，而不是完整任务矩阵。基于 `BG3-OFF-016`

## What must remain open questions

- `待验证问题`：`Mountain Pass / Creche` 与 `Act 2` 切换之间，哪些边界能继续公开压到 `Journal / objective / step` 层？
- `待验证问题`：这块的哪些后果会稳定折返到第一批 `camp night`，哪些只在局部对话或敌意变化中被读取？
- `待验证问题`：是否还需要补 1 条更直接讨论区域进入警告、阶段切换或门槛条件的官方来源，来继续压实“高压入口”这一层判断？

## Source IDs

- `BG3-OFF-003`
- `BG3-OFF-016`

## Notes

- 当前最稳的仓库口径应是：`Mountain Pass / Creche` 主要证明 BG3 在 `Act 1` 后段会把“结构门槛 + 伙伴张力”叠成同一块区域包，而不是证明某一条 `Lae'zel` 剧情支线本身有多完整。
- 这份 note 的作用不是替代未来的 `Act 2` 框架 note；它只负责说明在进入中盘前，BG3 已经开始把区域权限、局部敌意与营地后果压到同一块。
