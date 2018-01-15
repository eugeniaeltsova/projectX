from bs4 import BeautifulSoup

URL = 'https://www.theguardian.com/technology/bitcoin?page=4'
SELECT_DIV = 'fc-container--rolled-up-hide fc-container__body' # find inside block
ATTRS = {
    "class": "u-faux-block-link__overlay js-headline-text",
    "data-link-name": "article"
}


def get_links_for_page(page):
    """return list links on page_url for parse"""
    soup = BeautifulSoup(page, 'html.parser')
    containers = soup.find_all('div', class_=SELECT_DIV)
    list_attrs = []
    for container in containers:
        list_attrs += container.find_all('a', attrs=ATTRS)
    return [list_attr['href'] for list_attr in list_attrs]


if __name__ == '__main__':
    from article_parse import get_html
    page = get_html(URL)
    print(get_links_for_page(page))
