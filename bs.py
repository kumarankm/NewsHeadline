from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
new_url = "https://news.google.com/news/rss"
Client = urlopen(new_url)
xml_page = Client.read()
Client.close()
soup_page = soup(xml_page, "xml")
news_list = soup_page.findAll("item")
for news in news_list:
    print(news.title.text)
