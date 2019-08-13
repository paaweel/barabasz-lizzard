#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64


def talk():
    pub_fr1 = rospy.Publisher('/barabasz/front_right_leg_1_position_controller/command', Float64, queue_size = 10)
    pub_fr2 = rospy.Publisher('/barabasz/front_right_leg_2_position_controller/command', Float64, queue_size = 10)
    pub_fr3 = rospy.Publisher('/barabasz/front_right_leg_3_position_controller/command', Float64, queue_size = 10)

    pub_fl1 = rospy.Publisher('/barabasz/front_left_leg_1_position_controller/command', Float64, queue_size = 10)
    pub_fl2 = rospy.Publisher('/barabasz/front_left_leg_2_position_controller/command', Float64, queue_size = 10)
    pub_fl3 = rospy.Publisher('/barabasz/front_left_leg_3_position_controller/command', Float64, queue_size = 10)

    pub_rr1 = rospy.Publisher('/barabasz/rear_right_leg_1_position_controller/command', Float64, queue_size = 10)
    pub_rr2 = rospy.Publisher('/barabasz/rear_right_leg_2_position_controller/command', Float64, queue_size = 10)
    pub_rr3 = rospy.Publisher('/barabasz/rear_right_leg_3_position_controller/command', Float64, queue_size = 10)

    pub_rl1 = rospy.Publisher('/barabasz/rear_left_leg_1_position_controller/command', Float64, queue_size = 10)
    pub_rl2 = rospy.Publisher('/barabasz/rear_left_leg_2_position_controller/command', Float64, queue_size = 10)
    pub_rl3 = rospy.Publisher('/barabasz/rear_left_leg_3_position_controller/command', Float64, queue_size = 10)

    rospy.init_node('trajectory_ex')
    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        msg = Float64(0.0)
        print(msg)
        pub_fl1.publish(msg)
        pub_fl2.publish(msg)
        pub_fl3.publish(msg)

        pub_fr1.publish(msg)
        pub_fr2.publish(msg)
        pub_fr3.publish(msg)

        pub_rr1.publish(msg)
        pub_rr2.publish(msg)
        pub_rr3.publish(msg)

        pub_rl1.publish(msg)
        pub_rl2.publish(msg)
        pub_rl3.publish(msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        talk()
    except rospy.ROSInterruptException:
        pass
