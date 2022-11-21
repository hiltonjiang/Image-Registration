# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QStyleFactory

class Ui_MainWindow(object):
    """Ui MainWindow class

    In this class, PyQt5 UI code generator creates all the widget objects we put in the PyQt designer,
    which contains their settings like the position and scale.

    Important attributes:
    -----------
    label_69: label object
        The place to show the source image.
    label_68: label object
        The place to show the target image which is a reference for us to do image registration.
    label_67: label object
        The place to show the result of image registration.
    label_66: label object
        The place to show the grey image.
    comboBox: comboBox object
        A combo box to choose the method or loss function used for finding the transformation.
    pushButton : pushButton object
        A button for choosing the source image.
    pushButton_2 : pushButton object
        A button for choosing the target image.
    pushButton_4 : pushButton object
        A button to start image registration.
    pushButton_9 : pushButton object
        A button to reset all the displayed images.
    textEdit: textEdit object
        An input box to get the learning rate.
    textEdit_2: textEdit object
        An input box to get the setting of learing rate decay.
    textEdit_3: textEdit object
        An input box to get the max training iteration.
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 671)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1080, 741))
        self.stackedWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.pushButton = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.pushButton.setGeometry(QtCore.QRect(80, 30, 111, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 370, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 420, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_66 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_66.setEnabled(True)
        self.label_66.setGeometry(QtCore.QRect(640, 350, 351, 271))
        self.label_66.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_66.setMouseTracking(False)
        self.label_66.setAutoFillBackground(True)
        self.label_66.setFrameShape(QtWidgets.QFrame.Box)
        self.label_66.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_66.setText("")
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_67.setEnabled(True)
        self.label_67.setGeometry(QtCore.QRect(280, 350, 351, 271))
        self.label_67.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_67.setMouseTracking(False)
        self.label_67.setAutoFillBackground(True)
        self.label_67.setFrameShape(QtWidgets.QFrame.Box)
        self.label_67.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_67.setText("")
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_68.setEnabled(True)
        self.label_68.setGeometry(QtCore.QRect(640, 70, 351, 271))
        self.label_68.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_68.setMouseTracking(False)
        self.label_68.setAutoFillBackground(True)
        self.label_68.setFrameShape(QtWidgets.QFrame.Box)
        self.label_68.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_68.setText("")
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_69.setEnabled(True)
        self.label_69.setGeometry(QtCore.QRect(280, 70, 351, 271))
        self.label_69.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_69.setMouseTracking(False)
        self.label_69.setAutoFillBackground(True)
        self.label_69.setFrameShape(QtWidgets.QFrame.Box)
        self.label_69.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_69.setText("")
        self.label_69.setObjectName("label_69")
        self.label_10 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_10.setGeometry(QtCore.QRect(40, 120, 121, 16))
        self.label_10.setObjectName("label_10")
        self.comboBox = QtWidgets.QComboBox(self.stackedWidgetPage1)
        self.comboBox.setGeometry(QtCore.QRect(40, 150, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 70, 111, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.stackedWidgetPage1)
        self.textEdit.setGeometry(QtCore.QRect(40, 220, 81, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_11 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_11.setGeometry(QtCore.QRect(40, 190, 121, 16))
        self.label_11.setObjectName("label_11")
        self.textEdit_2 = QtWidgets.QTextEdit(self.stackedWidgetPage1)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 320, 191, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_12 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_12.setGeometry(QtCore.QRect(40, 270, 211, 16))
        self.label_12.setObjectName("label_12")
        self.textEdit_3 = QtWidgets.QTextEdit(self.stackedWidgetPage1)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 220, 81, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_13 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_13.setGeometry(QtCore.QRect(130, 190, 131, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_14.setGeometry(QtCore.QRect(40, 290, 211, 16))
        self.label_14.setObjectName("label_14")
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QtWidgets.QWidget()
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # set the style of our GUI and make it look better
        QApplication.setStyle(QStyleFactory.create('Fusion'))

    def retranslateUi(self, MainWindow):
        """
        Here we set the name of widgets and their items.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "选择初始图像"))
        self.pushButton_4.setText(_translate("MainWindow", "应用"))
        self.pushButton_9.setText(_translate("MainWindow", "重置图像"))
        self.label_10.setText(_translate("MainWindow", "选择算法"))
        self.comboBox.setItemText(0, _translate("MainWindow", "均方误差"))
        self.comboBox.setItemText(1, _translate("MainWindow", "K-L散度"))
        self.comboBox.setItemText(2, _translate("MainWindow", "互信息"))
        self.comboBox.setItemText(3, _translate("MainWindow", "皮尔逊相关系数"))
        self.comboBox.setItemText(4, _translate("MainWindow", "归一化互相关"))
        self.comboBox.setItemText(5, _translate("MainWindow", "非线性光流"))
        self.pushButton_2.setText(_translate("MainWindow", "选择目标图像"))
        self.label_11.setText(_translate("MainWindow", "设置学习率"))
        self.label_12.setText(_translate("MainWindow", "设置学习率衰减（步数;衰减率）"))
        self.label_13.setText(_translate("MainWindow", "设置最大训练步数"))
        self.label_14.setText(_translate("MainWindow", "eg: 50,100;0.5,0.5"))
        self.action1.setText(_translate("MainWindow", "1"))