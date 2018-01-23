from bs4 import BeautifulSoup
from parsers.parser import get_html
from datetime import datetime
from pytz import timezone
from storage.mongo import connect, write_one, read_all
import time
import re

SITE = 'https://www.bloomberg.com/'
TYPE = 'bloomberg'
QUERY = 'bitcoin'
URL = 'https://www.ya.ru'


def get_urls_over_filter(query, count=10, newest=True, page=1):
    """ Return list URLs
    over Query, return list urls.
    Keyword arguments:
    newest -- this part filter in bloomberg
    page -- this with how page start going
    count -- len list URLs
    """
    list_url = []
    if newest:
        sort = 'time:desc'
    else:
        sort = 'time:asc'
    end_time = datetime.now(timezone('UTC'))
    end_time = '{}Z'.format(end_time.strftime('%Y-%m-%dT%H:%M:%S'))
    filter_url = '{}search?query={}&sort={}&end_time={}&page='.format(SITE, query, sort, end_time)
    while count > len(list_url):
        filter_url += str(page)
        time.sleep(5)
        html = get_html(filter_url)
        soup = BeautifulSoup(html, 'html.parser')
        if soup.findAll('h1', 'search-result-story__headline'):
            for h1 in soup.findAll('h1', 'search-result-story__headline'):
                link = h1.find('a')['href']
                if not re.search('/videos/|/audio/', link):
                    list_url.append(link)
        else:
            print('NOT FOUND URLS ON PAGE {}'.format(page))
            return
        print('ANALISE SUCCESS: count urls: "{}" page: "{}" func: "get_urls_over_filter"'.format(len(list_url), page))
        page += 1
    return list_url[:count]


def get_text(url):
    """Return dict with [paragraphs] or text
    try find all <p>text</p> else return basic article
    Position arguments:
    url -- link articles
    """
    article = {
        'url': url,
        'type': TYPE,
        'query': QUERY,
        'title': '',
        'body': '',
        'date': '',
    }
    time.sleep(5)
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    dict_article = get_article(soup)
    article.update(dict_article)
    return article


def get_article(soup):
    """Return dict article
    try find title, body, datetime article
    this parents function get_text
    Position args:
    soup -- obj Beautiful soup
    """
    article = {}
    titles = soup.findAll('h1')
    for title in titles:
        if title.span:
            article['title'] = title.span.text
    div_body = soup.find('div', 'body-copy')
    if div_body:
        article['body'] = [x.text for x in div_body.findAll('p')]
    date_str = soup.find('time', 'article-timestamp')
    if date_str:
        date_str = date_str['datetime']
        date_str = date_str.split('T')[0]
        article['date'] = datetime.strptime(date_str, '%Y-%m-%d')
    return article


def save_newest_urls():
    """Return last newest urls
    Go to read all link's in mongodb
    While get url not in url mongodb
    i run query_filter by newest filter
    and save in mongo.
    """
    my_connect = connect()
    articles = read_all(my_connect, 'articles')
    if articles:
        list_url = [article['url'] for article in articles]
    else:
        list_url = []
    page = 0
    count_urls = 0
    while True:
        page += 1
        for url in get_urls_over_filter(QUERY, page=page):
            if url not in list_url:
                print("URL WRITE IN MONGODB {}".format(url))
                write_one(my_connect, {'url': url, 'type': TYPE, 'query': QUERY, 'title': '', 'body': '', 'date': ''})
                count_urls += 1
            else:
                print("COUNT NEWEST URLS {}".format(count_urls))
                return


def get_url_and_save_article(count=30):
    """Return True or False
    Go in mongodb and get 30:default dict with empty body
    next step take url and get article.
    next strp save in db
    if not articles with empty body: return False
    """
    mongo = connect()
    urls = list(mongo.articles.find({'body': ''})[:count])
    if len(urls) == 0:
        print("NOT FOUND EMPTY ARTICLE IN MONGODB, MAYBE NOTHING GET")
        return False
    for mongo_dict in urls:
        mongo_dict['latest_check'] = 'DATA CHECK: {}'.format(datetime.now().strftime('%Y-%m-%d'))
        url = mongo_dict['url']
        article = get_text(url)
        if not article['body']:
            print("ATTENTION NOT BODY ARTICLE, MAYBE YOU ARE BLOCKED url: {}".format(url))
        else:
            print("FIND ARTICLE: '{}', url: '{}'".format(article['title'], url))
        mongo_dict.update(article)
        mongo.articles.save(mongo_dict)
    return True


if __name__ == '__main__':
    # Run when you want check newest urls and save in mongodb
    save_newest_urls()
    # Run when you want go in mongodb and write in article for empty body
    while True:
        status = get_url_and_save_article()
        if not status:
            break
    print("ENDED")
