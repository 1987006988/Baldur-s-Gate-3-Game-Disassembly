# Case Note

## Case name

Minthara 营地反应链

## Related module

`docs/03_analysis/03_party_and_camp.md`

## Question

这个案例能否说明 BG3 会把前序招募 / 状态差异与关系反馈折返到营地对话层，并把“能否在营地被回应”本身做成正式维护的系统边界？

## What the player sees

- 玩家通过特定路径让 Minthara 留在可继续互动的状态。
- 玩家回到营地后，不只是确认她是否存在，还会期待能否继续对话、是否会收到同伴反应、关系线是否继续推进。
- 一旦这些营地对话或 companion reaction 缺失，玩家会直接感到“后果没有被接住”。

## System reading

- 这个案例的关键不是 Minthara 作为单个角色，而是营地承担了状态可达性、关系反馈和同伴评论的汇流点。
- `BG3-OFF-008` 直接暴露了三类需要单独维护的边界：
  - 能否在营地与 Minthara 对话
  - 同伴是否会对玩家与 Minthara 的关系做出反应
  - 营地外的队伍处理是否会影响营地内的反馈可达性
- `BG3-OFF-002` 提供更高层的补丁背景，说明 camp night、character reaction、writing / flow 会持续被修复，因此这不是单条角色文本，而是营地反馈链的一部分。

## Evidence status

- `事实`：
  - `BG3-OFF-008` 直接确认 Minthara 的营地对话可达性与 companion reaction 会被单独热修。
  - `BG3-OFF-008` 直接确认“在营地外解散后，回营地无法对话”属于需要修复的问题。
  - `BG3-OFF-002` 直接确认 camp night、character reaction、writing / flow 是被持续维护的公开边界。
- `推断`：
  - 营地中的 companion reaction 不是附属 flavor，而是玩家感知任务 / 关系后果是否闭环的主交互面之一。
  - Minthara 之所以适合作为候补案例，不是因为她代表普遍规律，而是因为她把营地反馈链中的多个边界一次性暴露出来。
- `待验证问题`：
  - 这些热修更偏向角色特例修补，还是足以支撑“营地反馈链会被系统性维护”这一更高层判断？
  - 是否能找到非 Minthara 角色的官方条目，证明营地 companion reaction 不是孤例？
  - 这一案例更适合在正文里作为候补案例，还是只作为实现验证层的系统入口？

## Source IDs

- `BG3-OFF-002`
- `BG3-OFF-008`

## Notes

- 这个案例比 `Dark Urge 营地 bard 事件` 更偏“系统边界暴露”，较弱于完整剧情链，但更强于营地反馈可达性的公开验证。
- 它适合作为 `03_party_and_camp` 的候补案例方向，而不是当前主案例。
