from bs4 import BeautifulSoup
import requests



def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except requests.exceptions.RequestsException:
        print("oops")
        return False
html = get_html("https://www.theguardian.com/technology/bitcoin")
bs = BeautifulSoup(html, "html.parser")

def get_link():
    for title in bs.find_all("li", class_="u-faux-block-link"):
        #print (title)
        l = title.find ("a", {'data-link-name': 'article'})
        link = link.attrs['href']

    return link


def get_article(link):
    
    html = get_html(link)
    bs = BeautifulSoup(html, "html.parser")
    result = requests.get(link)
    article = []

    if result.status_code == 200:
        for text in bs.find_all("div", class_ = "content__article-body from-content-api js-article__body"):
            text_p = text.find_all("p")
            # print(type(text_p))
            for i in text_p:
                print (i.text)
                # print (type(i))
                article.append(i.text)
        str_article = ''.join(article)
        with open('file.txt', 'w') as f:
            f.write(str_article)

    else:
        return "Error: {} code".format(result.status)
    
    return article

link = 'https://www.theguardian.com/business/nils-pratley-on-finance/2017/dec/07/gvc-and-ladbrokes-coral-david-gambles-on-goliath'
get_article(link)



