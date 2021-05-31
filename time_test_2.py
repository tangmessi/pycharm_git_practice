import time
from tkinter import *

time_begin = "2021-01-01 00:00:00"
time_end = "2022-01-01 00:00:00"
time_begin_str = time.mktime(time.strptime(time_begin,'%Y-%m-%d %H:%M:%S'))
time_end_str = time.mktime(time.strptime(time_end,'%Y-%m-%d %H:%M:%S'))
time_now_str = time.time()
time_span_str = time_end_str-time_now_str#距离下一年的时间戳差
a = time_span_str
print(a)


#def refresh_data(self):

#    self.after(10000, self.refresh_data)
def callback():
    var.set(a)
    root.after(10, callback)


root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('这是tkinter的第二节课')
textLabel = Label(frame1, textvariable=var,
                  justify=LEFT,
                  compound=CENTER,
                  fg='black')
textLabel.pack(side=LEFT)

imageLabel = Label(frame1)
imageLabel.pack(side=RIGHT)

theButton = Button(frame2,
                   text="这是按钮后的信息",
                   command=callback)
theButton.pack()
frame1.pack(padx=100, pady=100)
frame2.pack(padx=10, pady=10)
mainloop()


