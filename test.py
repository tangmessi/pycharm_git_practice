from tkinter import*
import time
root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
frame1.pack()
var = StringVar()
for i in range(2):
    a = str(i)
    print(a)
    var.set(a)
    textLabel1 = Label(frame1, textvariable=var,
                      justify=LEFT,
                      compound=CENTER,
                      fg='blue')
    textLabel1.pack(side=LEFT)
    time.sleep(0.1)

root.mainloop()
