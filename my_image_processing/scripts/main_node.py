import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
global bridge
bridge = CvBridge()
def image_callback(ros_image):
    print("got an image from camera")
    cv_image = bridge.imgmsg_to_cv2(ros_image, 'bgr8')
    edge_image = cv2.Canny(cv_image, 100, 150)
    ros_image = bridge.cv2_to_imgmsg(edge_image)
    image_pub.publish(ros_image)
    cv2.imshow("image_window",edge_image)
    cv2.waitKey(3) # Notice that if it takes zero as an arguement then it will wait a key press before showing next image
                    # if it takes a number more than 3 as an arguement then it will work as a delay in milliseconds 
    return
def main():
    rospy.init_node("image_convertor", anonymous=True)
    image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)
    global image_pub
    image_pub = rospy.Publisher("/canny_image", Image, queue_size=10)
    rospy.spin()
if __name__ == "__main__":
    main()
