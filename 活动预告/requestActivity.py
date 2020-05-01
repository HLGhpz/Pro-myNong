import requests
from pprint import pprint
from bs4 import BeautifulSoup
import re
import csv

url = 'http://www.hzau.edu.cn/hdyg/'
otherUrl = 'http://www.hzau.edu.cn/hdyg.htm'
baseUrl = 'http://www.hzau.edu.cn/'
staticListUrl = 'http://www.hzau.edu.cn/hdyg/statlist.js'
filePath = '活动预告\\activity.csv'
selectPath = 'div.zy-mainxrx ul li'


def getStaticList():
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
    reqUrls = []
    for index in range(number, 0, -1):
        if index == number:
            reqUrls.append(otherUrl)
        else:
            reqUrls.append(url + str(index) + '.htm')
    return reqUrls


def requestUrl(reqUrl):
    r = requests.get(reqUrl)
    r.encoding = 'utf-8'
    return r.text


def parserSoup(html, start, pageCount, index):
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.select(selectPath)
    for i, new in enumerate(news):
        if(index == 0):
            if(i < pageCount):
                # [title, link, sponsor, time] = [new.a['title'], baseUrl + new.a['href'], new.span.text, new.samll.text]
                # print([title, link, sponsor, time])
                # writeCsv([title, link, sponsor, time])
                if(new.span == []):
                    new.span.text = ""
                [title, link, sponsor, time] = [new.a['title'],
                                                baseUrl + new.a['href'], new.span.text, new.samll.text]
                writeCsv([title, link, sponsor, time])
        else:
            if(i >= start and i < start+pageCount):
                if(new.span == []):
                    new.span.text = ""
                [title, link, sponsor, time] = [new.a['title'],
                                                baseUrl + new.a['href'], new.span.text, new.samll.text]
                writeCsv([title, link, sponsor, time])


def writeCsv(new):
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

# for index in range(19, 0, -1):
#     if index == 19:
#         reqUrl = 'http://cet.hzau.edu.cn/xydt/tzgg.htm'
#     else:
#         reqUrl = url + str(index) + '.htm'

#     r = requests.get(reqUrl)
#     r.encoding = 'utf-8'
#     soup = BeautifulSoup(r.text, 'html.parser')
#     with open("pro-ZhiNong\cet_tzgg.csv", "a", encoding='utf-8') as csvFile:
#         writer = csv.writer(csvFile)
#         for news in soup.select('UL.list li'):
#             cet_new = news.a['title']
#             cet_link = base_url + news.a['href'].lstrip('../')
#             cet_time = news.span.text
#             writer.writerow([cet_new, cet_link, cet_time])
#     print('完成第' + str(index) + '页')
