from tkinter import *
root = Tk()
v = IntVar()
#只能选中一个
Radiobutton(root,text= "one",variable = v ,value = 1).pack(anchor = W)
Radiobutton(root,text= "two",variable = v ,value = 2).pack(anchor = E)
Radiobutton(root,text= "three",variable = v ,value = 3).pack(anchor = W)
mainloop()