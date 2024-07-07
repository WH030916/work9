from PyQt5.QtWidgets import QMainWindow, QLabel, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from pyqt5_plugins.examplebutton import QtWidgets
from pyqt5_plugins.examplebuttonplugin import QtGui

from vehicle_monitor.fourth_rec import rec_Dialog
from vehicle_monitor.select import Ui_Form
from vehicle_monitor.third_mon import mon_Dialog


class select_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel(self)
        self.setCentralWidget(self.label)

        self.pixmap = QtGui.QPixmap("./data/b1.jpg")
        # 设置QLabel的尺寸
        self.label.resize(self.width(), self.height())
        self.label.setScaledContents(True)
        # 将背景图片设置为QLabel的内容
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        # 监听窗口大小变化事件
        self.resizeEvent = self.on_resize
        self.ui = Ui_Form()
        self.ui.setupUi(self)


    def on_resize(self, event):
        self.label.resize(event.size())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(),
                                                aspectRatioMode=Qt.KeepAspectRatio,
                                                transformMode=Qt.SmoothTransformation))

    def goin_X(self):
        self.mondialog = mon_Dialog()
        self.mondialog.show()
        self.close()

    def goin_1(self):  #查看监控
        self.mondialog = mon_Dialog()
        self.mondialog.show()
        self.close()

    def goin_2(self):  #查看记录
        self.mondialog = rec_Dialog()
        self.mondialog.show()
        self.close()