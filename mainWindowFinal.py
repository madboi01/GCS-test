# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main-windowFinal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor, QDoubleValidator
from PyQt5.QtWidgets import QMessageBox
from dronekit import VehicleMode
from PyQt5.QtCore import *

from Widgets.add_waypoint import Ui_Dialog
from auto_mission import new_mission, returntolaunch, vehicle



class MyThread(QThread):

    change_value=pyqtSignal(float)
    change_gspeed=pyqtSignal(float)
    change_vspeed=pyqtSignal(float)
    change_mode=pyqtSignal(str)

    def run(self):
        print("Arming drone")

        while not vehicle.is_armable:
            time.sleep(1)

        vehicle.mode = VehicleMode("GUIDED")
        vehicle.armed = True

        while not vehicle.armed:
            time.sleep(1)

        print("Takeoff")
        vehicle.simple_takeoff(ui.talt)

        while True:
            altitude = vehicle.location.global_relative_frame.alt
            print(altitude)

            if altitude >= ui.talt - 0.05:
                print("Altitude reached")
                break

            time.sleep(0.3)
            self.change_value.emit(altitude)
            self.change_gspeed.emit(vehicle.groundspeed)
            self.change_vspeed.emit(-1*vehicle.velocity[2])
            self.change_mode.emit(vehicle.mode.name)

        self.change_value.emit(vehicle.location.global_relative_frame.alt)
        vehicle.mode = VehicleMode("AUTO")
        time.sleep(3)
        self.change_mode.emit(vehicle.mode.name)
        print(vehicle.mode.name)
        while vehicle.mode.name=="AUTO":
            time.sleep(0.3)
            print(vehicle.location.global_relative_frame.alt)
            self.change_value.emit(vehicle.location.global_relative_frame.alt)
            self.change_gspeed.emit(vehicle.groundspeed)
            self.change_vspeed.emit(-1*vehicle.velocity[2])

            #distance_home()
            #vehicle.velocity[2]
            if (vehicle.location.global_relative_frame.alt)<=0.005:
                break

        vehicle.mode.name="STABILIZE"
        time.sleep(3)
        self.change_mode.emit(vehicle.mode.name)




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 485)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setItalic(False)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setStyleSheet("QFrame{\n"
"background-color:rgb(52,52,52);\n"
"border-radius:5px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.connect = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connect.sizePolicy().hasHeightForWidth())
        self.connect.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.connect.setFont(font)
        self.connect.setStyleSheet("QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}\n""QPushButton:hover { background-color:rgb(223, 223, 223); }\n")
        self.connect.setObjectName("pushButton")
        self.connect.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout.addWidget(self.connect)
        self.closeConn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeConn.sizePolicy().hasHeightForWidth())
        self.closeConn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.closeConn.setFont(font)
        self.closeConn.setStyleSheet("QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}\n""QPushButton:hover { background-color:rgb(223, 223, 223); }")
        self.closeConn.setObjectName("pushButton_2")
        self.closeConn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.closeConn.clicked.connect(self.closeconn)
        self.horizontalLayout.addWidget(self.closeConn)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.takeoff = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.takeoff.sizePolicy().hasHeightForWidth())
        self.takeoff.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.takeoff.setFont(font)
        self.takeoff.setStyleSheet("QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}\n""QPushButton:hover { background-color:rgb(223, 223, 223); }")
        self.takeoff.setObjectName("pushButton_7")
        self.takeoff.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.takeoff.clicked.connect(self.armTakeoff)
        self.verticalLayout_3.addWidget(self.takeoff)
        self.verticalLayout_4.addWidget(self.frame)
        self.horizontalLayout_4.addWidget(self.groupBox)

        #PLANNER
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setItalic(False)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color:rgb(52,52,52);\n"
"border-radius:5px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.newMission = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newMission.sizePolicy().hasHeightForWidth())
        self.newMission.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.newMission.setFont(font)
        self.newMission.setStyleSheet("QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}\n""QPushButton:hover { background-color:rgb(223, 223, 223); }")
        self.newMission.setObjectName("pushButton_4")
        self.newMission.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.newMission.clicked.connect(self.newmission)
        self.verticalLayout.addWidget(self.newMission)
        self.addWaypoint = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addWaypoint.sizePolicy().hasHeightForWidth())
        self.addWaypoint.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addWaypoint.setFont(font)
        self.addWaypoint.setStyleSheet("QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}\n""QPushButton:hover { background-color:rgb(223, 223, 223); }")
        self.addWaypoint.setObjectName("pushButton_5")
        self.addWaypoint.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.addWaypoint.clicked.connect(self.addwaypoint)
        self.addWaypoint.setEnabled(False)
        self.verticalLayout.addWidget(self.addWaypoint)
        self.rtl = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rtl.sizePolicy().hasHeightForWidth())
        self.rtl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rtl.setFont(font)
        self.rtl.setStyleSheet("QPushButton{\n"
"background-color:rgb(255,255,255);\n"
"border-radius:5px;\n"
"}\n""QPushButton:hover { background-color:rgb(223, 223, 223); }")
        self.rtl.setObjectName("pushButton_6")
        self.rtl.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.rtl.clicked.connect(self.addrtl)
        self.rtl.setEnabled(False)
        self.verticalLayout.addWidget(self.rtl)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_4.addWidget(self.groupBox_2)

        #INSTRUMENT PANEL
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("QFrame{\n"
"background-color:rgb(52, 52, 52);\n"
"border-radius:10px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"}")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"}")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_9.addWidget(self.label_14)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"}")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"}")
        self.label_15.setText("")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_11.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_11.addWidget(self.label_16)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"}")
        self.label_17.setText("")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_12.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"}")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_12.addWidget(self.label_18)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.verticalLayout_13.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5=QtWidgets.QHBoxLayout()
        self.label_19=QtWidgets.QLabel()
        self.label_19.setText("Enter Takeoff Altitude(Rel.): ")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_5.addWidget(self.label_19)
        self.lineedit=QtWidgets.QLineEdit()
        self.lineedit.setObjectName("lineedit")
        self.taltvalidator = QDoubleValidator(0.0, 1000.0, 8)
        self.lineedit.setValidator(self.taltvalidator)
        self.horizontalLayout_5.addWidget(self.lineedit)
        self.altSave=QtWidgets.QPushButton()
        self.altSave.setText("Save")
        self.altSave.setObjectName("altSave")
        self.altSave.clicked.connect(self.saveAltitude)
        self.horizontalLayout_5.addWidget(self.altSave)
        self.verticalLayout_13.addLayout(self.horizontalLayout_5)

        self.talt=0.0
        #TABLE WIDGET
        self.row=0
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.setColumnWidth(0,300)
        self.tableWidget.setColumnWidth(1,120)
        self.tableWidget.setColumnWidth(2,120)
        self.tableWidget.setColumnWidth(3,105)
        self.tableWidget.setColumnWidth(4,90)
        self.tableWidget.setColumnWidth(5,80)
        self.verticalLayout_13.addWidget(self.tableWidget)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def saveAltitude(self):
        if self.taltvalidator.validate(self.lineedit.text(), 0)[0]==2:
            alt=self.lineedit.text()
            self.talt=float(alt)
            self.lineedit.setText("")
            self.takeoff.setDisabled(False)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Invalid takeoff altitude")
            msg.setWindowTitle("INVALID")
            msg.exec_()



    def closeconn(self):
            sys.exit()


    def newmission(self):
        new_mission()
        self.addWaypoint.setDisabled(False)
        self.rtl.setDisabled(False)
        self.takeoff.setEnabled(False)

    def addrtl(self):
            returntolaunch()

    def addwaypoint(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        resp=self.Dialog.exec_()
        if resp== QtWidgets.QDialog.Accepted:
            if (self.ui.latvalidator.validate(self.ui.lineEdit.text(), 0)[0]==2 and self.ui.longvalidator.validate(self.ui.lineEdit_2.text(), 0)[0]==2 and self.ui.altvalidator.validate(self.ui.lineEdit_3.text(), 0)[0]==2):
                self.newwaypoint()
            else:
                self.addwaypoint()


    def newwaypoint(self):
        state, lat, pos = self.ui.latvalidator.validate(self.ui.lineEdit.text(), 0)
        self.lati = float(lat)
        state, long, pos = self.ui.longvalidator.validate(self.ui.lineEdit_2.text(), 0)
        self.longi = float(long)
        state, alt, pos = self.ui.altvalidator.validate(self.ui.lineEdit_3.text(), 0)
        self.alti = float(alt)
        print(lat + " " + long + " " + alt)
        print(type(self.lati))
        print(type(self.longi))
        print(type(self.alti))
        self.addnewrow("WAYPOINT",lat,long,alt,"RELATIVE")

    def addnewrow(self, command, lat, long, alt, frame):
        self.tableWidget.setRowCount(self.row+1)
        self.tableWidget.setItem(self.row,0,QtWidgets.QTableWidgetItem(command))
        self.item3 = self.tableWidget.item(self.row, 0)
        self.item3.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(self.row,1,QtWidgets.QTableWidgetItem(lat))
        self.item=self.tableWidget.item(self.row,1)
        self.item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(self.row, 2, QtWidgets.QTableWidgetItem(long))
        self.item1 = self.tableWidget.item(self.row, 2)
        self.item1.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(self.row, 3, QtWidgets.QTableWidgetItem(alt))
        self.item2 = self.tableWidget.item(self.row, 3)
        self.item2.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(self.row, 4, QtWidgets.QTableWidgetItem(frame))
        self.item4= self.tableWidget.item(self.row, 4)
        self.item4.setTextAlignment(Qt.AlignCenter)
        self.row+=1

    def setAltitudeValue(self,alt):
        self.label_3.setText(str(alt)+" m")

    def setgspeed(self,speed):
        s=str(speed)
        s=s[:5]
        self.label_14.setText(s+" m/s")

    def setvspeed(self,speed):
        s = str(speed)
        s = s[:5]
        self.label_12.setText(s + " m/s")

    def setmode(self,mode):
        self.label_16.setText(mode)


    def armTakeoff(self):
        self.newMission.setEnabled(False)
        self.addWaypoint.setEnabled(False)
        self.rtl.setEnabled(False)
        self.altSave.setEnabled(False)
        self.thread = MyThread()
        self.thread.change_value.connect(self.setAltitudeValue)
        self.thread.change_gspeed.connect(self.setgspeed)
        self.thread.change_vspeed.connect(self.setvspeed)
        self.thread.change_mode.connect(self.setmode)
        self.thread.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GCS-Test"))
        self.groupBox.setTitle(_translate("MainWindow", "CONNECTION"))
        self.connect.setText(_translate("MainWindow", "CONNECT"))
        self.closeConn.setText(_translate("MainWindow", "CLOSE CONNECTION"))
        self.takeoff.setText(_translate("MainWindow", "ARM AND TAKEOFF"))
        self.groupBox_2.setTitle(_translate("MainWindow", "PLAN"))
        self.newMission.setText(_translate("MainWindow", "NEW MISSION"))
        self.addWaypoint.setText(_translate("MainWindow", "ADD WAYPOINT"))
        self.rtl.setText(_translate("MainWindow", "RETURN TO LAUNCH"))
        self.altSave.setText(_translate("MainWindow","Save"))
        self.label.setText(_translate("MainWindow", "ALTITUDE REL."))
        self.label_3.setText(_translate("MainWindow", "0.0 m"))
        self.label_9.setText(_translate("MainWindow", "DIST TO WP"))
        self.label_10.setText(_translate("MainWindow", "0.0 m"))
        self.label_13.setText(_translate("MainWindow", "GROUND SPEED"))
        self.label_14.setText(_translate("MainWindow", "0.0 m/s"))
        self.label_11.setText(_translate("MainWindow", "VERTICAL SPEED"))
        self.label_12.setText(_translate("MainWindow", "0.0 m/s"))
        self.label_15.setText(_translate("MainWindow", "MODE"))
        self.label_16.setText(_translate("MainWindow", "STABILIZE"))
        #self.label_17.setText(_translate("MainWindow",""))
        self.label_18.setText(_translate("MainWindow", "0.0"))
        self.label_19.setText(_translate("MainWindow", "Enter Takeoff Altitude(Rel.): "))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Command"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Lat"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Long"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Alt"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Frame"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Delete"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
