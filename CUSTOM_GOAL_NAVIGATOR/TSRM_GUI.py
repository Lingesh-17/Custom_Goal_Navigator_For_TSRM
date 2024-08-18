#!/usr/bin/env python3

import rospy
from actionlib import SimpleActionClient
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import sys
from PyQt5 import QtWidgets, uic
from playsound import playsound

class mainwindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mainwindow, self).__init__()

        uic.loadUi('Project_TSRM.ui', self)

        self.button1 = self.findChild(QtWidgets.QPushButton, 'bed1')
        self.button2 = self.findChild(QtWidgets.QPushButton, 'bed2')
        self.button3 = self.findChild(QtWidgets.QPushButton, 'bed3')
        self.button4 = self.findChild(QtWidgets.QPushButton, 'bed4')
        self.button5 = self.findChild(QtWidgets.QPushButton, 'bed5')
        self.button6 = self.findChild(QtWidgets.QPushButton, 'bed6')
        self.button7 = self.findChild(QtWidgets.QPushButton, 'home')
        self.button8 = self.findChild(QtWidgets.QPushButton, 'exit')

        self.button1.clicked.connect(self.bed_1)
        self.button2.clicked.connect(self.bed_2)
        self.button3.clicked.connect(self.bed_3)
        self.button4.clicked.connect(self.bed_4)
        self.button5.clicked.connect(self.bed_5)
        self.button6.clicked.connect(self.bed_6)
        self.button7.clicked.connect(self.home_button)
        self.button8.clicked.connect(self.quit_button)

        self.show()

    def bed_1(self):
        playsound('Assets/click.mp3')
        print("Navigating to BED 1")
        # Coordinates for the atelier location (you should update these to correct values)
        self.send_goal(3.4022674560546875, 4.023774147033691, -0.005853934771965811, 0.9999828655770485)

    def bed_2(self):
        playsound('Assets/click.mp3')
        print("Navigating to BED 2")
        # Coordinates for the media room location (you should update these to correct values)
        self.send_goal(2.8987998962402344, 0.577580451965332, -0.016931169953691858, 0.999856657468459)

    def bed_3(self):
        playsound('Assets/click.mp3')
        print("Navigating to BED 3")
        # Coordinates for the media room location (you should update these to correct values)
        self.send_goal(2.8800525665283203, -3.5761475563049316, 0.005956599654118902, 0.9999822593029141)

    def bed_4(self):
        playsound('Assets/click.mp3')
        print("Navigating to BED 4")
        # Coordinates for the media room location (you should update these to correct values)
        self.send_goal(-3.110417366027832, -3.3706536293029785, -0.9999332069209477, 0.011557754833409558)

    def bed_5(self):
        playsound('Assets/click.mp3')
        print("Navigating to BED 5")
        # Coordinates for the media room location (you should update these to correct values)
        self.send_goal(-3.0265016555786133, 0.3101615905761719, 0.9999223624633142, 0.012460700051942181)

    def bed_6(self):
        playsound('Assets/click.mp3')
        print("Navigating to BED 6")
        # Coordinates for the media room location (you should update these to correct values)
        self.send_goal(-3.322490692138672, 4.266844749450684, 0.9997837954228309, 0.020793326090814874)

    def home_button(self):
        playsound('Assets/click.mp3')
        print("Returning Home Position")
        # Coordinates for the media room location (you should update these to correct values)
        self.send_goal(-0.045203208923339844, -8.748315811157227, 0.7632381113254401, 0.6461173155243367)

    def quit_button(self):
        exit()               


    def send_goal(self, x, y, z, w):
        client = SimpleActionClient('move_base', MoveBaseAction)
        client.wait_for_server()

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        goal.target_pose.pose.orientation.z = z
        goal.target_pose.pose.orientation.w = w

        client.send_goal(goal)
        


def dis_ui():
    rospy.init_node('gui_goal_publisher')  # Initialize ROS node here
    app = QtWidgets.QApplication(sys.argv)
    ui = mainwindow()
    app.exec_()


if __name__ == "__main__":
    dis_ui()
