from tkinter import *

root = Tk()  # 计算器
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
def test(content):
    return content.isdigit()

testCMD = root.register(test)
e1 = Entry(root,textvariable = v1,validate = "key",\
    validatecommand = (testCMD,"%P")).grid(row=0, column=0)

#Label(root,text = "+").grid(row=0, column=1)

e2 = Entry(root,textvariable = v2,validate = "key",\
    validatecommand = (testCMD,"%P")).grid(row=0, column=2)

Label(root,text = "=").grid(row=0, column=3)

e3 = Entry(root,textvariable = v3,state = "readonly",\
    validatecommand = (testCMD,"%P")).grid(row=0, column=4)

def calc1():
    result = int(v1.get())+int(v2.get())
    v3.set(str(result))
def calc2():
    result = int(v1.get())-int(v2.get())
    v3.set(str(result))
def calc3():
    result = int(v1.get())*int(v2.get())
    v3.set(str(result))
def calc4():
    result = int(v1.get())/int(v2.get())
    v3.set(str(result))
Button(root,text="➕",command = calc1).grid(row=0, column=1)
Button(root,text="➖",command = calc2).grid(row=1, column=1)
Button(root,text="✖",command = calc3).grid(row=2, column=1)
Button(root,text="➗",command = calc4).grid(row=3, column=1)
mainloop()
#自己写的，输入数字后再点击计算方法