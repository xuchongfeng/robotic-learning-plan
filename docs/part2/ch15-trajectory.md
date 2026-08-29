# 第 15 章 轨迹生成：多项式、Reeds-Shepp、Frenet

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 12–13 |
| 路线 | 主干 |
| 对应项目 | `P03` |
| 所属篇 | `part2` |

## 需要掌握

- 路径是几何，轨迹带时间（位置、速度、加速度）
- 五次多项式为何能配位置与速度边界
- 非完整约束：车不能横着开，故 Dubins / Reeds-Shepp
- Frenet：沿道路中心线的横向/纵向解耦直觉

## 关键内容

规划器给出路点后，跟踪器吃的是带时间的参考。本章把「路」变成「可跟踪的曲线」。

## 推荐学习资料

### 必看（掌握本章）

- [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) quintic polynomials、Reeds Shepp、Frenet 最优轨迹
- Coursera Aerial Robotics 轨迹生成作业思路（若可及）— 多项式边界条件

### 进阶拓展

- Minimum snap / 微分平坦（四旋翼）— 选修飞行
- MR 第 9 章 Trajectory Generation
- Nav2 控制器用的路径插值 — 第 26 章对照

## 实验清单

- [ ] 必跑 quintic_polynomials、reeds_shepp、frenet；确认位置速度加速度连续

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
