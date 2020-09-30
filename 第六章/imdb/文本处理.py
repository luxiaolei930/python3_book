# 导入json库
import json
import nltk
from nltk import FreqDist
from nltk.tokenize import RegexpTokenizer


tokenizer = RegexpTokenizer(r'w+')
with open("./reviews.json", encoding="utf8") as f:
    data = json.load(f)
# 获取所有评论内容
reviews = [i["review"] for i in data]
########################### 去除停用词与标点符号 ##############################
# 打开英文停用词表en.json文件
with open("./en.json", encoding="utf-8") as f:
    stopwords = json.load(f)
# 英文标点符号
puncation = [".", ",", "?", "'", "/", "\\", "\"", ">", "<", "=", "-", "(", ")", "*", "&", "^", "#", "@", "!", " ``"]
stopwords.extend(puncation)
# 利用sent_tokenize()进行分句
result = []
for review in reviews:
    review_docs = nltk.sent_tokenize(review)
    # 存放去除停用词后的句子
    de_sw_result = []
    for review_doc in review_docs:
        review_tokens = [word.lower() for word in nltk.word_tokenize(review_doc) if word.lower() not in stopwords]
        # 去除停用词
        de_sw_result.append(review_tokens)
    result.append(de_sw_result)

########################### 词频统计 ##############################
# flatten()将多维列表转为一维列表
def flatten(a):
    if not isinstance(a, (list, )):
        return [a]
    else:
        b = []
        for item in a:
            b += flatten(item)
    return b

flatten_result = flatten(result)

text=nltk.text.Text(flatten_result)
fd = FreqDist(text)
fd.plot(20)

########################### 绘制词云图 ##############################
# 导入wordcloud库
import wordcloud
# 初始化WordCloud对象
w = wordcloud.WordCloud()
# 将列表转化为字符串
text_str = " ".join(flatten_result)
# 向对象w中加载text_str
w.generate(text_str)
# 导出png文件
w.to_file("wc.png")
print("已导出词云wc.png")
########################### 词性标注 ##############################
print(nltk.pos_tag(flatten_result))
########################### 关键字检索 ##############################
print(text.concordance("prison", width=100))
########################### 统计每个评论的形符类符比 ##############################
def cal_ttr(words):
    type = set(words)
    ttr = len(type)/len(words)*100
    return ttr
ttr_list = []
for review in reviews:
    word_token = nltk.word_tokenize(review)
    ttr_list.append(cal_ttr(word_token))
print(ttr_list)