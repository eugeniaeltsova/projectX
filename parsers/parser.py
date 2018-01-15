import requests


def get_html(url):
    """return page HTML.text for get url"""
    try:
        result = requests.get(url)
        return result.text
    except Exception as err:
        with open(FILE_ERROR, 'a', encoding='utf-8') as f:
            f.write(str(err) + '\n')
        return False