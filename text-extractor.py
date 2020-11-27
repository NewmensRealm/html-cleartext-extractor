import requests
from readability import Document
from bs4 import BeautifulSoup

response = requests.get(
    'https://domov.sme.sk/c/22542663/pred-vianocami-sa-do-skol-vrati-najviac-par-tisic-ziakov.html')
doc = Document(response.text)

data = doc.summary()
soup = BeautifulSoup(data, features='lxml')
extracted_text = '\n'.join(i for i in soup.article.find_all(text=True))
print(extracted_text)

f = open('clearText.txt', 'w')
f.write(extracted_text)
f.close()
