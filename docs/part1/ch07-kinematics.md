# 第 7 章 正运动学与逆运动学

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 6–7 |
| 路线 | 主干 |
| 对应项目 | `P02` |
| 所属篇 | `part1` |

## 需要掌握

- FK：关节角 → 末端位姿；平面 2R/3R 能手写
- IK：可达点数值求解能收敛；不可达时要能看出来
- 解析 IK 与数值 IK 的适用边界（自由度、唯一解、初值）
- DH 与指数积二选一先吃透一种，另一种当对照

## 关键内容

P02 的核心：FK 必须对，IK 用数值迭代即可。不要一上来写通用 6R 解析解。
多解、奇异、限位是 IK 的日常，实验里至少展示一种失败。

## 推荐学习资料

### 必看（掌握本章）

- [Modern Robotics 第 4、6 章](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) + Coursera Course 2 — FK/IK 主课
- [PythonRobotics Arm Navigation](https://github.com/AtsushiSakai/PythonRobotics#arm-navigation) — 看可视化
- 完成平面臂 FK/IK 可视化（P02）

### 进阶拓展

- 6R 工业臂解析 IK（Pieper 等）— 第五篇真机前再读
- 闭链机构（MR 第 7 章）— 选修，不挡 G1
- MoveIt 的 IK 插件（KDL/Trac-IK）— 第 29 章对照

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 实验清单

- [ ] 完成 P02：平面 2R/3R 的 FK/IK 可视化，往返误差低于自设阈值

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
