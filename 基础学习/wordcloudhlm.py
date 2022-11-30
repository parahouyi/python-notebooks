import jieba
from wordcloud import WordCloud

excludes = {'什么','一个','我们','自己','太太','这个','你们','怎么','没有','不是','那里','如今',\
            '说道','知道','起来','这里','老太太','一面','只见','两个','出来','他们','姑娘','奶奶',\
            '不知','听见','东西','告诉','就是','告诉','咱们','进来','这样','众人','回来','老爷','只是',\
            '只得','大家','丫头','这些','不敢','出去'}

f = open('红楼梦.txt', 'r', encoding='UTF-8')
txt = f.read()
f.close()

words = jieba.lcut(txt)

newtxt = ''.join(words)

wordcloud = WordCloud(background_color='white',\
                      width=800,\
                      height=600,\
                      font_path='msyh.ttc',\
                      max_words=20,\
                      max_font_size=80,\
                      stopwords=excludes,\
                      ).generate(newtxt)
wordcloud.to_file('词云.png')