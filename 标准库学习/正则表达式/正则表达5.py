import re


import re
# 用\b\w+(?=ing\b)查找I’m singing while you’re dancing.匹配到sing danc
patt = re.compile(r'(\b\w+(?=in))')#['sing', 'danc', 'typ', 'talk']
patt = re.compile(r'(\b\w+(?<=in))')#['singin', 'dancin', 'typin', 'talkin']
patt = re.compile(r'(\b\w+(?!in))')#['I', 'm', 'singing', 'while', 'you', 're', 'dancing', 'and', 'she', 'typin', 'he', 'talkings']
patt = re.compile(r'(\b\w+(?<!in))')#['I', 'm', 'singing', 'while', 'you', 're', 'dancing', 'and', 'she', 'typi', 'he', 'talkings']
st = "I’m singing while you’re dancing and she typin he talkings"
res = patt.findall(st)
print(res)

# 用(?<=\bre)\w+\b查找reading a book得到ading。