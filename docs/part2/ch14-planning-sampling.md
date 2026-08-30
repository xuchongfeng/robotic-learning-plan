# 第 14 章 路径规划 II：PRM / RRT / RRT*

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 11–12 |
| 路线 | 主干 |
| 对应项目 | `P03` |
| 所属篇 | `part2` |

## 需要掌握

- 高维（机械臂）为何更常用采样规划而不是细栅格
- PRM：先建路线图再查询
- RRT：向随机样本扩展树；RRT* 渐近最优的含义
- 碰撞检测是采样规划的实际瓶颈（概念）

## 关键内容

移动机器人 2D 用栅格往往够；臂的 C 空间用 RRT 族。G2 小车不必上 RRT，但要能讲清差别。

## 推荐学习资料

### 必看（掌握本章）

- [PythonRobotics PRM / RRT / RRT*](https://github.com/AtsushiSakai/PythonRobotics#path-planning)
- [Modern Robotics 第 10 章](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) 采样规划概念

### 进阶拓展

- RRT-Connect、Informed RRT*、BIT* — MoveIt 默认规划器相关
- OMPL 文档 — 第 29 章对照
- 动力学约束下的 kinodynamic RRT — 第 15 章之后

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 实验清单

- [ ] 必跑 PRM、RRT、RRT*，对比有无障碍时的树形状

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
