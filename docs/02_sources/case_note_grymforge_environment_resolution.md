# Case Note

## Case name

Grymforge / Grym 环境解法路径

## Related module

`docs/03_analysis/04_combat_and_environment.md`

次级回流模块：`docs/03_analysis/02_quests_and_choices.md`

## Question

能否用 Grymforge / Grym 这一类遭遇，说明 BG3 的“选择”不只发生在对白与任务日志里，也发生在战斗与环境解法层？

## 为什么锁定这条案例

- 它能把“选择”从对白、任务状态与营地反馈，扩展到战前布置、路线选择、环境利用与机关调用。
- 它和 `04_combat_and_environment` 天然同构，更适合作为战斗模块主案例，而不是直接塞进任务模块当主论据。
- 它仍然能反向支撑 `02_quests_and_choices`：说明 BG3 的选择系统并不只靠叙事分支成立。

## 本轮区域包收束口径

- 这份 note 当前应承担的不是“单个 Boss 战打法对照”，而是 `Underdark` 下游第一块高密度 `encounter bundle` 的区域包结论。
- 稳定可写的重点是：`Grymforge` 如何把区域推进、环境利用、复杂遭遇与任务语境压到同一块，而不是罗列全部机关或 cheese。
- 向 `02_quests_and_choices.md` 的回流应只停在高层边界：战斗 / 环境解法本身也是选择系统的一部分。

## 当前可确认的案例方向

- 以 `Grymforge / Grym` 为中心，观察玩家如何通过高差、落体、机关、远程击打拉杆、非常规站位与战前准备来重写战斗解决方式。

## 初步证据判断

### 可写为事实

- `BG3-OFF-003` 提供了高层设计意图：Adam Smith 明确把 BG3 的关卡设计比作 `Swiss cheese`，强调多入口结构与非常规 problem-solving。
- `BG3-OFF-006` 提供了高层区域框架：官方把 Grymforge 明确描述为包含 `new questlines, choices, ... complex combat encounters` 的区域，并在同一更新中引入新 Weapon Actions 与更多战术能动性。
- `BG3-PLY-004` 可作为案例入口，证明玩家确实把 `Grymforge / Grym` 理解为一个可以通过环境与空间重写的遭遇场景；但这只能写成玩家案例事实，不能写成系统普遍事实。

### 只能写为推断

- `Grymforge / Grym` 很适合作为“战斗 / 环境也是选择系统”的主案例，因为它把任务推进、空间利用与遭遇解决绑定在一起。
- 它可以补足 `02_quests_and_choices` 当前偏重叙事反馈的结构偏差。
- 但在当前证据结构下，它更适合先作为 `04_combat_and_environment` 的主深挖案例，再反向支撑任务模块。

### 必须保留为待验证问题

- 是否有更直接的官方来源支持这条案例，而不只停留在开发者高层表述、区域框架与社区案例之间？
- 哪一条具体执行路径最适合进入稳定正文，而不是只停留在“案例方向”层？
- 除高层判断外，哪些具体结论应该继续留在战斗模块，哪些才值得回流到任务模块？

## Notes

- 当前已确认的仓库口径是：这条案例首先属于 `04_combat_and_environment`，其次才在 `02_quests_and_choices` 中承担最小必要的高层回流作用。
- 因此它不再被视为“任务模块待补主案例”，而是“战斗模块主案例，可回流支撑任务模块”的桥接案例。

## 区域包结论

- `推断`：`Grymforge` 现在已经可以被写成 `Act 1` 第一块早期 `encounter bundle / combat-agency compression pack`，因为公开来源已同时暴露 `Underdark -> Grymforge` 的下游 setup、区域级 `choices + complex combat encounters` 框架，以及玩家如何把这类遭遇理解成环境重写问题。基于 `BG3-OFF-003`, `BG3-OFF-006`, `BG3-PLY-004`
- `推断`：对仓库主链来说，这块最重要的价值不是证明某条著名打法永远稳定，而是证明 BG3 会把“我怎么处理这场复杂遭遇”本身做成区域推进体验的一部分。基于 `BG3-OFF-003`, `BG3-OFF-006`
- `待验证问题`：现阶段仍不宜把具体熔炉机关、落体或远程拉杆路径直接升级成 objective / step 事实链；更细的路径判断仍应留在后续战斗模块与实现验证层继续压实。

## Revision notes

- 2026-04-24：将本 note 从“战斗补强方向”收束为 `Grymforge` 首轮区域包的工作底稿，明确主结论、回流边界与待验证范围。
