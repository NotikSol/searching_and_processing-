from bs4 import BeautifulSoup
from urllib.request import urlopen
import string

import nltk
import string
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
html_doc = urlopen('http://pstu.ru/student/new_timetable/').read()
soup = BeautifulSoup(html_doc, "lxml")
s = soup.body.find('div','content').text
print (s)

  #firstly let's apply nltk tokenization
tokens = nltk.word_tokenize(s)
#print(tokens)
 
  #let's delete punctuation symbols
tokens = [i for i in tokens if ( i not in string.punctuation )]

#print(tokens)
 
  #deleting stop_words
stop_words = stopwords.words('russian')
stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на'])
tokens = [i for i in tokens if ( i not in stop_words )]
 
    #cleaning words
tokens = [i.replace("«", "").replace("»", "") for i in tokens]
    
print(tokens)

#запись в файл для составления списка
#f = open('test.txt', 'w')
#f.write(s)
#f.close()
#каждое слово в своей строке
#with open('test.txt', 'r') as f:
#   for line in f:
#      for word in line.split():
#         print(word)
          
