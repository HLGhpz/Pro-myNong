import requests
from pprint import pprint
from bs4 import BeautifulSoup
import csv

def creatUrl(url, otherUrl, number):
    reqUrls = []
    for index in range(number, 0, -1):
        if index == number:
            reqUrls.append(otherUrl)
        else:
            reqUrls.append(url + str(index) + '.htm')
    return reqUrls


def requestUrl(url):
	r = requests.get(url)
	r.encoding = 'utf-8'
	return r.text


def parserSoup(html, baseUrl):
	soup = BeautifulSoup(html, 'html.parser')
	news = soup.select('ul li.Listyle1')
	for new in news:
		title = new.a['title']
		link = baseUrl + new.a['href']
		time = new.span.text
		writeCsv([title, link, time])

def writeCsv(new):
	with open("pro-ZhiNong\Science\lyx_tzgg.csv", "a", encoding='utf-8') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(new)

def main():
	url = 'http://lxy.hzau.edu.cn/tzgg/'
	otherUrl = 'http://lxy.hzau.edu.cn/tzgg.htm'
	baseUrl = 'http://lxy.hzau.edu.cn/'
	requestUrls = creatUrl(url, otherUrl, 16)
	for url in requestUrls:
		html = requestUrl(url)
		parserSoup(html, baseUrl)

if __name__ == "__main__":
	main()
