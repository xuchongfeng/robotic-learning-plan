# 公开课与培养路线对照

本书主线仍是「算法 → ROS 2 → 导航/操作 → 具身」。公开课用来 **补理论课表**，不要另开一条平行进度。同一周：先看课、再跑本章实验、篇末再做门禁项目。

高校培养通常拆成三条课：**机构与控制**（臂）、**自主移动**（车）、**感知**（视觉/SLAM）。本书把这三条按时间串起来，而不是一学期只学一门。

## 主课表（建议跟完）

| 本书篇 | 公开课 / 培养课 | 跟到什么程度 | 不要怎样用 |
|--------|-----------------|--------------|------------|
| 地基 | [Coursera Modern Robotics](https://www.coursera.org/specializations/modernrobotics) Course 1–3（西北大学 Lynch）；[Stanford CS223A](https://see.stanford.edu/Course/CS223A) 运动学与控制录像 | 作业用 Python 做，不必上 MATLAB/V-REP | 不要六门专项全部做完才开始 PythonRobotics |
| 算法 | [Stanford Principles of Robot Autonomy I](https://stanfordasl.github.io/PoRA-I/aa274a_aut2526/)（规划、KF/PF、SLAM 讲义）；[ETH Autonomous Mobile Robots](https://www.edx.org/learn/autonomous-robotics/eth-zurich-autonomous-mobile-robots) 选看定位与规划 | 概念对齐后，实现一律用 PythonRobotics | 宾大旧 Coursera Robotics 专项若已下架，用归档作业思路，不要找盗版视频当主课 |
| 系统 | [fishros/d2l-ros2](https://github.com/fishros/d2l-ros2)；PoRA Lab 0–2（ROS 安装与节点） | Humble 或 Jazzy 锁死一个 | 不要同时学 ROS 1 |
| 导航 | PoRA Lab 3–7（TurtleBot、到点、探索）；[Nav2 教程](https://docs.nav2.org/)；选读《视觉 SLAM 十四讲》前半（相机与前端） | 2D LiDAR 导航先闭环；视觉 SLAM 作为方向 A 加码 | 不要第一年就上完整 ORB-SLAM3 工程 |
| 操作 | Modern Robotics Course 5–6 的任务设计（移动操作、pick-and-place）；[MoveIt 2 教程](https://moveit.ai/) | 仿真抓取必须自己跑通 | Course 6 的 youBot/CoppeliaSim 可用 MoveIt+Gazebo 等价替换 |
| 智能 | [MIT Underactuated Robotics](https://underactuated.mit.edu/) 前几章建立欠驱动直觉；[CS231n](http://cs231n.stanford.edu/) 仅补 CNN；[every-embodied](https://github.com/datawhalechina/every-embodied) 当实验课 | 先闭环与模仿学习，再 VLA | 不要把 Underactuated 全书当第一年代数课 |
| 真机 | Robotisim 式作品集：一个可复现的导航或抓取演示；ROS 基金会训练营只作节奏参考 | 5 分钟演示 + 失败记录 | 不要用「完整人形」当考核 |

## 三条经典培养路线（用来核对有没有缺块）

**路线 M（机构学，Stanford CS223A / Modern Robotics）**  
空间变换 → FK/IK → 雅可比 → 动力学 → 关节/笛卡尔/力控制。对应本书第一篇 + 第五篇的控制部分。检验：能给平面臂写出 FK/IK，能调一个跟踪控制器。

**路线 A（自主移动，ETH AMR + Stanford PoRA + 宾大 Aerial/Planning 作业思路）**  
运动模型 → 滤波定位 → 栅格/采样规划 → 轨迹跟踪 →（可选）四旋翼 PD。对应本书第二、四篇。检验：同一仿真里「定位 + 规划 + 跟踪」能从 A 点到 B 点。

**路线 P（感知，CS231A / 视觉 SLAM 十四讲 / PoRA 感知实验）**  
相机模型 → 特征 → 多视几何 → 检测分割 → 2D/3D SLAM。对应本书第四篇。检验：标定有重投影误差数字；建图有 `map.yaml`。

工程师作品集（Robotisim 等）通常只要 **三个公开项目**：ROS 2 小包、仿真 SLAM/Nav2、再加一个方向专项。本书用七个 **篇门禁** 覆盖这三级，最后 P10 对应他们的专项。

## 每周时间怎么切

按 10 小时/周：约 3 小时看课/读书，5 小时写代码，2 小时写笔记与验收表。公开课进度服从门禁，不服从课表周数。
