import nltk
import string

from nltk.corpus import stopwords

from bs4 import BeautifulSoup

nltk.download('punkt')
nltk.download('stopwords')

ITEM_TEXT   = 1
ITEM_WEIGHT = 2
ITEM_LINK   = 3

weight_dict = {
	'a': 1,
	'b': 2,
	'title': 45,
	'h1': 66, 
	'div': 77,
	'strong': 88,
	'br': 22,
	'span': 3,
	'h6': 	67,
	'h4': 100,
	'hr': 100,
	'ul': 100,
	'img': 100,
	'p': 100,
	'li': 100,
}

def parse_dom(dom, n = 0):
	rez = []
	for elem in dom.children:
		print(n, elem)
		# try:
		# 	children = list(elem.children)
		# 	print(n, children)
		# 	if len(children) > 1:
		# 		rez += parse_dom(elem, n + 1)
		# 		print(3333333333)
		# 	else:
		# 		if elem.name == 'a':
		# 			rez += [(elem.name, elem.text, weight_dict[elem.name], 'tttttttt' + elem['href'])]
		# 		else:
		# 			rez += [(elem.name, elem.text, weight_dict[elem.name], 'jjjjjjjj')]
		# except AttributeError:
		# 	pass # NavString
	return rez


def get_tokens(content):
	parsed_dom = parse_dom(content)
	rez = []
	for item in parsed_dom:
		tokens = nltk.word_tokenize(item[ITEM_TEXT])
		rez += [(tokens, item[ITEM_WEIGHT], item[ITEM_LINK])]

	#print(rez)#test
	return rez
	# #print(tokens)
	# #print('--------------------------------')
	#   #let's delete punctuation symbols
	# tokens = [i for i in tokens if ( i not in string.punctuation )]
	# #print(tokens)
	# #print('--------------------------------')
	#   #deleting stop_words
	# stop_words = stopwords.words('russian')
	# stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на', 'по'])
	# tokens = [i for i in tokens if ( i not in stop_words )]
	 
	#     #cleaning words
	# tokens = [i.replace("«", "").replace("»", "").replace("...") for i in tokens]


if __name__ == '__main__':
	from bs4 import BeautifulSoup
	from get_content import get_content
	test = BeautifulSoup("<a href='http://pstu.ru/manage/rectorat/'>gfhf</a>пара пара пам", 'lxml')
	print(1, get_tokens(get_content()))
