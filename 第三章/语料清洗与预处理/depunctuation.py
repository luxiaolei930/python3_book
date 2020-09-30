source_text = "本解释施行后，案件尚在一审或者二审阶段的，适用本解释；本解释施行前已经终审，当事人申请再审或者按照审判监督程序决定再审的案件，不适用本解释。"

#中文标点符号
punctuation = ['–', '—', '‘', '’', '“', '”',
               '…', '、', '。', '〈', '〉', '《',
               '》', '「', '」', '『', '』', '【',
               '】', '〔', '〕', '！', '（', '）',
               '，', '．', '：', '；', '?']
target_text = [word for word in source_text if word not in punctuation]
print("去除标点符号前：", source_text)
print("去除标点符号后：", "".join(target_text))
