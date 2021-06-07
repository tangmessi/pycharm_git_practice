'''
from tkinter import *
root = Tk()
LANGS = [
    ("Python",1),
    ("Java",2),
    ("PHP",3)
]
v = IntVar()
v.set(1)
for i , j in LANGS:
    b = Radiobutton(root,text = i,variable = v,value = j,indicatoron = False)
    #indicatoron = False设置为方格，True为圆圈X
    #b.pack(anchor = W)
    b.pack(fill = 'x')#横向填充
mainloop()
'''
from tkinter import *
root = Tk()
group = LabelFrame(root,text= '最好的编程语言是？',padx = 5,pady = 30)#里面小框
group.pack(padx = 5,pady = 5)#整个方框的大小
LANGS = [
    ("Python",1),
    ("Java",2),
    ("PHP",3)
]
v = IntVar()
v.set(1)
for i , j in LANGS:
    b = Radiobutton(group,text = i,variable = v,value = j,indicatoron = False)
    #indicatoron = False设置为方格，True为圆圈X
    #b.pack(anchor = W)
    b.pack(fill = 'x')#横向填充
mainloop()
