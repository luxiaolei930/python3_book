# 导入csv库
import csv
# 新建列表data，用于存放csv内容
data = []
# 打开csv文件
with open("test.csv") as f:
    # 调用csv的reader（）方法，返回一个可迭代的对象
    f_csv = csv.reader(f)
    # for循环遍历f_csv中的每个元素，添加到data列表中
    for row in f_csv:
        data.append(row)
# 打印data
print(data)