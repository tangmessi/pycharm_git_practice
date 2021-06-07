import re
str1 = "sdfgasdgvsd*& dfedf1234"
str2 = "afsdfawefAD$213441234"
str3 = "3412354123fwefA54"
str4 = "sadf4324sdfw"
p = r'^(?![0-9]+$)(?![A-Z]+$)(?![a-z]+$)[\w\W]{2,100}$'#必须含有至少两种
p1 = r'^(?![0-9A-Z]+$)(?![0-9a-z]+$)(?![A-z]+$)\
    (?![A-Z\W]+$)(?![a-z\W]+$)(?![0-9\W]+$)[\w\W]{2,100}$'#必须含有至少三种
imglist = re.match(p1,str4)
if imglist == None:
    print('密码强度不足')
else:
    print('密码强')