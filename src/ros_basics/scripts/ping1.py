#!/usr/bin/env python3
import rospy
from random import choice as choose
from std_msgs.msg import String

def random_msg():                                   # subroutine for randomly choosing a message from an array of messages
    messages = ["Ping!", "Pong!", "Bleb!", "Meow!"] # let's make it fun! There are 4 possible messages chosen randomly
    choice = "%s" % (choose(messages))              # randomly chosen message from array "messages"
    return choice                                   # passed as function return value

def ping():
    rospy.init_node('ping_node', anonymous=True)            # "ping_node" node initialization
    pub = rospy.Publisher('ping', String, queue_size=100)   # publisher initialization --> publishing to /ping topic
    rate = rospy.Rate(1)                                    # publishing rate of 1Hz (1 msg/sec)
    while not rospy.is_shutdown():
        ping_str = random_msg()             # ping_str is set to the chosen message from before (by calling the random_msg subroutine)
        rospy.loginfo("Sent %s" % ping_str) # print the message on screen
        pub.publish(ping_str)               # node /ping_node publishes the message on /ping topic
        rate.sleep()

if __name__ == '__main__':
    try:
        ping()
    except rospy.ROSInterruptException:
        pass
