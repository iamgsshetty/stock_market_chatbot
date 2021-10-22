import requests

def stocknews():
    # stock news api
    main_url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=b827efaa651d4518b26156116dc4cded"

    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()

    s_news = ""
    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article[:10]:
        results.append(ar["title"])

    for i in article:
        s_news+=("Title: " + str(i['title']) + "\n" +
              "Description: " + str(i['description']) + "\n" +
              "URL: " + i['url'] + "\n")

    return s_news

