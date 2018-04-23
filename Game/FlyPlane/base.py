import os

# -*- coding: utf-8 -*-

import os

def sub_file(file_dir):
    name = {}
    for root, dirs, files in os.walk(file_dir):
        # print(root)
        # print(dirs)
        # print(files)
        try:
            if root.find('\\')!=-1:
                files_name=root[root.find('\\')+1:]
                if files_name=='image' or files_name=='sound' or files_name=='font':
                    name[root[root.find('\\')+1:]]=files
        except Exception as why:
            print(why)
    return name

# 其中os.path.splitext()函数将路径拆分为文件名+扩展名

if __name__=="__main__":
    print(sub_file('.\\res'))