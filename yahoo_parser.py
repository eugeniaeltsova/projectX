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

html = get_html("https://finance.yahoo.com/quote/BTCUSD=X/")
bs = BeautifulSoup(html, "html.parser")

# print (bs.prettify())

# for link in bs.find_all('a', class_="qa-heading-link lx-stream-post__header-link"):
#     print(link["href"])


# for title in bs.find_all("li", class_="u-faux-block-link"):
#     #print (title)
#     link = title.find ("a", {'data-link-name': 'article'})
#     print (link.attrs['href'])

   