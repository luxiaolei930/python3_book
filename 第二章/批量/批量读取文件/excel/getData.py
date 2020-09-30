import requests  
import bs4
import xlwt
    
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36' }     
a_=0  
for i in range(0,10):
    # 新建工作簿
    workbook = xlwt.Workbook()

    # 创建sheet，并命名为“豆瓣Top250”
    sheet = workbook.add_sheet('豆瓣Top250')
    sheet.write(0, 0, "Number")
    sheet.write(0, 1, "Title")
    sheet.write(0, 2, "Info")    
    #按照第一章的方式获取数据（参见第一章第四节）
    start_=i*25   
    response= requests.get("https://movie.douban.com/top250?start="+str(start_)+"&filter=", headers=headers)  
    soup=bs4.BeautifulSoup(response.text,"html.parser")  
    movie_titles=soup.find(id="content").find_all("div",class_="hd")  
    movie_info=soup.find(id="content").find_all("div",class_="bd")  
    #item为movie_titles数组中的每一个元素，idx为item在数组中的序号。
    for (idx, item) in enumerate(movie_titles):  
        sheet.write(idx+1, 0, idx+1+25*i)
        #提取item中含有<a></a>标签中的内容，使用strip()去除首尾的格式（如回车、空格等）
        sheet.write(idx+1, 1, item.a.text.strip())
        sheet.write(idx+1, 2, movie_info[idx].p.text.strip())
    top250_excel = str(i+1)+".xls"
    workbook.save(top250_excel)
