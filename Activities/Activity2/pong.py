#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

pong_str = "Pong!"
fail_str = "Failed!"

def callback(data):
    # ping_id = rospy.get_caller_id()
    if (data.data != "Ping!"):          # If we receive a random message
        rospy.loginfo("%s" % fail_str)  # send "Failed!"
    else                                # Else
        rospy.loginfo("%s" % pong_str)  # send "Pong!"

def pong():
    rospy.init_node('pong_node', anonymous=True)
    pub = rospy.Publisher('pong', String, queue_size=10)
    sub = rospy.Subscriber("ping", String, callback)
    rospy.spin()

if __name__ == '__main__':
    pong()
