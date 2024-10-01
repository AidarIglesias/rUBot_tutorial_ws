#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

pong_str = "Pong!"      # string vars definition for matching
fail_str = "Failed!"    # and non-matching messages

def callback(data):
    global pong_str, fail_str
    rospy.loginfo("%s", data.data)          # print received message on screen
    if (("%s" % data.data) == "Ping!"):     # if non-matching message is received
        rospy.loginfo("%s" % pong_str)      # send "Failed!"
    else:                                   # else, if matching message (i.e. "Ping!") is received
        rospy.loginfo("%s" % fail_str)      # send "Pong!"

def pong():
    rospy.init_node('pong_node', anonymous=True)            # "pong_node" initialization
    pub = rospy.Publisher('pong', String, queue_size=100)   # publisher initialization --> publishing to /pong topic
    sub = rospy.Subscriber("ping", String, callback)        # subscriber initialization --> subscribed to /ping topic
    rospy.spin()

if __name__ == '__main__':
    pong()
