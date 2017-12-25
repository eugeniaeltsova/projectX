from theguardian_site_parse.article_parse import get_html, get_article, save_in_file

URLS = 'urls.txt'
SET_URLS = ({link.rstrip() for link in open(URLS, 'r')})

count = 0
for url in SET_URLS:
    try:
        html = get_html(url)
        list_article = get_article(html)
        save_in_file(*list_article)
    except Exception as err:
        count += 1
        error = 'Error number {}: for next url {}\n got not article, \n {}'.format(count, url, err)
        with open('error.log', 'a') as f:
            f.write(error)
        print(error)
