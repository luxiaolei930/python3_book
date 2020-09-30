# 导入pandas工具包
import pandas as pd
# 使用pd.Series()建立Dataframe的列，包括内容value和索引index,命名为data
data = {
    'Name': pd.Series(['Luguirong', 'Zhengaiqing', 'Zhengyulin', 'Lubinliang'], index=list(range(4))),
    'Gender': ['Male', 'Female', 'Female', 'Male'],
    'Age': ['61', '57', '22', '99']
}
# 将data转换为DataFrame格式，命名为dataframe_。
dataframe_ = pd.DataFrame(data)
# 将DataFrame保存为excel
dataframe_.to_excel("excel.xls")