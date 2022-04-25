from urllib.request import urlopen
from bs4 import BeautifulSoup

def dxy_data_down(article_url):
    article_surl = 'https://ncov.dxy.cn/ncovh5/view/pneumonia';
    url = urlopen(article_surl)
    soup = BeautifulSoup(url, 'html.parser')  # parser����

    f = open("疫情数据.txt", "w", encoding="utf-8")
    f.write(str(soup))
    f.close()


dxy_data_down("https://ncov.dxy.cn/ncovh5/view/pneumonia")
