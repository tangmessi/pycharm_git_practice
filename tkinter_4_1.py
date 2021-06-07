from tkinter import *
root = Tk()
group = LabelFrame(root,text = '小洛',padx = 5,pady = 5)
group.pack(padx = 5,pady = 5)
enter = Entry(group)
enter.delete(0,END)
enter.insert(0, "请输入...")
enter.pack()

mainloop()