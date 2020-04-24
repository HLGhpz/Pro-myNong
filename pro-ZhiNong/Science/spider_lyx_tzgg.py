import requests
from pprint import pprint
from bs4 import BeautifulSoup
import re
import csv
url = 'http://lxy.hzau.edu.cn/tzgg/'
otherUrl = 'http://lxy.hzau.edu.cn/tzgg.htm'
baseUrl = 'http://lxy.hzau.edu.cn/'
staticListUrl = 'http://lxy.hzau.edu.cn/tzgg/statlist.js'


def getStaticList():
    r = requests.get(staticListUrl)
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


def parserSoup(html):
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.select('ul li.Listyle1')
    for [new] in news:
        print(new)
        [title, link, time] = [new.a['title'], baseUrl + new.a['href'], new.span.text]
        # title = new.a['title']
        # link = baseUrl + new.a['href']
        # time = new.span.text
        # writeCsv([title, link, time])


def writeCsv(new):
    with open("pro-ZhiNong\Science\lyx_tzgg.csv", "a", encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new)


def main():
    [start, pageCount, totalPages] = getStaticList()
    requestUrls = creatUrl(totalPages)
    for reqUrl in requestUrls:
    	html = requestUrl(reqUrl)
    	parserSoup(html, start, pageCount)


if __name__ == "__main__":
    main()
