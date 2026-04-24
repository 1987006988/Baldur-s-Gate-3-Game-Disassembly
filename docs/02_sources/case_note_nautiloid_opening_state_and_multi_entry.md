# Case Note

## Case name

Nautiloid 开场：多入口与早期状态埋点

## Related module

`docs/03_analysis/01_macro_structure.md`

次级回流模块：

- `docs/03_analysis/02_quests_and_choices.md`
- `docs/03_analysis/04_combat_and_environment.md`
- `docs/03_analysis/05_implementation_validation.md`

## Question

`Nautiloid` 能否作为 BG3 的第一个“模板区域包”，说明开场并不是纯教程，而是一个把多入口、早期战斗、队友收编与初始任务状态压缩到同一空间里的小型证明场？

## Research boundary

- 本 note 只处理 `Nautiloid` 自身如何组织空间入口、任务物件、队友加入与状态清理。
- 不延伸到海滩之后的长期后果链，也不把后续营地反馈提前写进本案。
- 不把开场流程复述成剧情摘要。

## First-pass source set

- `BG3-OFF-001`
- `BG3-OFF-002`
- `BG3-OFF-003`
- `BG3-OFF-012`
- `BG3-OFF-013`
- `BG3-OFF-014`
- `BG3-OFF-015`

## What can be written as facts

- `BG3-OFF-003` 直接说明，Larian 用 `Swiss cheese` 语言描述 BG3 的场景 / 路径组织方式：同一目标存在多个洞口与进入方法。
- `BG3-OFF-001` 说明官方对 BG3 的高层定位并不是单纯线性冒险，而是把区域推进、选择后果、队伍协作与回合制互动并列呈现。
- `BG3-OFF-015` 说明 `Nautiloid` 教程段包含明确的 narrator 触发物、可失败 / 受限的舱门检定、被高亮为 quest item 的关键物件，以及坠毁后的 harmful condition 清理。
- `BG3-OFF-002` 说明开场主任务 `Escape the Nautiloid` 的关闭条件会因为多人模式下的对话时序出错，表明它不是纯展示段，而是正式 Journal / flow 链的一部分。
- `BG3-OFF-002` 还说明 tutorial 结束后，角色身上的部分 buff 与装备状态需要被重新结算或交还，官方甚至专门修复了 `Lae'zel` 的 tutorial buff 持续与 `Shadowheart / Lae'zel` 的装备交接问题。
- `BG3-OFF-012`, `BG3-OFF-013`, `BG3-OFF-014` 共同说明：公开可见的任务结构至少能以 `Category → Quest → Objective → Step` 以及相应 trigger updates 的方式被理解，因此 `Escape the Nautiloid` 这类开场目标在验证层上应被视为真实 quest/objective 流，而不是纯教程标签。

## What can only be written as inferences

- `推断`：`Nautiloid` 已经把“空间多入口、任务目标、关键物件、同伴加入、战斗试探、状态清理”压成一个小型区域包，所以它更像 BG3 核心逻辑的缩略样本，而不是开场例外。
- `推断`：早期队友收编在这里不只是人物介绍，它与检定门槛、关键物件、战斗风险和后续状态交接绑定在一起。
- `推断`：如果连开场区域都需要长期维护 quest close、角色状态清理与物件交接，那么后续区域包以类似方式组织状态就不是偶然现象。

## What must remain open questions

- `待验证问题`：哪些 `Nautiloid` 阶段状态会继续回流到海滩后的招募、对话或任务判断，哪些会在坠毁时被统一清除？
- `待验证问题`：哪些开场元素只是强教程属性，哪些已经足以外推为后续区域包设计？
- `待验证问题`：是否值得在下一轮单独拆出 `case_note_nautiloid_early_party_recruitment.md`，还是继续把队友收编放在本 note 中即可？

## Notes

- 当前最稳的仓库口径应是：`Nautiloid` 先承担“模板区域包”的证明职责，不承担长链后果主案例职责。
- 它最适合反向支撑四个方向：
  - 宏观结构：起点就不是单一路径教程
  - 任务回流：开场就有正式目标、状态与关闭条件
  - 战斗 / 环境：第一块空间已经要求玩家把战斗与路径一起思考
  - 实现验证：补丁与 Journal / trigger 公开文档足以提供最小验证入口
