from theguardian_site_parse.article_parse import get_html
from theguardian_site_parse.url_parse import get_links_for_page

MAIN_URL = 'https://www.theguardian.com/technology/bitcoin'
LIST_URL = ['{}?page={}'.format(MAIN_URL, x) for x in range(21)]


for url in LIST_URL:
    page = get_html(url)
    links = get_links_for_page(page)
    with open('urls.txt', 'a') as f:
        for link in links:
            f.write(link + '\n')
