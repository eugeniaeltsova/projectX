
html = get_html("https://www.theguardian.com/technology/bitcoin")
bs = BeautifulSoup(html, "html.parser")

def get_link():
    for title in bs.find_all("li", class_="u-faux-block-link"):
        #print (title)
        l = title.find ("a", {'data-link-name': 'article'})
        link = link.attrs['href']

    return link