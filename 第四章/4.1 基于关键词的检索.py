# 导入nltk工具包
import nltk
# 原始文本
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
#利用word_tokenize()分词后存入列表words
words = []
for sent in sents:
    words.extend(nltk.word_tokenize(sent))
# 将words列表转换成Text对象
text_nltk=nltk.text.Text(words)
# 利用text_nltk.concordance()显示单词“Gulf”的上下文
# 利用text_nltk.similar()显示Gulf的相似词
# 利用text_nltk.count()统计单词出现次数
# 利用text_nltk.dispersion_plot()绘制words文档中出现的位置图
print("单词“Gulf”的上下文：")
print(text_nltk.concordance("Gulf", width=50))
print("显示Gulf的相似词：", text_nltk.similar("Gulf"))
print("统计单词出现次数（fish）：", text_nltk.count("fish"))
print("绘制words中文档中出现的位置图")
text_nltk.dispersion_plot(["man", "fish", "sun"])
