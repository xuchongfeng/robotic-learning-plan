#!/usr/bin/env python3
"""Render all book chapters from the catalog. Does not touch preface/projects."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# Each chapter: part, file, title, weeks, project, master, key, must, advanced, experiments
# Long notes / experiment checklists live in scripts/chapter_overrides/<stem>.{notes,experiments}.md
C = []
OVERRIDE = ROOT / "scripts" / "chapter_overrides"
DEFAULT_NOTES = "只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。"


def add(**kw):
    kw.setdefault("tracks", "主干")
    C.append(kw)


add(
    part="part1",
    file="ch01-overview.md",
    title="第 1 章 机器人全景：感知—规划—控制闭环",
    weeks="Week 1",
    project="P01",
    master=[
        "移动机器人与机械臂都能画成「感知 → 状态估计 → 规划 → 控制 → 执行」闭环",
        "分清算法层、ROS 2 系统层、硬件层各自解决什么问题",
        "频率直觉：控制环高、规划中、任务层低",
        "选定当前方向偏好（导航 / 机械臂 / 具身），允许以后改",
    ],
    key=[
        "机器人软件的核心不是单个模型，而是数据在闭环里怎么流。差速车：激光/相机 → 定位建图 → 路径 → cmd_vel → 电机。机械臂：关节/相机 → 位姿 → 运动规划 → 关节指令 → 驱动。",
        "本书主线：先在 Python 里看懂算法，再进 ROS 2 做系统，最后才选真机或具身。不要把「学 AI」放在会算坐标变换之前。",
    ],
    must=[
        "[Modern Robotics 第 1 章 Preview](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) — 建立机构/规划/控制的词汇",
        "[Stanford CS223A Lecture 1](https://see.stanford.edu/Course/CS223A) — 课程地图，看到应用与先修即可",
        "[公开课对照](../preface/courses.md) — 主干如何覆盖机构/移动/感知入门",
    ],
    advanced=[
        "[commitverse/Robotics-roadmap](https://github.com/commitverse/Robotics-roadmap) — 只当资源清单，不按其 Phase 0 先学 AI",
        "[kiloreux/awesome-robotics](https://github.com/kiloreux/awesome-robotics) — 课程/会议字典，按需查",
        "[Stanford PoRA I 课程主页](https://stanfordasl.github.io/PoRA-I/aa274a_aut2526/) — 看一眼学期实验长什么样",
    ],
    experiments=[
        "手绘差速车从激光到轮速的框图，标出典型频率",
        "列出本机：OS、Python、是否有 NVIDIA GPU",
    ],
)

add(
    part="part1",
    file="ch02-python.md",
    title="第 2 章 Python 工程实践与科学计算",
    weeks="Week 1–2",
    project="P01",
    master=[
        "虚拟环境、依赖冻结、pytest 最小测试",
        "NumPy 向量化：向量/矩阵/批量变换，避免 Python for 硬算几何",
        "Matplotlib 画 2D 轨迹，图上有轴标签与图例",
    ],
    key=[
        "机器人算法课的日常语言是 NumPy。坐标、旋转、一批点的变换都应写成数组运算。",
        "没有测试的几何函数后面会在 IK/滤波里炸掉。本章起每个核心函数至少 3 个断言。",
    ],
    must=[
        "[NumPy 绝对基础](https://numpy.org/doc/stable/user/absolute_beginners.html) — 广播、matmul、axis",
        "[Matplotlib 快速入门](https://matplotlib.org/stable/users/explain/quick_start.html) — 能画点与线",
        "[pytest 官方入门](https://docs.pytest.org/en/stable/getting-started.html) — 一个文件三种断言即可",
    ],
    advanced=[
        "Harvard CS50P — 仅当语法不熟时补，不要当本章主课",
        "[SciPy 空间变换](https://docs.scipy.org/doc/scipy/reference/spatial.transform.html) — 四元数/旋转后用，可与第 6 章对照",
        "类型标注与 ruff/mypy — 工程加码，不挡章实验",
    ],
    experiments=[
        "实现 2D 点绕原点旋转 θ，Matplotlib 画出轨迹",
        "为该函数补 3 个 pytest 用例",
    ],
)

add(
    part="part1",
    file="ch03-cpp.md",
    title="第 3 章 C++ 够用即可：指针、OOP、CMake",
    weeks="Week 2–3",
    project="无",
    master=[
        "值 / 引用 / 指针、类的最小写法、智能指针是干什么的",
        "能读懂 ROS 2 C++ 节点的 `#include`、构造、订阅回调结构",
        "最小 CMakeLists.txt 能编译出一个可执行文件",
        "判断：控制环与驱动常用 C++，算法原型与胶水用 Python",
    ],
    key=[
        "第一年不要求成为 C++ 专家。目标是打开 ROS 2 驱动和控制器代码时不迷路。",
        "先用 CMake 编一个打印 4×4 矩阵的程序，比先啃模板元编程有用。",
    ],
    must=[
        "[CMake 官方教程：A Basic Starting Point](https://cmake.org/cmake/help/latest/guide/tutorial/A%20Basic%20Starting%20Point.html) — 做到能编译",
        "[ROS 2 写一个简单的 C++ 发布者](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Cpp-Publisher-And-Subscriber.html) — 先看结构，本周不必跑 ROS",
        "A Tour of C++ 前几章，或任何「类型、引用、类」速通 — 语法即可",
    ],
    advanced=[
        "《C++ Primer》类与内存章节 — 读 ROS 驱动前再翻",
        "现代 C++（移动语义、RAII）— 写控制器时再补",
        "ament_cmake 包结构 — 第三篇与官方教程一起学",
    ],
    experiments=[
        "用 CMake 编译一个打印齐次变换矩阵的小程序，命令写进 README",
    ],
)

add(
    part="part1",
    file="ch04-linear-algebra.md",
    title="第 4 章 线性代数：向量、矩阵、坐标变换",
    weeks="Week 3–4",
    project="P02",
    status="进行中",
    master=[
        "点积、叉积（含二维有向面积）、行列式的几何含义；特征值本周只记「沿特征向量只缩放」",
        "矩阵的列 = 基向量被送到哪；矩阵乘法是变换复合，顺序不可随便换",
        "旋转：R.T @ R = I 且 det = 1；反射 det = -1，不是刚体转动",
        "基变换：同一向量在不同坐标系下数字不同",
        "2D/3D 齐次坐标，能手写 T 与 T^{-1}（R.T 与 -R.T @ t），并写死左乘约定",
        "能用 notebook 画出向量、房子变换、先转后移 vs 先移后转、复合与往返误差",
    ],
    key=[
        "机器人里的「算一下位姿」几乎都是：列向量乘矩阵。先把二维齐次变换画熟，三维只是 3x3 变成 4x4。",
        "约定写死：p_a = T_a_b @ p_b，复合 T_a_c = T_a_b @ T_b_c（从右往左读）。先转后移和先移后转一般不相等。",
        "刚体求逆用手写 R.T，不要盲信通用 inv。题目先纸笔，图在 projects/ch04_linear_algebra/ch04_linear_algebra.ipynb。",
    ],
    must=[
        "[3Blue1Brown Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) — 看到基变换、行列式、矩阵乘法（约前 7 集）",
        "`projects/ch04_linear_algebra/ch04_linear_algebra.ipynb` — 按实验 A–E 改数、出图",
        "MIT 18.06 前半（向量空间、正交）— 课或教材选一种，补「为什么 R.T @ R = I」",
    ],
    advanced=[
        "MIT 18.06 后半（SVD、正定）— 第 5、12 章最小二乘/ICP 再用",
        "Modern Robotics 附录旋转表示 — 与第 6 章一起读",
        "李群直觉（不必现在推公式）— 视觉 SLAM 加码时再看十四讲前几讲",
    ],
    experiments=[
        "实现 2D 齐次变换复合与求逆，用图形验证往返误差接近数值精度",
    ],
)

add(
    part="part1",
    file="ch05-calc-prob.md",
    title="第 5 章 微积分、概率与最小二乘",
    weeks="Week 4–5",
    project="无",
    master=[
        "离散时间积分：状态如何按控制量往前走一步",
        "雅可比是「向量函数的导数矩阵」，后面 FK/EKF 都会用",
        "高斯分布的均值与协方差；一维贝叶斯更新能手推",
        "最小二乘：带噪观测下拟合直线或速度",
    ],
    key=[
        "滤波是「预测（积分/运动模型）+ 更新（观测模型）」。最小二乘是更新的一种。",
        "不必在本章学完测度论。够用：正态分布、独立假设何时失效。",
    ],
    must=[
        "[Probabilistic Robotics 第 2 章概念](http://www.probabilistic-robotics.org/) — 贝叶斯滤波递推，不必通读全书",
        "任一本工科概率课：高斯、协方差 — 能算一维更新即可",
        "用 Python 对带噪匀速运动做最小二乘 — 本章实验",
    ],
    advanced=[
        "多元高斯与信息矩阵 — EKF 多维时再补",
        "《机器人学中的状态估计》（Barfoot）前几章 — 方向 A 加码",
        "自动微分直觉 — 数值 IK、学习型控制后用",
    ],
    experiments=[
        "带噪匀速运动最小二乘拟合，斜率与真值对比有表",
    ],
)

add(
    part="part1",
    file="ch06-rigid-body.md",
    title="第 6 章 刚体运动：旋转、齐次变换、旋量",
    weeks="Week 5–6",
    project="P02",
    master=[
        "SO(3) / SE(3) 是什么；旋转矩阵、轴角、四元数、欧拉角各自的坑",
        "欧拉角万向节锁：什么时候不能当唯一表示",
        "齐次变换如何描述「相机相对基座」「末端相对基座」",
        "角速度与旋转变化的关系（概念层，公式细节进必看教材）",
    ],
    key=[
        "同一刚体位姿有多种表示，工程上旋转矩阵与四元数最常用。互相转换必须做往返误差检查。",
        "旋量/指数积是 Modern Robotics 的主语言；本章先会齐次变换，旋量细节按必看教材跟，不在正文展开。",
    ],
    must=[
        "[Modern Robotics 第 3 章](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) + [Coursera Course 1](https://www.coursera.org/specializations/modernrobotics) — 刚体运动主课",
        "[Stanford CS223A 运动学前半](https://see.stanford.edu/Course/CS223A) — 空间变换录像",
        "自己实现旋转矩阵 ↔ 四元数 ↔ 轴角 — 本章实验",
    ],
    advanced=[
        "Modern Robotics 旋量与指数映射的完整推导 — 做空间臂 FK 前再精读",
        "《视觉 SLAM 十四讲》第 3–4 讲李群李代数 — 视觉方向加码",
        "单位四元数插值（slerp）— 轨迹生成时再看",
    ],
    experiments=[
        "实现三种旋转表示互转，往返误差检查入库",
    ],
)

add(
    part="part1",
    file="ch07-kinematics.md",
    title="第 7 章 正运动学与逆运动学",
    weeks="Week 6–7",
    project="P02",
    master=[
        "FK：关节角 → 末端位姿；平面 2R/3R 能手写",
        "IK：可达点数值求解能收敛；不可达时要能看出来",
        "解析 IK 与数值 IK 的适用边界（自由度、唯一解、初值）",
        "DH 与指数积二选一先吃透一种，另一种当对照",
    ],
    key=[
        "P02 的核心：FK 必须对，IK 用数值迭代即可。不要一上来写通用 6R 解析解。",
        "多解、奇异、限位是 IK 的日常，实验里至少展示一种失败。",
    ],
    must=[
        "[Modern Robotics 第 4、6 章](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) + Coursera Course 2 — FK/IK 主课",
        "[PythonRobotics Arm Navigation](https://github.com/AtsushiSakai/PythonRobotics#arm-navigation) — 看可视化",
        "完成平面臂 FK/IK 可视化（P02）",
    ],
    advanced=[
        "6R 工业臂解析 IK（Pieper 等）— 第五篇真机前再读",
        "闭链机构（MR 第 7 章）— 选修，不挡 G1",
        "MoveIt 的 IK 插件（KDL/Trac-IK）— 第 29 章对照",
    ],
    experiments=[
        "完成 P02：平面 2R/3R 的 FK/IK 可视化，往返误差低于自设阈值",
    ],
)

add(
    part="part1",
    file="ch08-jacobian.md",
    title="第 8 章 速度、雅可比与静力学",
    weeks="Week 7",
    project="P02",
    master=[
        "几何雅可比：关节速度 → 末端线速度/角速度",
        "奇异构型：雅可比秩下降，某些方向推不动",
        "静力学对偶：末端力/力矩 ↔ 关节力矩（概念）",
        "能从平面 FK 对关节角求导得到 J",
    ],
    key=[
        "控制与 IK 的增量步都依赖 J。奇异附近数值 IK 会抖，实验里把秩打出来。",
        "力控制细节进教材，本章只要能说出「对偶」二字和一张图。",
    ],
    must=[
        "[Modern Robotics 第 5 章](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) Velocity Kinematics and Statics",
        "[Stanford CS223A Jacobian 讲座](https://see.stanford.edu/Course/CS223A)",
        "画出平面 2R 奇异位形并打印 rank(J)",
    ],
    advanced=[
        "操作空间控制（Khatib）— CS223A 后半 / 力控方向",
        "可操作度椭球 — 臂设计选修",
        "差速底盘的非完整约束与雅可比 — 第 15–16 章对照",
    ],
    experiments=[
        "画出平面 2R 奇异位形，验证雅可比秩下降",
    ],
)

add(
    part="part1",
    file="ch09-dynamics-control.md",
    title="第 9 章 动力学与反馈控制：PID / LQR",
    weeks="Week 7–8",
    project="P01",
    master=[
        "P/I/D 各自消除什么误差、引入什么副作用",
        "二阶系统：超调、调节时间、稳态误差能从曲线读出",
        "LQR：要线性模型、二次代价，输出是增益矩阵 K",
        "动力学方程本章只要求「惯性 + 科氏 + 重力」的分层直觉",
    ],
    key=[
        "G1 要的是一套可复现的 PID 参数表，不是最优控制论文。先调简单对象（速度环或质量—弹簧—阻尼）。",
        "LQR 先看 PythonRobotics 动画建立直觉，公式跟 MR 第 11 章，不在正文展开 Riccati。",
    ],
    must=[
        "[Modern Robotics 第 11 章 Robot Control](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) 选读 PID/运动控制",
        "[PythonRobotics LQR 路径跟踪示例](https://github.com/AtsushiSakai/PythonRobotics#path-tracking) — 先看动画",
        "[MIT Underactuated 第 1 章](https://underactuated.mit.edu/) — 全驱动 vs 欠驱动直觉即可",
    ],
    advanced=[
        "MR 第 8 章开链动力学完整推导 — 写仿真器或真机辨识前再读",
        "Underactuated 倒立摆/行走后续章 — 第四篇之后选修",
        "MPC 作为带约束的滚动 LQR — 第 16 章主场",
    ],
    experiments=[
        "给二阶系统或小车速度环调 PID，记录超调、稳态误差、参数表（P01）",
    ],
)

add(
    part="part2",
    file="ch10-localization.md",
    title="第 10 章 定位：EKF、粒子滤波、直方图滤波",
    weeks="Week 6–8",
    project="P03",
    master=[
        "贝叶斯滤波的预测—更新循环",
        "EKF：在标称轨迹线性化，强非线性会失效",
        "粒子滤波：用样本近似分布；退化与重采样",
        "直方图滤波：离散栅格上的信念",
    ],
    key=[
        "三种滤波器做同一件事：融合运动模型与观测。差别是信念怎么表示。",
        "P03B 必须用「估计位姿」而不是真值去跟踪。本章先把三种算法分开跑通。",
    ],
    must=[
        "[PythonRobotics Localization](https://github.com/AtsushiSakai/PythonRobotics#localization) — 跑 EKF / PF / histogram",
        "[文档版教材](https://atsushisakai.github.io/PythonRobotics/) 对应 localization 页 — 公式看到预测与更新",
        "PoRA I 滤波讲座提纲 — 与课对照名词即可",
    ],
    advanced=[
        "Probabilistic Robotics 第 3–8 章 — 完整推导与变种",
        "UKF / 无迹变换 — EKF 不够时再上",
        "[ETH AMR](https://www.edx.org/learn/autonomous-robotics/eth-zurich-autonomous-mobile-robots) 定位模块 — 第二教材",
    ],
    experiments=[
        "必跑 extended_kalman_filter、particle_filter、histogram_filter，各留动画与五句原理",
    ],
)

add(
    part="part2",
    file="ch11-mapping.md",
    title="第 11 章 建图：栅格地图、射线投射、聚类",
    weeks="Week 8–9",
    project="P03",
    master=[
        "占用栅格：每格自由/占用概率的贝叶斯更新",
        "射线投射：一帧 LiDAR 如何改一排格子",
        "点云聚类与矩形拟合是「把格子变成物体」的简单手段",
    ],
    key=[
        "定位问「我在哪」，建图问「世界长什么样」。SLAM 两者一起估。",
        "2D 导航门禁用的就是占用栅格。本章把 LiDAR → 地图这一步做扎实。",
    ],
    must=[
        "[PythonRobotics Mapping](https://github.com/AtsushiSakai/PythonRobotics#mapping) — gaussian / raycasting / lidar_to_grid",
        "PoRA I 占用栅格与传感器讲座 — 对照名词",
    ],
    advanced=[
        "三维体素 / TSDF / 3DGS — 具身与仿真方向，不挡 G2",
        "语义地图 — 检测章之后选修",
        "Cartographer 子图与回环 — 第 25 章工程实现",
    ],
    experiments=[
        "必跑 gaussian_grid_map、raycasting_grid_map、lidar_to_grid_map",
    ],
)

add(
    part="part2",
    file="ch12-slam.md",
    title="第 12 章 SLAM：ICP、EKF-SLAM、FastSLAM",
    weeks="Week 9–10",
    project="P03",
    master=[
        "定位、建图、SLAM 的状态与观测各是什么",
        "ICP：两点云对齐，SVD 求 R、t",
        "EKF-SLAM：把路标放进同一个高斯向量，随路标增多变慢",
        "FastSLAM：粒子表示轨迹，每个粒子用 EKF 管路标",
    ],
    key=[
        "ICP 常当前端（配准），滤波/图优化是后端。本章先跑通滤波系 SLAM，图优化进进阶。",
        "G2 不要求完整 SLAM；但要能讲清为何开环里程计会漂。",
    ],
    must=[
        "[PythonRobotics SLAM](https://github.com/AtsushiSakai/PythonRobotics#slam) — ICP、EKF-SLAM、FastSLAM 1.0",
        "ICP 的 SVD 推导：教材或短文看懂一次即可",
    ],
    advanced=[
        "图 SLAM / 位姿图 / g2o / GTSAM — [gtbook/robotics](https://github.com/gtbook/robotics) 或十四讲后端",
        "视觉 SLAM 十四讲前端+后端 — 方向 A 加码，不挡 G2/G4",
        "Cartographer / slam_toolbox 工程 — 第 25 章",
    ],
    experiments=[
        "必跑 ICP Matching、EKF SLAM、FastSLAM 1.0",
    ],
)

add(
    part="part2",
    file="ch13-planning-grid.md",
    title="第 13 章 路径规划 I：Dijkstra / A* / D* / 势场",
    weeks="Week 10–11",
    project="P03",
    master=[
        "完备性、最优性、计算量三指标能用来对比算法",
        "Dijkstra 与 A*：启发函数可采纳则 A* 最优",
        "D* / D* Lite：环境变化时的增量搜索直觉",
        "势场：快但不完备，易局部最小",
    ],
    key=[
        "栅格规划是 Nav2 全局规划器的原型。G2 用 A*（或 Dijkstra）即可。",
        "启发不可采纳会丢最优，实验里对比扩展节点数。",
    ],
    must=[
        "[PythonRobotics 栅格搜索](https://github.com/AtsushiSakai/PythonRobotics#path-planning) — Dijkstra、A*、D* Lite、Potential Field",
        "宾大 Motion Planning 作业思路（A*/Dijkstra）— 若课下架则只对照算法，用 Python 实现",
    ],
    advanced=[
        "Modern Robotics 第 10 章搜索部分 — 理论补强",
        "覆盖路径 / 割草机规划 — 应用选修",
        "Nav2 Navfn / Smac Planner 源码 — 第 26–27 章",
    ],
    experiments=[
        "同图对比 Dijkstra 与 A* 的扩展节点数；再跑 D* Lite 与势场",
    ],
)

add(
    part="part2",
    file="ch14-planning-sampling.md",
    title="第 14 章 路径规划 II：PRM / RRT / RRT*",
    weeks="Week 11–12",
    project="P03",
    master=[
        "高维（机械臂）为何更常用采样规划而不是细栅格",
        "PRM：先建路线图再查询",
        "RRT：向随机样本扩展树；RRT* 渐近最优的含义",
        "碰撞检测是采样规划的实际瓶颈（概念）",
    ],
    key=[
        "移动机器人 2D 用栅格往往够；臂的 C 空间用 RRT 族。G2 小车不必上 RRT，但要能讲清差别。",
    ],
    must=[
        "[PythonRobotics PRM / RRT / RRT*](https://github.com/AtsushiSakai/PythonRobotics#path-planning)",
        "[Modern Robotics 第 10 章](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) 采样规划概念",
    ],
    advanced=[
        "RRT-Connect、Informed RRT*、BIT* — MoveIt 默认规划器相关",
        "OMPL 文档 — 第 29 章对照",
        "动力学约束下的 kinodynamic RRT — 第 15 章之后",
    ],
    experiments=[
        "必跑 PRM、RRT、RRT*，对比有无障碍时的树形状",
    ],
)

add(
    part="part2",
    file="ch15-trajectory.md",
    title="第 15 章 轨迹生成：多项式、Reeds-Shepp、Frenet",
    weeks="Week 12–13",
    project="P03",
    master=[
        "路径是几何，轨迹带时间（位置、速度、加速度）",
        "五次多项式为何能配位置与速度边界",
        "非完整约束：车不能横着开，故 Dubins / Reeds-Shepp",
        "Frenet：沿道路中心线的横向/纵向解耦直觉",
    ],
    key=[
        "规划器给出路点后，跟踪器吃的是带时间的参考。本章把「路」变成「可跟踪的曲线」。",
    ],
    must=[
        "[PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) quintic polynomials、Reeds Shepp、Frenet 最优轨迹",
        "Coursera Aerial Robotics 轨迹生成作业思路（若可及）— 多项式边界条件",
    ],
    advanced=[
        "Minimum snap / 微分平坦（四旋翼）— 选修飞行",
        "MR 第 9 章 Trajectory Generation",
        "Nav2 控制器用的路径插值 — 第 26 章对照",
    ],
    experiments=[
        "必跑 quintic_polynomials、reeds_shepp、frenet；确认位置速度加速度连续",
    ],
)

add(
    part="part2",
    file="ch16-tracking.md",
    title="第 16 章 路径跟踪：Stanley / LQR / MPC",
    weeks="Week 13–14",
    project="P03",
    master=[
        "纯追踪 / Stanley 的几何：预瞄与横向误差",
        "LQR 跟踪：线性化误差模型 + 增益",
        "MPC：滚动优化，能加约束（速度、转角）",
        "G2 跟踪必须吃定位结果，不能用真值作弊",
    ],
    key=[
        "控制器输出是速度与转向（或加速度）。调参看横向误差曲线，不要只看「最后到没到」。",
    ],
    must=[
        "[PythonRobotics Path Tracking](https://github.com/AtsushiSakai/PythonRobotics#path-tracking) — Stanley、LQR、MPC",
        "第 9 章 PID 笔记 — 对照：几何跟踪 vs 误差反馈",
    ],
    advanced=[
        "非线性 MPC、C-GMRES — PythonRobotics 高级示例",
        "Nav2 DWB / MPPI 局部规划 — 第 26 章",
        "差速与阿克曼模型差异 — 自己推一层运动学即可",
    ],
    experiments=[
        "必跑 Stanley、LQR speed/steering、MPC；G2 用其中之一接估计位姿",
    ],
)

add(
    part="part2",
    file="ch17-arm-biped.md",
    title="第 17 章 机械臂避障与双足规划初探",
    weeks="Week 14",
    project="P03",
    tracks="机械臂加码",
    master=[
        "关节空间规划：在 C 空间避障，不是只在工作空间画直线",
        "平面臂避障示例如何把第 13–14 章接上 FK",
        "倒立摆步态只建立直觉，不要求真机双足",
    ],
    key=[
        "移动机器人 G2 不依赖本章。本章是给第五篇和选修人形的预告片：同样是规划，状态定义不同。",
    ],
    must=[
        "[PythonRobotics Arm Navigation / Bipedal](https://github.com/AtsushiSakai/PythonRobotics#arm-navigation)",
    ],
    advanced=[
        "MIT Underactuated 行走与平衡章节",
        "MoveIt 规划组与碰撞 — 第 29 章",
        "Open_Duck / 宇树运动控制论文 — 第 41 章",
    ],
    experiments=[
        "必跑 N joint arm、arm obstacle avoidance、bipedal planner 各一，笔记里对比与小车规划的差别",
    ],
)

add(
    part="part3",
    file="ch18-ros2-intro.md",
    title="第 18 章 ROS 2 安装、概念与工作空间",
    weeks="Week 10–11",
    project="P04",
    status="进行中",
    master=[
        "发行版锁死 Humble 或 Jazzy，不用 ROS 1",
        "能讲清 ROS 2 解决发现、通信、启动、生态接口，不代替算法",
        "能画出分层：DDS/RMW → RCL → rclpy → 节点与工具 → 应用栈，并指出个人开发落在哪一层",
        "node、topic、package、workspace、overlay 各是什么",
        "colcon build、先 source 系统再 source 工作空间的顺序",
        "turtlesim 能讲清计算图；自写发布/订阅能跑",
    ],
    key=[
        "ROS 2 是中间件：帮多个进程发现彼此、按标准消息传数据、被 launch 一起拉起。EKF、A*、PID 仍是算法，不因进了节点就消失。",
        "分层是为了换传输不换节点、Python 与 C++ 共用一张计算图。个人主写节点和包，调用 rclpy，用 CLI / RViz；本周不碰 DDS，不改 Nav2。",
        "可与第二篇后半重叠安装，但 P03B 仍须完成后再把算法塞进回调。四种通信与 launch 见第 19 章，本周只做到 pub/sub。",
    ],
    must=[
        "[fishros/d2l-ros2 第 1–2 章](https://github.com/fishros/d2l-ros2) 或 [在线教程](https://fishros.com/d2lros2/)",
        "[ROS 2 官方 Beginner](https://docs.ros.org/en/humble/Tutorials.html) 安装与 turtlesim",
        "PoRA Lab 0：Install ROS — 节奏对照",
    ],
    advanced=[
        "DDS / RMW 实现差异 — 多机通信时再读官方 Concepts",
        "[mmabas77 ROS 2 Roadmap 2025](https://github.com/mmabas77/ROS-2-Practical-Course-Roadmap-2025) — 实验课式周历",
        "Docker 内装 ROS — 环境隔离选修",
    ],
    experiments=[
        "创建 colcon 工作空间，编写并运行一个 Python 发布节点",
    ],
)

add(
    part="part3",
    file="ch19-communication.md",
    title="第 19 章 通信：话题、服务、参数、Action",
    weeks="Week 11–13",
    project="P04",
    status="进行中",
    master=[
        "能讲清话题是多对多数据流，服务是客户端按服务名做一次请求—应答（服务端之间不会自动互调）",
        "会为连续传感、偶发命令、长任务、配置分别选型：topic / service / action / param",
        "能把「摄像头 → 识别 → 播报」拆成多个节点，而不是一个进程里读图+模型+发音",
        "自定义 srv/msg 与 launch 拉起多节点；P04 同一包四种原语各出现一次",
    ],
    key=[
        "节点只靠具名接口通信。话题适合图像和检测结果这种流；服务适合「说一句话」这种问完要等说完；Action 适合可取消的长任务；参数是挂在节点上的配置，不是传感器通道。",
        "服务不会和服务通信：一个节点提供 `/speak`，另一个节点当客户端去调这个名字。要把识别和播报串起来，需要中间的策略节点把话题流变成服务调用。",
        "摄像头场景：camera 只发图，detector 只发检测，announcer 决定何时说，tts 只负责发音。本周用字符串假数据跑通形状即可。P04 四种原语要在同一 launch 里能指出来；TF 遥控车留给第 20 章。",
    ],
    must=[
        "[fishros/d2l-ros2 第 3–4 章](https://github.com/fishros/d2l-ros2) — 话题与服务",
        "[Understanding topics](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/Understanding-ROS2-Topics.html) / [services](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Services/Understanding-ROS2-Services.html) / [actions](https://docs.ros.org/en/humble/Tutorials/Intermediate/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html) — CLI 先摸清形态",
        "[Writing a simple service and client (Python)](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html) — 过实验 C",
    ],
    advanced=[
        "QoS（可靠/尽力、深度）— 激光与无线丢包时必看官方 QoS",
        "生命周期节点 — Nav2 里大量使用，第 26 章对照",
        "组件容器与零拷贝 — 性能选修",
    ],
    experiments=[
        "P04：同一功能包覆盖四种通信，launch 一键起",
    ],
)

add(
    part="part3",
    file="ch20-tools.md",
    title="第 20 章 工具链：TF2、URDF、Launch、RViz",
    weeks="Week 13–14",
    project="P04",
    master=[
        "TF 树：父子坐标系，查询 base_link → laser",
        "URDF/Xacro 描述连杆与关节",
        "RViz 检查坐标系、激光、模型是否对齐",
        "Launch 组合节点与参数",
    ],
    key=[
        "机器人系统最常见的 bug 是 TF 断了或时间戳不对。G3 验收要 TF 树截图。",
    ],
    must=[
        "d2l-ros2 第 5 章及机器人学篇中的 TF",
        "[tf2 教程](https://docs.ros.org/en/humble/Tutorials/Intermediate/Tf2/Introduction-To-Tf2.html)",
        "[URDF 教程](https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/URDF-Main.html)",
    ],
    advanced=[
        "robot_state_publisher 与关节状态 — 仿真/真机共用",
        "REP-105 坐标系约定（map/odom/base_link）— 第 25 章必读",
        "自定义 RViz 插件 — 不挡 G3",
    ],
    experiments=[
        "静态 TF + RViz 对齐模型和激光，TF 树无断",
    ],
)

add(
    part="part3",
    file="ch21-sim.md",
    title="第 21 章 建模与仿真：Gazebo / Webots",
    weeks="Week 14–16",
    project="P05",
    master=[
        "差速车 URDF 含激光与 IMU，能在仿真里遥控",
        "里程计与激光话题名称、坐标系正确",
        "同一阶段只深挖一个仿真器（Gazebo 或 Webots）",
    ],
    key=[
        "仿真是假物理、真接口。G3 要「自己的车能遥控」，不必等 TurtleBot 官方包。",
    ],
    must=[
        "d2l-ros2 第 8–9 章建模仿真",
        "所选仿真器的官方 ROS 2 教程（[Gazebo](https://gazebosim.org/) 或 [Webots ROS 2](https://github.com/cyberbotics/webots_ros2)）",
        "PoRA Lab：RViz + Turtlebot — 对照传感器话题",
    ],
    advanced=[
        "SDF 与 URDF 的差别、Gazebo 版本（Classic vs Harmonic）与 ROS 发行版匹配",
        "传感器噪声模型 — 后面 SLAM 调参",
        "Isaac Sim 桥 — 第六篇再碰",
    ],
    experiments=[
        "仿真键盘遥控小车，确认里程计与激光话题",
    ],
)

add(
    part="part3",
    file="ch22-control.md",
    title="第 22 章 ros2_control 与 Micro-ROS",
    weeks="Week 16–18",
    project="P06",
    master=[
        "hardware interface、controller manager、diff_drive_controller 各干什么",
        "为何不要长期手写「假 cmd_vel → 轮速」桥",
        "Micro-ROS：MCU 上跑精简 ROS 客户端的定位",
    ],
    key=[
        "仿真里先把 ros2_control 跑通，真机只是换 hardware plugin。P06 会用到。",
    ],
    must=[
        "d2l-ros2 第 13–15 章（Control / Micro-ROS / 硬件实战概览）",
        "[ros2_control 文档](https://control.ros.org/) 入门与差速示例",
    ],
    advanced=[
        "编写自定义 hardware interface — 真机驱动时",
        "Micro-ROS 官方教程 — 有 MCU 再做",
        "实时内核与控制频率 — 选修",
    ],
    experiments=[
        "仿真中用 ros2_control 驱动轮子；若仍用手写桥，必须在笔记写明原因",
    ],
)

add(
    part="part4",
    file="ch23-cv.md",
    title="第 23 章 计算机视觉基础：OpenCV 与标定",
    weeks="Week 16–18",
    project="无",
    master=[
        "针孔模型：内参、畸变、像素 ↔ 光线",
        "棋盘格标定流程，重投影误差有数字",
        "OpenCV 读写图像、去畸变、画框",
    ],
    key=[
        "没有内参，后面的检测框无法变成空间点。G4 用激光可以不过本章，但操作/具身方向必须过。",
    ],
    must=[
        "[OpenCV 相机标定教程](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)",
        "OpenCV Python 入门：图像 IO 与几何变换",
        "PoRA I 相机与特征讲座提纲",
    ],
    advanced=[
        "[Stanford CS231A](http://web.stanford.edu/class/cs231a/) 多视几何 — 视觉 SLAM 加码",
        "《视觉 SLAM 十四讲》第 5 讲相机与图像",
        "手眼标定（eye-in-hand / eye-to-hand）— 第 28 章",
    ],
    experiments=[
        "用手机或 USB 摄像头完成标定，保存 yaml，记下重投影误差",
    ],
)

add(
    part="part4",
    file="ch24-detection.md",
    title="第 24 章 目标检测、分割与深度感知",
    weeks="Week 18–20",
    project="无",
    master=[
        "检测框、分割掩码、类别分数分别是什么",
        "深度从哪来：RGB-D、双目、LiDAR、单目估计的差别",
        "能在仿真或图片上跑通一次 YOLO（或等价）并可视化",
    ],
    key=[
        "导航门禁 G4 可以只用激光。检测是为了后面抓取与 VLA。先跑通推理，训练留进阶。",
    ],
    must=[
        "YOLO 官方文档：安装与一次推理（版本自选，记下型号）",
        "every-embodied 视觉章节中「检测/分割」入门页（有 GPU 再上 SAM）",
    ],
    advanced=[
        "[CS231n](http://cs231n.stanford.edu/) 检测与分割讲座 — 第六篇前补 CNN",
        "6D 位姿估计 / AnyGrasp — 第五篇抓取加码",
        "把检测框发到 ROS 2 话题 — 与 Nav2/MoveIt 集成时做",
    ],
    experiments=[
        "对仿真或数据集图片跑检测，框可视化入库；有 mAP 更好，没有则写清数据来源",
    ],
)

add(
    part="part4",
    file="ch25-slam-practice.md",
    title="第 25 章 SLAM 建图实战：slam_toolbox / Cartographer",
    weeks="Week 18–21",
    project="P05",
    master=[
        "2D 激光 SLAM 出图：slam_toolbox 或 Cartographer 选一个跑通",
        "map.yaml + pgm 的含义；map / odom / base_link（REP-105）",
        "回环如何抑制里程计漂移（现象层）",
    ],
    key=[
        "G4 必须有一张自己录的图。算法细节已在第 12 章，本章是工程 bringup。",
    ],
    must=[
        "d2l-ros2 第 10 章 SLAM 建图",
        "[slam_toolbox](https://github.com/SteveMacenski/slam_toolbox) 或 Nav2 官方 mapping 教程",
        "REP-105 坐标系短文",
    ],
    advanced=[
        "Cartographer 调参与 3D — 需要时再上",
        "视觉 SLAM（ORB-SLAM 等）— 方向 A，不挡 G4",
        "多雷达标定 — 真机选修",
    ],
    experiments=[
        "TurtleBot3 或自己的仿真车出图，保存 map.yaml 与 pgm，过程截图入库",
    ],
)

add(
    part="part4",
    file="ch26-nav2.md",
    title="第 26 章 Nav2 导航框架仿真实战",
    weeks="Week 20–23",
    project="P05",
    master=[
        "节点图：定位 → 全局规划 → 局部规划 → 控制 → 恢复",
        "代价地图膨胀半径、足迹 footprint 的直观效果",
        "行为树（BT）决定失败后干什么（概念）",
        "G4：三个航点 + 一次挡路",
    ],
    key=[
        "Nav2 是工业导航栈。调参比改源码优先。长期转圈先查定位和膨胀，不要先骂规划器。",
    ],
    must=[
        "d2l-ros2 第 11 章 Nav2 仿真实战",
        "[Nav2 文档 Getting Started](https://docs.nav2.org/)",
        "PoRA Lab：Nav to goal / waypoint 思路",
    ],
    advanced=[
        "BT 节点编写 — 第 27 章",
        "MPPI / DWB 控制器对比 — 调参加码",
        "多机与定位融合（EKF 里程计+IMU）— robot_localization 包",
    ],
    experiments=[
        "完成 P05：三航点到达；人为挡路一次，能恢复或写清失败与参数",
    ],
)

add(
    part="part4",
    file="ch27-nav2-advanced.md",
    title="第 27 章 Nav2 进阶：自定义规划器与恢复行为",
    weeks="Week 23–24",
    project="P06",
    tracks="导航加码",
    master=[
        "参数与 BT 能改出可观察的行为差",
        "插件接口：全局/局部规划器如何挂进 Nav2（读懂即可）",
        "P06：自己的 URDF 车也能导航（满分项，不挡 G4）",
    ],
    key=[
        "把 PythonRobotics 的 A* 接到 Nav2 是高难度加码，不是 G4 要求。先改参数证明你能控制栈。",
    ],
    must=[
        "d2l-ros2 第 12 章 Nav2 进阶",
        "[Nav2 插件与参数说明](https://docs.nav2.org/)",
    ],
    advanced=[
        "编写 nav2_core 规划器插件 — 作品集加分",
        "SMAC Hybrid-A* 与阿克曼 — 车辆运动学",
        "keepout filter / 速度限制层 — 场地部署",
    ],
    experiments=[
        "改膨胀半径或恢复行为并对比两次实验；P06 按满分项目标推进",
    ],
)

add(
    part="part5",
    file="ch28-grasp.md",
    title="第 28 章 抓取与操作：接触、夹爪、手眼标定",
    weeks="Week 20–22",
    project="无",
    master=[
        "眼在手上 / 眼在外侧两种标定",
        "抓取是接触任务：规划成功 ≠ 物体被拿起",
        "相机、末端、物体三个坐标系如何画在一张图上",
    ],
    key=[
        "G5 在仿真里用 MoveIt 做 pick-and-place。本章先把坐标关系画对，避免第 29 章盲目调姿态。",
    ],
    must=[
        "[Modern Robotics 第 12 章](https://hades.mech.northwestern.edu/index.php/Modern_Robotics) Grasping 概念（接触、力闭合点到为止）",
        "every-embodied 手眼协调笔记（若与当前仿真栈匹配）",
    ],
    advanced=[
        "力闭合 / 形闭合完整条件 — 操作研究方向",
        "夹爪选型与欠驱动手 — 硬件选修",
        "6D 抓取检测论文线 — 与第 24 章衔接",
    ],
    experiments=[
        "画出相机—末端—物体三坐标系，标明眼在手或眼在外",
    ],
)

add(
    part="part5",
    file="ch29-moveit.md",
    title="第 29 章 MoveIt 2 仿真：规划、碰撞、抓取流水线",
    weeks="Week 22–25",
    project="P07",
    master=[
        "planning scene、碰撞对象、规划组",
        "规划到预抓取 → 闭合夹爪 → 放置",
        "G5：抓取放置 ≥ 8/10",
    ],
    key=[
        "对标 Modern Robotics Course 6 的 pick-and-place，用 MoveIt+仿真实现，不必上 CoppeliaSim/youBot。",
    ],
    must=[
        "d2l-ros2 第 19–20 章 MoveIt 仿真与进阶",
        "[MoveIt 2 官方教程](https://moveit.ai/)",
        "MR Course 6 任务描述（移动操作）— 只借鉴任务，不强制原仿真器",
    ],
    advanced=[
        "笛卡尔路径与约束规划 — 精细插入任务",
        "MoveIt Servo — 遥操作",
        "与 Nav2 组合的移动操作 — 终章方向 B+",
    ],
    experiments=[
        "P07：规划场景至少一个物体；抓取放置成功率写入 README",
    ],
)

add(
    part="part5",
    file="ch30-moveit-hw.md",
    title="第 30 章 MoveIt 2 进阶与真机控制",
    weeks="Week 25–27",
    project="P07",
    tracks="机械臂加码",
    master=[
        "仿真控制器与真机驱动的差异：延迟、限位、标定误差",
        "急停、关节限位、电流/力矩限制、工作空间围栏",
        "无真机则写清仿真边界，不假装做过真机",
    ],
    key=[
        "真机不是 G5 的门槛。安全清单是本章的验收。有硬件再换 hardware interface。",
    ],
    must=[
        "d2l-ros2 第 21 章 MoveIt 真机控制（按你的硬件选读）",
        "厂商或 ros2_control 真机示例中的安全段落",
    ],
    advanced=[
        "重力补偿与拖动示教 — 协作臂",
        "力控 / 阻抗 — CS223A 力控讲座",
        "ISO 机器人安全标准导读 — 工业部署",
    ],
    experiments=[
        "列出急停、限位、电流三条安全清单；无真机则写仿真无法覆盖的风险",
    ],
)

add(
    part="part5",
    file="ch31-lerobot.md",
    title="第 31 章 LeRobot 与桌面机械臂入门",
    weeks="Week 26–28",
    project="P10",
    tracks="机械臂加码 · 具身加码",
    master=[
        "遥操作 → 数据集 → 策略训练的数据闭环",
        "一条 episode 里观测、动作、时间戳字段是什么",
        "LeRobot 仿真或官方 notebook 能跑通最小例子",
    ],
    key=[
        "这是方向 B/C 的数据层。G5 不要求训练策略。预算不够不要买臂，先把数据格式搞懂。",
    ],
    must=[
        "[huggingface/lerobot](https://github.com/huggingface/lerobot) README 与官方示例",
        "every-embodied 中 LeRobot / 遥操作入门（与硬件匹配再跟）",
    ],
    advanced=[
        "SO-ARM101 装配与标定文档 — 有预算再买",
        "ACT / Diffusion Policy 数据需求 — 第 35 章",
        "多机采集与版本管理 — 规模化选修",
    ],
    experiments=[
        "记录一条最小遥操作或仿真 episode，写清数据字段名",
    ],
)

add(
    part="part6",
    file="ch32-simulators.md",
    title="第 32 章 仿真引擎矩阵：Webots / MuJoCo / Isaac Lab / Genesis",
    weeks="Week 24–26",
    project="P08",
    master=[
        "按任务选引擎：教学（Webots）、接触控制（MuJoCo）、大规模 RL（Isaac Lab）、具身通用（Genesis）",
        "同一项目锁死一个引擎",
        "P08 默认 MuJoCo + every-embodied Hello",
    ],
    key=[
        "换仿真器不是进步。G6 在一个环境里把闭环成功率做出数字。",
    ],
    must=[
        "[every-embodied 快速开始](https://github.com/datawhalechina/every-embodied) — Hello MuJoCo",
        "所选引擎的官方 installation 一页（只装一个）",
    ],
    advanced=[
        "Isaac Lab 官方教程 — 有 GPU 且做 RL 再上",
        "Genesis / Habitat / CARLA — 按方向打开，勿并行",
        "域随机与 Sim2Real 清单 — 第 36 章",
    ],
    experiments=[
        "跑通 MuJoCo Hello（或等价官方 demo），命令写入 README",
    ],
)

add(
    part="part6",
    file="ch33-rl.md",
    title="第 33 章 机器人强化学习：PPO / SAC / 模仿学习",
    weeks="Week 26–30",
    project="无",
    master=[
        "MDP：状态、动作、奖励、折扣",
        "on-policy（PPO）与 off-policy（SAC）的差别一句话能说清",
        "模仿学习（BC、ACT）与 RL 的关系：先克隆再强化（概念）",
        "一次最小训练：Pendulum 或到位任务有回报曲线",
    ],
    key=[
        "G6 可以用脚本闭环而不训练 RL。本章是为了读懂 P09 和论文方法部分。",
    ],
    must=[
        "every-embodied 或 dive-into-embodied-ai 强化学习入门章",
        "[Spinning Up on-policy / off-policy 概述](https://spinningup.openai.com/en/latest/) 或 CleanRL 一个 PPO 脚本对照",
        "[MIT Underactuated](https://underactuated.mit.edu/) 中与轨迹优化/学习相关的选读（点到为止）",
    ],
    advanced=[
        "PPO/SAC 论文 — 实现细节",
        "Isaac Lab 并行 RL — 有 GPU",
        "奖励工程与 sim-to-real 域随机 — 第 36 章",
    ],
    experiments=[
        "Pendulum 或到位任务跑通 PPO 或 SAC 一次，回报曲线入库",
    ],
)

add(
    part="part6",
    file="ch34-embodied-loop.md",
    title="第 34 章 具身入门：识别—规划—抓取闭环",
    weeks="Week 28–32",
    project="P08",
    master=[
        "脚本闭环：检测或颜色 → 目标位姿 → 运动 → 夹爪",
        "失败要能归因：感知 / 规划 / 接触",
        "G6：固定场景 ≥ 20 次，成功率 ≥ 50%",
    ],
    key=[
        "这是第六篇门禁。先不用大模型。能稳定抓杯子再谈 VLA。",
    ],
    must=[
        "[every-embodied 第一、二阶段](https://github.com/datawhalechina/every-embodied) 识别—规划—抓取",
        "第 28–29 章自己的坐标系图 — 对照闭环每一步",
    ],
    advanced=[
        "DAgger / 人类介入 — 提高成功率",
        "多物体与遮挡 — 加码场景",
        "真机同一脚本 — 第 37 章后",
    ],
    experiments=[
        "完成 P08，成功率与失败分类写入 README",
    ],
)

add(
    part="part6",
    file="ch35-vla.md",
    title="第 35 章 VLA：RT 系列、OpenVLA、SmolVLA、π0",
    weeks="Week 32–36",
    project="P09",
    tracks="具身加码",
    master=[
        "VLA = 视觉 + 语言指令 → 动作；能画数据流",
        "微调与零样本不可混为一谈",
        "P09 选一条算力够的线（ACT 或 SmolVLA 等）做出评测数字",
    ],
    key=[
        "P09 不挡 G6。算力不够就精读一篇 + 小规模微调，禁止只 clone。",
    ],
    must=[
        "every-embodied VLA 章节：RT 系列解读 + 一条可跑通的 SmolVLA 或 ACT 教程",
        "OpenVLA / π0 选一篇官方 README 看清输入输出维度",
    ],
    advanced=[
        "LIBERO / SIMPLER 评测协议原文",
        "后续 SOTA 导读（WALL、3DVLA 等）— 组队学习可选，勿全开",
        "真机策略服务器（EVA-Client 等）— 有机群再读",
    ],
    experiments=[
        "P09：配置入库、评测数字、写明微调或零样本",
    ],
)

add(
    part="part6",
    file="ch36-vln-sim2real.md",
    title="第 36 章 VLN、世界模型与 Sim2Real",
    weeks="Week 34–36",
    project="无",
    tracks="具身加码",
    master=[
        "VLN 是语言引导导航，与操作型 VLA 任务不同",
        "Sim2Real 典型缺口：感知、延迟、接触、域随机",
        "世界模型本章只要求「能 rollout 或能当数据引擎」的分类直觉",
    ],
    key=[
        "主线不要求复现 ETPNav 或视频世界模型。一篇笔记 + 一张自绘框图即可过章。",
    ],
    must=[
        "every-embodied VLN 概念页或 ETPNav 导读的「任务定义」一节",
        "自列 5 条 Sim2Real 缺口，对照自己的 P08 仿真",
    ],
    advanced=[
        "Habitat / VLN-CE 实验 — 方向 C 导航分支",
        "LeWM / GE-Sim 等世界模型导读 — 科研选修",
        "域随机在 Isaac Lab 中的配置 — 有 GPU",
    ],
    experiments=[
        "800 字以内笔记 + 自绘数据流；不强制训练",
    ],
)

add(
    part="part7",
    file="ch37-low-cost.md",
    title="第 37 章 低成本真机：开源小车与 OttoDIY",
    weeks="Week 12 起可并行",
    project="P10",
    tracks="选修",
    master=[
        "真机第一目标是安全与可重复，不是炫技",
        "开环动作：指令与实际运动对得上",
        "无预算则用 BOM/接线图阅读代替，并在笔记标明",
    ],
    key=[
        "真机不是前 24 周门槛。与主线并行时占用时间必须写进附录 E，避免冲掉门禁。",
    ],
    must=[
        "[OttoDIY/PLUS](https://github.com/OttoDIY/PLUS) 或你手头套件的官方入门",
        "d2l-ros2 实体机器人篇第 16–18 章结构（有车再跟）",
        "[附录 D 硬件预算](../appendix/d-hardware.md)",
    ],
    advanced=[
        "树莓派 + 激光小车 ROS 2 bringup — 方向 A",
        "电控、电源、接地 — 避免烧掉口",
        "Micro-ROS 上 MCU — 第 22 章实践",
    ],
    experiments=[
        "有硬件：完成一次开环动作；无硬件：BOM 与接线图阅读笔记",
    ],
)

add(
    part="part7",
    file="ch38-track-nav.md",
    title="第 38 章 方向 A：移动机器人导航完整项目",
    weeks="Week 28–40",
    project="P10",
    tracks="导航加码",
    master=[
        "交付：地图、三航点以上演示、失败恢复、参数表",
        "能向别人 5 分钟讲清 TF、定位、规划、控制各看哪个话题",
    ],
    key=[
        "G7 若选 A：在 G4/P06 上加障碍、恢复、文档，而不是新开第三套仿真。",
    ],
    must=[
        "P05、P06 全部产物与 Nav2 调参笔记",
        "[Nav2 真机 TurtleBot 教程](https://docs.nav2.org/tutorials/docs/navigation2_on_real_turtlebot3.html) — 有真机再跟",
    ],
    advanced=[
        "视觉定位 / GPS 融合 — 室外",
        "多机编队 — 选修",
        "覆盖清扫等应用层任务",
    ],
    experiments=[
        "按附录 E 与 P10 填写复盘；演示视频或连续截图",
    ],
)

add(
    part="part7",
    file="ch39-track-arm.md",
    title="第 39 章 方向 B：桌面机械臂操作完整项目",
    weeks="Week 28–40",
    project="P10",
    tracks="机械臂加码",
    master=[
        "交付：抓取演示、相机方案、安全清单",
        "仿真或真机二选一写清边界",
    ],
    key=[
        "G7 若选 B：把 G5 做成可重复的流水线，并接上第 31 章数据记录（即使不训练）。",
    ],
    must=[
        "P07 与第 30–31 章产物",
        "[PAROL6](https://github.com/PCrnjak/PAROL6-Desktop-robot-arm) 或 SO-ARM 文档 — 仅在采购后作为主手册",
    ],
    advanced=[
        "双手 / 灵巧手 — 远超第一年范围",
        "力控装配 — 选修",
        "移动操作（底盘+臂）— MR C6 完整版",
    ],
    experiments=[
        "P10 演示与安全清单；真机必须含急停演练记录",
    ],
)

add(
    part="part7",
    file="ch40-track-vla.md",
    title="第 40 章 方向 C：具身 VLA 完整项目",
    weeks="Week 28–40",
    project="P10",
    tracks="具身加码",
    master=[
        "一条能跑完的线：数据或微调 + 评测协议 + 成功率",
        "写清不是同时开三条 SOTA",
    ],
    key=[
        "G7 若选 C：在 P08/P09 上收口，禁止新开第三套模型当「学习」。",
    ],
    must=[
        "P08、P09 与 every-embodied 第三阶段中你实际跟的那一条教程",
        "对应 benchmark 的官方评测说明（LIBERO 等）",
    ],
    advanced=[
        "世界模型后训练 — 仅当算力和主线都完成",
        "真机策略部署 — 有臂再做",
        "论文级消融 — 科研选修",
    ],
    experiments=[
        "P10：训练配置、评测协议、成功率、失败案例",
    ],
)

add(
    part="part7",
    file="ch41-electives.md",
    title="第 41 章 选修：四足 / 人形 / 云端与安全",
    weeks="按需",
    project="无",
    tracks="选修",
    master=[
        "主线门禁未完成前，本章不得占用每周 10 小时配额",
        "若选修：锁一个仿真器、一套官方任务，写清放弃了主线哪部分时间",
    ],
    key=[
        "云机器人与网络安全不是第一年主线，只保留意识清单。完整人形不是考核。",
    ],
    must=[
        "[附录 A 资源地图](../appendix/a-resources.md) 对应条目",
        "宇树 / Open_Duck 官方仿真 README（仅当真正选修）",
    ],
    advanced=[
        "Isaac Lab 四足/人形任务",
        "commitverse Phase 8–9 云与安全资源 — 意识即可",
        "多机器人 DDS 域与鉴权 — 部署选修",
    ],
    experiments=[
        "写清为什么现在选修、占用了主线哪部分时间；否则本章保持「待学习」且不占用工时",
    ],
)


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {x}" for x in items)


def materials(items: list[str]) -> str:
    return "\n".join(f"- {x}" for x in items)


SKIP_NOTE = {
    "导航加码": "本章为 **导航加码**。终章不加深导航的，读完标题即可跳过，不挡 G1–G6。",
    "机械臂加码": "本章为 **机械臂加码**。终章不加深机械臂的，读完标题即可跳过，不挡 G1–G6。",
    "机械臂加码 · 具身加码": "本章为 **机械臂 / 具身加码**。两条都不加深的，读完标题即可跳过。",
    "具身加码": "本章为 **具身加码**。终章不加深 VLA 的，读完标题即可跳过，不挡 G6（P08 仍要做）。",
    "选修": "本章为 **选修**。主干门禁未完成前不要占用每周配额。",
}


def skip_banner(tracks: str) -> str:
    if tracks == "主干":
        return ""
    note = SKIP_NOTE.get(tracks, f"本章为「{tracks}」，非对应加码方向可跳过。")
    return f"""
