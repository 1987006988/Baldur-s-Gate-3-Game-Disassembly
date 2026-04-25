# Stage 6 Third Section Release Units

## Scope

本文只承载阶段 6 第七个子单元的首批实际发布单元：

- `第三段：延迟反馈折叠`

这里不重复最低配置，也不替代 `presentation_forms.md`。它只回答一件事：

> 第三段当前已经能实际拿去制作的第一组 `excerpt card / asset spec / traceback card` 到底是什么？

## 第三段：延迟反馈折叠

### Excerpt Card | `THIRD-EXCERPT-001` | `camp fold / delayed feedback` 折返层卡

- 卡片目标：把“营地 / 长休为什么是反馈折叠层”与“哪些营地锚点只能停在 supporting bundle”压进同一组实际发布文案
- 主展示文案：
  - “BG3 的营地 / 长休重要，不是因为它额外提供了一层人物氛围，而是因为它把前面分散在任务推进、区域压力与关系张力里的状态重新折成玩家可见的延迟反馈。”
  - “从 `Dark Urge bard` 的局部 `camp-state shift`，到 `Grove / Goblin` 的 delayed camp readout，再到 `Mountain Pass / Creche` 的 `camp night` reread，玩家会在营地重新读到自己刚才造成的变化。”
- 边界条文案：
  - “`BG3-OFF-007` 与 `BG3-OFF-010` 当前只稳定支撑 `reflection / roster-state` 与 `dialogue accessibility maintenance` supporting bundles；它们能证明营地反馈被持续维护，但还不能被并排画成第二条公开营地主干。”
- 默认 handoff：
  - `docs/03_analysis/05_implementation_validation.md`
- 直接锚点：
  - `docs/03_analysis/03_party_and_camp.md`
  - `docs/03_analysis/05_implementation_validation.md`
- 使用边界：
  - 这张卡只负责证明“第三段是折返层”
  - 不能把它扩写成 camp scene 清单、同伴人物志或恋爱系统总览
  - 不能把 `Dark Urge bard`、`Minthara`、`Lae'zel`、`Karlach` 硬写成同一条具体因果链

### Asset Spec | `THIRD-ASSET-001` | `task result -> camp fold -> reread` 折返图

- 图的职责：把第三段画成“状态如何在营地 / 长休重新可见”的折返关系，而不是 camp scene 年表或同伴 roster 图
- 必须出现的结构：
  - 上游输入：
    - `Act 1 地表主区`
      - 标注：`upstream state-density`
    - `Dark Urge bard`
      - 标注：`local camp-state shift`
    - `Grove / Goblin`
      - 标注：`first delayed camp readout`
    - `Mountain Pass / Creche`
      - 标注：`camp-night reread`
    - `Last Light / Moonrise / Gauntlet`
      - 标注：`convergence-adjacent reread`
  - 中央折返节点：
    - `camp / long rest readout`
      - 标注：`state regrouping -> dialogue accessibility -> relationship feedback`
  - 右侧交接：
    - `supporting bundles / handoff boundary`
      - 标注：`reflection / roster-state`, `dialogue accessibility maintenance`, `ending-feedback handoff`
- 必须出现的 handoff：
  - 图尾必须标出“下一段进入 `05_implementation_validation.md`，说明哪些折返已经够稳、哪些仍只是当前最强解释”
- 视觉禁区：
  - 不把第三段画成 camp scene 列表或同伴 roster 网
  - 不把 `BG3-OFF-007`、`BG3-OFF-010` 与 late-game `ending feedback` 重新画成第二条对称 camp spine
  - 不把终局 `ending-feedback handoff` 反向吞回第三段主卡中心

### Traceback Card | `THIRD-TRACE-001` | 第三段折返层回链

- 读者可见主张：第三段负责证明 BG3 的反应性不只被写进任务流，也会在营地 / 长休被重新折回成可感知反馈；它是“状态 reread 层”，不是平行人物附录
- 文档回链：
  - `docs/03_analysis/03_party_and_camp.md`
  - `docs/03_analysis/05_implementation_validation.md`
- Source ID 回链：
  - `BG3-OFF-002`
  - `BG3-OFF-005`
  - `BG3-OFF-007`
  - `BG3-OFF-008`
  - `BG3-OFF-010`
  - `BG3-OFF-016`
  - `BG3-PLY-002`
- 当前安全层级：
  - 可安全发布“`camp fold / delayed feedback` 已成立，并且存在 `supporting bundle / handoff` 边界”这一层
  - 可安全发布“`Dark Urge bard`、`Grove / Goblin`、`Mountain Pass / Creche` 与 `Act II` 收束点组共同构成第一条公开营地折返主干”这一层
- 不可越级之处：
  - 不可把这张 trace card 扩写成长休调度规则、触发优先级模型或 camp scene 全表
  - 不可把 `reflection / roster-state`、`dialogue accessibility maintenance` 或 late-game `ending feedback` 升格成第二条公开营地主干
  - 不可让第三段提前吞掉收尾段的证据分级职责

## 当前完成定义

- `第三段：延迟反馈折叠` 已有首个可复用的 `excerpt card / asset spec / traceback card`
- 这组单元已能同时回链到 `03_party_and_camp.md`、`05_implementation_validation.md` 与对应 `Source ID`
- 第三段的“主折返层 + supporting-bundle 边界条”口径已被写死，后续制作不需要再回头重写 queue
- 下一步应切到“收尾段：证据分级”的首批实际发布单元，而不是继续回头重写入口页 / 第一段 / 第二段 / 第三段的规则
