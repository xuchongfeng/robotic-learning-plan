# 第 2 章 Python 工程实践与科学计算

| 字段 | 内容 |
|------|------|
| 状态 | 待学习 |
| 周次 | Week 1–2 |
| 路线 | 主干 |
| 对应项目 | `P01` |
| 所属篇 | `part1` |

## 需要掌握

- 虚拟环境、依赖冻结、pytest 最小测试
- NumPy 向量化：向量/矩阵/批量变换，避免 Python for 硬算几何
- Matplotlib 画 2D 轨迹，图上有轴标签与图例

## 关键内容

机器人算法课的日常语言是 NumPy。坐标、旋转、一批点的变换都应写成数组运算。
没有测试的几何函数后面会在 IK/滤波里炸掉。本章起每个核心函数至少 3 个断言。

## 推荐学习资料

### 必看（掌握本章）

- [NumPy 绝对基础](https://numpy.org/doc/stable/user/absolute_beginners.html) — 广播、matmul、axis
- [Matplotlib 快速入门](https://matplotlib.org/stable/users/explain/quick_start.html) — 能画点与线
- [pytest 官方入门](https://docs.pytest.org/en/stable/getting-started.html) — 一个文件三种断言即可

### 进阶拓展

- Harvard CS50P — 仅当语法不熟时补，不要当本章主课
- [SciPy 空间变换](https://docs.scipy.org/doc/scipy/reference/spatial.transform.html) — 四元数/旋转后用，可与第 6 章对照
- 类型标注与 ruff/mypy — 工程加码，不挡章实验

## 实验清单

- [ ] 实现 2D 点绕原点旋转 θ，Matplotlib 画出轨迹
- [ ] 为该函数补 3 个 pytest 用例

## 笔记

只记自己的推导、踩坑、数字和截图。不要把教材抄进这一节。

## 复盘

- 卡住的地方：
- 下一章开始前必须补上的漏洞：
