# 利用nltk工具包进行分句和分词
# 导入nltk
import nltk
# 待分句、分词文本，使用\符号隔开目的是方便阅读。
text = "He was an old man who fished alone in a skiff in the Gulf Stream and he had gone eighty-four days now without taking a fish. In the first forty days a boy had been with him." \
       " But after forty days without a fish the boy’s parents had told him that the old man was now definitely and finally salao, which is the worst form of unlucky, and the boy had gone at their orders in another boat which caught three good fish the first week. " \
       "It made the boy sad to see the old man come in each day with his skiff empty and he always went down to help him carry either the coiled lines or the gaff and harpoon and the sail that was furled around the mast."
print("原始文本：")
print(text)
# 利用sent_tokenize()进行分句
sents = nltk.sent_tokenize(text)
print("输出分句结果：")
for i, sent in enumerate(sents):
    print("第"+str(i+1)+"句：", sent)
# 利用word_tokenize()进行对每个句子进行分词
words = [nltk.word_tokenize(sent) for sent in sents]
print("输出分词结果：")
for i, word in enumerate(words):
    print("第"+str(i+1)+"句：", word)


