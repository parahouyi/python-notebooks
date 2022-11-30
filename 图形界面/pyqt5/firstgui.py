from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QFont
import sys


class FirstGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my first gui coded")
        self.resize(400, 400)

        self.btn = QPushButton(self)
        self.btn.move(25, 35)
        self.btn.setText('确定')
        self.btn2 = QPushButton(self)
        self.btn2.move(126, 35)
        self.btn2.setText('取消')
        self.btn2.geometry()

        def onClick_button():
            print('退出了吗')
            self.btn.setText('我去')
            print(self.btn.geometry())
        self.btn.clicked.connect(onClick_button)

        def onClick_button2():
            self.btn2.hide()
        self.btn2.clicked.connect(onClick_button2)
        def onRelease_button2():
            self.btn2.show()
        self.btn2.released.connect(onRelease_button2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = FirstGui()
    mw.show()
    sys.exit(app.exec_())
