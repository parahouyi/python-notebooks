import jieba
from wordcloud import WordCloud

excludes = {'什么','一个','我们','自己','太太','这个','你们','怎么','没有','不是','那里','如今',\
            '说道','知道','起来','这里','老太太','一面','只见','两个','出来','他们','姑娘','奶奶',\
            '不知','听见','东西','告诉','就是','告诉','咱们','进来','这样','众人','回来','老爷','只是',\
            '只得','大家','丫头','这些','不敢','出去','所以','不过','的话','姐姐','不好','一时','不能','过来','心里','二爷' }

f = open('红楼梦.txt', 'r', encoding='UTF-8')
txt = f.read()
f.close()

words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

for word in excludes:
    del(counts[word])

items = list(counts.items())

items.sort(key=lambda x: x[1], reverse=True)


for i in range(15):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word,count))