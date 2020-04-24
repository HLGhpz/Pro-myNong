import requests
from pprint import pprint
from bs4 import BeautifulSoup
import csv

def parserSoup(filePath):
	soup = BeautifulSoup(open(filePath, encoding='utf-8'), 'html.parser')
	news = soup.select('ul.list li')
	for new in news:
		pprint(new)
		# title = new.a['title']
		# link = new.a['href']
		# time = new.span.text

def main():
	filePath = 'pro-ZhiNong\hzau_cet.html'
	parserSoup(filePath)

if __name__ == "__main__":
	main()
