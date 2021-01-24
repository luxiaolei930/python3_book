import csv 
#导入csv库
with open('test.csv','a',newline='') as file:
    #使用with open（）函数打开文件,文件命名为test。这里需要加上newline 函数，否则每一行数据之间会有多余空行。
    csv_= csv.writer(file)
    #传入文件
    csv_.writerow(['Name','Gender','Age'])
    #按行写入
    csv_.writerow(['xiaolu','female','18'])
    csv_.writerow(['xiaohong','male','20'])
    csv_.writerow(['xiaohan','male','19'])


