# Study Moveit2

## panda 机械臂

```shell
ros2 launch moveit2_tutorials demo.launch.py
# 或者: ros2 launch moveit2_tutorials demo.launch.py rviz_config:=panda_moveit_config_demo_empty.rviz
ros2 run pymoveit2 ex_joint_goal.py --ros-args -p joint_positions:="[1.57, -1.57, 0.0, -1.57, 0.0, 1.57, 0.7854]"
```
