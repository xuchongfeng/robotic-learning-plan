# 第 25 章 SLAM 建图实战：slam_toolbox / Cartographer

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 18–21 |
| 对应项目 | `P05` |
| 所属篇 | `part4` |

## 需要掌握

- 2D 激光 SLAM 出图：slam_toolbox 或 Cartographer 选一个跑通
- map.yaml + pgm 的含义；map / odom / base_link（REP-105）
- 回环如何抑制里程计漂移（现象层）

## 关键内容

G4 必须有一张自己录的图。算法细节已在第 12 章，本章是工程 bringup。

## 推荐学习资料

### 必看（掌握本章）

- d2l-ros2 第 10 章 SLAM 建图
- [slam_toolbox](https://github.com/SteveMacenski/slam_toolbox) 或 Nav2 官方 mapping 教程
- REP-105 坐标系短文

### 进阶拓展

- Cartographer 调参与 3D — 需要时再上
- 视觉 SLAM（ORB-SLAM 等）— 方向 A，不挡 G4
- 多雷达标定 — 真机选修

## 实验清单

- [ ] TurtleBot3 或自己的仿真车出图，保存 map.yaml 与 pgm，过程截图入库

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
