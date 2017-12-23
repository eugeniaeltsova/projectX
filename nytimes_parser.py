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

html = get_html("https://www.nytimes.com/topic/subject/bitcoin")
bs = BeautifulSoup(html, "html.parser")
# print (bs.prettify())
for title in bs.find_all("div", class_="story-body"):
    # print (title)
    link = title.find ("a", {'class': 'story-link'})
    print (link.attrs['href'])

# выдает разные результаты каждый раз