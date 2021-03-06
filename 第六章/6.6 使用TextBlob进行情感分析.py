# 引入textblob工具包
from textblob import TextBlob
import json
# 读取影评数据
with open("./reviews.json", encoding="utf8") as f:  
    reviews = json.load(f)
# 去除没有评分的评论
data = [i for i in reviews if i["rate"] is not None] 
# 定义情感分析函数
def analyze_by_textblob(text):
    tb = TextBlob(text)
    polarity = tb.sentiment.polarity
    # 情感极性范围为[-1,1]，设定>0为正面情感
    if polarity>0:
        return "positive"
    else:
        return "negative"
# sentiments列表，用于存放所有的情感分析结果
sentiments = []
# 遍历影评列表进行情感分类
for i in data: 
    # 获取影评中的评论review字段
    test_text = i["review"]
    # 情感分析
    sent = analyze_by_textblob(test_text)
    # 将情感分析结果加入到sentiments列表中
    sentiments.append(sent)
    
# 以用户的评分为标签，>=5的为正面评价，<5的为负面评价
rates = [i["rate"] for i in data]
labels = []
for rate in rates:
    if int(rate)<5:
        labels.append("negative")
    else:
        labels.append("positive")
# 根据模型预测结果，使用sklearn计算各项指标
from sklearn.metrics import *
# 计算准确率
acc = accuracy_score(labels, sentiments)
# 计算精确度
precision = precision_score(labels, sentiments, average='macro')
# 计算召回率
recall = recall_score(labels, sentiments, average='macro')
# 计算f1_core
f1_score = f1_score(labels, sentiments, average='macro')
print("准确率：{}".format(acc))
print("精确度：{}".format(precision))
print("召回率：{}".format(recall))
print("f1_core：{}".format(f1_score))