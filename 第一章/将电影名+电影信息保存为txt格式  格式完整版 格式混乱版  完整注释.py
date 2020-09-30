#引入 requests 库
import requests
#引入BeautifulSoup4 解析库
import bs4
# a_的初始值为0
a_=0
#查看网址链接，发现top250的电影名称总共有10页，每页所列的电影数目为25。使用for循环实现翻页，设置代表页码的i变量，取值为0-9之间。
for i in range(0,10):
    #查看网址链接，发现翻页的时候变化的是start参数，网页每页所列的电影数目为25，start参数每页增加25。 用i*25表示参数的变化，将其命名为start_，i的取值范围为（0,10）
    start_=i*25 
     #使用requests.get获取页面内容，其中start参数在每次循环时变化，使用str()函数将start_转换成字符串。
    response= requests.get("https://movie.douban.com/top250?start="+str(start_)+"&filter=")
    #使用BeautifulSoup 解析库中的标准库（"html.parser"）来解析已获取页面的文本内容（response.text）
    soup=bs4.BeautifulSoup(response.text,"html.parser")
    #找到id为content下所有"div"标签中class为"hd"的内容
    movie_titles=soup.find(id="content").find_all("div",class_="hd")
    #找到id为content下所有"div"标签中class为"bd"的内容
    movie_info=soup.find(id="content").find_all("div",class_="bd")
    #给a_赋值为a_+1，以实现文档以数字形式依次编号。
    a_=a_+1
    #使用with open()函数打开名为movies的文件夹，命名为a_的字符串形式，a表明使用读写的方式打开文件（详见附录）
    # 将文档编码为utf-8，并将打开的文件设定为movie_变量。
    with open("./movies/"+str(a_)+'.txt','a',encoding='utf-8') as movie_:
    #使用for...in循环，依次把movie_titles中需要的元素依次迭代出来
        for each in movie_titles:
            # 使用index()函数，找到与movie_titles中每项（each）对应的movie_info，并将其以字符串的形式，与each.a.text相加，定义为titles_info。
            titles_info=str(each.a.text+movie_info[movie_titles.index(each)].p.text)
            # 将titles_info中的内容写入文档。
            movie_.write(titles_info)