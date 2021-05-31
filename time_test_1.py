import time as tm
import easygui as g
#birth_time = "1997-03-20"#出生时间
birth_time = str(g.enterbox(title = '小洛制作', msg = "输入你的生日(如1949-10-01)"))
#print(type(birth_time))
birth_time_str = tm.mktime(tm.strptime(birth_time,'%Y-%m-%d'))#把出生时间转化为时间戳
now_time =tm.strftime("%Y-%m-%d")#把时间元祖变成0000—00-00格式
now_time_str = tm.mktime(tm.strptime(now_time,'%Y-%m-%d'))#获取现在的时间戳
time_span_str = now_time_str - birth_time_str#时间戳做差
time_year = time_span_str / (31536000+8*3600)#用时间戳的差除以一年的秒数，后面的为闰年补偿
time_day = time_span_str / (3600*24)
'''
print(birth_time)
print(now_time)
print(birth_time_str)
print(now_time_str)#测试代码
'''
print ("您已经%f岁了" % time_year)
print ("您已经在这世界上呼吸了%d天的空气了" % time_day)