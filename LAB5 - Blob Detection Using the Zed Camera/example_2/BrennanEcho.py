#!/usr/bin/env python
import cv2
import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import imutils

class Echo:
    def __init__(self):
        self.node_name = "Echo"
        self.sub_image = rospy.Subscriber("/camera/rgb/image_rect_color",Image, self.cbImage, queue_size=1)
        self.pub_image = rospy.Publisher("~echo_image",Image, queue_size=1)
        self.bridge = CvBridge()

        rospy.loginfo("[%s] Initialized." %(self.node_name))

    def cbImage(self,img):
        im = self.bridge.imgmsg_to_cv2(img)

        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

        r1 = np.array([0, 220, 200])

        r2 = np.array([15, 255, 230])
        mask = cv2.inRange(hsv, r1, r2)

        mask = cv2.GaussianBlur(mask, (21,21), 0)
        mask = cv2.erode(mask, (5, 5), iterations=5)
        contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours)>0:
            lgContour = contours[0]
            lgArea=cv2.contourArea(lgContour)

            for j in range(0, len(contours)):
                if cv2.contourArea(contours[j])>lgArea:
                    lgContour = coutours[j]
                    lgArea=cv2.contourArea(coutours[j])

            M = cv2.moments(lgContour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # draw the contour and center of the shape on the image
            cv2.drawContours(im, [lgContour], -1, (0, 255, 0), 2)
            cv2.circle(im, (cX, cY), 4, (255, 255, 255), -1)

        self.pub_image.publish(self.bridge.cv2_to_imgmsg(im, "bgr8"))


if __name__=="__main__":
    rospy.init_node('Echo')
    e = Echo()
    rospy.spin()
