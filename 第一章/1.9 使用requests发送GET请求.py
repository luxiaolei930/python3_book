#打开requests库  
import requests  
#向服务器发出GET请求，返回的响应定义为response  
response=requests.get("http://www.baidu.com")  
#打印response
print(response.text)  
