import json
import os
import requests
from bs4 import BeautifulSoup

DIR_ARTICLE = 'articles'
FILE_ERROR = 'error.log'
URL_ARTICLE = 'https://www.theguardian.com/business/nils-pratley-on-finance/2017/dec/07/gvc-and-ladbrokes-coral-david-gambles-on-goliath'
DATE_ARTICLE = {'itemprop': 'datePublished'}


def get_html(url):
    """return page HTML.text for get url"""
    try:
        result = requests.get(url)
        return result.text
    except Exception as err:
        with open(FILE_ERROR, 'a', encoding='utf-8') as f:
            f.write(str(err) + '\n')
        return False


def get_article(text):
    """return article text for get HTML.text"""
    soup = BeautifulSoup(text, "html.parser")
    title = soup.h1.text
    if not title:
        title = 'Not Title'
    body = soup.find("div", class_='content__article-body from-content-api js-article__body').text
    return [title, body]


def get_date(text):
    """return date in format datetime for HTML.text"""
    from datetime import datetime
    soup = BeautifulSoup(text, "html.parser")
    time_article = soup.find('time', attrs=DATE_ARTICLE)
    date_article = time_article['datetime'].split('T')[0]
    return datetime.strptime(date_article, '%Y-%m-%d')


def save_in_file(title, text, url):
    """save in file and numerate over index"""
    index = len(os.listdir('articles'))
    # for linux dir was other. You need change symbol //
    name_file = '{}/article_{}.txt'.format(DIR_ARTICLE, index)
    json_to_file = json.dumps({'title': title, 'text': text, 'url': url})
    with open(name_file, 'w', encoding='utf-8') as f:
        f.write(json_to_file)


if __name__ == '__main__':
    # For example
    html = get_html(URL_ARTICLE)
    print(get_date(html))
