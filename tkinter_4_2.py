'''
from tkinter import *
root = Tk()
group1 = LabelFrame(root,text = '作品',padx = 5,pady = 5)
group1.pack(padx = 5,pady = 5)
group2 = LabelFrame(root,text = '作品',padx = 5,pady = 5)
group2.pack(padx = 5,pady = 5)
enter1 = Entry(group1)
enter1.insert(0, "请输入姓名")
enter2 = Entry(group2)
enter2.insert(0, "请输入学号")
button1 = Button(root,text = '获取信息')
button2 = Button(root,text = '退出')
button1.pack(side = LEFT)
button2.pack(side = RIGHT)

enter1.pack()
enter2.pack()

mainloop()
#自己先写的
'''

'''#初始版本
from tkinter import *

root = Tk()  # 使用grid管理位置


Label(root, text="球队:").grid(row=0, column=0)  # row行
Label(root, text="代表球员:").grid(row=1, column=0)

enter1 = Entry(root)
enter2 = Entry(root)
enter1.grid(row=0, column=1, padx=5, pady=5)
enter2.grid(row=1, column=1, padx=5, pady=5)


def show():
    print('球队:%s' % enter1.get())  # 获取输入框字符用.get()方法
    print('代表球员:%s' % enter2.get())  # %s格式化字符串


button1 = Button(root, text='获取信息', width=10, command=show)  # 这里调用方法不用加（）
button2 = Button(root, text='退出', width=10, command=root.quit)
button1.grid(row=2, column=0, padx=5, pady=5, sticky=W)
button2.grid(row=2, column=1, padx=5, pady=5, sticky=E)
mainloop()
'''


#密码带*号改进版
from tkinter import *

root = Tk()  # 使用grid管理位置


Label(root, text="账号:").grid(row=0, column=0)  # row行
Label(root, text="密码：").grid(row=1, column=0)
v1 = StringVar()
v2 = StringVar()

enter1 = Entry(root,textvariable =v1)
enter2 = Entry(root,textvariable =v2,show ="**")#show表示用字符替代你的输入
enter1.grid(row=0, column=1, padx=5, pady=5)
enter2.grid(row=1, column=1, padx=5, pady=5)


def show():
    print('账号:%s' % enter1.get())  # 获取输入框字符用.get()方法
    print('密码:%s' % enter2.get())  # %s格式化字符串


button1 = Button(root, text='获取信息', width=10, command=show)  # 这里调用方法不用加（）
button2 = Button(root, text='退出', width=10, command=root.quit)
button1.grid(row=2, column=0, padx=5, pady=5, sticky=W)
button2.grid(row=2, column=1, padx=5, pady=5, sticky=E)
mainloop()