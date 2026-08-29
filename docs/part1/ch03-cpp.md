# 第 3 章 C++ 够用即可：指针、OOP、CMake

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 2–3 |
| 对应项目 | 本章以笔记与小实验为主 |
| 所属篇 | `part1` |

## 需要掌握

- 值 / 引用 / 指针、类的最小写法、智能指针是干什么的
- 能读懂 ROS 2 C++ 节点的 `#include`、构造、订阅回调结构
- 最小 CMakeLists.txt 能编译出一个可执行文件
- 判断：控制环与驱动常用 C++，算法原型与胶水用 Python

## 关键内容

第一年不要求成为 C++ 专家。目标是打开 ROS 2 驱动和控制器代码时不迷路。
先用 CMake 编一个打印 4×4 矩阵的程序，比先啃模板元编程有用。

## 推荐学习资料

### 必看（掌握本章）

- [CMake 官方教程：A Basic Starting Point](https://cmake.org/cmake/help/latest/guide/tutorial/A%20Basic%20Starting%20Point.html) — 做到能编译
- [ROS 2 写一个简单的 C++ 发布者](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber.html) — 先看结构，本周不必跑 ROS
- A Tour of C++ 前几章，或任何「类型、引用、类」速通 — 语法即可

### 进阶拓展

- 《C++ Primer》类与内存章节 — 读 ROS 驱动前再翻
- 现代 C++（移动语义、RAII）— 写控制器时再补
- ament_cmake 包结构 — 第三篇与官方教程一起学

## 实验清单

- [ ] 用 CMake 编译一个打印齐次变换矩阵的小程序，命令写进 README

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
