from bs4 import BeautifulSoup
from urllib.request import urlopen
import string
html_doc = urlopen('http://pstu.ru/student/new_timetable/').read()
soup = BeautifulSoup(html_doc, "lxml")
s = soup.body.find('div','content').text
print (s)

s = ''.join([c for c in s if c not in ('!','.',',','"','?','(',')')])
print(s)

f = open('test.txt', 'w')
f.write(s)
f.close()

with open('test.txt', 'r') as f:
   for line in f:
      for word in line.split():
         print(word)
          
