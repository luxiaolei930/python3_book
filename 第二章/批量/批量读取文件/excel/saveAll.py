'''
该文件的目标是批量读入Excel文件内容，并将其合并到当个excel文件中
'''
# 导入xlrd和xlwt工具包
import xlrd
import xlwt
import glob
#新建个Excel工作簿，用于存放所有数据
workbook_all = xlwt.Workbook()
#创建sheet，并命名为“豆瓣Top250”
sheet_all = workbook_all.add_sheet('豆瓣Top250')
#写入表头
sheet_all.write(0, 0, "Number")
sheet_all.write(0, 1, "Title")
sheet_all.write(0, 2, "Info") 
#使用glob()获取当前目录下的所有.xls文件
target_files=glob.glob(pathname='./*.xls')
files_num = len(target_files)
#所有文件的序列id
index_all = 0
for i in range(len(target_files)):
    data = xlrd.open_workbook(target_files[i])
    # 获取所有sheet名称
    # 通过sheet_by_index(0)获取第一个sheet
    sheet = data.sheet_by_index(0)
    # 列数为3，还需获取当前sheet的行数
    rows = sheet.nrows
    for j in range(rows-1):
        #每写入一行数据index_all加1
        index_all+=1
        # 忽略单个文件中的表头，从第二行开始读取，并将读取的结果写入sheet_all当中
        print(j+1)
        sheet_all.write(index_all, 0, sheet.cell_value(j+1, 0))
        sheet_all.write(index_all, 1, sheet.cell_value(j+1, 1))
        sheet_all.write(index_all, 2, sheet.cell_value(j+1, 2))
workbook_all.save("all.xls")