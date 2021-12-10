#!/usr/bin/python2

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface() 
group_name = 'manipulator'   
move_group = moveit_commander.MoveGroupCommander("manipulator")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)


joint_goal = move_group.get_current_joint_values()


#zero
joint_goal[0] = 0
joint_goal[1] = 0
joint_goal[2] = 0
joint_goal[3] = 0
joint_goal[4] = 0
joint_goal[5] = 0
move_group.go(joint_goal, wait=True)
move_group.stop()

#up
joint_goal[0] = 0
joint_goal[1] = -pi/2
joint_goal[2] = 0
joint_goal[3] = -pi/2
joint_goal[4] = 0
joint_goal[5] = 0
move_group.go(joint_goal, wait=True)
move_group.stop()

#up right
joint_goal[0] = 0
joint_goal[1] = -pi/2
joint_goal[2] = pi/2
joint_goal[3] = 0
joint_goal[4] = 0
joint_goal[5] = 0
move_group.go(joint_goal, wait=True)
move_group.stop()

#above bowl
joint_goal[0] = -1.780
joint_goal[1] = -pi/2
joint_goal[2] = pi/2
joint_goal[3] = -pi/2
joint_goal[4] = -pi/2
joint_goal[5] = pi/2
move_group.go(joint_goal, wait=True)
move_group.stop()

#down bowl
joint_goal[0] = -1.780
joint_goal[1] = -1.222
joint_goal[2] = 2.147
joint_goal[3] = -2.513
joint_goal[4] = -pi/2
joint_goal[5] = 1.361
move_group.go(joint_goal, wait=True)
move_group.stop()

#above bowl
joint_goal[0] = -1.780
joint_goal[1] = -pi/2
joint_goal[2] = pi/2
joint_goal[3] = -pi/2
joint_goal[4] = -pi/2
joint_goal[5] = pi/2
move_group.go(joint_goal, wait=True)
move_group.stop()

#above position 1
joint_goal[0] = 1.693
joint_goal[1] = -pi/2
joint_goal[2] = pi/2
joint_goal[3] = -pi/2
joint_goal[4] = -pi/2
joint_goal[5] = pi/2
move_group.go(joint_goal, wait=True)
move_group.stop()

#down position 1
joint_goal[0] = 1.693
joint_goal[1] = -1.187
joint_goal[2] = 2.129
joint_goal[3] = -2.129
joint_goal[4] = -pi/2
joint_goal[5] = pi/2
move_group.go(joint_goal, wait=True)
move_group.stop()

#above position 1
joint_goal[0] = 1.693
joint_goal[1] = -pi/2
joint_goal[2] = pi/2
joint_goal[3] = -pi/2
joint_goal[4] = -pi/2
joint_goal[5] = pi/2
move_group.go(joint_goal, wait=True)
move_group.stop()

#above bowl
joint_goal[0] = -1.780
joint_goal[1] = -pi/2
joint_goal[2] = pi/2
joint_goal[3] = -pi/2
joint_goal[4] = -pi/2
joint_goal[5] = pi/2
move_group.go(joint_goal, wait=True)
move_group.stop()

#down bowl
joint_goal[0] = -1.780
joint_goal[1] = -1.222
joint_goal[2] = 2.147
joint_goal[3] = -2.513
joint_goal[4] = -pi/2
joint_goal[5] = 1.361
move_group.go(joint_goal, wait=True)
move_group.stop()

#above bowl
joint_goal[0] = -1.780
joint_goal[1] = -pi/2
joint_goal[2] = pi/2
joint_goal[3] = -pi/2
joint_goal[4] = -pi/2
joint_goal[5] = pi/2
move_group.go(joint_goal, wait=True)
move_group.stop()

#above position 2
joint_goal[0] = 1.292
joint_goal[1] = -pi/2
joint_goal[2] = pi/2
joint_goal[3] = -pi/2
joint_goal[4] = -pi/2
joint_goal[5] = pi/2
move_group.go(joint_goal, wait=True)
move_group.stop()

#down position 2
joint_goal[0] = 1.344
joint_goal[1] = -1.274
joint_goal[2] = 2.077
joint_goal[3] = -2.356
joint_goal[4] = -pi/2
joint_goal[5] = 1.623
move_group.go(joint_goal, wait=True)
move_group.stop()

#above position 2
joint_goal[0] = 1.292
joint_goal[1] = -pi/2
joint_goal[2] = pi/2
joint_goal[3] = -pi/2
joint_goal[4] = -pi/2
joint_goal[5] = pi/2
move_group.go(joint_goal, wait=True)
move_group.stop()





plan1 = move_group.plan()

rospy.sleep(5)

moveit_commander.roscpp_shutdown()

move_group.execute(plan1, wait=True)

