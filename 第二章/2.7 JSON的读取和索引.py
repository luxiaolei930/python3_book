import json
#使用“r+”以读写方式打开store.json文件
with open('store.json', 'r+') as file:
  #使用file.read()函数读取文件中的内容，并定义为json_str2字符串
    json_str2=file.read()
    #使用json.loads()函数将读取出来的json_str2字符串转换成JSON对象，并定义为json_array2
    json_array2 = json.loads(json_str2)
    #打印json_array2列表
    print(json_array2)
