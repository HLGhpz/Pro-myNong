import requests
from pprint import pprint
from bs4 import BeautifulSoup
import csv

url_test = 'http://cet.hzau.edu.cn/xydt/tzgg/1.htm'
url = 'http://cet.hzau.edu.cn/xydt/tzgg/'
base_url = 'http://cet.hzau.edu.cn/'

for index in range(19, 0, -1):
    if index == 19:
        reqUrl = 'http://cet.hzau.edu.cn/xydt/tzgg.htm'
    else:
        reqUrl = url + str(index) + '.htm'

    r = requests.get(reqUrl)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    with open("pro-ZhiNong\cet_tzgg.csv", "a", encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)
        for news in soup.select('UL.list li'):
            cet_new = news.a['title']
            cet_link = base_url + news.a['href'].lstrip('../')
            cet_time = news.span.text
            writer.writerow([cet_new, cet_link, cet_time])
    print('完成第' + str(index) + '页')

