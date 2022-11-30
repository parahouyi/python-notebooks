#
from mytest.printing import printing

# ls = ['北京', '上海', '天津', '重庆']
# f = open('city.csv', 'w', encoding = 'utf-8')
# f.write(','.join(ls) + '\n')
# f.close()
# f = open('city.csv', 'r+', encoding = "utf-8")
# ls = f.read().strip('\n').split(',')
# f.close()
# printing(ls)
raw = '''序号	统计时间	居民消费价格月度同比涨跌（%）	城市消费价格月度同比涨跌（%）	农村消费价格月度同比涨跌（%）
1	2016年1月	1.8	1.8	1.5
2	2016年2月	2.3	2.3	2.2
3	2016年3月	2.3	2.3	2.2
4	2016年4月	2.3	2.3	2.4
5	2016年5月	2.0	2.0	2.1
6	2016年6月	1.9	1.9	1.9
7	2016年7月	1.8	1.8	1.5
8	2016年8月	1.3	1.4	1.0
9	2016年9月	1.9	2.0	1.6
10	2016年10月	2.1	2.2	1.8
11	2016年11月	2.3	2.3	2.0
12	2016年12月	2.1	2.1	1.9'''
rawl1 = raw.split('\n')
rawl = [i.split('\t') for i in rawl1]
f = open('cpi.csv', 'r', encoding='utf-8')
ls = []
for i in f:
    ls.append(i.strip('\n').split(','))
print(ls)

e = open('cpi3.csv', 'w', encoding='utf-8')
# for i in sorted(ls, key=lambda a: a[-1], reverse=True):
#     e.write(','.join(i) + '\n')
# e.close()
for row in ls:
    line = ''
    for item in row:
        line += '{:^30}'.format(item)
    e.write(line + '\n')
    print(line)
e.close()
