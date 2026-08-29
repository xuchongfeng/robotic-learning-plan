# 第 11 章 建图：栅格地图、射线投射、聚类

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 8–9 |
| 对应项目 | `P03` |
| 所属篇 | `part2` |

## 需要掌握

- 占用栅格：每格自由/占用概率的贝叶斯更新
- 射线投射：一帧 LiDAR 如何改一排格子
- 点云聚类与矩形拟合是「把格子变成物体」的简单手段

## 关键内容

定位问「我在哪」，建图问「世界长什么样」。SLAM 两者一起估。
2D 导航门禁用的就是占用栅格。本章把 LiDAR → 地图这一步做扎实。

## 推荐学习资料

### 必看（掌握本章）

- [PythonRobotics Mapping](https://github.com/AtsushiSakai/PythonRobotics#mapping) — gaussian / raycasting / lidar_to_grid
- PoRA I 占用栅格与传感器讲座 — 对照名词

### 进阶拓展

- 三维体素 / TSDF / 3DGS — 具身与仿真方向，不挡 G2
- 语义地图 — 检测章之后选修
- Cartographer 子图与回环 — 第 25 章工程实现

## 实验清单

- [ ] 必跑 gaussian_grid_map、raycasting_grid_map、lidar_to_grid_map

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
