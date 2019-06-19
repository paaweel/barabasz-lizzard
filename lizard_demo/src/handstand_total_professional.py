#!/usr/bin/env python
import rospy
import operator
from std_msgs.msg import Float64MultiArray

def talk():
    pub_fr = rospy.Publisher('/lizard_fr_leg_controller/command', Float64MultiArray, queue_size = 10)
    pub_fl = rospy.Publisher('/lizard_fl_leg_controller/command', Float64MultiArray, queue_size = 10)
    pub_rr = rospy.Publisher('/lizard_rr_leg_controller/command', Float64MultiArray, queue_size = 10)
    pub_rl = rospy.Publisher('/lizard_rl_leg_controller/command', Float64MultiArray, queue_size = 10)
    rospy.init_node('trajectory_ex')
    array = [0, 0, 0]
    rate = rospy.Rate(5)

    state = 0
    while not rospy.is_shutdown():
        #stand up
        if state == 0:
            posDelta = [0.1, 0, 0];
            array = list(map(operator.add, array, posDelta))
            msg = Float64MultiArray(data=array)
            if (array[0] < 1.5):
                print msg
                pub_fl.publish(msg)
                pub_rr.publish(msg)
            else:
                state = 1
                array = [0, 0, 0]
                posDel = [0.05, 0, 0]
                rate = rospy.Rate(65)

        # lower rl leg
        elif state == 1:
            array = list(map(operator.add, array, posDel))
            msg = Float64MultiArray(data=array)
            pub_fr.publish(msg)
            print msg
            if array[0] > 0.8:
                posDel[0] = -0.05
            elif array[0] < 0:
                posDel[0] = 0.05
        rate.sleep()

if __name__ == '__main__':
    try:
        talk()
    except rospy.ROSInterruptException:
        pass
