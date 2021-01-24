import nltk

text = "strange lying saved discusses men builds"
print("原始文本：")
print(text)
# 词性标注之前先进行分词
tokens = nltk.word_tokenize(text)
print("词性标注结果：")
print(nltk.pos_tag(tokens))
