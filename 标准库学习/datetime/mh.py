import sys
import time

from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QLabel
from PyQt6.QtGui import QFont
import datetime


class MeetHistory(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        label = QLabel(self)
        label.move(100, 100)

        # label.setText(self.output)
        label.setFont(QFont('楷体', 24))
        label.setStyleSheet('color:red')
        # label.setStyleSheet('color'='red')
        label.adjustSize()

        self.setGeometry(300, 300, 550, 250)
        self.setWindowTitle('Meet history')
        while True:
            meet = datetime.datetime(2020, 4, 6, 18, 0, 0)
            # # history = (datetime.datetime.now() - meet)
            # days = (datetime.datetime.now() - meet).days
            # # seconds = (datetime.datetime.now() - meet).seconds
            # hours = (datetime.datetime.now() - meet).seconds // 3600
            # minutes = (datetime.datetime.now() - meet).seconds // 3600 // 60
            # second = (datetime.datetime.now() - meet).seconds // 3600 % 60

            print(datetime.datetime.now())
            history = datetime.datetime.now()- meet
            print(datetime.datetime.now()- meet)
            print(f'我和亲爱的老婆大人已相识\n{(datetime.datetime.now() - meet).days}天{((datetime.datetime.now() - meet).seconds // 3600)}小时{((datetime.datetime.now() - meet).seconds // 3600 // 60)}分{((datetime.datetime.now() - meet).seconds // 3600 % 60)}秒')
            time.sleep(1)

def main():
    app = QApplication(sys.argv)
    ex = MeetHistory()
    ex.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
