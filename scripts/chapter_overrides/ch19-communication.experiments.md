每条先写清要回答的问题。在 Ubuntu 里做；每个终端先 source 系统 ROS，再用到自己的包时 overlay 工作空间。相机和 YOLO **本周用假数据**；真相机放到第四篇。建议继续用第 18 章的工作空间，或在 `~/ros2_ws/src` 新建 `demo_comm`。

- [ ] **实验 A：只设计、不写代码（摄像头场景）**
    - **要回答的问题**：图像、检测结果、播报、阈值分别该走话题、服务、Action 还是参数？节点怎么拆，才不会焊成一个进程？
    - **步骤**：在笔记「实验记录」里画出节点图（可手绘拍照），填一张表：节点名、发布/订阅的话题、提供/调用的服务、参数。对照本章笔记里的四节点拆法，写下你若合并某两个节点会坏在哪。
    - **通过线**：图上至少 3 个节点；图像是话题；播报不是每帧一条话题；有一个节点专门做「何时说」，而不是让 detector 直接发音。没有代码也可以勾。

- [ ] **实验 B：服务是一次一答（先用现成服务看清形态）**
    - **要回答的问题**：服务端和客户端谁先存在？请求和响应各长什么样？它和 `ros2 topic echo` 有什么不同？
    - **步骤**（三个终端均已 source）：
        1. `ros2 run turtlesim turtlesim_node`
        2. `ros2 service list`，找到 `/spawn`、`/clear`、`/turtle1/set_pen` 一类名字。
        3. `ros2 service type /clear`，再 `ros2 interface show` 该类型（例如 `std_srvs/srv/Empty`）。
        4. `ros2 service call /clear std_srvs/srv/Empty`，看海龟轨迹是否被清掉。
        5. `ros2 service call /spawn turtlesim/srv/Spawn "{x: 2.0, y: 3.0, theta: 0.0, name: 'leo'}"`，再 `ros2 node list` / `ros2 topic list` 看是否多了一只龟的话题。
    - **通过线**：能口述：调用的是 **服务名**，不是节点名；应答回来之前这次调用没结束；`/turtle1/pose` 仍是话题在连续刷，和 `/clear` 不是一类东西。把一次 `service list` 和一次 `call` 的输出贴进笔记。

- [ ] **实验 C：自己写一个 `/speak` 服务（假 TTS）**
    - **要回答的问题**：节点如何 **提供** 服务、另一个节点如何 **调用**？两个服务会不会自动互调？
    - **步骤**：
        1. 需要「一句话」时，跟 [Creating custom srv](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.html) 做 `Speak.srv`（Request: `string text`，Response: `bool ok`）。练手也可用 `example_interfaces`。
        2. `tts_node`：`create_service`，回调里 `get_logger().info('speaking: ...')`，再填 `ok=True`（本周不接真实喇叭也行）。
        3. 命令行当客户端：`ros2 service call /speak <你的类型> "{text: 'cup'}"`，日志里出现 `cup`。
        4. 再写 `announcer`：`create_client`，等到 `service_is_ready`，再 `call_async`。确认 tts **没有** `import` announcer，announcer **没有** 直接调 tts 的类。
    - **通过线**：只启动 tts 时，`ros2 service list` 有 `/speak`；再 `service call` 或启动 announcer 能看到日志。笔记写一句：服务端不主动找客户端，是客户端找服务名。

- [ ] **实验 D：话题流 + 服务事件（假识别不要每帧都说）**
    - **要回答的问题**：连续检测结果为什么用话题？怎样避免 10 Hz 的「杯子」被念十遍？
    - **步骤**：
        1. `detector_node` 用定时器（例如 2 Hz）发布 `std_msgs/String` 到 `/detections`，内容在连续多帧 `cup` 和偶尔一次 `book` 之间切换。
        2. `announcer` 订阅 `/detections`：仅当标签 **相对上次已播报发生变化** 时，才调用 `/speak`。
        3. 三个节点一起跑（可先三个终端 `ros2 run`）。
        4. `ros2 topic echo /detections` 应很密；tts 日志应明显更稀，连续 `cup` 只播报一次。
    - **通过线**：能讲清 announcer 把「流」变成「事件」。`rqt_graph` 截图：detector → `/detections` → announcer，announcer 与 tts 之间是服务不是话题。

- [ ] **实验 E：参数改行为，不改代码**
    - **要回答的问题**：配置和数据通道有什么区别？
    - **步骤**：给 `announcer` 声明参数 `min_repeat_s`（默认 2.0），或给假 detector 声明当前 `label`。运行中 `ros2 param get <节点> <名>`，再 `ros2 param set ...` 看行为变化。
    - **通过线**：不重新编译，只 set 参数就能改变行为。笔记记下参数属于哪个节点。

- [ ] **实验 F（P04 本章部分）：同一包里四种原语都出现 + launch**
    - **要回答的问题**：四种原语能否在一个 launch 里同时被看到，而不是四个互不相关的 demo？
    - **步骤**：在 `demo_comm` 或 `projects/p04_ros2_ws` 里让假场景具备：话题 `/detections`、服务 `/speak`、至少一个参数、一个最小 Action（官方 [Writing an action server and client (Python)](https://docs.ros.org/en/humble/Tutorials/Intermediate/Writing-an-Action-Server-Client/Py.html)，Goal 可用「播报秒数」冒充长任务）。`ros2 launch ...` 一键起。TF / URDF 遥控车是第 20 章和 P04 门禁后半，**不必本实验做完**。
    - **通过线**：`ros2 topic list`、`ros2 service list`、`ros2 action list`、`ros2 param dump <某节点>` 各能指到场景里的一个名字。README 写出发行版和 launch 命令。
