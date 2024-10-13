#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys

robot_x = 0
robot_y = 0

def pose_callback(pose):
    global robot_x, robot_y
    robot_x = pose.x
    robot_y = pose.y
    rospy.loginfo("Robot X = %f\t Robot Y = %f\n",pose.x, pose.y)

def move_turtle(lin_vel,ang_vel,duration):
    global robot_x, robot_y
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose',Pose, pose_callback)
    rate = rospy.Rate(10) # 10hz
    vel = Twist()
    t0 = rospy.Time.now()                                                   # Get starting time of movement
    while not rospy.is_shutdown():
        t1 = rospy.Time.now()                                               # Get actual time of movement
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel

        if (t1.to_sec()-t0.to_sec()) > rospy.Duration(duration).to_sec():   # If time passed since start of movement
            rospy.loginfo("Time is over!")                                  # is greater than target duration, stop
            rospy.logwarn("Stopping robot")
            break
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('move_turtle', anonymous=False)#Has to be called here at the begining!
        v= rospy.get_param("~v")
        w= rospy.get_param("~w")
        t= rospy.get_param("~t")
        move_turtle(v,w,t)
    except rospy.ROSInterruptException:
        pass