import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Float32MultiArray

import cv2
import imutils
import numpy as np


class Callback:
    def __init__(self):
        rospy.init_node("ball_node")
        self.sub = rospy.Subscriber("/webcam_image", Image, self.publisher)
        self.pub = rospy.Publisher("/ball_position", Float32MultiArray, queue_size=1)
        rospy.spin()

    def publisher(self, data):
        try:
            img = np.frombuffer(data.data, dtype=np.uint8).reshape(480, 640, -1)
            img_blur = cv2.GaussianBlur(img, (9, 9), 0)
            img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(img_hsv, (35, 60, 5), (85, 255, 255))
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)

            cv2.imshow("mask", mask)
            cv2.waitKey(1)

            cnts = cv2.findContours(
                mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )
            cnts = imutils.grab_contours(cnts)
            center = None

            if len(cnts) > 0:
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)

                if radius > 10:
                    M = cv2.moments(c)
                    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                    cv2.circle(img, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                    cv2.circle(img, center, 5, (0, 0, 255), -1)

                cv2.imshow("ball_image", img)
                cv2.waitKey(1)

            if center == None:
                ball_pos = Float32MultiArray(data=[-1, -1])
            else:
                ball_pos = Float32MultiArray(data=[center[0] / 640, center[1] / 480])

            self.pub.publish(ball_pos)

        except:
            cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        callback = Callback()
    except rospy.ROSInterruptException:
        print("Error!")