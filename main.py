import sys

from PyQt5.QtWidgets import QApplication

from vehicle_monitor.app import MonitorApp

if __name__ == '__main__':
    app = MonitorApp()
    sys.exit(app.exec())
