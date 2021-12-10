# Capstone-project
movement algorithms for a UR5 robot

motion_planning_test.py is a python script designed to test movement on a UR5 robot from industrial robots.
This file was designed to be used for ROS Melodic.

this file should be added alone in the catkin workspace folder that the universal robot package was downloaded to.





to run the motion_planning_test.py script, follow the directions from universal robot simulation for launching the UR5 robot in gazebo, moveit, and rviz. In a seperate terminal, use the command,

python2 motion_planning_test.py

Once the command is typed or coppied into the terminal, press enter and the robot should run through the motion path and execute a simulation of picking and placing.

The code was designed to simulate a bowl in the location of (0,-0.5)

the robot will move down to the "bowl" location, then move to position 1 (-0.5,0.5) to "place" a simulated object.
The robot will then move back to the bowl location to "pick".
After the robot has picked the second time from the bowl, it will move to the final location, position 2 (0,0.5), to place once again.
