from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngine import *
import sys


class QLineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.edit1 = QLineEdit()
        self.edit1.setValidator(QIntValidator())
        self.edit1.setMaxLength(4)
        self.edit1.setAlignment(Qt.AlignRight)
        self.edit1.setFont(QFont('Arial', 20))
        # edit1.editingFinished.connect(self.searchWord)

        okbtn = QPushButton('确定')
        okbtn.clicked.connect(self.lcdover)
        # okbtn.mouseDoubleClickEvent.connect(self.textChange)
        okbtn.setIcon(QIcon('hbing.ico'))
        formLayout = QFormLayout()
        formLayout.addRow('整数校验', self.edit1)
        formLayout.addRow('开始搜索', okbtn)
        self.lcd = QLCDNumber()
        self.lcd.value()
        formLayout.addWidget(self.lcd)

        # web = QtWebEngine()

        self.lcd.overflow.connect(self.lcdover)
        self.setLayout(formLayout)
        self.setWindowTitle('综合案例')
        self.setWindowIcon(QIcon('hbing.ico'))

    def textChange(self):
        print('输入内容：' + self.edit1.text())
        # self.lcd.resize(100,100)
        self.lcd.display(self.edit1.text())
    def lcdover(self):
        self.lcd.setFont(QFont('Arial',24))
        self.lcd.close()
    # def searchWord(self):
    #     text = self.edit1.text
    #     print(text)
    #     return text


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QLineEditDemo()
    demo.show()
    sys.exit(app.exec_())
