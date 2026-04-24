# Source Note

## Source ID

`BMK-003`

## Title

How my Boss Key dungeon graphs work

## Type

benchmark / space-graph method note

## Why this source matters

这条来源把 Boss Keys 的核心图式方法写得很清楚：入口、Boss、钥匙、锁门、关键道具、障碍和开关都可以被抽象成一张依赖图。对 BG3 来说，这非常适合拿来处理“高密度区域包、多入口推进、门槛、绕路与回环”，但不能单独解释状态回流与营地折叠。

## Reliable facts

- 作者明确说，这套 graph system 是为分析 Zelda dungeon 设计出来的，也可以拿来分析其他游戏或辅助做新游戏。
- 该方法用固定符号表示入口、Boss、小钥匙、锁门、关键道具、障碍和开关。
- 作者示范时先画地图，再根据“当前物理可达什么”去构造依赖图。

## Useful inferences

- `推断`：BG3 的区域包分析很适合借用 Boss Keys 的“入口 / 门槛 / 障碍 / 回环”图式来整理空间骨架。
- `推断`：但 BG3 还必须额外补“任务状态、营地反馈、同伴反应”的第二层图，否则会只剩空间分析。

## Limits and bias

- 这条方法原本主要面向 dungeon / world design，不直接处理叙事状态回流。
- 它更适合做区域包的空间骨架，不适合单独充当 BG3 的总逻辑。

## Where to use

- `docs/00_project/deconstruction_display_overview.md`
- `docs/00_project/deconstruction_granular_codex_plan.md`

## Follow-up questions

- `待验证问题`：BG3 的哪些区域最适合直接画 Boss Keys 式依赖图？
- `待验证问题`：是否需要为 BG3 自定义“状态回流 / 营地折叠”图例？
