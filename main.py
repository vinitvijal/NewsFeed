from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='e5d9a31db0bf4bd38783bd79c1a57753')

top_headlines = newsapi.get_top_headlines(language='en',
                                          q='India Russia',
                                          country='in')

# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# # /v2/top-headlines/sources
sources = newsapi.get_sources()


print(top_headlines)