import os

for file in os.listdir('.'):    #os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
    if file[-2: ] == 'py':
        continue   #过滤掉改名的.py文件
    name = "bilibili_"+file
    os.rename(file, name)