from gensim.models import Word2Vec       # 引入Word2Vec包  
mode = Word2Vec.load("word60.model")     # 加载训练好的60维词向量模型  
mode. most_similar ("语言学")             # 获取与“语言学”相关度高的词 