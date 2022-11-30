import sys
import time

import PyQt5.QtGui
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel
from PyQt5.QtGui import QFont, QPicture, QPixmap
import datetime

class MeetHistory(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        self.label = QLabel(self)
        self.label.move(100, 100)
        self.label.setFont(QFont('华文新魏',28))
        self.label.setStyleSheet('color:red')


        self.meet = datetime.datetime(2020, 4, 6, 18, 0, 0)
        self.history = datetime.datetime.now() - self.meet
        self.days = self.history.days
        self.seconds = self.history.seconds
        self.hours = self.seconds // 3600
        self.minutes = self.seconds % 3600 // 60
        self.second = self.seconds % 60
        self.output = f'我和亲爱的老婆大人已相识\n  ❤{self.days}天{self.hours}小时{self.minutes}分{self.second}秒❤'
        self.startTimer(1000)

        self.label.setText(self.output)
        self.label.adjustSize()
        self.label.repaint()

        label2 = QLabel(self)
        couple_pic = QPixmap('couple.jpg')
        # couple_pic.scaled(150,100)
        label2.setFixedSize(250,200)
        label2.setPixmap(couple_pic)
        label2.move(200,200)
        self.setGeometry(300, 200, 600,500)
        self.setWindowTitle('Meet history')

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        self.meet = datetime.datetime(2020, 4, 6, 18, 0, 0)
        self.history = datetime.datetime.now() - self.meet
        self.days = self.history.days
        self.seconds = self.history.seconds
        self.hours = self.seconds // 3600
        self.minutes = self.seconds % 3600 // 60
        self.second = self.seconds % 60
        self.output = f'我和亲爱的老婆大人已相识\n  ❤{self.days}天{self.hours:02d}小时{self.minutes:02d}分{self.second:02d}秒❤'
        self.startTimer(1000)

        self.label.setText(self.output)
        self.label.adjustSize()
        self.label.repaint()
    def enterEvent(self, event) -> None:
        print('mouse enter')
        self.setCursor(QCursor(QPixmap('sakuran.ico')))

def main():
    app = QApplication(sys.argv)
    ex = MeetHistory()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
