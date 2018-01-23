
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import dateparser
from save_mongo import connect, write_one


start_url = "https://www.huffingtonpost.com/topic/bitcoin"

def get_html(start_url):
    # возвращает html для url и записывает сообщения об ошибках в файл errors_html.txt
    # returns html by url and writes error notifications into the errors_html.txt
    try:
        result = requests.get(start_url,  headers={'Accept-Encoding': 'identity', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'})
        return result

    except Exception as err:
        with open('errors_html.txt', 'a', encoding='utf-8') as f:
            f.write(str(err) + '\n')
        return False


def get_articles(html):
    # создает словарь с ключами ссылка, текст, заголовок и дата выхода статьи, соединяется с бд и записывает документ в бд
    # writes dict with keys link, text, title and date of the article, connects to db, writes the dict as doc into the db
    bs = BeautifulSoup(html.text, "html.parser")
    doc = []
    db = connect()
    for articles in bs.find_all("h2", class_="card__headline js-card-headline"):
        link = "{}{}".format("https://www.huffingtonpost.com", articles.find("a").attrs['href']) 
        title = articles.text
        html = get_html(link)
        bs = BeautifulSoup(html.text, "html.parser")
        article = bs.find("div", class_="entry__text js-entry-text bn-entry-text yr-entry-text")
        try:
            body = [x.text for x in article.find_all('p')]
        except Exception:
            pass

        article_time = bs.find('span', class_="timestamp__date--published")
        date = dateparser.parse(article_time.text) if article_time.text else None
        date = str(date.date()) 

        art = {"link" : link, "title" : title, "issue_date" : date, "text" : body}
        db.huffpost.save(art)
        doc.append(art)
        print (title)
    return doc


def collect_pages():
    # проходит по urls всех страниц от первой до последней, собирает все статьи и отправляет их в бд
    # goes through urls of all requested pages, collects articles and saves them in db
    
    i = 1
    for i in range(i, i+1):
        url = "{}?page={}".format(start_url, str(i))
        html = get_html(url)
        if html.status_code != 404:
            i += 1
    
        get_articles(html)

        

if __name__ == '__main__':
    collect_pages()