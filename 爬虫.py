import urllib.request as url_r  # 爬网站
import urllib.parse
import json

"""q = url_r.urlopen("http://www.fishc.com")
a1 = q.read()
a2 = a1.decode("utf-8")
print(a2)"""  # 访问网站
'''url_weibo = 'https://weibo.com/aj/like/status?ajwvr=6&object_ids=1042018%3A85cfc90564066d465d68669b97cc5094%2C1042018' \
            '%3Af588638ba9d0c45151a22ce44e115305&_t=0&__rnd=1619897351543 '
url_cat = "http://placekitten.com/g/600/600"
url_91 = "http://www.91porn.com"
url_music = 'http://music.163.com/song/media/outer/url?id=436514312.mp3'
response = url_r.urlopen(url_music)
cat_imge = response.read()
# str_file = "D:\\python\\photo\\cat500*601.jpg"
# print(str_file)
file = open('d:/python/photo/cat101.mp3', 'wb')
file.write(cat_imge)
input("完成:")'''  # 下载图片

import urllib.request as url_r  # 有道翻译
import urllib.parse
import json
import easygui as g
import tkinter
import random

tkinter.Tk

'''def translation():
    title1 = "唐唐翻译器"
    while True:
        a = g.enterbox("请输入要翻译的内容（输入q退出）：", title=title1)
        if a == 'q':
            g.msgbox('唐唐翻译器现在退出', title=title1)
            break
        else:
            url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
            data = {}
            data['i'] = a
            data['from'] = 'AUTO'
            data['to'] = 'AUTO'
            data['smartresult'] = 'dict'
            data['client'] = 'fanyideskweb'
            data['doctype'] = 'json'
            data['version'] = '2.1'
            data['keyfrom'] = 'fanyi.web'
            data['action'] = 'FY_BY_REALTlME'
            data['typoResult'] = 'false'
            data = urllib.parse.urlencode(data).encode('utf-8')
            response = url_r.urlopen(url, data)
            cat_imge = response.read().decode('utf-8')
            print(type(cat_imge))
            resoult = json.loads(cat_imge)['translateResult'][0][0]['tgt']
            g.msgbox(resoult, title=title1)


translation()'''  # 爬有道翻译

url = 'http://45.32.164.128/ip.php'
iplist = ['123.253.36.99:8080'] #'114.233.171.250:8009','49.85.188.222:8017', '36.56.101.120:9999']
proxy_support = url_r.ProxyHandler({'http':'123.253.36.99:8080'})#random.choice(iplist)})
opener = url_r.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                    '(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51')]
url_r.install_opener(opener)
response = url_r.urlopen(url)
html1 = response.read().decode('utf_8')
# html = json.loads(html1)
print(html1)
