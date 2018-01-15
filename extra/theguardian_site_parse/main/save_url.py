
# This is script save url's for site guardian and
# put in file "urls.txt" links. For example:
# ...
# https://www.theguardian.com/world/2013/mar/22/silk-road-online-drug-marketplace
# https://www.theguardian.com/business/2013/mar/04/bitcoin-currency-of-vice
# ...


from extra.theguardian_site_parse import get_html
from extra.theguardian_site_parse import get_links_for_page


MAIN_URL = 'https://www.theguardian.com/technology/bitcoin'
LIST_URL = ['{}?page={}'.format(MAIN_URL, x) for x in range(21)]


open('urls.txt', 'w').write("")
for url in LIST_URL:
    page = get_html(url)
    links = get_links_for_page(page)
    with open('urls.txt', 'a') as f:
        for link in links:
            f.write(link + '\n')
