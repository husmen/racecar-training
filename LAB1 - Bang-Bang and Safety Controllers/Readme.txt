These projects are the ros project. First we go to the catkin_ws / src directory 
and create a new ros package there.

cd catkin_ws
source devel/setup.bash
cd src
catkin_create_pkg Bang_Bang std_msgs rospy roscpp

cd Bang_Bang/src
Here we open the python file. We paste it into the code

Open new Terminal
roscore

Run in catkin_ws directory
rosrun Bang_Bang codeFolderOfName.py
