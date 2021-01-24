import multiprocessing  
import os.path  
import sys  
import jieba  
  
from gensim.models import Word2Vec  
#由于语料太大，不能一次性加载到内存训练，gensim提供了-  
#PathLineSentences(input_dir)这个类，会去指定目录依次-  
#读取语料数据文件，采用iterator方式加载训练数据到内存。  
from gensim.models.word2vec import PathLineSentences  
      
input_dir = 'corpus'  
outp1 = 'baike.model'  
outp2 = 'word2vec_format'  
# 训练模型   
# 输入语料目录:PathLineSentences(input_dir)  
# embedding size:256 共现窗口大小:10 去除出现次数5以下的词,多线程运行,迭代10次  
model = Word2Vec(PathLineSentences(input_dir),
                size=256, window=10, min_count=5,
                workers=multiprocessing.cpu_count(), iter=10)  
model.save(outp1)  
model.wv.save_word2vec_format(outp2, binary=False) 