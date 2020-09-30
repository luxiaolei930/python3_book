python
import requests
#向服务器发出get请求，返回的响应定义为response
response=requests.get("http://www.douban.com")
#使用encoding设置编码格式
response.encoding="utf-8"
print(response.text)