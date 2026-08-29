每条都先写清「要回答什么问题」，再给步骤和通过线。在 **Ubuntu 22.04（Humble）或 24.04（Jazzy）** 里做；macOS 宿主不要硬装 Desktop，用虚拟机或 Docker 进 Linux 再跑。每个新终端都要先 `source /opt/ros/$ROS_DISTRO/setup.bash`（工作空间编过之后再 overlay 一次 `install/setup.bash`）。

- [ ] **实验 A：环境自检**
    - **要回答的问题**：当前这台机器能不能跑 ROS 2？发行版是 Humble 还是 Jazzy？shell 有没有 source？
    - **步骤**：
        1. `echo $ROS_DISTRO`。若为空，先按 [官方安装](https://docs.ros.org/en/humble/Installation.html)（Jazzy 把 URL 里的 `humble` 换成 `jazzy`）装完，再 `source /opt/ros/<发行版>/setup.bash`，并考虑写进 `~/.bashrc`。
        2. `ros2 --help` 能列出子命令。
        3. `printenv | grep -E 'ROS_DISTRO|ROS_VERSION|RMW_IMPLEMENTATION'` 记进笔记。
    - **通过线**：`ROS_DISTRO` 为 `humble` 或 `jazzy`；`ROS_VERSION=2`。把发行版写进本仓库 `projects/p04_ros2_ws/README.md`（没有就新建一句）。

- [ ] **实验 B：turtlesim —— 不写代码先看计算图**
    - **要回答的问题**：节点和话题在运行时长什么样？谁在发速度指令、谁在听？
    - **步骤**（三个终端，都已 source 系统 ROS）：
        1. 若尚未安装：`sudo apt install ros-$ROS_DISTRO-turtlesim`
        2. 终端 1：`ros2 run turtlesim turtlesim_node`
        3. 终端 2：`ros2 run turtlesim turtle_teleop_key`，点一下该终端，用方向键让乌龟动。
        4. 终端 3 依次执行并保存输出：
            - `ros2 node list`
            - `ros2 topic list`
            - `ros2 topic info /turtle1/cmd_vel -v`
            - `ros2 topic echo /turtle1/cmd_vel --once`
            - `ros2 interface show geometry_msgs/msg/Twist`
            - `ros2 topic hz /turtle1/pose`（看几秒后 Ctrl+C）
    - **通过线**：能用自己的话讲清：teleop 往 `/turtle1/cmd_vel` 发 `Twist`，turtlesim 订阅后改海龟位姿，又往 `/turtle1/pose` 发布。把 `node list` 和 `topic list` 贴进笔记。

- [ ] **实验 C：colcon 工作空间与 overlay**
    - **要回答的问题**：自己的代码放哪、怎么编、另一个终端怎样才能 `ros2 run` 到它？
    - **步骤**（路径可改成你 Ubuntu 上 clone 的本书目录）：
        ```bash
        source /opt/ros/$ROS_DISTRO/setup.bash
        mkdir -p ~/ros2_ws/src
        cd ~/ros2_ws/src
        ros2 pkg create --build-type ament_python --license Apache-2.0 \
          --dependencies rclpy std_msgs demo_chatter
        cd ~/ros2_ws
        colcon build --packages-select demo_chatter
        source install/setup.bash
        ros2 pkg list | grep demo_chatter
        echo $AMENT_PREFIX_PATH
        ```
        观察：`AMENT_PREFIX_PATH` 应同时包含你的 `~/ros2_ws/install/...` 和 `/opt/ros/$ROS_DISTRO`。**新开的终端**如果只 source 了系统、没 source 工作空间，`ros2 pkg list` 里就没有 `demo_chatter`。
    - **通过线**：`colcon build` 成功；source 工作空间后能列出该包。笔记里写清「漏 source 时的现象」和你实际用的工作空间路径。若希望代码进本书仓库，把 `src/demo_chatter` 放到 `projects/p04_ros2_ws/src/` 再编一次。

- [ ] **实验 D：写一个发布节点（固定频率往外扔数据）**
    - **要回答的问题**：节点如何按定时器发布？启动后在图上叫什么名字？话题类型和名字是什么？
    - **步骤**：在 `demo_chatter` 包里放发布者（包名以你 `pkg create` 的为准）。最小逻辑如下，接到包的入口（`setup.py` 的 `console_scripts` 或 `ros2 run demo_chatter talker`）上：
        ```python
        import rclpy
        from rclpy.node import Node
        from std_msgs.msg import String

        class Talker(Node):
            def __init__(self):
                super().__init__('talker')
                self.pub = self.create_publisher(String, 'chatter', 10)
                self.timer = self.create_timer(0.5, self.tick)
                self.i = 0

            def tick(self):
                msg = String()
                msg.data = f'hello {self.i}'
                self.pub.publish(msg)
                self.get_logger().info(msg.data)
                self.i += 1

        def main():
            rclpy.init()
            node = Talker()
            rclpy.spin(node)
            node.destroy_node()
            rclpy.shutdown()
        ```
        改完后 `colcon build --packages-select demo_chatter`，source，再 `ros2 run demo_chatter talker`（入口名以 `setup.py` 为准）。另开终端：`ros2 topic echo /chatter`、`ros2 topic hz /chatter`。
    - **通过线**：echo 持续出现 `hello N`；hz 大约 2 Hz（定时器 0.5 s）。笔记记下节点名、话题名、消息类型、实测频率。对照：[Writing a simple publisher and subscriber (Python)](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)。

- [ ] **实验 E：订阅者 + 计算图（两个节点只靠话题耦合）**
    - **要回答的问题**：订阅者如何在完全不 `import` 发布者代码的情况下收到数据？关掉发布者之后图上会发生什么？
    - **步骤**：
        1. 按同一官方教程补一个 `listener` 节点，订阅 `/chatter`，`get_logger().info` 打印 `msg.data`。
        2. 两个终端分别 `ros2 run` talker 与 listener（都 overlay 了工作空间）。
        3. 第三个终端：`ros2 node list`、`rqt_graph`（需 `sudo apt install ros-$ROS_DISTRO-rqt-graph`；若命令是 `ros2 run rqt_graph rqt_graph` 也可以）。
        4. 停掉 talker，观察 listener 是否还刷新消息；再看 `rqt_graph`。
    - **通过线**：listener 日志与 talker 的 `hello N` 对应；`rqt_graph` 截图进笔记，能指出 `/chatter` 连着两个节点。口头讲清：耦合点是话题，不是 Python 模块。
    - **本章到此即可。** 服务、参数、Action、launch 一键起多节点是 [第 19 章](ch19-communication.md) 和 [P04](../projects/p04-ros2-ws.md)，不要本周一次做完。
