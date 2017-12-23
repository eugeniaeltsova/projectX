from bs4 import BeautifulSoup
import requests

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        print(result.encoding)
        return result.text
    except requests.exceptions.RequestsException:
        print("oops")
        return False

html = get_html("https://www.rbc.ru/tags/?tag=Bitcoin")

bs = BeautifulSoup(html, "html.parser")

print (bs.prettify(formatter='html'))

#for title in bs.find_all("div", class_="search-item"):
#    print (title.encode('utf-8'))
    # link = title.find ("a", class_="search-item")
    # print (link.attrs['href'])
