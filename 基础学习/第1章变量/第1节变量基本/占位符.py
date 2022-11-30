
#占位符一

# name,age = eval(input('please input your name and age here:'))
'''同时给多个变量输入值的办法，要用eval函数。否则会识别成一个整个的字符串'''
name = 'simon'
age = 2544
print('your name is %s,and your age is %d'%(name,int(age)))

#占位符二
print('your name is {},and your age is {:08d}'.format(name,age))
print('your name is {0},and your age is {1},this is the info about {0}'.format(name,age))
print('your name is {name:29},and your age is {age:08d},this is the info about {name}'.format(name=name,age=age))

#占位符三

print(f'your name is {name},and your age is {age}')
x = 3
print(f'{x+1=}')   # Python 3.8

#无法格式化输出，宽度，对齐等，小数位
s = set()
s.add('a')
print(s)





