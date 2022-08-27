from time import sleep, perf_counter

import rospy
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

import cv2


def publisher():
    rospy.init_node("webcam_node")
    pub = rospy.Publisher("/webcam_image", Image, queue_size=1)
    bridge = CvBridge()

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc("M", "J", "P", "G"))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)

    try:
        while not rospy.is_shutdown():
            t0 = perf_counter()
            ret, img = cap.read()
            if ret:
                cv2.imshow("webcam_image", img)
                cv2.waitKey(1)
                webcam_img = bridge.cv2_to_imgmsg(img)

            while True:
                diff = t0 + 1 / 30 - perf_counter()
                if diff <= 0:
                    break
                else:
                    sleep(diff / 2)

            pub.publish(webcam_img)

    except:
        pass

    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        print("Error!")