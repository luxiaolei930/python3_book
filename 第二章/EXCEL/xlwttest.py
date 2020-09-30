# 1.导入xlwt工具包
import xlwt

# 2.新建workbook
workbook = xlwt.Workbook()

# 3.创建sheet，并命名为“SheetTest1”
sheet = workbook.add_sheet('SheetTest1')

# 4. 依次写入第1行数据，第1行为表头，
sheet.write(0, 0, "Name")
sheet.write(0, 1, "Gender")
sheet.write(0, 2, "Age")

# 5.写入第2行数据
sheet.write(1, 0, "Luguirong")
sheet.write(1, 1, "Male")
sheet.write(1, 2, "61")

# 写入第3行数据
sheet.write(2, 0, "Zhengaiqing")
sheet.write(2, 1, "Female")
sheet.write(2, 2, "57")

# 写入第4行数据
sheet.write(2, 0, "Zhengyulin")
sheet.write(2, 1, "Female")
sheet.write(2, 2, "22")

# 保存xls
workbook.save("xlwt_excel.xls")