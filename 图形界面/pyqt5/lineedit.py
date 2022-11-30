from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys


class QLineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial', 20))

        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        edit3 = QLineEdit()
        edit3.setInputMask('99_9999_999999;#')

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChange)

        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)

        edit6 = QLineEdit('Hello pyqt')
        edit6.setReadOnly(True)

        self.disp = QLabel()

        formLayout = QFormLayout()
        formLayout.addRow('整数校验', edit1)
        formLayout.addRow('浮点校验', edit2)
        formLayout.addRow('input mask', edit3)
        formLayout.addRow('文本变化', edit4)
        formLayout.addRow('输入内容', edit5)
        formLayout.addRow('只读', edit6)
        formLayout.addRow('显示 ', self.disp)
        self.setLayout(formLayout)
        self.setWindowTitle('综合案例')
        self.setWindowIcon(QIcon('hbing.ico'))

    def textChange(self, text):
        print('输入内容：' + text)
        self.disp.setText(text)
        # value = int(text)
        # self.disp.setFont(QFont(pointSize = value))

    def enterPress(self):
        print('已输入值')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QLineEditDemo()
    demo.show()
    sys.exit(app.exec_())