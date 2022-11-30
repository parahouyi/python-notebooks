import re

patt = re.compile(r'(\d(\d(\d(\d))))\2')#用序号来指代
# print(patt.groups)
# print(patt.groupindex)
# print(patt.flags)
patt = re.compile(r'(?P<a>\d\d\d\w)(?P=a)')#用名字来指代
st = '123a123a  123b123b  345c345c'
res = patt.findall(st)
print(res)