# 第 17 章 机械臂避障与双足规划初探

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 14 |
| 路线 | 机械臂加码 |
| 对应项目 | `P03` |
| 所属篇 | `part2` |

!!! warning "可跳过"
    本章为 **机械臂加码**。终章不加深机械臂的，读完标题即可跳过，不挡 G1–G6。

## 需要掌握

- 关节空间规划：在 C 空间避障，不是只在工作空间画直线
- 平面臂避障示例如何把第 13–14 章接上 FK
- 倒立摆步态只建立直觉，不要求真机双足

## 关键内容

移动机器人 G2 不依赖本章。本章是给第五篇和选修人形的预告片：同样是规划，状态定义不同。

## 推荐学习资料

### 必看（掌握本章）

- [PythonRobotics Arm Navigation / Bipedal](https://github.com/AtsushiSakai/PythonRobotics#arm-navigation)

### 进阶拓展

- MIT Underactuated 行走与平衡章节
- MoveIt 规划组与碰撞 — 第 29 章
- Open_Duck / 宇树运动控制论文 — 第 41 章

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 实验清单

- [ ] 必跑 N joint arm、arm obstacle avoidance、bipedal planner 各一，笔记里对比与小车规划的差别

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
