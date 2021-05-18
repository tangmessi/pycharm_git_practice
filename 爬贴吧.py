import urllib.request as url_r  # 爬网站
import requests
import re


def open_url(url):
    req = url_r.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51')
    page = url_r.urlopen(req)
    html = page.read().decode('utf-8')
    print(html)
    return html


#open_url('https://tieba.baidu.com/p/6131348235')

def get_image(html):
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)'
    imglist = re.findall(p,html)
    for each in imglist:
        print(each)
    '''for each in imglist:
        filename = each.split('/')[-1]
        url_r.urlretrieve(each,filename,None)'''


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/6131348235'
    html = open_url(url1)
    get_image(html)
