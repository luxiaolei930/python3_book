import os
#total的数值初始化为0
total = 0
file_dir = "./data/"
# 要搜索的关键字为“法院”
keyword = "法院"
result = []
def file_name(file_dir):
    # root: 当前目录路径
    # dirs: 当前路径下所有子目录
    # files: 当前路径下所有非目录子文件
    for root, dirs, files in os.walk(file_dir):
        return files
# 所有文件名
files = file_name(file_dir)
# 遍历所有文件名，统计字数
for file in files:
    with open("./data/"+file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        # find()函数的作用是从字符串中找出特定的关键词，如果关键词不存在，返回的值为-1。
        #如果返回的值不等于-1，则说明该关键词存在。
        #!=的意思为不等于
        # 如果存在该关键字（即返回的值不等于-1时），则在result中加入该段落
        if line.find(keyword)!=-1:
            result.append(line)
with open("./result.txt", "w", encoding="utf-8") as f:
    f.writelines((result))