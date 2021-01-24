import nltk
from nltk import FreqDist
text = "He was an old man who fished alone in a skiff in the Gulf Stream and he had gone eighty-four days now without taking a fish. " \
       "In the first forty days a boy had been with him. But after forty days without a fish the boy’s parents had told him that the " \
       "old man was now definitely and finally salao, which is the worst form of unlucky, and the boy had gone at their orders in another" \
       " boat which caught three good fish the first week. It made the boy sad to see the old man come in each day with his skiff empty and " \
       "he always went down to help him carry either the coiled lines or the gaff and harpoon and the sail that was furled around the mast. " \
       "The sail was patched with flour sacks and, furled, it looked like the flag of permanent defeat." \
       "The old man was thin and gaunt with deep wrinkles in the back of his neck. " \
       "The brown blotches of the benevolent skin cancer the sun brings from its reflection on the tropic sea were on his cheeks." \
       "The blotches ran well down the sides of his face and his hands had the deep-creased scars from handling heavy fish on the cords. " \
       "But none of these scars were fresh. They were as old as erosions in a fishless desert."
# 利用nltk.sent_tokenize()分句
sents = nltk.sent_tokenize(text)
# word_tokenize()分词后存在列表words中
words = []
for sent in sents:
    words.extend(nltk.word_tokenize(sent))
# 将words列表转换成Text对象
# 使用FreqDist()统计数组当中单词出现的次数，命名为fd
text=nltk.text.Text(words)
fd = FreqDist(text)
# 获取长度超过3，使用频次超过2的单词
result = [w for w in set(words) if len(w)>3 and fd[w]>2]
print("长度超过3，使用频次超过2的单词:", result)
# 将前10个出现频率最高的单词依据出现频率绘制成图
fd.plot(10)
