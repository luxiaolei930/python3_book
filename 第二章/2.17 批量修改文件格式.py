import os
# 数据目录：file_dir
file_dir = "./data/"
def file_name(file_dir):
    # root: 当前目录路径
    # dirs: 当前路径下所有子目录
    # files: 当前路径下所有非目录子文件
    # 使用os.walk()游走,遍历数据目录file_dir
    for root, dirs, files in os.walk(file_dir):
        return files
# 所有文件名
files = file_name(file_dir)
# 遍历所有文件名，使用rename()修改文件名
for file in files:
    os.rename(file_dir+file, file_dir+file.split(".")[0]+".txt")
