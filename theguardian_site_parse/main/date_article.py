
# This script write in mongodb date PublishedArticle for each article
# Each result in mongodb, script walk in URL on website and search date publish
# When it found, it update and put back on mongodb


from theguardian_site_parse.article_parse import get_html, get_date
from theguardian_site_parse.administer_mongo import connect, update_one, read_all


obj = connect()
for article in read_all(obj, 'articles'):
    html = get_html(article['url'])
    date_article = get_date(html)
    article['datePublished'] = date_article
    if update_one(obj, {'_id': article['_id']}, article):
        print(' for article: {} success update date article: {} '.format(article['title'], date_article))
