import re


import re
# 用\b\w+(?=ing\b)查找I’m singing while you’re dancing.匹配到sing danc
patt = re.compile(r'((?<=\bre)\w+\b)')#['adings'],匹配了re但是不取  取后面的
st = "I’m singing while you’re repainting and she readings he talkings"
res = patt.findall(st)
print(res)

# 用(?<=\bre)\w+\b查找reading a book得到ading。
patt = re.compile(r'((?!\bsa)\w+\b)')#匹配第一个，不符就取，符合就跳过取下面的（包括第2，3）
st = "I’m singing while you say repainting and she readings talkings"
res = patt.findall(st)
print(res)
# patt = re.compile(r'((?<!\bread)ing)')#匹配所有，如果符合就跳过，不符就取后面的）
# st = "I’m singing while you say repainting and she readings"
# res = patt.findall(st)#['ing', 'ing', 'ing']
# print(res)