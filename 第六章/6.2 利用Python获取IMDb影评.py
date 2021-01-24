# 导入requests库，用于发送http请求
import requests
# 导入BeautifulSoup库，用于解析html
from bs4 import BeautifulSoup
# 导入json库
import json
# 新建数组reviews_all,用于存放所有评论
reviews_all = []
# http请求头
headers = {
    "referer": "https://www.imdb.com/title/tt0111161/reviews?ref_=tt_urv",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
# requests发送get请求
r = requests.get("https://www.imdb.com/title/tt0111161/reviews?ref_=tt_urv", headers=headers).content
# 用BeautifulSoup将字符串转换为html格式
bs =BeautifulSoup(r, "html.parser")
# 获取评论元素-观察html发现评论内容div的class值为“lister-item-content”
ct = bs.select('div[class="lister-item-content"]')
# 遍历解析出的所有div，获取内容
for i in range(len(ct)):
    # 获取评论标题
    title = ct[i].select('a[class="title"]')[0].get_text()
    # 获取评论正文
    review = ct[i].select('div[class="text show-more__control"]')[0].get_text()
    # 获取评论分数
    rate = ct[i].select('span[class="rating-other-user-rating"]')
    # 部分评论没有给分，因此需要判断是否存在打分。若存在，则获取rate值，否则rate=None
    if len(rate)<1:
        rate = None
    else:
        rate = rate[0].select("span")[0].get_text()
    # 将获取的评论添加到reviews_all列表中
    reviews_all.append({"title":title,"review": review, "rate": rate})
print("共获取了"+str(len(reviews_all))+"条评论")
# 解决load-more的问题，影评内容通过点击load-more按钮，逐步加载内容
while True:
    # 如果页面没有load-more按钮，说明数据全部加载显示，退出循环
    if len(bs.select(".load-more-data"))<1:
        break
    # 获取paginationKey参数，用于发送请求更多数据
    paginationKey = bs.select(".load-more-data")[0].attrs["data-key"]
    # 发送get请求
    r = requests.get("https://www.imdb.com/title/tt0111161/reviews/_ajax?ref_=undefined&paginationKey="+ paginationKey, headers=headers).content
    # 将请求结果转为html格式
    bs = BeautifulSoup(r, "html.parser")
    # 获取评论元素-观察html发现评论内容div的class值为“lister-item-content”
    ct = bs.select('div[class="lister-item-content"]')
    # 遍历解析出的所有div，获取内容
    for i in range(len(ct)):
        # 获取评论标题
        title = ct[i].select('a[class="title"]')[0].get_text()
        # 获取评论正文
        review = ct[i].select('div[class="text show-more__control"]')[0].get_text()
        # 获取评论分数
        rate = ct[i].select('span[class="rating-other-user-rating"]')
        # 部分评论没有给分，因此需要判断是否存在打分。若存在，则获取rate值，否则rate=None
        if len(rate) < 1:
            rate = None
        else:
            rate = rate[0].select("span")[0].get_text()
        # 将获取的评论添加到reviews_all列表中
        reviews_all.append({"title": title, "review": review, "rate": rate})
    print("共获取了" + str(len(reviews_all)) + "条评论")
# 将结果写入reviews.txt
with open("reviews.json", "w", encoding="utf8") as f:
    json.dump(reviews_all, f)