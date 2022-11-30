from docx import Document
import jieba
import os
from lxml import etree

def openDocx(file):  # 打开指定DOCX文件，读取文字
    doc = Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        if paragraph.text:
            text += paragraph.text
        else:
            body_xml_str = doc._body._element.xml  # 获取body中的xml
            body_xml = etree.fromstring(body_xml_str)  # 转换成lxml结点
            text = etree.tounicode(body_xml) #转换成字符串格式
    # else:
    #
        # print('读取文档内容完成！')
    return text  # 返回字符串


def fenci(text):
    words = [i for i in jieba.lcut(text) if len(i) == 2]  # ->list
    newtxt = ' '.join(words)  # ->string
    return newtxt


def readFiles(path):
    t = os.walk(path)  # 生成器，包含的是元组，没有完整目录。元组第一个是目录（字符串），第二个是包含的子文件夹（列表），第三个是文件列表
    files = []
    for i in t:
        if i[2]:  # 表示有文件
            for j in i[2]:
                if not j.startswith(('~', '.')):
                    files.append(f'{i[0]}\\{j}')  # 完整目录名加上文件名
    # for file in files:
    #     if file.endswith('.doc'):
    #         os.rename(file, file+'x') #修改了也没有用
    return files


def getSpecificType(files, filetype=('docx', '.doc')):  # filetype用一个字符串元素组成的元组
    type_files = [file for file in files if file.endswith(filetype)]
    return type_files  # 列表


def searchKeyWord(text, kwlist):
    exist = True
    for kw in kwlist:
        if kw not in text:
            exist = False
            break
    return exist


def main():
    input_content = input('请在下方输入搜索的目录和需要查找的内容关键字（可以多个）（中间以空格间隔，按回车结束）：……' + '\n').split()
    directory, search_words = input_content[0], input_content[1:]  # 即使只有两个元素，第一个也成为元素本身的类型，而第二个是只有一个元素的列表类型
    files = readFiles(directory)
    type_files = getSpecificType(files)
    searchedFiles = []
    count = 0
    for file in type_files:
        try:
            text = openDocx(file)
            if searchKeyWord(text, search_words):
                count += 1
                searchedFiles.append(file)
                print(f'第{count:02}个： ', file)
        except:
            continue
    if not searchedFiles:
        print('没有找到符合条件的文件！')
    else:
        f = open('查询结果.txt', 'w', encoding='utf-8')
        f.write('\n'.join(searchedFiles))
        f.close()
        print(f'总共找到{len(searchedFiles)}个文件！')
        # os.startfile(filename)
    return searchedFiles


results = main()
if results:
    open_num = input('您想要打开第几个文件，请输入数字 ')
    filename = results[int(open_num) - 1]
    os.startfile(filename)
    input('回车键退出')
else:
    input('回车键退出')
