import os
from bs4 import BeautifulSoup
# 数据目录：file_dir
file_dir = "txt/"
def file_name(file_dir):
    # root: 当前目录路径
    # dirs: 当前路径下所有子目录
    # files: 当前路径下所有非目录子文件
    for root, dirs, files in os.walk(file_dir):
        return files
# 所有文件名
files = file_name(file_dir)
# 遍历所有文件
result = []
for file in files:
    with open(file_dir+file, encoding="utf8") as f:
        # 读取文件内容-字符串
        content = f.read()
        # 利用html.parser将字符串转为BeautifulSoup对象
        soup = BeautifulSoup(content, 'html.parser')
        # 使用get_text()获取html中的文本，放进数组result中
        result.append(soup.get_text())
# 将结果写入cleaned.txt
with open("clean_html/cleaned.txt", "w", encoding="utf8") as f:
    f.writelines(result)



