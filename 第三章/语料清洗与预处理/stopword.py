import json
#打开英文停用词表en.json文件
with open("./en.json", encoding="utf-8") as f:
    stopwords = json.load(f)

# 待处理文本
source_text = "For the purposes of accurately applying the extinctive prescription rules in the General Provisions..."
source_text_list = source_text.split(" ")
#去除停用词后
target_text = [word for word in source_text_list if word not in stopwords]
print("去除停用词前：", source_text)
print("去除停用词后：", " ".join(target_text)) #" ".join 数组转字符串