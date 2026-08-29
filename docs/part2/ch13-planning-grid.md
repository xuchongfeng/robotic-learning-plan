# 第 13 章 路径规划 I：Dijkstra / A* / D* / 势场

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 10–11 |
| 对应项目 | `P03` |
| 所属篇 | `part2` |

## 需要掌握

- 完备性、最优性、计算量三指标能用来对比算法
- Dijkstra 与 A*：启发函数可采纳则 A* 最优
- D* / D* Lite：环境变化时的增量搜索直觉
- 势场：快但不完备，易局部最小

## 关键内容

栅格规划是 Nav2 全局规划器的原型。G2 用 A*（或 Dijkstra）即可。
启发不可采纳会丢最优，实验里对比扩展节点数。

## 推荐学习资料

### 必看（掌握本章）

- [PythonRobotics 栅格搜索](https://github.com/AtsushiSakai/PythonRobotics#path-planning) — Dijkstra、A*、D* Lite、Potential Field
- 宾大 Motion Planning 作业思路（A*/Dijkstra）— 若课下架则只对照算法，用 Python 实现

### 进阶拓展

- Modern Robotics 第 10 章搜索部分 — 理论补强
- 覆盖路径 / 割草机规划 — 应用选修
- Nav2 Navfn / Smac Planner 源码 — 第 26–27 章

## 实验清单

- [ ] 同图对比 Dijkstra 与 A* 的扩展节点数；再跑 D* Lite 与势场

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
