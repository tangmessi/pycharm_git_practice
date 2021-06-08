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

def calc():
    result = int(v1.get())+int(v2.get())
    v3.set(str(result))
  
  


Button(root,text="计算器",command = calc).grid(row=1, column=2)
mainloop()

'''
def compute(a):
    if a == 1:
        print("111")
        return 1
    elif a == 2:
        print("222")
        return 2
    elif a == 3:
        return 2
    elif a == 4:
        return 4
    else:
        pass


Checkbutton(root,text= "➕",variable = v4 ,command = compute(1)).grid(row=0, column=1)
Checkbutton(root,text= "➖",variable = v4 ,command = compute(2)).grid(row=1, column=1)
Checkbutton(root,text= "✖",variable = v4 ,command = compute(3)).grid(row=2, column=1)
Checkbutton(root,text= "➗",variable = v4 ,command = compute(4)).grid(row=3, column=1)

def calc(b):
    if b == 1:
        result = int(v1.get())+int(v2.get())
        v3.set(str(result))
    elif b == 2:
        result = int(v1.get())-int(v2.get())
        v3.set(str(result))
    elif b == 3:
        result = int(v1.get())*int(v2.get())
        v3.set(str(result))
    elif b == 4:
        result = int(v1.get())/int(v2.get())
        v3.set(str(result))
    else:
        pass

'''