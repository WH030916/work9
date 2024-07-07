import threading
import time

from PyQt5.QtCore import pyqtSignal

from api.attributes import car_att
from api.car import vehicle_detect
# # 重写run()方法: 线程执行的内容
# # Thread的实例对象.start()  run()就会自动执行

from PyQt5.QtCore import QThread, pyqtSignal
import cv2 as cv

class Video(QThread):
    # send: pyqtSignal = pyqtSignal(int, int, int, bytes, int, int, str)
    send: pyqtSignal | pyqtSignal = pyqtSignal(int, int, int, bytes, int, int, str)  # emit


    def __init__(self, video_id):
        super().__init__()
        self.dev = cv.VideoCapture(video_id)
        self.th_id = 1 if video_id == 'data/vd1.mp4' else 2

    def run(self):
        i = 0
        ret, frame = self.dev.read()
        first_result = car_att(frame)
        # print(first_result)
        num = vehicle_detect(frame)
        while not self.isInterruptionRequested():
            ret, frame = self.dev.read()
            if not ret:
                break
            i += 1
            if i % 100 == 0:  # 防止视频太卡、调用次数用完，隔一段时间再调用
                first_result = car_att(frame)  # 返回车型识别得分最高结果 车名
                # print(first_result)
                num = vehicle_detect(frame)  # 返回车流量
            h, w, c = frame.shape
            img_bytes = frame.tobytes()
            self.send.emit(h, w, c, img_bytes, self.th_id, num, first_result)
            time.sleep(0.01)  # 10ms

    def stop(self):
        self.requestInterruption()
        self.dev.release()  # 释放视频捕获设备
        self.quit()  # 退出线程
        self.wait()  # 等待线程结束
