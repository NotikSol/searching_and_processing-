import nltk
import string

from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

ITEM_TEXT   = 1
ITEM_WEIGHT = 2
ITEM_LINK   = 3

weight_dict = {
	'a': 1,
	'b': 2,
	'title': 100
}

def parse_dom(dom, n = 0)
	rez = []
	for elem in dom.children:
		try:
			children = list(elem.children)
			# print(n, children)
			if len(children) > 1:
				rez += parse_dom(elem, n + 1)
			else:
				if elem.name == 'a':
					rez += [(elem.name, elem.text, weight_dict[elem.name], elem['href'])]
				else:
					rez += [(elem.name, elem.text, weight_dict[elem.name], '')]
		except AttributeError:
			pass # NavString
	return rez


def get_tokens(content):
	parsed_dom = parse_dom(content)
	rez = []
	for item in parse_dom:
		tokens = nltk.word_tokenize(item[ITEM_TEXT])
		rez += [(tokens, item[ITEM_WEIGHT], item[ITEM_LINK])]
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
	test = BeautifulSoup("<a href='http://ya.ru'>gfhf</a>пара пара пам", 'lxml')
	print(1, get_tokens(get_content()))
