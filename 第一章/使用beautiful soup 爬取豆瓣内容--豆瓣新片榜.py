import requests
#引入 requests 库
import bs4
#引入BeautifulSoup4 解析库
response= requests.get("https://movie.douban.com/chart")
#使用requests.get获取页面内容
soup=bs4.BeautifulSoup(response.text,"html.parser")
#使用BeautifulSoup 解析库中的标准库（"html.parser"）来解析已获取页面的文本内容（response.text）
content=soup.find_all("div",class_="pl2")
#找到所有"div"标签中class为"pl2"的内容
for each in content:
#使用for...in循环，依次把内容中需要的元素迭代出来
    print(each.a.text)
#打印<a><a/>标签中的文本


