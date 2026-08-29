# 动手学机器人

从 **算法** 到 **ROS 2 工程** 再到 **具身智能** 的开源学习书。正文是笔记，`projects/` 是项目。默认每周约 10 小时，核心路径 12 个月。

## 设计原则

1. **先算法后框架**：PythonRobotics 看懂再进 ROS 2，避免在 launch 文件里迷路。
2. **一条主线**：外部仓库当教材，本仓库当唯一笔记入口。
3. **终章可完成**：不做「整机人形」考核；第 28 周后在导航 / 机械臂 / 具身中三选一。
4. **两层检验**：章实验证明知识点；[篇门禁](projects/gates.md) 证明能集成。不过关不进下一篇。
5. **章节只写关键内容**：正文是「需要掌握 + 关键内容」；推导和进阶放在每章的推荐资料里，写法见 [笔记与项目约定](preface/conventions.md)。

## 相对常见路线图的调整

[commitverse/Robotics-roadmap](https://github.com/commitverse/Robotics-roadmap) 适合当资源清单，但 Phase 0 先学 AI、以及把云机器人 / 网络安全 / 完整人形各占一整个阶段，并不适合作为第一年主线。本书把数学与运动学前置，云与安全放入附录，人形降为选修。

动手学 ROS 2 请用 [fishros/d2l-ros2](https://github.com/fishros/d2l-ros2)（配套站点 [fishros.com/d2lros2](https://fishros.com/d2lros2/)），发行版锁定 **Humble 或 Jazzy**。

## 七篇结构

| 篇 | 周次 | 公开课主线 | 门禁（不过关不进下一篇） |
|----|------|------------|--------------------------|
| 地基 | 1–8 | Modern Robotics C1–C3、CS223A | G1：P01 PID + P02 FK/IK |
| 算法 | 6–14 | PoRA 规划/滤波、ETH AMR | G2：P03 散装 + **P03B 定位—规划—跟踪一条龙** |
| 系统 | 10–18 | d2l-ros2、PoRA ROS 实验 | G3：P04 且自己的仿真车能遥控 |
| 导航 | 16–24 | PoRA Lab、Nav2 | G4：P05 三航点 + 一次挡路 |
| 操作 | 20–28 | MR C5–C6 任务、MoveIt | G5：P07 抓取放置 ≥ 8/10 |
| 智能 | 24–36 | Underactuated 选读、every-embodied | G6：P08 闭环成功率 ≥ 50% |
| 真机 | 28–40 | 作品集专项 | G7：P10 五分钟演示 |

公开课怎么嵌进每周，见 [公开课对照](preface/courses.md)。章实验表见 [章实验](projects/labs.md)。章节写法见 [笔记与项目约定](preface/conventions.md)。周表见 [附录 C](appendix/c-weekly.md)。本地预览：`mkdocs serve`。
