# 第 12 章 SLAM：ICP、EKF-SLAM、FastSLAM

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 9–10 |
| 对应项目 | `P03` |
| 所属篇 | `part2` |

## 需要掌握

- 定位、建图、SLAM 的状态与观测各是什么
- ICP：两点云对齐，SVD 求 R、t
- EKF-SLAM：把路标放进同一个高斯向量，随路标增多变慢
- FastSLAM：粒子表示轨迹，每个粒子用 EKF 管路标

## 关键内容

ICP 常当前端（配准），滤波/图优化是后端。本章先跑通滤波系 SLAM，图优化进进阶。
G2 不要求完整 SLAM；但要能讲清为何开环里程计会漂。

## 推荐学习资料

### 必看（掌握本章）

- [PythonRobotics SLAM](https://github.com/AtsushiSakai/PythonRobotics#slam) — ICP、EKF-SLAM、FastSLAM 1.0
- ICP 的 SVD 推导：教材或短文看懂一次即可

### 进阶拓展

- 图 SLAM / 位姿图 / g2o / GTSAM — [gtbook/robotics](https://github.com/gtbook/robotics) 或十四讲后端
- 视觉 SLAM 十四讲前端+后端 — 方向 A 加码，不挡 G2/G4
- Cartographer / slam_toolbox 工程 — 第 25 章

## 实验清单

- [ ] 必跑 ICP Matching、EKF SLAM、FastSLAM 1.0

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
