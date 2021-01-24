import pandas as pd
import jieba

df = pd.read_table("./BosonNLP_sentiment_score.txt",sep= " ",names=['key','score'])
key = df['key'].values.tolist()
score = df['score'].values.tolist()

def getscore(line):
    segs = jieba.lcut(line)  #分词
    score_list  = [score[key.index(x)] for x in segs if(x in key)]
    return  sum(score_list)  #计算得分
text1 = "今天阳光明媚"
text2 = "连续几天的下雨，我不想出去了"
print(getscore(text1))
print(getscore(text2))