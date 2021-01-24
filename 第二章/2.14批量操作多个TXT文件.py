#引入glob库（python的glob模块可以对文件夹下所有文件进行遍历）
import glob
#获取当前目录movies文件夹下的所有.txt文件，命名为target_files，数据形式为数组
target_files=glob.glob(pathname='./movies/*.txt')
#新建data数组用来存放读进来的所有文件数据
data = []
#使用for循环遍历target_files中的所有文件，将每个文件的数据存入data数组，“r”代表只读，编码方式为“utf-8”
#使用readlines()函数一次性读取文件中的所有行，并返回列表
#使用extend()函数扩充数组
for file_ in target_files:
    with open(file_, "r", encoding='utf-8') as f:
        lines = f.readlines()
        data.extend(lines)
#将data（已存储文件夹下所有语料）写入文件all.txt，“w”代表只写
with open("all.txt", "w", encoding="utf-8") as f:
    f.writelines(data)
