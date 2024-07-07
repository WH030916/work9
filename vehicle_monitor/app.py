from PyQt5.QtWidgets import QApplication

from vehicle_monitor.first_login import MainDialog

import sys


class MonitorApp(QApplication):
    def __init__(self):
        super(MonitorApp, self).__init__(sys.argv)
        self.dialog = MainDialog()
        self.dialog.show()

