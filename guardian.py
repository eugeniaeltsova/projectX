from datetime import datetime
from bs4 import BeautifulSoup
import requests
import dateparser
from save_mongo import connect, write_one
start_url = "https://www.theguardian.com/technology/bitcoin"



def get_html(start_url):
    # возвращает html для url и записывает сообщения об ошибках в файл errors_html.txt
    # returns html by url and writes error notifications into the errors_html.txt
    import requests

    try:
        result = requests.get(start_url)
        return result.text
    except Exception as err:
        with open('errors_html.txt', 'a', encoding='utf-8') as f:
            f.write(str(err) + '\n')
        return False

def get_articles(html):
    # создает словарь с ключами ссылка, текст, заголовок и дата выхода статьи, соединяется с бд и записывает документ в бд
    # writes dict with keys link, text, title and date of the article, connects to db, writes the dict as doc into the db
    bs = BeautifulSoup(html, "html.parser")
    doc = []
    db = connect()
    for articles in bs.find_all("a", class_="u-faux-block-link__overlay js-headline-text"):
        link = articles.attrs['href']
        title = articles.text
        html = get_html(link)
        bs = BeautifulSoup(html, "html.parser")
        article = bs.find("div", class_="content__article-body from-content-api js-article__body")
        try:
            body = [x.text for x in article.find_all('p')]
        except Exception:
            pass

        article_time = bs.find('time', attrs = {'itemprop': 'datePublished'})
        article_date = article_time['datetime'].split('T')[0]
        date = dateparser.parse(article_date) if article_time.text else None
        date = str(date.date()) 

        art = {"link" : link, "title" : title, "issue_date" : date, "text" : body}
        db.huffpost.save(art)
        doc.append(art)
        print (title, date)
    return doc
  

       

        
def collect_pages(page):
    # проходит по urls всех страниц от первой до последней, собирает все статьи и отправляет их в бд
    # goes through urls of all requested pages, collects articles and saves them in db
    for i in range(1, page):
        url = "{}?page={}".format(start_url, str(i))
        html = get_html(url)
        print(get_articles(html))

if __name__ == '__main__':
    collect_pages(page = 23)


