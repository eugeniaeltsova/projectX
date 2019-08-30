
# This is script walk in file "urls.txt"
# and save each article in dir "articles"
# If for some reason scripts will be crash in error.
# It's save error and url in file "error.log"


from extra.theguardian_site_parse import get_html, get_article, save_in_file

URLS = 'urls.txt'
SET_URLS = ({link.rstrip() for link in open(URLS, 'r')})


count = 0
open('error.log', 'w').write("")
for url in SET_URLS:
    try:
        html = get_html(url)
        list_article = get_article(html)
        list_article.append(url)
        save_in_file(*list_article)
    except Exception as err:
        count += 1
        error = 'Error number {}: for next url {}\n got not article, \n {}\n'.format(count, url, err)
        with open('error.log', 'a') as f:
            f.write(error)
        print(error, end=" ")
