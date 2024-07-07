from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QLabel, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtCore, QtWidgets, QtGui
from PyQt5 import QtWidgets

from vehicle_monitor.record import Ui_Form


class rec_Dialog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)  # 调用自动生成的 setupUi 方法

        # 假设你的表格对象是 self.ui.tableWidget
        table_widget = self.ui.tableWidget

        # 设置表格列数
        table_widget.setColumnCount(2)
        table_widget.setHorizontalHeaderLabels(["时间", "车辆图片"])

        # 添加一些示例数据
        for i in range(5):
            # 添加行
            row = table_widget.rowCount()
            table_widget.insertRow(row)

            # 创建 QTableWidgetItem 对象
            time_item = QTableWidgetItem(QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss"))

            # 创建图片项
            image_item = QTableWidgetItem()
            # pixmap = QPixmap('./data/car1.jpg')  # 确保 图片路径正确
            pixmap = QPixmap(f'./data/car{i + 1}.jpg')  # 确保 图片路径正确
            # 调整图片大小，这里将图片宽度调整为300像素，高度自动保持比例
            pixmap = pixmap.scaled(300, 300, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            image_item.setIcon(QIcon(pixmap))

            # 将 QTableWidgetItem 对象添加到表格中
            table_widget.setItem(row, 0, time_item)  # 时间列
            table_widget.setItem(row, 1, image_item)  # 信息列

        # 调整列宽
        table_widget.setColumnWidth(0, 300)  # 时间列宽
        table_widget.setColumnWidth(1, 400)  # 信息列宽
        # 调整行高
        for i in range(5):  # 假设您有5行数据
            table_widget.setRowHeight(i, 400)  # 设置每一行的高度为100像素

    def on_resize(self, event):
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))

    def goin(self):
        from vehicle_monitor.second_select import select_Dialog
        dialog = select_Dialog()
        dialog.show()
        self.close()


