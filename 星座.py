import easygui as g
import time

ticks = time.time()
KnowTime = time.localtime(time.time())
WeekTime = KnowTime[6] + 1
Time_body = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
Time_week = "星期%d" % WeekTime
Weeks = int(time.strftime("%u", time.localtime())) + 1
Time_week_num = "今天是%d年的第%d个星期" % (KnowTime[0], Weeks)
Time_day_num = "今年已经过了%d天" % KnowTime[7]

title1 = '我是可爱的小洛噢'
tit2 = '我输入好了'
image1 = 'C:\\19383\\good.gif'


def xingzuo(xz):
    g.msgbox(msg="你是可爱的" + xz + "座",
             title=title1, image='C:\\19383\\22.jpg')


g.msgbox(msg="你好我是你的星座小助理小洛，初次见面请多关照！\n" + Time_week_num + "\n" + Time_day_num,
         title=title1 + "," + Time_body + "   " + Time_week, ok_button='好的，我知道了，下一步', image=image1)
m_input = g.enterbox(title=title1 + "," + Time_body + Time_week,
                     msg="请告诉小洛你的出生月份，小洛会保密的哦:\n",
                     image='C:\\19383\\333.jpg')
while True:
    try:
        m = int(m_input)
        break
    except (RuntimeError, TypeError, NameError,ValueError):
        m_input = g.enterbox(title=title1 + "," + Time_body + Time_week,
                             msg="输入不正确\n"+"请再次告诉小洛你的出生月份，小洛会保密的哦:\n",
                             image='C:\\19383\\333.jpg')

d_input = g.enterbox(title=title1 + Time_body + "   " + Time_week + '(数字输入错误)',
                                 msg="现在请重新告诉小洛你的出生日期（1-31的数字），"
                                     "小洛同样会保密的哦:",
                                 image='C:\\19383\\22.jpg')
while True:
    try:
        d = int(d_input)
        break
    except (RuntimeError, TypeError, NameError,ValueError):
        d_input = g.enterbox(title=title1 + "," + Time_body + Time_week,
                             msg="输入不正确\n"+"请再次告诉小洛你的出生日期，小洛会保密的哦:\n",
                             image='C:\\19383\\333.jpg')







# 输入月份
"""
while True:
    if m_input.isdecimal():
        if 1 <= int(m_input) <= 12:
            break
        else:
            m_input = g.enterbox(title=title1 + "," + Time_body + "   " + Time_week + '(数字输入错误)',
                                 msg="请告诉小洛你的出生月份（1-12的数字），"
                                     "小洛会保密的哦:",
                                 image='C:\\19383\\333.jpg')
    else:
        m_input = g.enterbox(title=title1 + "," + Time_body + "   " + Time_week + '(字符输入错误)',
                             msg="请告诉小洛你的出生月份（1-12的数字），"
                                 "小洛会保密的哦:",
                             image='C:\\19383\\333.jpg')
m = int(m_input)
# 判断输入月份的正确性（是否为数字以及是否在1-12月里，最后把字符串换成整型）
d_input = g.enterbox(title=title1 + "," + Time_body + "   " + Time_week, msg="那么现在请告诉小洛你的出生日期，"
                                                                             "小洛同样会保密的哦:",
                     image='C:\\19383\\22.jpg')
while True:
    if d_input.isdecimal():
        if 1 <= int(d_input) <= 31:
            break
        else:
            d_input = g.enterbox(title=title1 + Time_body + "   " + Time_week + '(数字输入错误)',
                                 msg="现在请重新告诉小洛你的出生日期（1-31的数字），"
                                     "小洛同样会保密的哦:",
                                 image='C:\\19383\\22.jpg')
    else:
        d_input = g.enterbox(title=title1 + Time_body + '(字符输入错误)',
                             msg="现在请重新告诉小洛你的出生日期（1-31的数字），"
                                 "小洛同样会保密的哦:",
                             image='C:\\19383\\22.jpg')
d = int(d_input)
# 判断输入日期的正确性（是否为数字以及是否在1-31日里，最后把字符串换成整型）
"""
g.msgbox(title=title1 + Time_body + "   " + Time_week, msg="你的生日是：%d月%d日" % (m, d), image='C:\\19383\\333.jpg')
if (m == 1) and (d >= 20) or (m == 2) and (d <= 18):
    xingzuo('水瓶')
elif (m == 2) and (d >= 19) or (m == 3) and (d <= 20):
    xingzuo('双鱼')
elif (m == 3) and (d >= 21) or (m == 4) and (d <= 20):
    xingzuo('白羊')
elif (m == 4) and (d >= 21) or (m == 5) and (d <= 20):
    xingzuo('金牛')
elif (m == 5) and (d >= 21) or (m == 6) and (d <= 21):
    xingzuo('双子')
    g.msgbox("听说双子座和天秤座最配噢", image='C:\\19383\\55.jpg')
elif (m == 6) and (d >= 22) or (m == 7) and (d <= 22):
    xingzuo('巨蟹')
elif (m == 7) and (d >= 23) or (m == 8) and (d <= 22):
    xingzuo('狮子')
elif (m == 8) and (d >= 23) or (m == 9) and (d <= 22):
    xingzuo('处女')
elif (m == 9) and (d >= 23) or (m == 10) and (d <= 22):
    xingzuo('天枰')
    g.msgbox("听说天秤座和双子座最配噢", image='C:\\19383\\55.jpg')
elif (m == 10) and (d >= 23) or (m == 11) and (d <= 21):
    xingzuo('天蝎')
elif (m == 11) and (d >= 22) or (m == 12) and (d <= 21):
    xingzuo('射手')
elif (m == 12) and (d >= 22) or (m == 1) and (d <= 19):
    xingzuo('摩羯')
