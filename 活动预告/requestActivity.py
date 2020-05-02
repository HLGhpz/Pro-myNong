import requests
from pprint import pprint
from bs4 import BeautifulSoup
import re
import csv

url = 'http://www.hzau.edu.cn/hdyg/'
staticListUrl = 'http://www.hzau.edu.cn/hdyg/statlist.js'
# 用于请求分页数据
otherUrl = 'http://www.hzau.edu.cn/hdyg.htm'
# 第一页URL
baseUrl = 'http://www.hzau.edu.cn/'
# 添加到请求链接前的baseUrl
selectPath = 'div.zy-mainxrx ul li'
# 获取每一条新闻数据
selectImagePath = 'div.v_news_content p img'
# 获取具体的图片链接
filePath = '活动预告\\activityAll.csv'
# 保存数据


def getStaticList():
    # 获取分页数据函数
    r = requests.get(staticListUrl)
    print('获取静态变量')
    r.encoding = 'utf-8'
    staticList = []
    staticList = re.findall(r"\d+", r.text)
    rowCount = int(staticList[0])
    pageCount = int(staticList[1])
    totalPages = int(staticList[2])
    start = (pageCount - rowCount % pageCount) % pageCount
    return [start, pageCount, totalPages]


def creatUrl(number):
    # 创建请求URL
    reqUrls = []
    for index in range(number, 0, -1):
        if index == number:
            reqUrls.append(otherUrl)
        else:
            reqUrls.append(url + str(index) + '.htm')
    return reqUrls


def requestUrl(reqUrl):
    # 请求URL
    r = requests.get(reqUrl)
    r.encoding = 'utf-8'
    return r.text


def parserSoup(html, start, pageCount, index):
    # 解析活动数据
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.select(selectPath)
    for i, new in enumerate(news):
        if(index == 0):
            if(i < pageCount):
                dealActivity(new)
        else:
            if(i >= start and i < start+pageCount):
                dealActivity(new)


def dealActivity(new):
    # 处理活动数据
    imageHtml = requestUrl(baseUrl + new.a['href'].strip('./'))
    imageSoup = BeautifulSoup(imageHtml, 'html.parser')
    listLen = len(imageSoup.select(selectImagePath))
    # print(imageSoup.select(selectImagePath))
    imgLink = []
    for imgIndex in range(listLen):
        imgLink.append(
            baseUrl + imageSoup.select(selectImagePath)[imgIndex]['src'].strip('./'))
    # print(imgLink)
    if(new.span is None):
        sponsor = ""
    else:
        sponsor = new.span.text
    [title, link, time] = [new.a['title'],
                           baseUrl + new.a['href'].strip('./'), new.small.text]
    writeCsv([title, link, sponsor, time, imgLink])


def writeCsv(new):
    # 写入活动数据到CSV
    with open(filePath, "a", encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new)


def main():
    [start, pageCount, totalPages] = getStaticList()
    requestUrls = creatUrl(totalPages)
    for index, reqUrl in enumerate(requestUrls):
        print('reqUrl = ' + reqUrl)
        html = requestUrl(reqUrl)
        parserSoup(html, start, pageCount, index)


if __name__ == "__main__":
    main()
