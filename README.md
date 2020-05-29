[**Superpoject github link**](https://github.com/Lupasic/strirus_full)

# Robot "StriRus" Gazebo representation

# Control StriRus robot via gamepad:

**Configure gamepad**:
- ```$ roscore```
- ```$ rosparam set joy_node/dev "/dev/input/js#"``` # Set node for gamepad, check input driver fx#
- ```$ rosrun joy joy_node```

**Configure Robot**:
- ```name_ws:$ source devel/setup.bash```
- ```$ roslaunch strirus_gazebo strirus_gazebo.launch``` # Simulate world and some parameters
- ```$ roslaunch strirus_control strirus_control.launch``` # Main start point, run plagins, spawn robot model, spawn joints_states

**Run Python script for gamepad control**:
- ```$ python joy_control.py``` 

## Needed packages
- [Joy2ROS package](http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick)
- [ROS control package](http://wiki.ros.org/ros_control)
## Launch files

- ```strirus_gazebo.launch```
- ```strirus_control.launch```
- ```strirus_rviz.launch```

[**Superpoject github link**](https://github.com/Lupasic/strirus_full)

