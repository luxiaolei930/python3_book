import json

json_array= [
    {"name": "xiaolu", "gender": "female", "age": "18"},
    {"name": "xiaohong", "gender": "male", "age": "20"},
    {"name": "xiaohan", "gender": "male", "age": "19"}
]
#需使用json.dumps()函数将json_array数组转换为json格式文本字符串json_str，再存储。
json_str=json.dumps(json_array)
#使用with open()函数打开一个文件，a表明使用读写的方式打开文件
with open('store.json', 'a') as file:
#将json_str中的内容写入store.json之中。
    file.write(json_str)
    