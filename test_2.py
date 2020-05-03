#encoding=gbk
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton

from PyQt5.QtCore import QBasicTimer


class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self)

        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('��ʼ', self)

        self.btn.move(40, 80)

        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()

        self.step = 0

        self.setGeometry(300, 300, 280, 170)

        self.setWindowTitle('������')

        self.show()

    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()

            self.btn.setText('���')

            return

        self.step = self.step + 1

        self.pbar.setValue(self.step)

    def doAction(self, value):

        if self.timer.isActive():

            self.timer.stop()

            self.btn.setText('��ʼ')

        else:

            self.timer.start(100, self)

            self.btn.setText('ֹͣ')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())