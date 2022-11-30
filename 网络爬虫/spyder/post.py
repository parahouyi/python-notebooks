import urllib.request
import urllib.parse

# req = urllib.request.urlopen('http://www.hbrd.net')
# content = req.read().decode(encoding='utf-8')
# print(content)

url = 'https://fanyi.baidu.com/sug'
headers = {'Accept':'text/css,*/*;q=0.1',
           'Accept-Encoding':'gzip, deflate, br',
           'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'Connection':'keep-alive',
           'Host':'fanyi-cdn.cdn.bcebos.com',
           'Referer':'https://fanyi.baidu.com/',
           'Sec-Fetch-Dest':'style',
           'Sec-Fetch-Mode':'no-cors',
           'Sec-Fetch-Site':'cross-site',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}
data = urllib.parse.urlencode({'kw': 'spyder'})  # 需要是编码的字节类型
print(type(data))
req = urllib.request.Request(url, data=data.encode('utf8'), headers=headers)
res = urllib.request.urlopen(req)
content = res.read().decode('utf8')
print(content)
# import json
# obj = json.loads(content)
# print(obj)