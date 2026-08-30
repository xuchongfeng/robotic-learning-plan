# 第 22 章 ros2_control 与 Micro-ROS

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 16–18 |
| 路线 | 主干 |
| 对应项目 | `P06` |
| 所属篇 | `part3` |

## 需要掌握

- hardware interface、controller manager、diff_drive_controller 各干什么
- 为何不要长期手写「假 cmd_vel → 轮速」桥
- Micro-ROS：MCU 上跑精简 ROS 客户端的定位

## 关键内容

仿真里先把 ros2_control 跑通，真机只是换 hardware plugin。P06 会用到。

## 推荐学习资料

### 必看（掌握本章）

- d2l-ros2 第 13–15 章（Control / Micro-ROS / 硬件实战概览）
- [ros2_control 文档](https://control.ros.org/) 入门与差速示例

### 进阶拓展

- 编写自定义 hardware interface — 真机驱动时
- Micro-ROS 官方教程 — 有 MCU 再做
- 实时内核与控制频率 — 选修

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 实验清单

- [ ] 仿真中用 ros2_control 驱动轮子；若仍用手写桥，必须在笔记写明原因

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
