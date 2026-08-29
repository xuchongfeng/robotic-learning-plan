# 第 18 章 ROS 2 安装、概念与工作空间

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 10–11 |
| 对应项目 | `P04` |
| 所属篇 | `part3` |

## 需要掌握

- 发行版锁死 Humble 或 Jazzy，不用 ROS 1
- node、topic、package、workspace、overlay 各是什么
- colcon build、source install/setup.bash 的顺序
- turtlesim 或自写发布节点能跑

## 关键内容

ROS 2 是中间件：帮你传数据、管启动，不代替算法。算法没懂就写节点会在 launch 里迷路。
可与第二篇后半重叠安装，但 P03B 仍须完成。

## 推荐学习资料

### 必看（掌握本章）

- [fishros/d2l-ros2 第 1–2 章](https://github.com/fishros/d2l-ros2) 或 [在线教程](https://fishros.com/d2lros2/)
- [ROS 2 官方 Beginner](https://docs.ros.org/en/humble/Tutorials.html) 安装与 turtlesim
- PoRA Lab 0：Install ROS — 节奏对照

### 进阶拓展

- DDS / RMW 实现差异 — 多机通信时再读官方 Concepts
- [mmabas77 ROS 2 Roadmap 2025](https://github.com/mmabas77/ROS-2-Practical-Course-Roadmap-2025) — 实验课式周历
- Docker 内装 ROS — 环境隔离选修

## 实验清单

- [ ] 创建 colcon 工作空间，编写并运行一个 Python 发布节点

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
