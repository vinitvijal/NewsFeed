from itertools import count
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='e5d9a31db0bf4bd38783bd79c1a57753')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(language='en',
                                          country='in')

# dic = {}

# no_of_results = top_headlines['totalResults']
headlines = top_headlines['articles']
# count = 1

print(headlines[1].keys())
# # for i in range(10):     
#     current_headline = headlines[i]
#     print()
#     print(str(i+1) + ' : ' + current_headline['source']['name'])
#     print()
#     print('Title : ' + current_headline['title'])
#     print()
#     print()

