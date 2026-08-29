# 第 10 章 定位：EKF、粒子滤波、直方图滤波

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 6–8 |
| 对应项目 | `P03` |
| 所属篇 | `part2` |

## 需要掌握

- 贝叶斯滤波的预测—更新循环
- EKF：在标称轨迹线性化，强非线性会失效
- 粒子滤波：用样本近似分布；退化与重采样
- 直方图滤波：离散栅格上的信念

## 关键内容

三种滤波器做同一件事：融合运动模型与观测。差别是信念怎么表示。
P03B 必须用「估计位姿」而不是真值去跟踪。本章先把三种算法分开跑通。

## 推荐学习资料

### 必看（掌握本章）

- [PythonRobotics Localization](https://github.com/AtsushiSakai/PythonRobotics#localization) — 跑 EKF / PF / histogram
- [文档版教材](https://atsushisakai.github.io/PythonRobotics/) 对应 localization 页 — 公式看到预测与更新
- PoRA I 滤波讲座提纲 — 与课对照名词即可

### 进阶拓展

- Probabilistic Robotics 第 3–8 章 — 完整推导与变种
- UKF / 无迹变换 — EKF 不够时再上
- [ETH AMR](https://www.edx.org/learn/autonomous-robotics/eth-zurich-autonomous-mobile-robots) 定位模块 — 第二教材

## 实验清单

- [ ] 必跑 extended_kalman_filter、particle_filter、histogram_filter，各留动画与五句原理

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
