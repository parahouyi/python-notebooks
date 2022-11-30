from wordcloud import WordCloud
import jieba
from PIL import Image
from imageio.v3 import imread, imwrite
ms = imread('微信图片_20220308103734.jpg')
ms22 = Image.open('微信图片_20220308103734.jpg')
print(type(ms22))
print(ms22.mode)
# with open('三国演义2.txt', 'r', encoding='utf8') as f:
#
#     sanguo = f.read()
#
#
# # print(sanguo[:200])
# psanguo = sanguo[:int(1e4)]
# fenci = jieba.lcut(psanguo)
#
# wc = WordCloud(font_path='msyh', background_color='white',min_font_size=10,\
#                max_words=50,mask=ms).generate(' '.join(fenci))
# wc.to_file('sg.png')
# print(type(ms))
# print(ms.shape)
# ms2 = ms.copy()
# ms2[:,:,1] = 0
# imwrite('1.jpg', ms2)
