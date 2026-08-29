# 第 33 章 机器人强化学习：PPO / SAC / 模仿学习

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 26–30 |
| 对应项目 | 本章以笔记与小实验为主 |
| 所属篇 | `part6` |

## 需要掌握

- MDP：状态、动作、奖励、折扣
- on-policy（PPO）与 off-policy（SAC）的差别一句话能说清
- 模仿学习（BC、ACT）与 RL 的关系：先克隆再强化（概念）
- 一次最小训练：Pendulum 或到位任务有回报曲线

## 关键内容

G6 可以用脚本闭环而不训练 RL。本章是为了读懂 P09 和论文方法部分。

## 推荐学习资料

### 必看（掌握本章）

- every-embodied 或 dive-into-embodied-ai 强化学习入门章
- [Spinning Up on-policy / off-policy 概述](https://spinningup.openai.com/en/latest/) 或 CleanRL 一个 PPO 脚本对照
- [MIT Underactuated](https://underactuated.mit.edu/) 中与轨迹优化/学习相关的选读（点到为止）

### 进阶拓展

- PPO/SAC 论文 — 实现细节
- Isaac Lab 并行 RL — 有 GPU
- 奖励工程与 sim-to-real 域随机 — 第 36 章

## 实验清单

- [ ] Pendulum 或到位任务跑通 PPO 或 SAC 一次，回报曲线入库

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
