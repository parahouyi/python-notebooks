from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys


class QFile(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.okbtn = QPushButton('打开文件夹')
        self.okbtn.clicked.connect(self.showfiledial)
        formLayout = QFormLayout()

        formLayout.addWidget(self.okbtn)
        self.setLayout(formLayout)
        self.setWindowTitle('打开文件')
        self.setWindowIcon(QIcon('hbing.ico'))

    def showfiledial(self):
        qf = QFileDialog()
        # qf.getOpenFileName(self)
        diropen = qf.getExistingDirectory(self)
        # qf.getOpenFileUrl()
        # qf.getOpenFileUrl()
        print(type(diropen))
        print(diropen)


        # value = int(text)
        # self.disp.setFont(QFont(pointSize = value))

    def enterPress(self):
        print('已输入值')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QFile()
    demo.show()
    sys.exit(app.exec_())