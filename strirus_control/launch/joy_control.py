import rospy
from geometry_msgs.msg import *
from sensor_msgs.msg import *
from std_msgs.msg import *


# Receives joystick messages (subscribed to Joy topic)
# then converts the joystick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizontal controls angular speed

def init():
    joints_arr_l = []
    joints_arr_r = []
    for i in range(6):
        str_l = "/strirus_legged_robot/joint{0}_position_controller_l/command".format(i)
        str_r = "/strirus_legged_robot/joint{0}_position_controller_r/command".format(i)
        joints_arr_l.append(str_l)
        joints_arr_r.append(str_r)
        # print(joints_arr_l)
    return joints_arr_l, joints_arr_r


def start_conf(joints_arr_l, joints_arr_r):
    start_pos = 0.0
    for i in range(len(joints_arr_l)):
        rospy.Publisher(joints_arr_l[i], Float64, queue_size=10).publish(start_pos)
        rospy.Publisher(joints_arr_r[i], Float64, queue_size=10).publish(start_pos)


def configuration_1(joints_arr_l, joints_arr_r):
    phase_1 = 0.0
    phase_2 = 1.22
    for i in range(len(joints_arr_l)):
        if i % 2 != 0:
            rospy.Publisher(joints_arr_l[i], Float64, queue_size=10).publish(phase_1)
            rospy.Publisher(joints_arr_r[i], Float64, queue_size=10).publish(phase_1)
        else:
            rospy.Publisher(joints_arr_r[i], Float64, queue_size=10).publish(phase_2)
            rospy.Publisher(joints_arr_l[i], Float64, queue_size=10).publish(phase_2)


def callback(data):
    config_1 = data.buttons[0]
    config_2 = data.buttons[1]
    config_3 = data.buttons[2]
    config_4 = data.buttons[3]
    l, r = init()
    if config_1 == 1:
        position = 0.0
        print("Using start configuration")
        # put all legs to configuration 1
        start_conf(l, r)
    if config_2 == 1:
        print("Using configuration #1")
        configuration_1(l, r)
    for i in range(len(l)):
        rospy.Publisher(l[i], Float64, queue_size=10).publish(data.axes[0] * 3.14)
        rospy.Publisher(r[i], Float64, queue_size=10).publish(data.axes[0] * 3.14)


# Initializes everything
def start():
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('Joy2StriRus')
    rospy.spin()


if __name__ == '__main__':
    start()
