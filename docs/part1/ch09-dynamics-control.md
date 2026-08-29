# 第 9 章 动力学与反馈控制：PID / LQR

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 7–8 |
| 路线 | 主干 |
| 对应项目 | `P01` |
| 所属篇 | `part1` |

## 需要掌握

- P/I/D 各自消除什么误差、引入什么副作用
- 二阶系统：超调、调节时间、稳态误差能从曲线读出
- LQR：要线性模型、二次代价，输出是增益矩阵 K
- 动力学方程本章只要求「惯性 + 科氏 + 重力」的分层直觉

## 关键内容

G1 要的是一套可复现的 PID 参数表，不是最优控制论文。先调简单对象（速度环或质量—弹簧—阻尼）。
LQR 先看 PythonRobotics 动画建立直觉，公式跟 MR 第 11 章，不在正文展开 Riccati。

## 推荐学习资料

### 必看（掌握本章）

- [Modern Robotics 第 11 章 Robot Control](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) 选读 PID/运动控制
- [PythonRobotics LQR 路径跟踪示例](https://github.com/AtsushiSakai/PythonRobotics#path-tracking) — 先看动画
- [MIT Underactuated 第 1 章](https://underactuated.mit.edu/) — 全驱动 vs 欠驱动直觉即可

### 进阶拓展

- MR 第 8 章开链动力学完整推导 — 写仿真器或真机辨识前再读
- Underactuated 倒立摆/行走后续章 — 第四篇之后选修
- MPC 作为带约束的滚动 LQR — 第 16 章主场

## 实验清单

- [ ] 给二阶系统或小车速度环调 PID，记录超调、稳态误差、参数表（P01）

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
