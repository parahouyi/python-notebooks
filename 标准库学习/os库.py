# 批量查找指定文件夹下的DOC文档

import os

from mytest.printing import printing
#
# files = []
#
#
# def openfile(path):
#     filelist = os.listdir(path)
#     for i in filelist:
#         if os.path.isdir(i):  # 如果是文件夹
#             openfile(i)
#         else:
#             filelist += i
#     return filelist
#
#
# t = openfile(r'F:\BaiduYunDownload')
# print(t)
t = os.walk('F:\BaiduYunDownload') #生成器，包含的是元组，没有完整目录。元组第一个是目录（字符串），第二个是包含的子文件夹（列表），第三个是文件列表
files = []
for i in t:
    if i[2]: #表示有文件
        for j in i[2]:
            files.append(i[0] +'\\'+j) #完整目录名加上文件名

mp3files = [file for file in files if file.endswith(('doc', 'docx', 'avi'))]
for i in mp3files:
    print(i)
