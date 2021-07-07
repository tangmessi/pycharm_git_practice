import json
import requests
from tkinter import *
import re
def input_msg():
    msg = input("输入：")
    return msg
def dudu():
    msg_input = str(v1.get())
    url = "http://openapi.tuling123.com/openapi/api/v2"#图灵api
    payload = {
        "perception": {
            "inputText": {
                "text": msg_input
                },
        },
        "userInfo": {
            "apiKey": "7342f844b4e64db3918d0f4c0ba03c88",#嘟嘟，api
            #"apiKey": "629241794bb947ac80775760256094af",#糖糖
            "userId": "664068464"
            }
    }
    html_return= requests.post(url, data=json.dumps(payload))#post信息到api
    p = r'"values":{"text":"([^"]+)'#正则表达式筛选
    answer = re.findall(p,html_return.text)[0]
    v2.set(answer)
    print(answer)

root = Tk()#用户操作界面
frame1 = Frame(root)
label1 = Label(frame1,text = "嘟嘟聊天器")
v1 = StringVar()
v2 = StringVar()
e2 = Entry(frame1,textvariable = v1,validate = "key",\
    ).grid(row=1, column=0)#输入框
Button(frame1,text="发送",command = dudu).grid(row=1, column=1)
e3 = Entry(frame1,textvariable = v2,state = "readonly",\
    ).grid(row=2, column=0)#输出框，不可变，可复制
frame1.pack(padx = 10,pady = 10)
label1.grid(row=0)
mainloop()
