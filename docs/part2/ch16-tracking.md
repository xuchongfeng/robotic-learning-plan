# 第 16 章 路径跟踪：Stanley / LQR / MPC

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 13–14 |
| 路线 | 主干 |
| 对应项目 | `P03` |
| 所属篇 | `part2` |

## 需要掌握

- 纯追踪 / Stanley 的几何：预瞄与横向误差
- LQR 跟踪：线性化误差模型 + 增益
- MPC：滚动优化，能加约束（速度、转角）
- G2 跟踪必须吃定位结果，不能用真值作弊

## 关键内容

控制器输出是速度与转向（或加速度）。调参看横向误差曲线，不要只看「最后到没到」。

## 推荐学习资料

### 必看（掌握本章）

- [PythonRobotics Path Tracking](https://github.com/AtsushiSakai/PythonRobotics#path-tracking) — Stanley、LQR、MPC
- 第 9 章 PID 笔记 — 对照：几何跟踪 vs 误差反馈

### 进阶拓展

- 非线性 MPC、C-GMRES — PythonRobotics 高级示例
- Nav2 DWB / MPPI 局部规划 — 第 26 章
- 差速与阿克曼模型差异 — 自己推一层运动学即可

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 实验清单

- [ ] 必跑 Stanley、LQR speed/steering、MPC；G2 用其中之一接估计位姿

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
