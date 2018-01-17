start_url = "https://www.theguardian.com/technology/bitcoin"
def parse():
    html = get_html(start_url)
    articles = get_articles(html)
    save_articles(articles)

def get_html(start_url):
    # returns html by url and writes error notifications into the errors_file
    import requests

    try:
        result = requests.get(start_url)
        return result.text
    except Exception as err:
        with open('errors_html.txt', 'a', encoding='utf-8') as f:
            f.write(str(err) + '\n')
        return False

def get_articles(html):
    #returns link, text and date of the article
    # заголовок нам не нужен, лучше вывести количество просмотров
    from datetime import datetime
    from bs4 import BeautifulSoup
    # from ..storage.save_mongo import write_one, connect
    html = get_html(start_url)
    bs = BeautifulSoup(html, "html.parser")
    for articles in bs.find_all("a", class_="u-faux-block-link__overlay js-headline-text"):
        
        link = articles.attrs['href']
        title = articles.text
        
        
        html = get_html(link)
        bs = BeautifulSoup(html, "html.parser")

        article = bs.find("div", class_="content__article-body from-content-api js-article__body")
        try:
            body = [x.text for x in article.find_all('p')]
            return body
        except Exception:
            pass



        article_time = bs.find('time', attrs = {'itemprop': 'datePublished'})
        article_date = article_time['datetime'].split('T')[0]
        date = datetime.strptime(article_date, '%Y-%m-%d') #кроме даты еще в конце появляется 00:00:00
        print (body, title, link, date)

        

# get_articles("https://www.theguardian.com/technology/bitcoin?page=1")

def collect_pages():
    for i in range (1,23):
        url = "https://www.theguardian.com/technology/bitcoin?page=" + str(i)
        get_articles(url)

collect_pages()


