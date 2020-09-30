import os
# 数据目录：file_dir
file_dir = "law/cn/"
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files
# 所有文件名
files = file_name(file_dir)
#中文标点符号
punctuation = ['–', '—', '‘', '’', '“', '”',
               '…', '、', '。', '〈', '〉', '《',
               '》', '「', '」', '『', '』', '【',
               '】', '〔', '〕', '！', '（', '）',
               '，', '．', '：', '；', '?']
# 新建result数组，用于存放所有结果
result = []
# 遍历所有文件
for file in files:
    # 打开路径file_dir下的文件，file为文件名
    with open(file_dir+file, encoding="utf8") as f:
        # 读取文件内容
        lines = f.readlines()
        # 新建newlines数组用于存放去除标点后的新的多个句子
        newlines = []
        # 遍历lines中的每一行
        for line in lines:
            # 新建字符串，用于存放去除标点后的单个句子
            newline = ""
            # 遍历每个句子中的字
            for word in line:
                # 判断：如果该字不是标点符号， 那么将其加入到newline中，newline+=word类似于newline=newline+word
                if word not in punctuation:
                    newline+=word
            newlines.append(newline)
        result.append(newlines)
# 遍历result数组
for i in range(len(result)):
    # 在law/cn_clean/路径下新建0.txt、1.txt...文件，依次写入去除标点后的多个句子
    with open("law/cn_clean/"+str(i+1)+".txt", "w", encoding="utf8") as f:
        # 将多个句子写入文件中
        f.writelines(result[i])