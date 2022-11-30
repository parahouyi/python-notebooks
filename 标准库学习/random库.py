import random
import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.flag = True
        names = '杨智明  高增勇  刘治奇  杨亚东 巨利军 于秋峰 任建国 洪宇  杨军梅 张登岩 吴国利  李佳怡  肖杰文  张建广  崔晓晔   韩晓磊'
        self.name_list = names.split()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(self.start)
        # btn.mouseDoubleClickEvent.connect(self.stop)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.setAutoRepeat(True)

        btn2 = QPushButton('stop', self)
        btn2.clicked.connect(self.stop)
        btn2.move(150, 50)
        self.label = QLabel(self)
        self.label.move(50, 70)
        self.label.setFixedSize(100, 100)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Quit button')

    def stop(self):
        self.label.setText(random.choice(self.name_list))

    def start(self):
        while self.flag:
            self.label.setText(random.choice(self.name_list))
            self.label.repaint()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

#
# if __name__ == '__main__':
#     main()
# #
# random.random()
# print(dir(random))
# random, randint, randrange, uniform, choice, sample, shuffle
names = '杨智明  高增勇  刘治奇  杨亚东 巨利军 于秋峰 任建国 洪宇  杨军梅 张登岩 吴国利  李佳怡  肖杰文  张建广  崔晓晔   韩晓磊'
name_list = names.split()
print(random.choices(name_list, k=2))
print(random.sample(name_list, 2))


