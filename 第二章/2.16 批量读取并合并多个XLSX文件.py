# 导入xlrd和xlwt工具包
import xlrd
import xlwt
import glob
#新建一个Excel工作簿，用于存放所有数据
workbook_all = xlwt.Workbook()
#创建sheet，并命名为“豆瓣Top250”
sheet_all = workbook_all.add_sheet('豆瓣Top250')
#写入表头，Number, Title, Info
sheet_all.write(0, 0, "Number")
sheet_all.write(0, 1, "Title")
sheet_all.write(0, 2, "Info") 
#使用glob()获取当前目录下的所有.xls文件,使用len()计算文件个数
target_files=glob.glob(pathname='./*.xls')
files_num = len(target_files)
#将已获取的内容写入文件中，按行写入，行id命名为index_all,初始值为0（即第1个）（index_all表示最后形成的单个文件中的“行序号”）
index_all = 0
for i in range(files_num):
    #逐个打开工作簿
    data = xlrd.open_workbook(target_files[i])
    # 获取所有sheet名称
    # 通过sheet_by_index(0)获取第一个sheet
    sheet = data.sheet_by_index(0)
    # 已知列数为3（表头中已体现出），还需获取当前sheet的行数。sheet.nrows代表当前的sheet中有多少行。
    rows = sheet.nrows
    for j in range(rows-1):
        #每写入一行数据index_all加1
        index_all+=1
        # 忽略单个文件中的表头，从第二行开始读取，并将读取的结果写入sheet_all当中，sheet.cell_value()代表原有文件中某单元格的值（括号内为单元格坐标）
        print(j+1)
        sheet_all.write(index_all, 0, sheet.cell_value(j+1, 0))
        sheet_all.write(index_all, 1, sheet.cell_value(j+1, 1))
        sheet_all.write(index_all, 2, sheet.cell_value(j+1, 2))