import os
from pypinyin import lazy_pinyin

for file in os.listdir('.'):    #os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
    if file[-2: ] == 'py':
        continue   #过滤掉改名的.py文件
    if "bilibili_" in file:
        idx1 = file.index("t")
        idx2 = file.index(".")
        chs = file[idx1+3:idx2-1]
        name = file[:idx1-1] + "".join(lazy_pinyin(chs)) + ".png"
        os.rename(file, name)