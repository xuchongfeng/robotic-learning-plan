# 第 21 章 建模与仿真：Gazebo / Webots

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 14–16 |
| 路线 | 主干 |
| 对应项目 | `P05` |
| 所属篇 | `part3` |

## 需要掌握

- 差速车 URDF 含激光与 IMU，能在仿真里遥控
- 里程计与激光话题名称、坐标系正确
- 同一阶段只深挖一个仿真器（Gazebo 或 Webots）

## 关键内容

仿真是假物理、真接口。G3 要「自己的车能遥控」，不必等 TurtleBot 官方包。

## 推荐学习资料

### 必看（掌握本章）

- d2l-ros2 第 8–9 章建模仿真
- 所选仿真器的官方 ROS 2 教程（[Gazebo](https://gazebosim.org/) 或 [Webots ROS 2](https://github.com/cyberbotics/webots_ros2)）
- PoRA Lab：RViz + Turtlebot — 对照传感器话题

### 进阶拓展

- SDF 与 URDF 的差别、Gazebo 版本（Classic vs Harmonic）与 ROS 发行版匹配
- 传感器噪声模型 — 后面 SLAM 调参
- Isaac Sim 桥 — 第六篇再碰

## 实验清单

- [ ] 仿真键盘遥控小车，确认里程计与激光话题

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
