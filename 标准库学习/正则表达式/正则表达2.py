import re
'''修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：
修饰符	描述
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。'''
salary = '''
张三， 总监，10000，8000
李四， 销售经理，8000，6000
王五五，销售员，6000，5000
'''
patt = re.compile(r'，(?P<a>\d+$)',re.M)
res = patt.findall(salary)
print(res)
sear = patt.search(salary)
print(sear)
print(sear.start(),sear.end(), sear.span())

# print(type(sear))
print(bool(sear))
