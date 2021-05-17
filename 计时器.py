import self as self

import time

""""class MyTime():
    def __repr__(self):
        try:
            #print("开始时间是%d" % self.Time_number_start)
            #print("结束时间是%d" % self.Time_number_stop)

            return "一共用时：%d秒"%self.Time_jiange
            #print("一共用时%d秒" % self.Time_jiange)
        except:
            return ("请开始开始计时")

    def start(self):
        print("计时开始：\n")
        self.Time_number_start = time.time()
        print("时间是%d" % self.Time_number_start)

    def stop(self):
        self.Time_number_stop = time.time()
        try:
            print("计时停止")
            self.Time_jiange = self.Time_number_stop - self.Time_number_start
        except:
            print("请先调用start（）开始计时")
            del self.Time_number_stop

    #def __init__(self):
        #print("计时未开始")

    def __add__(self, other):
        return (self.Time_jiange+other.Time_jiange)


b = MyTime()
# print(b)
b.start()
b.stop()
t = MyTime()
t.start()
t.stop()
t+b
"""


class Rectangle:
    def __init__(self,width=2,length = 3):
        self.width = width
        self.length = length

    def __getattribute__(self, item):
        print("查找属性")
        return super().__getattribute__(item)

    def __getattr__(self, name):
        print("被访问属性")

    def __setattr__(self, name, value):
        if name == "square":
            self.width = value
            self.length = value
        super().__setattr__(name, value)

    def show(self):
        print(":%d"%int(self.width))

    def GetArea(self):
        return self.width*self.length


a = Rectangle()
#a.x
#a.square=5
#a.square
print(a.length)
print(a.width)
print(a.GetArea())
a.width=10
a.length=5
print(a.length)
print(a.width)
print(a.weight)
print(a.GetArea())