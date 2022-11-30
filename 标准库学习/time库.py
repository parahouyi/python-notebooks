import time
import datetime
from libstudy import libstudy
from mytest.printing import printing

# print(time.__dict__)
# print(help(time))
# print(dir(time))

time.localtime() # 当地时间
time.gmtime() # ->时间类，标准时间，差8小时
time.ctime() #->字符串
time.time() #->浮点数