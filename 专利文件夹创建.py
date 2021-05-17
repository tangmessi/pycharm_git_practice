import os, sys,shutil#创建专利文案需要的文件夹

path = r"C:\Users\Administrator\Desktop"
filename = '一种专利文案'

print("当前工作目录为 %s" % os.getcwd())# 查看当前工作目录
os.makedirs('C:\\Users\\Administrator\\Desktop\\'+filename+'\\'+filename )
os.makedirs('C:\\Users\\Administrator\\Desktop\\'+filename+'\\'+'图' )
file_tem = open('C:\\Users\\Administrator\\Desktop\\'+filename+'\\'+filename+'\\'+filename+'————说明书附图.pdf','wb')
file_tem.close()
file_tem = open('C:\\Users\\Administrator\\Desktop\\'+filename+'\\'+filename+'\\'+filename+'————摘要附图.pdf','wb')
file_tem.close()
#os.mknod('C:\\Users\\Administrator\\Desktop\\'+filename+'\\'+filename+'\\'+filename+'————说明书附图.pdf' )
path1 = "C:\\Users\\Administrator\\Desktop\\"+filename


os.chdir(path1)# 修改当前工作目录


print("目录为: %s" % os.listdir(os.getcwd()))# 查看修改后的工作目录
# os.renames('666','aaa')
