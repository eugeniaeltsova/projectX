import requests


def get_html(url):
    """return page HTML.text for get url"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        proxies = dict(http='socks5://127.0.0.1:1234',
                       https='socks5://127.0.0.1:1234')
        result = requests.get(url, headers=headers, proxies=proxies)
        return result.text
    except Exception as err:
        with open(FILE_ERROR, 'a', encoding='utf-8') as f:
            f.write(str(err) + '\n')
        return False