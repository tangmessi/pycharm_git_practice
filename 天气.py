# 禁止转载  [url=https://www.52pojie.cn/thread-1423918-1-1.html]https://www.52pojie.cn/thread-1423918-1-1.html[/url]
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

global contents
contents = ''


# 北京
def sign():
    yburl = 'https://free-api.heweather.com/s6/weather/forecast'
    value = {
        'location': '北京',
        'key': '【和风天气的key】',
        'lang': 'zh'
    }
    ybreq = requests.get(yburl, params=value)
    ybjs = ybreq.json()

    # 返回api参数:
    # print(ybjs)

    for i in range(2):
        yb = ybjs['HeWeather6'][0]['daily_forecast']
        d1 = yb[i]['date'] + ' ' + yb[i]['cond_txt_d'] + ' ' + yb[i]['tmp_min'] + '—' + yb[i]['tmp_max'] + '℃' + ' ' + \
             yb[i]['wind_dir'] + ' ' + yb[i]['wind_sc'] + '级'
        # output(d1)
    # qq推送
    qqtalk = 'https://qmsg.zendee.cn/send/【qmsg的key】?msg=' + d1 + '&qq=【接收消息的qq号】'
    requests.get(qqtalk)


def main():
    sign()


def main_handler(event, context):
    return main()


if __name__ == '__main__':
    main()