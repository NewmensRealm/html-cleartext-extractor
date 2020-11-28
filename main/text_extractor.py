import requests
from readability import Document
from bs4 import BeautifulSoup
from file_handler import clear_text


def get_clear_text(urls, file_name):
    for url in urls:
        response = requests.get(url)
        doc = Document(response.text)

        data = doc.summary()
        soup = BeautifulSoup(data, features='lxml')
        extracted_text = '\n'.join(
            i for i in soup.find_all(text=True))
        cleared_text = clear_text(extracted_text, '\n*:0123456789(-)').strip()

        f = open(f'{file_name}.txt', 'a', encoding='utf-8')
        f.write(cleared_text)
        f.close()
