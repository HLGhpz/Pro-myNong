import requests
from bs4 import BeautifulSoup

requestUrl = "http://www.hzau.edu.cn/info/1062/8488.htm"
requesBadUrl = "http://www.hzau.edu.cn/../info/1062/10781.htm"
selectImagePath = 'div.v_news_content p img'
# 获取具体的图片链接

r = requests.get(requesBadUrl)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.select(selectImagePath))
