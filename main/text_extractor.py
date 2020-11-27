import requests
from readability import Document
from bs4 import BeautifulSoup


def get_clear_text(urls, file_name):
    for url in urls:
        response = requests.get(url)
        doc = Document(response.text)

        data = doc.summary()
        soup = BeautifulSoup(data, features='lxml')
        extracted_text = '\n'.join(
            i for i in soup.article.find_all(text=True)).strip('\n*:0123456789()')

        f = open(f'{file_name}{urls.index(url)}.txt', 'w')
        f.write(extracted_text)
        f.close()
