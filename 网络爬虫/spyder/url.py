import urllib.request
import urllib.parse
# req = urllib.request.urlopen('http://www.hbrd.net')
# content = req.read().decode(encoding='utf-8')
# print(content)

url='http://www.hbrd.gov.cn/cwhjg/cjhhzgzwyh/gzdt/index.shtml'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}
req = urllib.request.Request(url,headers=headers)
res = urllib.request.urlopen(req)
content = res.read().decode('utf8')
print(content)
# urllib.request.get().quote
print(urllib.parse.quote('周杰化')) #实际上转了了16进制UNICODE，只是%取代了X
#%E5%91%A8%E6%9D%B0%E5%8C%96
dict1 = {
    'name':'张建广',
    'sex':'男',
    'location':'中国河北'

}
print(urllib.parse.urlencode(dict1))