import urllib.request as url_r
import re
import random
import easygui as g



def open_url_ip(url):
    req = url_r.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62')
    page = url_r.urlopen(req)
    html = str(page.read())
    print(html)
    return html


def get_image(html):
    p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
    #筛选ip地址，有问题，（）会变成子组,在（后加上?:即可修复
    iplist = re.findall(p, html)
    #print (iplist)
    return iplist
    '''for each in iplist:
        print(each)'''

def choice_ip(iplist):
    a = random.choice(iplist)
    print(a)
    return a

def show_ip(ip):
    url1 = 'http://45.32.164.128/ip.php'
    url2 = 'https://www.whatismyip.com/'
    url = 'http://ip.myhostadmin.net/'
    proxy_support = url_r.ProxyHandler({'http': '66.70.176.30:8888'})

    opener = url_r.build_opener(proxy_support)
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62')]
    response = url_r.urlopen(url)
    html1 = response.read().decode('utf_8')
    # html = json.loads(html1)
    print(html1)
    return html1


if __name__ == '__main__':
    url = 'https://www.89ip.cn/'
    html = open_url_ip(url)
    iplist = get_image(html)
    ip = choice_ip(iplist)
    g.msgbox(show_ip(ip))


