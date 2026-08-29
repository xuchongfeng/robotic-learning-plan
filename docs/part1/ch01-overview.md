# 第 1 章 机器人全景：感知—规划—控制闭环

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 1 |
| 路线 | 主干 |
| 对应项目 | `P01` |
| 所属篇 | `part1` |

## 需要掌握

- 移动机器人与机械臂都能画成「感知 → 状态估计 → 规划 → 控制 → 执行」闭环
- 分清算法层、ROS 2 系统层、硬件层各自解决什么问题
- 频率直觉：控制环高、规划中、任务层低
- 选定当前方向偏好（导航 / 机械臂 / 具身），允许以后改

## 关键内容

机器人软件的核心不是单个模型，而是数据在闭环里怎么流。差速车：激光/相机 → 定位建图 → 路径 → cmd_vel → 电机。机械臂：关节/相机 → 位姿 → 运动规划 → 关节指令 → 驱动。
本书主线：先在 Python 里看懂算法，再进 ROS 2 做系统，最后才选真机或具身。不要把「学 AI」放在会算坐标变换之前。

## 推荐学习资料

### 必看（掌握本章）

- [Modern Robotics 第 1 章 Preview](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) — 建立机构/规划/控制的词汇
- [Stanford CS223A Lecture 1](https://see.stanford.edu/Course/CS223A) — 课程地图，看到应用与先修即可
- [公开课对照](../preface/courses.md) — 主干如何覆盖机构/移动/感知入门

### 进阶拓展

- [commitverse/Robotics-roadmap](https://github.com/commitverse/Robotics-roadmap) — 只当资源清单，不按其 Phase 0 先学 AI
- [kiloreux/awesome-robotics](https://github.com/kiloreux/awesome-robotics) — 课程/会议字典，按需查
- [Stanford PoRA I 课程主页](https://stanfordasl.github.io/PoRA-I/aa274a_aut2526/) — 看一眼学期实验长什么样

## 实验清单

- [ ] 手绘差速车从激光到轮速的框图，标出典型频率
- [ ] 列出本机：OS、Python、是否有 NVIDIA GPU

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
