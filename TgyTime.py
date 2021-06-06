import time

NowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
NowTimeYear = time.strftime("%Y", time.localtime())
time_begin = NowTimeYear + "-01-01 00:00:00"
time_end = str(int(NowTimeYear) + 1) + "-01-01 00:00:00"
time_begin_str = time.mktime(time.strptime(time_begin, '%Y-%m-%d %H:%M:%S'))  # 转化时间戳
time_end_str = time.mktime(time.strptime(time_end, '%Y-%m-%d %H:%M:%S'))  # 转化时间戳
time_now_str = time.time()
time_span_str = time_end_str - time_now_str  # 距离下一年的时间戳差
last_second = time_span_str  # 今年剩余时间（S）
sum_time_day = (time_end_str - time_begin_str) / 3600 / 24  # 今年时间天数
last_time_day = last_second / 3600 / 24  # 今年剩余天数
perent_time = last_time_day / sum_time_day * 100  # 今年剩余百分数


def nowTime():
    print(NowTime)


# 今年是否闰年
def IsLeapYear():
    if sum_time_day == 365:
        return False
    elif sum_time_day == 366:
        return True


def IsLeapYearShow():
    if sum_time_day == 365:
        print("今年不是闰年")
    elif sum_time_day == 366:
        print("今年是闰年")


# 今年总共时间
def TotalDay():
    return sum_time_day


def TotalDayShow():
    print('今年一共有%d天' % sum_time_day)


# 今年过去百分比
def PastDay():
    return 100 - perent_time


def PastDayShow():
    print('今年已经过去了%.3f%%' % (100 - perent_time))


'''
IsLeapYearShow()
nowTime()
TotalDayShow()
PastDayShow()
'''
