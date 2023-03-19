# My Image Processing Package

This ROS package performs edge detection on an image stream from a camera and publishes the resulting image on the `/canny_image` topic.

## Requirements

- ROS (tested on ROS Melodic)
- USB camera
- `usb_cam` package

## Installation

1. Clone this repository into your workspace:

    ```
    cd ~/catkin_ws/src
    git clone https://github.com/<your-username>/my_image_processing.git
    ```

2. Build the package:

    ```
    cd ~/catkin_ws
    catkin_make
    ```

## Usage

1. Run `roscore`:

    ```
    roscore
    ```

2. Launch the USB camera node:

    ```
    roslaunch usb_cam usb_cam-test.launch
    ```

3. Run the image processing node:

    ```
    rosrun my_image_processing main_node.py
    ```
