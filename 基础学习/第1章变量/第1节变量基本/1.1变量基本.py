#一次进行多个赋值
a,b = 1,5

#多个变量同值

c = d = e = f =8

for i in 'abcdef':
    print('变量'+i+'的值是',end = ':')
    print(eval(i)) #i不再是字符串而成为变量名，用eval函数