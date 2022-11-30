from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import os
from docx import Document


class DocProecess(QWidget):

    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.file_dail = QFileDialog(self)  # 如果不写self，运行时会直接打开
        self.choosebtn = QPushButton('选择文件夹')
        self.searchbtn = QPushButton('开始搜索')
        self.searchbtn.clicked.connect(self.startSearch)
        self.choosebtn.clicked.connect(self.chooseDir)
        self.lable = QLabel('选择指定目录')
        self.lablec = QLabel('选择目录为')
        self.lable2 = QLabel('输入关键词')
        self.lable3 = QLabel('点击开始搜索')
        self.display = QTextEdit()
        self.inputkw = QLineEdit()
        self.inputkw.returnPressed.connect(lambda :self.searchbtn.click())
        self.choosedirname = QLineEdit()
        self.choosedirname.setReadOnly(True)
        self.inputkw.setPlaceholderText('如果需要输入多个关键词请以空格分开：')
        # self.display.setText('搜索到的文件在下面')
        self.table = QTableWidget()
        # self.display.returnPressed.connect()
        # self.event()
        # self.enterEvent() 想要加上回车也开始搜索的功能
        layout = QFormLayout()
        layout.addWidget(self.file_dail)
        layout.addRow(self.lable, self.choosebtn)
        layout.addRow(self.lablec, self.choosedirname)
        layout.addRow(self.lable2, self.inputkw)
        layout.addRow(self.lable3, self.searchbtn)
        layout.addWidget(self.display)
        layout.addWidget(self.table)

        self.resize(500, 500)
        self.setLayout(layout)
        self.setWindowTitle('WORD文件内容搜索小工具')
        self.setWindowIcon(QIcon('8.jpg'))

    def chooseDir(self):
        self.chosendir = self.file_dail.getExistingDirectory()
        self.choosedirname.setText(self.chosendir)
    def startSearch(self):
        self.display.setPlainText('正在搜索中，请稍候……') #为什么无法实现
        self.display.repaint()
        kwlist = self.inputkw.text().split()
        # print('搜索关键字是：' + str(kwlist))
        # print('目录是' + self.chosendir)
        content = os.walk(self.chosendir)
        self.result = []
        for i in content:
            for j in i[2]:
                if j.endswith('.docx'):
                    # print(i[0] + j)
                    self.result.append(i[0] + '/' + j)
        self.searched_result = []
        for i in self.result:
            # print('正在打开' + i)

            try:
                doc = Document(i)
                txt = ''
                for para in doc.paragraphs:
                    txt += para.text
                    # print(txt)
                if all(kw in txt for kw in kwlist):
                    self.searched_result.append(i)
            except:
                # print('打开文件失败')
                continue
        #     self.table.setRowCount(len(self.result))
        #     self.table.setItem(0, 0, i)
        if self.searched_result:
            self.display.setPlainText('\n'.join(self.searched_result))
        else:
            self.display.setText('没有找到符合条件的文件!')


if __name__ == '__main__':
    # os.environ['CUDA-VISIBLE-DEVICES'] = '-1'
    app = QApplication(sys.argv)
    w = DocProecess()
    w.show()
    sys.exit(app.exec_())
