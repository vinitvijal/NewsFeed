from distutils.log import error
from newsapi import NewsApiClient
import sys

newsapi = NewsApiClient(api_key='e5d9a31db0bf4bd38783bd79c1a57753')

def breaking_news():
        # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(language='en',
                                            country='in')

    no_of_results = top_headlines['totalResults']
    headlines = top_headlines['articles']
    
    for i in range(len(headlines)):     
        current_headline = headlines[i]
        print()
        print(str(i+1) + ' : ' + current_headline['source']['name'])
        print()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Title : ' + current_headline['title'])
        print()
        print('Description : ' + current_headline['description'])
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()




def init():
    print()
    print(' ~~~ Main Menu ~~~')
    print()
    print('1. Breaking News Live')
    print('2. News of India')
    print('3. Political News')
    print('4. Sports News')
    print('5. Search Articles and News')
    print()
    close = False
    try:
        option = input('Select Any Option : ')
        if option == 'exit':
            close = True
        elif int(option) in [1,2,3,4,5,6]:
            print()
            if option == '1':
                breaking_news()
            elif option == '2':
                news_of_india()
            elif option == '3':
                politics_news()
            elif option == '4':
                sports()
            elif option == '5':
                search()
        
        else:
            raise error
    finally:
        if close:
            pass
        else:
            print()
            print()
            print('Wrong Input Selected Try Again...')
            print()
            print()
            init()

    if close:
        sys.exit(1)

    

if __name__ == "__main__":
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('                NEWSFEED                ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()
    print()
    init()
    