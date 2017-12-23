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

html = get_html("http://edition.cnn.com/search/?q=bitcoin")
bs = BeautifulSoup(html, "html.parser")
# print (bs.prettify())
for title in bs.find_all("h3", class_="cnn-search__result-contents"):
    print (title)
  # через форму поиска не работает