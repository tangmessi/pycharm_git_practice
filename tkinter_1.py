import tkinter as tk
'''
#第一次尝试
master = tk.Tk()
master.title('tang demo')
thelabel = tk.Label(master,text='hello world')
thelabel.pack()
master.mainloop()
'''
class APP:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack(side = tk.RIGHT,padx = 10 ,pady = 10)
        self.nihao = tk.Button(frame,text = '你好',bg = 'green',fg = 'blue',command = self.say_hi)
        #fg前景色，bg背景色
        self.nihao.pack()
    def say_hi(self):
        print("大家好")


root = tk.Tk()
app = APP(root)
root.mainloop()