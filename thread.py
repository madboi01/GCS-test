import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyThread(QThread):

    change_value=pyqtSignal(int)

    def run(self):
        cnt=0
        while cnt<100:
            cnt+=1

            time.sleep(0.3)
            self.change_value.emit(cnt)


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.InitUI()
        self.show()

    def InitUI(self):
        vbox=QVBoxLayout()
        self.progressbar=QProgressBar()
        vbox.addWidget(self.progressbar)
        self.button=QPushButton("Run Progress")
        vbox.addWidget(self.button)
        self.button.clicked.connect(self.startprogressbar)
        self.setLayout(vbox)

    def setprogress(self,val):
        self.progressbar.setValue(val)

    def startprogressbar(self):
        self.thread=MyThread()
        self.thread.change_value.connect(self.setprogress)
        self.thread.start()


App=QApplication(sys.argv)
window=Window()
sys.exit(App.exec())