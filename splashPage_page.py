from PySide6 import QtCore
from PySide6.QtWidgets import QWidget
from ui_splashPage import Ui_Form
import time


class splashPage(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.progressBar_splash.setMinimum(0)
        self.progressBar_splash.setMaximum(100)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.start_progress()
        # Progress Value
        self.progress_value = 0

    def start_progress(self):
        self.progress_value = 0
        self.progressBar_splash.setValue(self.progress_value)
        self.timer.start(20)  # Update every 100 milliseconds

    def update_progress(self):
        if self.progress_value < 100:
            self.progress_value += 1
            self.progressBar_splash.setValue(self.progress_value)
        else:
            self.timer.stop()
