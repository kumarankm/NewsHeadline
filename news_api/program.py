import requests
api_key = "912e84ae13e64bf6b83737197fb741c4"


def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=912e84ae13e64bf6b83737197fb741c4"
    news = requests.get(main_url).json()
    # print(news)
    article = news["articles"]
    # print(article)

    news_article = []
    for arti in article:
        news_article.append([arti['title'], arti['url']])
        print(news_article)


news()
