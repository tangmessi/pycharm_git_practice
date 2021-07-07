import json
import requests
from tkinter import *
import re
def input_msg():
    msg = input("输入：")
    return msg
def dudu(msg_input):
    url = "http://openapi.tuling123.com/openapi/api/v2"
    payload = {
        "perception": {
            "inputText": {
                "text": msg_input
                },
        },
        "userInfo": {
            "apiKey": "7342f844b4e64db3918d0f4c0ba03c88",
            "userId": "664068464"
            }
    }
    html_return= requests.post(url, data=json.dumps(payload))
    p = r'"values":{"text":"([^"]+)'
    answer = re.findall(p,html_return.text)[0]
    print(answer)
