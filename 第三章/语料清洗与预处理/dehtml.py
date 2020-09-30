'''
介绍BeautifulSoup直接提取html内容的方法；
读者也可以使用正则表达式去除html标签
'''
#引入BeautifulSoup
from bs4 import BeautifulSoup
html = '''<a href="https://movie.douban.com/subject/1292052/" class="">
                <span class="title">肖申克的救赎</span>
                <span class="title">The Shawshank Redemption</span>
                <span class="other">月黑高飞(港)  /  刺激1995(台)</span>
            </a>'''

#使用html.parser模块解析文本
soup = BeautifulSoup(html, 'html.parser')
#使用get_text()函数从大段html中提取文本
print(soup.get_text())