import nltk
#原始文本
text = "He was an old man who fished alone in a skiff in the Gulf Stream and he had gone eighty-four days now without taking a fish."
print("原始文本：")
print(text)
print("将文本全部转为大写字母：")
#使用text.upper()将文本全部转为大写字母
upper_text = text.upper()
print(upper_text)
print("将文本全部转为小写字母：")
#使用text.lower()将文本全部转为小写字母
lower_text = text.lower()
print(lower_text)
print("将文本每个单词首字母转为大写字母：")
#使用text.title()将文本每个单词首字母转为大写字母
title_text = text.title()
print(title_text)

#统计大小写词频
#分词
tokens = nltk.word_tokenize(text)
# 初始化大、小写字母的数量upper_num、lower_num为0
upper_num, lower_num = 0, 0
# 遍历句子中的每个单词
for token in tokens:
    # token[0]代表单词的首字母,isupper()判断首字母是否为大写
    # 如果是大写，则upper_num加1；否则lower_num加1。
    if token[0].isupper():
        upper_num+=1
    else:
        lower_num+=1
print("原始文本中首字母大写字母的单词个数：", upper_num)
print("原始文本中首字母小写字母的单词个数：", lower_num)
