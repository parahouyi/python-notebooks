import re

'''
正则表达式
findall   match

通配符：

.  除了换行以外任何一个字符
+ 匹配1次或任意次前面的表达式
*  匹配0次或任意次前面的表达式
 ?  单个时表示0或1次，    组合时表示非贪婪，尽可能少匹配
 "?"      Matches 0 or 1 (greedy) of the preceding RE.
 *?,+?,?? Non-greedy versions of the previous three special characters.
 {m,n}    Matches from m to n repetitions of the preceding RE.
    {m,n}?   Non-greedy version of the above.
 
\d \D 
\w 包括下划线在内的任意单词字符
 \W 
\b 代表单词的开始或者结束（以标点、空格、换行作为分割
\s 任何空白字符，包含空格 回车  制表
 \s
() 分组 可以有多个,返回以元组为元素的列表，可以嵌套
(?:...)  Non-grouping version of regular parentheses.
[] 筛选条件 
{} 出现次数 范围/固定
{n}   {n,}  {n,m} 可配合?
^ $
[^a] 非a全取

re.M = Multilines
re.S 使.取值包含换行在内的所有字符
'''

# re.match()# 返回一个地址，可以用bool来转换
# findall, search, sub subn compile

pattern = r'.'  #['中', '华', '人', '民', '共', '和', '国']
pattern = r'.*' #['中华人民共和国', '']
pattern = r'.*?' #['', '中', '', '华', '', '人', '', '民', '', '共', '', '和', '', '国', '']
pattern = r'.+'  #['中华人民共和国']
pattern = r'.+?'  #['中', '华', '人', '民', '共', '和', '国']
pattern = r'.?' #['中', '华', '人', '民', '共', '和', '国', '']
pattern = r'.??'#['', '中', '', '华', '', '人', '', '民', '', '共', '', '和', '', '国', '']
pattern = r'..' #['中华', '人民', '共和']
pattern = r'..' #['中华', '人民', '共和']

pattern = r'..? '#['中华', '人民', '共和', '国']
pattern = r'..*' #['中华人民共和国']
pattern = r'(..)*' #['共和', '', '']
pattern = r'(?:..)*' #['中华人民共和', '', '']
pattern = r'(?:..)*?' #['中华人民共和国']
pattern = r'(..*)' #['中华人民共和国']

res = re.findall(pattern, '中华人民共和国')
print(res)

patt = re.compile(r'w')
t = patt.split('hellow world!!!!')
t = patt.sub('WW','helow  world wide web')
print(t) #['hello', ' ', 'orld!!!!']
