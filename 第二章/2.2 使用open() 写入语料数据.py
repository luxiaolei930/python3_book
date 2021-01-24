import requests  
import bs4  
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36' }   
a_=0  
for i in range(0,10):  
	start_=i*25   
	response= requests.get("https://movie.douban.com/top250?start="+str(start_)+"&filter=", headers=headers)  
	soup=bs4.BeautifulSoup(response.text,"html.parser")  
	movie_titles=soup.find_all("div",class_="hd")  
	a_=a_+1  
	#使用open()函数打开一个文件，a表明使用读写的方式打开文件，将文档编码为utf-8。  
	file=open(str(a_)+'.txt','a',encoding='utf-8')  
	#使用数字（字符串的形式）对保存的文件进行编码，用a_=a_+1对其赋值，a_的初始值为0  
	for each in movie_titles:  
		#将<a><a/>标签中的文本写入被编号的文件中  
		file.write(each.a.text)  
		#关闭文件  
	file.close()    
