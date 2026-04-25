# Stage 6 Second Section Release Units

## Scope

本文只承载阶段 6 第六个子单元的首批实际发布单元：

- `第二段：局部行动到状态回流`

这里不重复最低配置，也不替代 `presentation_forms.md`。它只回答一件事：

> 第二段当前已经能实际拿去制作的第一组 `excerpt card / asset spec / traceback card` 到底是什么？

## 第二段：局部行动到状态回流

### Excerpt Card | `SECOND-EXCERPT-001` | 局部 agency 与状态读回的章节双联摘录

- 卡片目标：把“玩家先在哪一层感到自己能这样试”与“系统后来怎样把处理方式写回状态”压进同一组章节双联摘录
- 左侧展示文案：
  - “BG3 的战斗 / 环境自由感，不只是数值优化，而是系统允许玩家把眼前遭遇改写成空间、位置、机关与开战方式共同组成的问题。”
  - “从 `Nautiloid` 的压缩样本，到 `Act 1 地表主区` 的常态化，再到 `Grymforge` 的成熟 `combat-agency compression pack`，玩家会先学会把局部遭遇读成‘我能这样试’。”
- 右侧展示文案：
  - “BG3 的任务反应性也不只是分支数量，而是会把处理方式写进后续状态：`Grove / Goblin` 能被压成一份 `resolution matrix`，其中 `Minthara` 的 `knocked out / killed`、长休时序与 `Act II` 读回都有公开锚点。”
  - “第二段因此先让读者看见局部 agency，再让读者看见这种 agency 不是空气，而会在后续任务流里被重新读取。”
- 默认 handoff：
  - `docs/03_analysis/03_party_and_camp.md`
- 直接锚点：
  - `docs/03_analysis/04_combat_and_environment.md`
  - `docs/03_analysis/02_quests_and_choices.md`
- 使用边界：
  - 左侧只负责证明局部 action space 的成立
  - 右侧只负责证明高可见 readback 的存在
  - 不能把这组双联摘录误写成“`Grymforge` 直接导致 `Moonrise Towers` 读回”的单一案例因果链

### Asset Spec | `SECOND-ASSET-001` | `local agency -> readback` 接力图

- 图的职责：把第二段画成“章节接力关系”，而不是画成单一事件树或全任务总表
- 必须出现的结构：
  - 左侧：`Nautiloid -> Act 1 地表主区 -> Grymforge -> Shadow-Cursed Lands`
    - 标注：`compressed sample -> normalization -> mature compression pack -> regional pressure loop`
  - 中央：`处理方式被系统记账`
    - 标注：这里只表达“局部行动与后续读回属于同一展示段”，不表达单一案例因果同一
  - 右侧：`Grove / Goblin -> Moonrise Towers / Act II readback`
    - 标注：`resolution matrix -> long-rest timing -> cross-region reread`
- 必须出现的 handoff：
  - 图尾必须标出“下一段进入 `03_party_and_camp.md`，解释这些状态如何在营地 / 长休被折返读出”
- 视觉禁区：
  - 不把 `Grymforge` 直接画箭头连到 `Moonrise Towers`
  - 不把整张图扩成全游戏 objective / step 总表
  - 不把 late-game supporting bundle 重新画成第二条对称 spine

### Traceback Card | `SECOND-TRACE-001` | 第二段双联卡回链

- 读者可见主张：第二段负责把“局部 agency”与“状态读回”并排压实，证明 BG3 的高反应性不是只有对白分支，也不是只有战术自由，而是二者之间存在可追溯的接力关系
- 文档回链：
  - `docs/03_analysis/04_combat_and_environment.md`
  - `docs/03_analysis/02_quests_and_choices.md`
  - `docs/03_analysis/05_implementation_validation.md`
- Source ID 回链：
  - `BG3-OFF-003`
  - `BG3-OFF-006`
  - `BG3-OFF-002`
  - `BG3-OFF-004`
  - `BG3-OFF-012`
  - `BG3-OFF-013`
  - `BG3-OFF-014`
  - `BG3-PLY-004`
- 当前安全层级：
  - 可安全发布“局部 action space 与高可见 readback 属于同一展示段”的层级
  - 可安全发布“`Grymforge` 是当前最稳的局部 agency 锚点，`Minthara -> Moonrise Towers` 是当前最稳的高可见 readback 锚点”这一层
- 不可越级之处：
  - 不可把这张 trace card 扩写成“所有局部解法都会被同级别读回”
  - 不可把 `Grymforge` 与 `Minthara` 压成同一条具体因果链
  - 不可把第二段升级成全游戏 objective 总表、第二条对称 spine，或提前吞掉第三段的营地折返职责

## 当前完成定义

- `第二段：局部行动到状态回流` 已有首个可复用的 `excerpt card / asset spec / traceback card`
- 这组单元已能同时回链到 `04_combat_and_environment.md`、`02_quests_and_choices.md` 与对应 `Source ID`
- 第二段的“章节接力关系”与“单一案例因果链”边界已被写死，后续制作不需要再回头重写 queue
- 下一步应切到“第三段：延迟反馈折叠”的首批实际发布单元，而不是继续回头重写入口页 / 第一段 / 第二段规则
