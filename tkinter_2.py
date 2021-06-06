from tkinter import *


def callback():
    var.set("这是按钮背后的消息")


root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('这是tkinter的第二节课')

photo = PhotoImage(file=r'C:\Users\Administrator\Pictures\1.gif')
textLabel = Label(frame1, textvariable=var,
                  justify=LEFT,
                  compound=CENTER,
                  fg='blue')
textLabel.pack(side=LEFT)

imageLabel = Label(frame1, image=photo)
imageLabel.pack(side=RIGHT)

#var.set("666")
theButton = Button(frame2,
                   text = "这是按钮上的信息",
                   command = callback)
theButton.pack()
frame1.pack(padx = 100,pady = 100)
frame2.pack(padx = 10,pady = 10)

mainloop()
