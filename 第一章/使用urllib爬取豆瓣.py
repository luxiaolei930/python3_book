#打开python
python
#引入urllib的request模块
import urllib.request
#从服务器上获取响应：使用urlopen()函数打开URL，其响应为response。
response=urllib.request.urlopen("https://www.douban.com")
#将获取的对象用read()读出来,命名为douban
douban=response.read()
#将读出来的douban打印出来
print(douban)
#打印结果为二进制字符串而并非源代码，需要使用decode()解码
douban=douban.decode("UTF-8")
#将解码后的源代码打印出来
print(douban)