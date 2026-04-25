# Stage 6 Final Section Release Units

## Scope

本文只承载阶段 6 第八个子单元的首批实际发布单元：

- `收尾段：证据分级`

这里不重复最低配置，也不替代 `presentation_forms.md`。它只回答一件事：

> 收尾段当前已经能实际拿去制作的第一组 `excerpt card / asset spec / traceback card` 到底是什么？

## 收尾段：证据分级

### Excerpt Card | `FINAL-EXCERPT-001` | `facts / inferences / open questions` 证据分级主卡

- 卡片目标：把“前四段已经建立了什么”与“这些结论分别处在什么证据强度层”压进同一组实际发布文案，而不是把 `05_implementation_validation.md` 重写成技术细节导论。
- 主展示文案：
  - “这套 BG3 拆解当前最稳的公开表达，不是‘我们已经反编译出完整实现’，而是‘我们已经分别为入口边界、命题与导航、局部 `agency`、状态读回与营地折返建立了可追溯的公开证据入口，但这些入口的可说强度并不相同。’”
  - “因此收尾段必须把前四段重新分成三层：可被官方补丁、访谈与 Journal / modding 文档直接支撑的事实；由多个公开入口共同压实的当前最强解释；以及仍需停在 objective-adjacent fragment、supporting-bundle threshold 与方法级开放问题层的未决边界。”
- 边界条文案：
  - “`BG3-OFF-011` 到 `BG3-OFF-014` 提供的是公开验证语言，不是 shipped content 的私有脚本实锤；`BG3-OFF-002`、`BG3-OFF-007`、`BG3-OFF-010`、`BG3-OFF-016` 暴露的是维护边界，不等于所有后果都已被完全枚举。”
- 默认结束动作：
  - `结束并反向回链前四段 actual units`
- 直接锚点：
  - `docs/03_analysis/05_implementation_validation.md`
  - `docs/00_project/stage6_entry_first_section_release_units.md`
  - `docs/00_project/stage6_second_section_release_units.md`
  - `docs/00_project/stage6_third_section_release_units.md`
- 使用边界：
  - 这张卡只负责把前四段重分级。
  - 不能把它扩写成实现架构图、全局 objective 总表或“已完全解释 BG3”的总结口号。
  - 不能把 `待验证问题` 抹平成已解决结论。

### Asset Spec | `FINAL-ASSET-001` | `claim tier -> document anchor -> source entry` 证据分级矩阵

- 图的职责：把收尾段画成“前四段 actual units 的证据分级矩阵”，而不是画成新的技术结构图或来源堆砌表。
- 必须出现的结构：
  - 行：
    - `入口页`
      - 标注：`project question + anti-story-recap boundary + benchmark traceback`
    - `第一段：命题与导航`
      - 标注：`high-level claim + region / pressure ladder`
    - `第二段：局部行动到状态回流`
      - 标注：`local agency + visible readback`
    - `第三段：延迟反馈折叠`
      - 标注：`camp fold + supporting-bundle boundary`
  - 列：
    - `事实`
    - `当前最强解释`
    - `待验证问题`
    - `traceback path`
  - 右侧回链：
    - `README / deconstruction_display_overview`
    - `00_core_thesis / 01_macro_structure`
    - `04_combat_and_environment / 02_quests_and_choices`
    - `03_party_and_camp`
    - `05_implementation_validation`
  - `入口页` 这一行必须显式保留：
    - `BMK-002 / BMK-003`
    - `BG3-OFF-001 / BG3-OFF-003`
    - 以及 `README.md` 与 `docs/00_project/deconstruction_display_overview.md` 的双重 traceback path
- 必须出现的开放问题条：
  - `implementation validation checklist` 是否要独立成方法文件
  - objective-adjacent fragment 未来需要什么级别的官方来源才能继续升级
  - supporting bundle 升格为 spine anchor 的最低证据门槛
- 视觉禁区：
  - 不把矩阵画成“只剩事实列”的胜利图
  - 不把 Journal / Osiris 文档单独画成“实现已证实”列
  - 不让收尾段吞掉前四段本身的 excerpt / asset / trace 职责

### Traceback Card | `FINAL-TRACE-001` | 收尾段证据分级回链

- 读者可见主张：收尾段负责证明“这套发布包已经拥有一张可追溯的证据分级矩阵”，而不是证明“仓库已经拥有 BG3 的完整私有实现图”。
- 文档回链：
  - `docs/03_analysis/05_implementation_validation.md`
  - `docs/00_project/stage6_entry_first_section_release_units.md`
  - `docs/00_project/stage6_second_section_release_units.md`
  - `docs/00_project/stage6_third_section_release_units.md`
- Source ID 回链：
  - `BMK-002`
  - `BMK-003`
  - `BG3-OFF-011`
  - `BG3-OFF-012`
  - `BG3-OFF-013`
  - `BG3-OFF-014`
  - `BG3-OFF-016`
  - `BG3-OFF-002`
  - `BG3-OFF-007`
  - `BG3-OFF-010`
- 当前安全层级：
  - 可安全发布“`入口页`、第一段、第二段、第三段对应的公开证据入口已经建立，但它们必须重新分成 `事实 / 推断 / 待验证问题` 三层”这一层。
  - 可安全发布“modding / Journal 文档当前提供的是公开验证语言与结构边界，而不是 shipped content 的直接实现实锤”这一层。
- 不可越级之处：
  - 不可把这张 trace card 扩写成新的总论页或方法宣言。
  - 不可把开放问题条抹掉，只保留“已经证实”的部分。
  - 不可让收尾段反向取代前四段的正文与实际单元。

## 当前完成定义

- `收尾段：证据分级` 已有首个可复用的 `excerpt card / asset spec / traceback card`
- 这组单元已能同时回链到 `入口页`、第一段、第二段、第三段这四组实际单元、`05_implementation_validation.md` 与对应 `Source ID`
- 收尾段的“重分级而不越级证实”口径已被写死，后续制作不需要再回头重写 queue
- 阶段 6 的五段首批实际发布单元在当前计划下已闭合；下一步如继续推进，应先做总装配 / 审阅，而不是重写任一段既有单元
