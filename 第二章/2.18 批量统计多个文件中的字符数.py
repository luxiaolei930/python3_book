import os
#total的初始值为0
total = 0
file_dir = "./data/"
def file_name(file_dir):
    # root: 当前目录路径
    # dirs: 当前路径下所有子目录
    # files: 当前路径下所有非目录子文件
    for root, dirs, files in os.walk(file_dir):
        return files
# 所有文件名
files = file_name(file_dir)
# 遍历所有文件名，使用len()统计字数
for file in files:
    with open("./data/"+file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        char_num = len(line.strip())
        #total+=char_num的意思为total=total+char_num
        total+=char_num
print(total)