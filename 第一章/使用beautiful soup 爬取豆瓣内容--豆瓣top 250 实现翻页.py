#引入 requests 库
import requests
#引入BeautifulSoup4 解析库
import bs4
#查看网址链接，发现top250的电影名称总共有10页，每页所列的电影数目为25。使用for循环实现翻页，设置代表页码的i变量，取值为0-9之间。（range的取值范围为左闭右开区间。即大于等于第一个参数，小于第二个参数。）
for i in range(0,10):
    #查看网址链接，发现翻页的时候变化的是start参数，网页每页所列的电影数目为25，start参数每页增加25。 用i*25表示参数的变化，将其命名为start_，i的取值范围为（0,10）
    start_=i*25 
    #使用requests.get获取页面内容，其中start参数在每次循环时变化，使用str()函数将start_转换成字符串。
    response= requests.get("https://movie.douban.com/top250?start="+str(start_)+"&filter=")
    #使用BeautifulSoup 解析库中的标准库（"html.parser"）来解析已获取页面的文本内容（response.text）
    soup=bs4.BeautifulSoup(response.text,"html.parser")
    #找到所有"div"标签中class为"hd"的内容
    content=soup.find_all("div",class_="hd")
    #使用for...in循环，依次把内容中需要的元素迭代出来
    for each in content:
    #打印<a><a/>标签中的文本
        print(each.a.text)
        
