#!/usr/bin/env python
import rospy
import operator
from std_msgs.msg import Float64MultiArray

def talk():
    pub = rospy.Publisher('/lizard_fr_leg_controller/command', Float64MultiArray, queue_size = 10)
    rospy.init_node('trajectory_ex')
    array = [0, 0, 0]
    rate = rospy.Rate(50)
    posDel = [0.05, 0, 0]
    while not rospy.is_shutdown():
        array = list(map(operator.add, array, posDel))
        msg = Float64MultiArray(data=array)
        print msg
        if array[0] > 0.8:
            posDel[0] = -0.2
        elif array[0] < 0:
            posDel[0] = 0.2
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talk()
    except rospy.ROSInterruptException:
        pass
