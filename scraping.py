# -*- coding: utf-8 -*-
def searcher(input_word):
    import requests
    from bs4 import BeautifulSoup
    meaning=""
    weblio_data = requests.get("http://ejje.weblio.jp/content/"+input_word)
    soup = BeautifulSoup(weblio_data.text,'html.parser')
    word_meanings = soup.findAll("td",class_ = 'content-explanation')
    len2 = len(word_meanings)
    if len2 > 0:
        for i in range(len2):
            meaning = word_meanings[i].text
        return meaning
    else:
        return "NotFound"