!!! warning \"可跳过\"
    {note}
"""


def load_override(ch: dict, kind: str) -> str | None:
    path = OVERRIDE / f"{Path(ch['file']).stem}.{kind}.md"
    if path.exists():
        return path.read_text(encoding="utf-8").strip()
    return None


def render(ch: dict) -> str:
    proj = f"`{ch['project']}`" if ch["project"] != "无" else "本章以笔记与小实验为主"
    exp = load_override(ch, "experiments")
    if not exp:
        exp = "\n".join(f"- [ ] {e}" for e in ch["experiments"])
    notes = ch.get("notes") or load_override(ch, "notes") or DEFAULT_NOTES
    tracks = ch.get("tracks", "主干")
    status = ch.get("status", "待学习")
    banner = skip_banner(tracks)
    head = f"""# {ch['title']}

| 字段 | 内容 |
|------|------|
| 状态 | {status} |
| 周次 | {ch['weeks']} |
| 路线 | {tracks} |
| 对应项目 | {proj} |
| 所属篇 | `{ch['part']}` |
{banner}
## 需要掌握

{bullets(ch['master'])}

## 关键内容

{chr(10).join(ch['key'])}

## 推荐学习资料

### 必看（掌握本章）

{materials(ch['must'])}

### 进阶拓展

{materials(ch['advanced'])}

## 实验清单

"""
    return (
        head
        + exp
        + "\n\n## 笔记\n\n"
        + notes
        + "\n\n## 复盘\n\n- 卡住的地方：\n- 下一章开始前必须补上的漏洞：\n"
    )


def main() -> None:
    assert len(C) == 41, len(C)
    for ch in C:
        path = DOCS / ch["part"] / ch["file"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(ch).strip() + "\n", encoding="utf-8")
    print(f"wrote {len(C)} chapters")


if __name__ == "__main__":
    main()
