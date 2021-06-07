import requests
import re

# 关于requests的练习 https://docs.python-requests.org/zh_CN/latest/user/quickstart.html
'''url = "https://tieba.baidu.com/p/6131348235"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62'}
r = requests.get(url, headers=headers)
print(r.content)
p = r'<img class="BDE_Image" src="([^"]+\.jpg)'
imglist = re.findall(p, r.text)
for each in imglist:
    print(each)
'''

'''
url = "https://tieba.baidu.com/p/6131348235"
url1 = 'http://ip.myhostadmin.net/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62'}
proxies = {
  "http": "http://112.32.126.198:1081",
}
r = requests.get(url1, headers=headers,proxies=proxies)
print(r.text)
'''
url = ('http://www.tgy.com')
r = requests.get(url)
#print (r.text)
#print(r.raise_for_status())