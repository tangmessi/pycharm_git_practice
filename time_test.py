import time  # 引入time模块

ticks = time.time()
print("当前时间戳为:", ticks)
KnowTime=time.localtime(time.time())
WeekTime = KnowTime[6] + 1
print(time.strftime("现在是北京时间%Y-%m-%d %H:%M:%S",time.localtime()))
print("今天是星期%d"%WeekTime)
Weeks = int(time.strftime("%u",time.localtime())) + 1
print("今天是%d第%d个星期"%(KnowTime[0],Weeks))
print("今年已经过了%d天"%KnowTime[7])
print("今天是和小小落同学在一起的1032天，今天又比前一天更喜欢她了呢！")

#stamp=time.mktime(time.strptime('2016-11-24 14:00:21', '%Y-%m-%d %H:%M:%S'))
#print(int(stamp))