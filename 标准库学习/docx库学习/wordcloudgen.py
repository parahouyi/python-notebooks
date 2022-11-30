from docx import Document
import jieba
from wordcloud import WordCloud
import os
import shutil


def openDocx(file):  # 打开指定DOCX文件，读取文字
    doc = Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        if paragraph:
            text += paragraph.text
    else:
        f = open('../zongjie.txt', 'w', encoding='utf-8')
        f.write(text)
        f.close()
        print('读取文档内容完成！')
    return text


def fenci(text):
    words = [i for i in jieba.lcut(text) if len(i) == 2]  # ->list
    newtxt = ' '.join(words)  # ->string
    return newtxt


def genWordCloud(file, newtxt):
    exclusion = {'什么', '一个', '我们', '自己', '太太', '这个', '你们', '怎么', '没有', '不是', '那里', '如今', \
                 '说道', '知道', '起来', '这里', '告诉', '就是', '告诉', '咱们', '进来', '这样', '众人', '回来', '老爷', '只是', \
                 '只得', '大家', '丫头', '这些', '不敢', '出去', '工作', '进展', '主任', '的', '为', '河北省', '常委会', '和', '情况', '等', '我省', \
                 '关于', '省政府', '报告', '开展', '人大', '加强', '年', '以'}
    if newtxt:
        wc = WordCloud(font_path='msjh.ttc', width=800, height=1000, stopwords=exclusion, max_words=50).generate(newtxt)
        filename = file.strip('.docx').split('\\')[-1] + '词云.png'
        wc.to_file(filename)
        return filename


# file = input('请输入文件名（包括目录）：')
# text = openDocx(file)
# file = input('请输入文件名（包括目录）：'.center(100,'*') +'\n')
# text = openDocx(file)
# newtxt = fenci(text)
# genWordCloud(newtxt)
# os.startfile(filename)

def readFiles(path):
    t = os.walk(path)  # 生成器，包含的是元组，没有完整目录。元组第一个是目录（字符串），第二个是包含的子文件夹（列表），第三个是文件列表
    files = []
    for i in t:
        if i[2]:  # 表示有文件
            for j in i[2]:
                files.append(f'{i[0]}\\{j}')  # 完整目录名加上文件名
    return files


def getSpecificType(files, filetype):
    type_files = [file for file in files if file.endswith(f'.{filetype}')]
    return type_files


def main():
    directory, filetype = input('请在下方输入搜索的目录和文件类型（中间以空格间隔，按回车结束）：……'+'\n').split()
    files = readFiles(directory)
    type_files = getSpecificType(files, filetype)
    for file in type_files:
        text = openDocx(file)
        new_txt = fenci(text)
        filename = genWordCloud(file, new_txt)
        os.startfile(filename)

main()