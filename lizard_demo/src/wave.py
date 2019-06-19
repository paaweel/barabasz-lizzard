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
        if state == 0:
            # stand up
            posDelta = [0, 0.1, 0];
            array = list(map(operator.add, array, posDelta))
            msg = Float64MultiArray(data=array)
            if (array[1] < 2.3):
                print msg
                pub_fr.publish(msg)
                pub_fl.publish(msg)
                pub_rr.publish(msg)
            else:
                state = 1
        # lower rl leg
        elif state == 1:
            posDelta = [0, -0.1, 0];
            array = list(map(operator.add, array, posDelta))
            if (array[1] < 1.5):
                pub_rl.publish(msg)
            else:
                state = 2
        # rise fr leg
        elif state == 2:
            posDelta = [0, -0.1, 0];
            array = list(map(operator.add, array, posDelta))
            if (array[1] < 3.5):
                pub_fr.publish(msg)
            else:
                state = 3
        # wave leg
        elif state == 3:
            posDelta = [0, 0, 0.1];
            array = list(map(operator.add, array, posDelta))
            pub_fr.publish(msg)
            if (abs(array[2]) > 0.45):
                posDelta[2] = posDelta[2] *(-1)

        rate.sleep()

if __name__ == '__main__':
    try:
        talk()
    except rospy.ROSInterruptException:
        pass
