import nltk
text = "strange lying saved discusses men builds"
print("原始文本：")
print(text)
# 词干提取与词形还原之前先进行分词
tokens = nltk.word_tokenize(text)

# stemming-提取词干
# 导入stem.porter和Lancaster工具包
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
# 实例化PosterStemmer对象
porter_stemmer = PorterStemmer()
# 实例化LancasterStemmer对象
lancaster_stemmer = LancasterStemmer()
# 新建stemmed_list和lancaster_list数组，用于分别存放PorterStemmer和LancasterStemmer的结果
stemmed_list = []
lancaster_list = []
for token in tokens:
    stemmed_list.append(porter_stemmer.stem(token))
    lancaster_list.append(lancaster_stemmer.stem(token))
print("提取词干结果：")
print("1.PorterStemmer:", stemmed_list)
print("2.LancasterStemmer:", lancaster_list)

# Lemmatization-词形还原
# nltk的Lemmatization是基于WordNet实现的，导入WordNetLemmatizer。
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
# 新建lem_list数组，用于存放词形还原
lem_list = []
for token in tokens:
    lem_list.append(wordnet_lemmatizer.lemmatize(token))
print("词形还原结果：")
print(lem_list)
