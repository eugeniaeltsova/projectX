from parsers.parser import get_html
from datetime import datetime
from bs4 import BeautifulSoup

START_URL = "https://www.theguardian.com/technology/bitcoin"


def get_urls_on_page(html):
    pass


def get_articles(html):
    """Return dict article

    Position attribute:
    html -- text
    """

    bs = BeautifulSoup(html, "html.parser")
    for articles in bs.find_all("a", class_="u-faux-block-link__overlay js-headline-text"):
        link = articles.attrs['href']
        title = articles.text
        html = get_html(link)
        body = []
        bs = BeautifulSoup(html, "html.parser")
        article = bs.find("div", class_="content__article-body from-content-api js-article__body")
        try:
            body = [x.text for x in article.find_all('p')]
            return body
        except Exception:
            pass
        article_time = bs.find('time', attrs={'itemprop': 'datePublished'})
        article_date = article_time['datetime'].split('T')[0]
        date = datetime.strptime(article_date, '%Y-%m-%d')  # кроме даты еще в конце появляется 00:00:00
        print(body, title, link, date)


def collect_pages(page=1):
    """Return list
    """
    for i in range(1, page):
        url = "https://www.theguardian.com/technology/bitcoin?page=" + str(i)
        html = get_html(url)
        print(get_articles(html))


if __name__ == '__main__':
    collect_pages(4)