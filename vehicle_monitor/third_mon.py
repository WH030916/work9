import threading

from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from PyQt5.uic.properties import QtCore, QtWidgets, QtGui
from PyQt5 import QtWidgets

from vehicle_monitor.monitor import Ui_Form
from vehicle_monitor.video import Video


class mon_Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.th1 = Video('data/vd1.mp4')
        # 绑定信号与槽函数
        self.th1.send.connect(self.showimg)
        self.th1.start()

    def showimg(self, h, w, c, b, th_id, num, first_result):

        img = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(img)
        if th_id == 1:
            # 自动缩放
            width = self.ui.video1.width()
            height = self.ui.video1.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.video1.setPixmap(scale_pix)
            # str(num) 类型转换
            # print("设置carnum")
            self.ui.carnum.setText(str(num))
            # print(num)
            current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
            # print("输出时间")
            self.ui.label_2.setText(current_time)  # 假设self.ui.label_2已经正确设置
            # print("输出检测结果")
            self.ui.label_9.setText(first_result)
            # print("输出",first_result)

    def goin(self):
        # 停止视频播放
        self.th1.stop()  # 调用停止视频播放的方法
        self.th1.wait()  # 等待线程结束
        # 打開另一個界面
        from vehicle_monitor.second_select import select_Dialog
        dialog = select_Dialog()
        dialog.show()
        self.close()
