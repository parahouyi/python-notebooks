import os, shutil, zipfile


'''
os.path.abspath
os.path.isdir
os.path.isfile

os.path.basename  文件名或最后一个子文件夹名
os.path.split  返回一个元组，前面的和BASENAME两部分
os.path.join  必须是几段字符串，不能是元组或列表,如果是列表或元组可以用*拆包
os.path.getsize

os.getcwd
os.listdir
os.remove  删除文件，直接删除了，不放进回收站
os.removedirs
os.rmdir
os.mkdir/makedirs
os.sep

shutil.rmtree(dir)  删除路径下的所有文件、目录，无论是否有文件
shutil.copytree(src, dtn)   返回创建的新文件夹
shutil.copy(源文件，目标文件） 返回目标路径加文件名
shutil.move(src,dtn) 移动和重命名

zipfile.ZipFile(文件名，'w')  写入  'a' 追加, r'读取 with **** as z  z.
               .write
               .extract 解压时不能有同名文件，否则报错
               .namelist
               .close
'''

path = r'C:\Users\parah\PycharmProjects\pythonProject'
path2 = 'learning'
c = os.path.abspath(path)
print(c)
c2 = os.path.abspath(path2)
print(c2)

# z = zipfile.ZipFile('abc.zip','w') #创建空的
# path = r'd:\写作'
# for x in os.listdir(path): #这样无法把子文件夹里的文件加进来，只有空的子文件夹
#     z.write(path + os.sep + x)
# z.close()

with zipfile.ZipFile('abc.zip','r') as f:
    for file in f.namelist():
        print(file)
        f.extract(file, 'zip')



