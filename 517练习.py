import urllib.request as url_r
import re


def open_url(url):
    req = url_r.Request(url)
    req.add_header('Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62')
    page = url_r.urlopen(req)
    html = str(page.read())
    print(html)
    return html

    if __name__ == '__main__':
        url = 'http://www.66ip.cn/'
        html = open_url(url)
        get_image(html)