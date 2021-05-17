import urllib.request as url_r  # 爬网站
import requests
import json
import re


def open_url(url):
    req = url_r.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62')
    page = url_r.urlopen(req)
    html = str(page.read())
    #print(html)
    return html


#open_url('https://tieba.baidu.com/p/6131348235')

def get_image(html):
    p = r'a href="[^"]+"'
    p_wyyyy = r'song\?id=[^"]+"'
    p_qq = r'img src="[^"]+jpg"'
    p1 = r'href = "[^"]+"'
    imglist = re.findall(p_wyyyy,html)
    for each in imglist:
        print(each)
    '''for each in imglist:
        filename = each.split('/')[-1]
        url_r.urlretrieve(each,filename,None)'''


if __name__ == '__main__':
    url = 'http://music.163.com/playlist?id=2819176995'
    url2 = 'https://y.qq.com/n/ryqq/player'
    html = open_url(url)
    get_image(html)