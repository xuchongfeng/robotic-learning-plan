# 第 20 章 工具链：TF2、URDF、Launch、RViz

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 13–14 |
| 路线 | 主干 |
| 对应项目 | `P04` |
| 所属篇 | `part3` |

## 需要掌握

- TF 树：父子坐标系，查询 base_link → laser
- URDF/Xacro 描述连杆与关节
- RViz 检查坐标系、激光、模型是否对齐
- Launch 组合节点与参数

## 关键内容

机器人系统最常见的 bug 是 TF 断了或时间戳不对。G3 验收要 TF 树截图。

## 推荐学习资料

### 必看（掌握本章）

- d2l-ros2 第 5 章及机器人学篇中的 TF
- [tf2 教程](https://docs.ros.org/en/humble/Tutorials/Intermediate/Tf2/Introduction-To-Tf2.html)
- [URDF 教程](https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/URDF-Main.html)

### 进阶拓展

- robot_state_publisher 与关节状态 — 仿真/真机共用
- REP-105 坐标系约定（map/odom/base_link）— 第 25 章必读
- 自定义 RViz 插件 — 不挡 G3

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 实验清单

- [ ] 静态 TF + RViz 对齐模型和激光，TF 树无断

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
