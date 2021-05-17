import urllib.request as url_r
import re


def open_url(url):
    req = url_r.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62')
    page = url_r.urlopen(req)
    html = str(page.read())
    print(html)
    return html


def get_image(html):
    p = r'(([0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}([0,1]?\d?\d|2[0-4]\d|25[0-5]'
    imglist = re.findall(p, html)
    for each in imglist:
        print(each)


if __name__ == '__main__':
    url = 'https://www.kuaidaili.com/free/'
    html = open_url(url)
    get_image(html)
