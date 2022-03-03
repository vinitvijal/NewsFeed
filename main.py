from distutils.log import error
from tkinter import N
from newsapi import NewsApiClient
import sys

newsapi = NewsApiClient(api_key='e5d9a31db0bf4bd38783bd79c1a57753')


def breaking_news(case=True,n=0,m=5):
       
        # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(language='en',country='in')

    headlines = top_headlines['articles']

    def SingleHeadline(n):
        current_headline = headlines[n-1]
        print()
        print(str(n) + ' : ' + current_headline['source']['name'])
        print()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Title : ' + current_headline['title'])
        print()
        print('Description : ' + current_headline['description'])
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        print()
        print('Article : ' + current_headline['content'])
        print()
        print()
        print('Published At : ' + current_headline['publishedAt'])
        sourceName, title, description, content, publishedAt =  current_headline['source']['name'], current_headline['title'], current_headline['description'], current_headline['content'], current_headline['publishedAt'] 
        print()
        print()
        print('  (S) - Save Article For Later    |     (M) - Main Menu.    |     (P) - Previous Menu.')
        print('')
        print('')
        try:
            menuSel = input('Select Option : ')
            if menuSel in ('S','s'):
                Save(sourceName, title, description, content, publishedAt)
            elif menuSel in ('M','m'):
                init()
            elif menuSel in ('P','p'):
                breaking_news()
            else:
                raise error
        except:
            print('Wrong Input... Choose Correct')
            print()
            print()
            SingleHeadline(n)

            pass

    if case == False :
        n = 0 
        m = len(headlines)
    else:
        pass

    for i in range(n,m):     
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
    print()
    print()
    print('--> (N) - Next Page.')
    print('--> (P) - Previous Page.')
    print('--> (A) - All Headlines.')
    print('--> Select Any Headline By SN.')
    print('--> (exit) To Exit App')
    print()
    print()
    Options = input('Enter Your Input : ')
    if Options in ('A','a','All','all'):
        breaking_news(False)
    elif Options in ('N','n'):
        n += 5
        m += 5
        breaking_news(True,n,m)
    elif Options in ('P','p'):
        n -= 5
        m -= 5
        breaking_news(True,n,m)
    
    elif int(Options) in range(0,21):
        sourceName, title, description, content, publishedAt = SingleHeadline(int(Options))
        

    
    else:
        init()





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
    except :
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
    