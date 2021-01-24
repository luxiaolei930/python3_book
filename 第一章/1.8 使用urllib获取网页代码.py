# 导入urllib库  
import urllib.request  	  

# 要请求的网站  
url="http://www.douban.com"  
  
# 方法1：创建opener对象  
#注意：在urllib使用opener时，headers是元组格式  
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE")  
opener=urllib.request.build_opener()  
opener.addheaders=[headers]  
data=opener.open(url)  
data = data.read().decode("UTF-8")  
print(data)  
	  
# 方法2：创建Request对象  
#注意：在urllib 中使用创建Request的方式，headers必须是字典格式
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}  
req=urllib.request.Request(url=url,headers=headers)  
file=urllib.request.urlopen(req)  
data = file.read().decode("UTF-8")  
print(data)  
