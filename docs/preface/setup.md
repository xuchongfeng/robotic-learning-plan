# 环境与工具链

## 建议配置

- **OS**：Ubuntu 22.04（Humble）或 24.04（Jazzy）。不要用 ROS 1。
- **语言**：Python 3.10+ 为主；C++17 能读能改即可。
- **GPU**：第一至五篇不强制。第六篇 VLA / Isaac Lab 建议 NVIDIA RTX 3060 及以上。
- **仿真**：Webots 或 Gazebo 选一个作为 ROS 阶段主力；MuJoCo 留给具身。

## 推荐安装顺序

1. Git、conda/uv、CMake
2. Python 科学计算栈（NumPy SciPy Matplotlib）
3. clone PythonRobotics 并能跑一个 A* 动画
4. 安装 ROS 2（第 10 周再装也不迟）
5. 第六篇再装 MuJoCo / Isaac 相关栈

## 本书本地预览

```bash
pip install -r requirements-docs.txt
mkdocs serve
```
