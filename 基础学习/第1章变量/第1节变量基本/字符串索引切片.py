
a = 'I love you my dear friend!!!'
print(enumerate(a))#<enumerate object at 0x00000244F92AB5C0>

print(list(enumerate(a)))#元素为元组的列表
print(dict(enumerate(a)))#字典
print(tuple(enumerate(a)))#元素为元组的元组
stra = str(enumerate(a))#没有内容，只是把返回的枚举器变成字符串了
print(stra)
print(type(stra))
print(type(enumerate(a)))

for i,element in enumerate(a):
    print(i,element)

print(a[::-1]) #反转
print(a[::-2])#反转步长
print(a[5:33])
cc = a[33:35]
print(cc,type(cc))
print(bool(cc))
print(a.partition(' '))#('I', ' ', 'love you my dear friend!!!')

b = a.split('')
print(b)