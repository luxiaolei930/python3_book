import glob  
target_files=glob.glob(pathname='./法律英语平行语料数据-陆晓蕾/*.txt')  
data = []  
for file_ in target_files:  
    #开头文字  
    head_str = ["本资料由陆晓蕾收集、整理","\n", ]  
    #结尾文字  
    tail_str = ["本资料由陆晓蕾收集、整理","\n"]  
    with open(file_,"r", encoding='utf-8') as f:  
        #读取单文件中的所有行，定义为lines  
        lines = f.readlines()  
        #以head_str为开头，并在开头文字后面添加文本内容lines，形成开头+内容结构的数组  
        head_str.extend(lines)  
        #使用extend()函数添加结尾文字，形成开头+内容+结尾的数组
        #使用append()函数将开头+内容+结尾数组放入data数组中。  
        head_str.extend(tail_str)  
        data.append(head_str)  
#使用数字按序号给文件重新命名，初始值为1，在法律英语平行语料数据-陆晓蕾（整理后）路径下新建.txt文件，将数据分别写入文件中  
i = 1  
for item in data:      
    with open("./法律英语平行语料数据-陆晓蕾（整理后）/"+str(i)+".txt", "w", encoding="utf-8") as f:  
        f.writelines(item)  
        #经历循环之后，将i更新为i+1  
        i=i+1  