start_url = "https://www.theguardian.com/technology/bitcoin"
def parse():
    html = get_html(start_url)
    articles = get_articles(html)
    save_articles(articles)

def get_html(start_url):
    # returns html by url and writes error notifications into the errors_file
    try:
        result = requests.get(url)
        return result.text
    except Exception as err:
        with open(errors_html, 'a', encoding='utf-8') as f:
            f.write(str(err) + '\n')
        return False

def get_articles(html):
    #returns link, text and date of the article
    # заголовок нам не нужен, лучше вывести количество просмотров
    from datetime import datetime
    html = get_html(start_url)
    bs = BeautifulSoup(html, "html.parser")
    for title in bs.find_all("li", class_="u-faux-block-link"):
        link = title.find ("a")
        link = link.attrs['href']
       
        html = get_html(link)
        bs = BeautifulSoup(html, "html.parser")

        article = bs.find("div", class_="content__article-body from-content-api js-article__body").text
        article_time = bs.find('time', attrs = {'itemprop': 'datePublished'})
        article_date = article_time['datetime'].split('T')[0]
        date = datetime.strptime(article_date, '%Y-%m-%d') #кроме даты еще в конце появляется 00:00:00