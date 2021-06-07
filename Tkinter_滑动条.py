import tkinter as tk
master = tk.Tk()#生成主窗口
master.title('小洛')
thelabel = tk.Label(master,text='hello world')
thelabel.pack()

scroll = tk.Scrollbar(master)#生成滚动条
scroll.pack(side='right',fill='y')#滚动条在右

LB = tk.Listbox(master, yscrollcommand = scroll.set)#,height = 5)
for item in range(1,200
                  ):
    LB.insert('end',item)
LB.pack(side='left', fill='both')#LB在左
scroll.config(command=LB.yview)
thebutton = tk.Button(master,text="删除",command = lambda x=LB:x.delete(tk.ACTIVE))
thebutton.pack()
tk.mainloop()#c窗口一直出现
