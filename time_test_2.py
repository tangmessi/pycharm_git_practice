import time
from tkinter import *


def get_time():
    NowTimeYear = time.strftime("%Y", time.localtime())
    print(NowTimeYear)#得到今年年份
    time_begin = NowTimeYear+"-01-01 00:00:00"
    time_end = str(int(NowTimeYear)+1)+"-01-01 00:00:00"
    print(time_end)
    time_begin_str = time.mktime(time.strptime(time_begin, '%Y-%m-%d %H:%M:%S'))#转化时间戳
    time_end_str = time.mktime(time.strptime(time_end, '%Y-%m-%d %H:%M:%S'))#转化时间戳
    time_now_str = time.time()
    time_span_str = time_end_str - time_now_str  # 距离下一年的时间戳差
    last_second = time_span_str#今年剩余时间（S）
    sum_time_day = (time_end_str-time_begin_str)/3600/24#今年时间天数
    last_time_day = last_second/3600/24#今年剩余天数
    perent_time = last_time_day/sum_time_day*100#百分数
    print('今年一共有'+str(sum_time_day)+'天')
    print('已经过去了%.3f%%'%(100-perent_time))#%表示过去时间
    print("还剩%.1f天"%last_time_day)
    return last_second
get_time()







