import os
import shutil
def copy_file():
    source_path = os.path.abspath(r'C:\Users\Administrator\Desktop\一种WHAT')
    target_path = os.path.abspath(r'E:\唐国毅\专利撰写\ing\一种WHAT')

    '''if not os.path.exists(target_path):
        # 如果目标路径不存在原文件夹的话就创建
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree(target_path)'''
    shutil.copytree(source_path, target_path)
copy_file()
