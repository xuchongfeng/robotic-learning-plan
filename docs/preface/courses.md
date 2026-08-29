# 公开课与培养路线对照

公开课用来 **补主干课表**，不要另开平行进度。同一周：先看课、再跑本章实验、篇末做门禁。

高校常常把课拆成机构与控制、自主移动、感知三门。本书 **不选边**：主干把三块入门都覆盖；只有加码章才打标签，见 [主干与加码](tracks.md)。

## 主课表（主干建议跟完）

| 本书篇 | 公开课 / 培养课 | 跟到什么程度 | 不要怎样用 |
|--------|-----------------|--------------|------------|
| 地基 | [Coursera Modern Robotics](https://www.coursera.org/specializations/modernrobotics) Course 1–3；[Stanford CS223A](https://see.stanford.edu/Course/CS223A) | 作业用 Python，覆盖机构学入门 | 不要六门专项全部做完才开始 PythonRobotics |
| 算法 | [Stanford PoRA I](https://stanfordasl.github.io/PoRA-I/aa274a_aut2526/)；[ETH AMR](https://www.edx.org/learn/autonomous-robotics/eth-zurich-autonomous-mobile-robots) 选看 | 概念对齐后实现用 PythonRobotics | 宾大旧专项若下架，只借鉴作业结构 |
| 系统 | [fishros/d2l-ros2](https://github.com/fishros/d2l-ros2)；PoRA Lab 0–2 | Humble 或 Jazzy 锁死一个 | 不要同时学 ROS 1 |
| 导航 | PoRA Lab 3–7；[Nav2](https://docs.nav2.org/) | 2D LiDAR 导航闭环（主干 G4） | 视觉 SLAM 十四讲是导航加码 |
| 操作 | Modern Robotics C5–C6 任务；[MoveIt 2](https://moveit.ai/) | 仿真抓取跑通（主干 G5） | youBot/CoppeliaSim 可用 MoveIt 等价替换 |
| 智能 | [MIT Underactuated](https://underactuated.mit.edu/) 前几章；[every-embodied](https://github.com/datawhalechina/every-embodied) | 脚本闭环（主干 G6）；CS231n 按需 | VLA 训练是具身加码 |
| 真机 | 作品集：一个可复现演示 | G7 只加深一条加码 | 不要用完整人形当考核 |

## 用三块课核对主干有没有漏（不是三选一）

**机构学入门（CS223A / Modern Robotics）** — 主干第一、五篇：空间变换、FK/IK、雅可比、PID、仿真 pick-and-place。加码才到力控、6R 解析 IK、真机臂。

**自主移动入门（ETH AMR / PoRA）** — 主干第二、四篇：滤波定位、栅格规划、跟踪、Nav2 到点。加码才到自定义车、规划器插件、视觉 SLAM。

**感知入门（PoRA 相机实验 / OpenCV）** — 主干第二十三、二十四章 + 建图出图：标定、检测跑通一次、2D 地图。加码才到多视几何、ORB-SLAM、分割大模型。

作品集常见三级：ROS 小包、仿真导航、再加一个加深项。本书 G1–G6 覆盖前两级并带上抓取闭环；G7 对应加深项。

## 每周时间怎么切

按 10 小时/周：约 3 小时看课、5 小时写代码、2 小时笔记。加码章不计入主干周数。公开课服从门禁，不服从课表周数。
