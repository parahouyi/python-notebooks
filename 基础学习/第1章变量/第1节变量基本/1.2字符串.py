#字符串的常用方法
txt = 'I love you python and here is another sentence宝贝'


#删除字符串中的某些特定字符
txt2 = txt.replace(' ','') #txt本身并没有被修改，而是要将结果赋予给新的变量
print(txt2)
print(txt)

txt3 = txt.replace('\n','**')
print(txt3)

#大小写的改变
txt4 = txt.upper()
txt5 = txt.lower()
txt6 = txt.capitalize()
txt7 = txt.title()
txt8 = txt.casefold()
txt9 = txt.swapcase()
for i in range(4,10):
    print('变量txt%s的值是：'%i,eval('txt'+str(i)))
# help(str)
#判断字符串的属性
print(txt.isalnum())
print(txt.isalpha())
print(txt.isprintable())
print('12334433'.isalnum())
print('abcddef'.isalpha())

print(txt.center(60,'*'))
print(txt.lstrip('I'))

print(txt.ljust(60,'-'))
# txt.rjust();txt.zfill()
print(txt.zfill(60))

#查找
print(txt.find('z'))#如果不存在返回-1
print(txt.rfind('o'))
#index()，找不到会发生错误
print(txt.rindex('lov'))

#strip,lstrip,rstrip
# 分割合并
txtu = 'I love you \n my whole life \r yes i am very sure of that'
txt10 = txt.split(' ',4)
txt13 = txt.rsplit(' ',4)
print(txt10)
print(txt13)
txt11 =txtu.splitlines()
print(txt11)
txt14 = txt.split('I')
print(txt14)#分成一个空字符串和其余一个部分
txt15 = txt.split('sentence')
print(txt15)
txt16=txt.maketrans('aco','123')#返回的是一个字典，转换规则
print(type(txt16))
print(txt16)
print(txt.translate(txt16))

# eval(),
# str(),repr()有什么区别
# dict = {'runoob': 'runoob.com', 'google': 'google.com'}
# ccc = repr(dict);ccc2 = str(dict)
# print(ccc==ccc2)#true

#编码和解码
print(txt.encode('utf-8'))#bytes
# 在交互模式中，最后被输出的表达式结果被赋值给变量 _
