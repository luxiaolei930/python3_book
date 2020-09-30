# 引入nltk.parse.corenlp中的CoreNLPDependencyParser
from nltk.parse.corenlp import CoreNLPDependencyParser
# 引入nltk中的tree用于绘制句法树
from nltk import tree
# CoreNLPDependencyParser构造对象，调用本地已启动的coreNLP Server（基于java）
eng_parser = CoreNLPDependencyParser(url='http://localhost:9000')
# 目标句子
str_ = "He was an old man who fished alone in a skiff in the Gulf Stream"
# 进行依存句法分析
parse, = eng_parser.raw_parse(str_)
# 以列表的方式打印分析结果
print(parse.to_conll(4))
# 显示句法分析树
tree.Tree.draw(parse.tree())
'''
也可以直接访问http://localhost:9000进入人工界面，进行句法分析
'''