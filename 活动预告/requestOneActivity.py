import requests
from pprint import pprint
from bs4 import BeautifulSoup
import re
import csv

url = 'http://www.hzau.edu.cn/hdyg/'
staticListUrl = 'http://www.hzau.edu.cn/hdyg/statlist.js'
# 用于请求分页数据
# otherUrl = 'http://www.hzau.edu.cn/hdyg.htm'
otherUrl = 'http://www.hzau.edu.cn/hdyg/30.htm'
# 第一页URL
baseUrl = 'http://www.hzau.edu.cn/'
# 添加到请求链接前的baseUrl
selectPath = 'div.zy-mainxrx ul li'
# 获取每一条新闻数据
selectImagePath = 'div.v_news_content p img'
# 获取具体的图片链接
filePath = '活动预告\\activityAll.csv'
# 保存数据

def requestUrl(requestUrl):
    # 请求URL
    r = requests.get(requestUrl)
    r.encoding = 'utf-8'
    return r.text


def parserSoup(html):
    # 解析请求回来活动数据
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.select(selectPath)
    for i, new in enumerate(news):
        if (i == 0):
            dealActivity(new)
        else:
            # print(i)
            pass



def writeCsv(new):
    # 将活动数据存入CSV
    with open(filePath, "a", encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new)

def dealActivity(new):
    # 处理活动数据得到图片URL
    imageHtml = requestUrl(baseUrl + new.a['href'])
    imageSoup = BeautifulSoup(imageHtml, 'html.parser')
    print(imageSoup)
    listLen = len(imageSoup.select(selectImagePath))

    # imgLink = []
    # for index in range(listLen):
    #     imgLink.append(baseUrl + imageSoup.select(selectImagePath)[index]['src'])
    # if(new.span is None):
    #     sponsor = ""
    # else:
    #     sponsor = new.span.text
    # [title, link, time] = [new.a['title'],
    #                         baseUrl + new.a['href'], new.small.text]
    # print(imgLink)
    # writeCsv([title, link, sponsor, time, imgLink])


def main():
    html = requestUrl(otherUrl)
    parserSoup(html)


if __name__ == "__main__":
    main()
