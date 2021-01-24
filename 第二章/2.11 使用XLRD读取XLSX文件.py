# 导入xlrd工具包  
import xlrd  
# 打开Excel文件,读取工作簿数据  
data = xlrd.open_workbook("excel.xls")  
# 获取所有sheet名称  
sheet_names = data.sheet_names()  
print(sheet_names) #结果: ['Sheet1']  
# 通过sheet_by_index(0)获取第一个sheet,即Sheet1  
sheet = data.sheet_by_index(0)  
# 显示sheet的行列数量,nrows和ncols分别代表行和列的数量。  
print("行数：" + str(sheet.nrows))  
print("列数：" + str(sheet.ncols))  
# 通过row_values(n)获取第(n+1)行数据  
row_value = sheet.row_values(1) #获取第二行数据  
print(row_value)  
# 通过col_values(n)获取第(n+1)行数据  
col_value = sheet.col_values(1) #获取第二列数据  
print(col_value)  
# 通过cell_value(m, n)获取(m+1)行，(n+1)列单元格的内容  
content = sheet.cell_value(1,1)  
print(content) 
