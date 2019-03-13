from bs4 import BeautifulSoup
from urllib.request import urlopen

class UnsupportedLink(Exception):
	pass		

def get_content(url='http://pstu.ru/manage/rectorat/'):
	try:
		html_doc = urlopen(url).read()
		soup = BeautifulSoup(html_doc, "lxml")
		content = soup.body.find('div','content')
	except (AttributeError, ):
		raise UnsupportedLink(url)
	return content

if __name__ == '__main__':
	print(1, get_content())	
	# print(2, get_content('http://ya.ru'))
	# print(3, get_content('http://yadfsdfsdfsd.ru'))
