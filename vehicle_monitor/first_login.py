from PyQt5 import QtWidgets, QtGui, QtCore
from vehicle_monitor.login import Ui_Form
from vehicle_monitor.second_select import select_Dialog

class MainDialog(QtWidgets.QMainWindow):
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
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))


    def goin(self):
        input_text1 = self.ui.plainTextEdit.toPlainText()  # 获取plainTextEdit中的文本  用户输入用户名
        input_text2 = self.ui.plainTextEdit_2.toPlainText()  # 获取plainTextEdit_2中的文本  用户输入密码
        if input_text1 == "123":  # 管理员用户名设置
            if input_text2 == "123":
                self.monitorframe = select_Dialog()    # 相同则跳转
                self.monitorframe.show()
                # print("展示，关闭")
                self.close()
            else:   # 不相同则弹窗提示
                QtWidgets.QMessageBox.warning(self, "警告", "密码错误！")
        else:
            QtWidgets.QMessageBox.warning(self, "警告", "用户名错误！")

