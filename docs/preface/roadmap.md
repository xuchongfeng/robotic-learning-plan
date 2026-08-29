# 学习路线总览

```mermaid
flowchart LR
  A[地基 编程数学运动学] --> B[算法 PythonRobotics]
  B --> C[系统 ROS 2]
  C --> D[导航 视觉 SLAM Nav2]
  D --> E[操作 MoveIt LeRobot]
  E --> F[智能 RL VLA]
  F --> G[三选一终章]
  B -.-> C
  D -.-> E
```

重叠含义：PythonRobotics 可以从第 6 周开始穿插；ROS 2 可以从第 10 周安装，不必等算法篇全部结束。**第二篇门禁 P03B 仍须完成**，再把节点写进 ROS。导航与操作在时间上可部分并行，但不要两个方向各开一个真机。

公开课与高校培养路线对照见 [公开课对照](courses.md)。每篇结束的集成考核见 [篇门禁](../projects/gates.md)。

对 commitverse 11 阶段的改动见首页。
