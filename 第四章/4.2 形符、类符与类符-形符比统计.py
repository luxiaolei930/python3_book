#引入nltk  
import nltk  
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
# word_tokenize()分词后存在列表tokens中  
# 利用set() 函数创建一个无序不重复元素集，定义为typetokens= []  
# 使用len()函数计算数量  
tokens = []  
for sent in sents:  
    tokens.extend(nltk.word_tokenize(sent))  
type = set(tokens)  
#形符/类符（TTR）:评估词汇密度，词汇密度对分析话语风格、文本难度等有意义。  
ttr = len(type)/len(tokens)  
print("类符数：", len(type))  
print("形符数：", len(tokens))  
print("类符/形符（TTR）:", str(ttr)) 