from tkinter import *
tk = Tk()
'''v = IntVar()#测试
c = Checkbutton(tk,text ="test",variable = v)
c.pack()
d = Label(tk,textvariable = v)
d.pack()
mainloop()'''
FOOTBALL= ['莱奥.梅西','C罗','小罗']
soccer=[]
for football in FOOTBALL:
    soccer.append(IntVar())
    print(soccer.append(IntVar()))
    b = Checkbutton(tk,text = football,variable = soccer[-1])
    b.pack(anchor = NW )#对齐方式 NEWS八个方位
mainloop()