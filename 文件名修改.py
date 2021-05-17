import os
import sys
import easygui as g
title1 = '小唐制作'
path =g.enterbox('输入你工作文件夹的存放路径（请直接去文件管理器复制）',title= title1) #r"C:\Users\Administrator\Desktop"  # 工作文件夹存放路径
filename1 = '一种专利文案'  # 你的模板名称，全部一致
filename2 =g.enterbox('输入你分配的案件名称',title= title1)  # 分配的案件名称
user_choice = g.choicebox(msg = '确定运行？',title =title1 ,choices=('yes','no'))
if user_choice == 'no':
    g.msgbox(msg = '按任意键退出',title =title1)
    sys.exit(0)
elif user_choice == 'yes':

    path1 = path + '\\' + filename1
    path2 = path + '\\' + filename2
    path2_1 = path2 + '\\' + filename1
    path2_2 = path2 + '\\' + filename2
    path2_2_1 = path2_2 + '\\' + filename1
    path2_2_2 = path2_2 + '\\' + filename2
    os.rename(path1, path2)  # 重命名第一层文件夹

    os.rename(path2_1, path2_2)  # 重命名第二层文件夹

    os.rename(path2_2_1 + '————说明书附图.pdf', path2_2_2 + '————说明书附图.pdf')

    os.rename(path2_2_1 + '————摘要附图.pdf', path2_2_2 + '————摘要附图.pdf')  # 重命名两个pdf文件

    os.rename(path2 + '\\' + '图' + '\\' + filename1 + '.spolt', path2 + '\\' + '图' + '\\' + filename2 + '.spolt')
    # 重命名空的sw文件，用于初始保存

    os.rename(path2 + '\\' + filename1 + '.docx', path2 + '\\' + filename2 + '.docx')  # 重命名模板主文件夹里的初始word文件
    g.msgbox(msg='运行完成', title=title1)



