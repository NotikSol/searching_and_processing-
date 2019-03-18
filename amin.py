#from bs4 import BeautifulSoup
#from urllib.request import urlopen
#import string

#import nltk
#import string
#from nltk.corpus import stopwords

#nltk.download('punkt')
#nltk.download('stopwords')
#html_doc = urlopen('http://pstu.ru/title1/student/pamyatka/').read()
#soup = BeautifulSoup(html_doc, "lxml")
#s = soup.body.find('div','content').text
#print (s)
#s = s.lower()
#print(s)
#print('--------------------------------')
  #firstly let's apply nltk tokenization
#tokens = nltk.word_tokenize(s)
#print(tokens)
#print('--------------------------------')
  #let's delete punctuation symbols
#tokens = [i for i in tokens if ( i not in string.punctuation )]
#print(tokens)
#print('--------------------------------')
  #deleting stop_words
#stop_words = stopwords.words('russian')
#stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на', 'по'])
#tokens = [i for i in tokens if ( i not in stop_words )]
 
    #cleaning words
#tokens = [i.replace("«", "").replace("»", "").replace("...") for i in tokens]
    
#print(tokens)
#print('--------------------------------')

#запись в файл для составления списка
#f = open('test.txt', 'w')
#f.write(s)
#f.close()
#каждое слово в своей строке
#with open('test.txt', 'r') as f:
#   for line in f:
#      for word in line.split():
#         print(word)

from tokenize import tokenize
from get_content import get_content
from get_tokens import get_tokens
from is_xlsx_link import is_xlsx_link, link_from_token
from xlsx_get_content import xlsx_get_content
from parse import parse
from is_normal_link import is_normal_link

rezult = []
def amin(start_url = 'http://pstu.ru'):
	content = get_content(start_url)
	tokens = get_tokens(content)
	print(3333, tokens)
	exit(0)
	for token in tokens:
		if is_xlsx_link(token):
			xlsx_content = xlsx_get_content(link_from_token(token))
			xlsx_tokens = tokenize_xlsx(xlsx_content)
			for cell in xlsx_content:
				time, lecture, teacher, room = parse(cell)
				rezult.append(link_from_token(token), xlsx_tokens, time, lecture, teacher, room)
		elif is_normal_link(link_from_token(token)):
			print(2,token)
			# amin(link_from_token(token))
	#rezult.append(start_url, tokens)
	rezult.append(start_url)
	rezult.append(tokens)
	return rezult

if __name__ == '__main__':
	#print(amin('http://pstu.ru/title1/aspirantu/'))
	print(1, amin('http://pstu.ru/student/new_timetable/?sp=%D0%90%D0%94%D0%A4&kaf=%D0%90&gr=%D0%90%2B%2B%2B-15-1%D0%B1'))

