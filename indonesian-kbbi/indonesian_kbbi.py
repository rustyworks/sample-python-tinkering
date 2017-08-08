import urllib.request

from urllib.error import URLError

from bs4 import BeautifulSoup


KBBI_SITE = 'http://www.kbbi.web.id'

while True:
    word = input('Silakan masukkan kata dalam bahasa Indonesia [Ctrl+C untuk keluar]: ')
    url = '{kbbi_site}/{word}'.format(kbbi_site=KBBI_SITE, word=word)
    try:
        response = urllib.request.urlopen(url).read()
        html = response.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        explanation = soup.find(id='d1').get_text()
        if explanation.strip():
            print(explanation)
        else:
            print('Kata tidak ditemukan')
    except URLError:
        print('No connection or connection error')
    print('\n' * 5)
