#创建集合的方法
import os, sys
sys.path.append(os.path.dirname(os.path.dirname((os.path.dirname(os.path.abspath(__file__))))))
from main import printer

s1 = {2,7,8.9,91,'s'}
printer(s1)
s2 = s1.copy()
printer(s2)
printer(s1.pop())
printer(s1.pop())
printer(s1.pop())
s1.difference
