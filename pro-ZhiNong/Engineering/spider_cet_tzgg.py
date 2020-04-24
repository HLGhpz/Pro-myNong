import requests
from pprint import pprint
from bs4 import BeautifulSoup
import re
import csv

url = 'http://cet.hzau.edu.cn/xydt/tzgg/'
otherUrl = 'http://cet.hzau.edu.cn/xydt/tzgg.htm'
baseUrl = 'http://cet.hzau.edu.cn/'
staticListUrl = 'http://cet.hzau.edu.cn/xydt/tzgg/statlist.js'
filePath = 'pro-ZhiNong\Engineering\cet_tzgg.csv'


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
    news = soup.select('ul li.Listyle1')
    for i, new in enumerate(news):
        print('开始第%d页'%i)
        if(index == 0):
            if(i < pageCount):
                [title, link, time] = [new.a['title'], baseUrl + new.a['href'], new.span.text]
                writeCsv([title, link, time])
        else:
            if(i >= start and i < start+pageCount):
                [title, link, time] = [new.a['title'], baseUrl + new.a['href'], new.span.text]
                writeCsv([title, link, time])

def writeCsv(new):
    with open(filePath, "a", encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new)

def main():
    [start, pageCount, totalPages] = getStaticList()
    requestUrls = creatUrl(totalPages)
    for index,reqUrl in enumerate(requestUrls):
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

