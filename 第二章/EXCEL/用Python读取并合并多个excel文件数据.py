import pandas as pd
#引入pandas工具包
import os
#引入os工具包
data_merge=pd.DataFrame()
#将文件格式设定为DataFrame
for each in os.listdir('./test/'):
#对于'/test'路径下的所有文件。需注意Python打开文件路径的格式，应当为'/'而非'\'，因为python中的反斜杠'\'表示转义字符。
    data=pd.read_excel('./test/'+each)
    #使用pd.read_excel()函数读取数据
    data_merge=pd.concat([data_merge,data_merge1])
    #使用pd.concat()函数合并数据
    data_merge.to_excel()
    #将文档保存在
