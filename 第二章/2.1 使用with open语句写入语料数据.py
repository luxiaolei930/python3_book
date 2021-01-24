import requests  
import bs4  
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36' }     
a_=0  
for i in range(0,10):  
	start_=i*25   
	response= requests.get("https://movie.douban.com/top250?start="+str(start_)+"&filter=", headers=headers)  
	soup=bs4.BeautifulSoup(response.text,"html.parser")  
	movie_titles=soup.find(id="content").find_all("div",class_="hd")  
	movie_info=soup.find(id="content").find_all("div",class_="bd")  
	a_=a_+1  
	#使用with open()函数打开名为movies的文件夹，命名为a_的字符串形式。  
	#a表明使用读写的方式打开文件。将文档编码为utf-8，并将打开的文件设定为movie_变量。  
	with open("./movies/"+str(a_)+'.txt','a',encoding='utf-8') as movie_:  
	#使用for...in循环，依次把movie_titles中需要的元素依次迭代出来  
		for each in movie_titles:  
	# 使用index()函数，找到与movie_titles中每项（each）对应的movie_info。  
	# 并将其以字符串的形式，与each.a.text相加，定义为titles_info。  
			titles_info=str(each.a.text+movie_info[movie_titles.index(each)].p.text)  
	# 将titles_info中的内容写入文档。  
			movie_.write(titles_info)   
