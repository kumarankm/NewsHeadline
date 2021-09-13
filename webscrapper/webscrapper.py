from requests_html import HTMLSession

session = HTMLSession()
url = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"

r = session.get(url)

r.html.render(sleep=1, scrolldown=5)
articles = r.html.find('article')
# print(articles)

newslist = []

for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        newsarticle = {
            'title': newsitem.text,
            'link': newsitem.absolute_links
        }
        newslist.append(newsarticle)
    except:
        pass
print(newslist)
