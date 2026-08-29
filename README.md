# 动手学机器人

从算法到 ROS 2，再到具身智能的 **GitHub 开源书**：笔记在 `docs/`，代码在 `projects/`。用 MkDocs Material 渲染，可发布到 GitHub Pages。

默认按每周约 10 小时、**12 个月核心路径** 设计；方向分流和真机可拉长到 16–18 个月。

## 本地阅读

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

浏览器打开提示的本地地址即可。完整目录、周计划和项目验收写在书里，仓库首页只保留入口。

## 怎么学

1. 读 [前言：如何使用本书](docs/preface/how-to-use.md) 和 [路线总览](docs/preface/roadmap.md)。
2. 按篇填写各章笔记。每章只写关键知识点，细节跟该章「必看 / 进阶」资料；写法见 `docs/preface/conventions.md`。
3. 算法在 [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) 里跑懂，再进 [动手学 ROS 2](https://github.com/fishros/d2l-ros2)。第二篇必须完成 **P03B 集成小车**（定位+规划+跟踪一条龙），不能只交 12 个独立动画。
4. 公开课对照与七个门禁写在书里：`docs/preface/courses.md`、`docs/projects/gates.md`。
5. 第 28 周后在 **导航 / 机械臂 / 具身 VLA** 中只选一条做完 P10。

不要并行维护第二份路线图。外部仓库是教材，本仓库是你的消化产物。

## 结构

```
docs/          书籍正文（MkDocs）
projects/      可运行项目（按 P01–P10）
scripts/       render_chapters.py 生成各章正文
mkdocs.yml     导航与主题
```

## 许可

笔记与文档默认允许你自己学习、修改、公开；引用上游教程时请遵守对应仓库的许可证，不要整本搬运他人文档。
