from distutils.log import error
from newsapi import NewsApiClient
import sys
import mysql.connector
from weather import init as weatherNews


mydb = mysql.connector.connect(
  host="brfytvylwdzhculozfq5-mysql.services.clever-cloud.com",
  user="uh06snweshud7gzj",
  password="24c1orUcFmlEOgctcpFH",
  database="brfytvylwdzhculozfq5"
)


def Save(sourceName, title, description, content, publishedAt, url):

    mycursor = mydb.cursor()

    sql = "INSERT INTO NewsFeeds (sourceName, title, description, content, publishedAt, url) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (sourceName, title, description, content, publishedAt, url)
    mycursor.execute(sql, val)

    mydb.commit()

    print("NewsFeed Saved !!!")


def SavedNews():
    def OptionsSaved():
        print()
        print()
        print('If You Want To Ready Any Article - SN. (1,2,3...) ')
        print('If You Want To Delete Any Article - (D1, D2, D12, D13....')
        print('To Main Menu : M')
    mycursor = mydb.cursor()

    mycursor.execute("SELECT SN, sourceName, title, description, publishedAt FROM NewsFeeds")

    myresult = mycursor.fetchall()

    for x in myresult: 
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        print(str(x[0]) + '. ' + x[1])
        print()
        print('Title : ' + x[2])
        print()
        print('Description : ' + x[3])
        print()
        print('Dated On : ' + x[4])
        print()
    OptionsSaved()
  
    answer = input('Your Option : ')
    if answer.isnumeric():
        sql = "SELECT SN, sourceName, title, description, content, publishedAt, url FROM NewsFeeds where SN Like %s"
        val = int(answer)

        mycursor.execute(sql, val)

        myresult = mycursor.fetchall()

        for x in myresult: 

            print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')
            print()
            print()
            print(str(x[0]) + '. ' + x[1])
            print()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('Title : ' + x[2])
            print()
            print('Description : ' + x[3])
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print()
            print()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print()
            
            print('Article : ' + x[4])
            print()
            print('Read More : ' + x[6])
            print()
            print('Published At : ' + x[5])
            print()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print()



    # Now Write Code For Input Options Here To See Data and Delete Data + Menu Next Previous Exit
       




newsapi = NewsApiClient(api_key='e5d9a31db0bf4bd38783bd79c1a57753')


query = ''
breaking = False
india = False
health =  False
sports = False
searching = False

def breaking_news(case=True,n=0,m=5):  
    if breaking == True:     
        top_headlines = newsapi.get_top_headlines(language='en')
    elif india == True:
        top_headlines = newsapi.get_top_headlines(language='en',country='in')
    elif sports == True:
        top_headlines = newsapi.get_top_headlines(language='en', category='sports')
    elif health == True:
        top_headlines = newsapi.get_top_headlines(language='en', category='health')
    elif searching == True:
        top_headlines = newsapi.get_everything(language='en', q=query)





        

    headlines = top_headlines['articles']

    def SingleHeadline(n):
        current_headline = headlines[n-1]
        print()
        print()
        print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')
        print()
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
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        
        print('Article : ' + current_headline['content'])
        print()
        print('Read More : ' + current_headline['url'])
        print()
        print('Published At : ' + current_headline['publishedAt'])
        print()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        sourceName, title, description, content, publishedAt, url =  current_headline['source']['name'], current_headline['title'], current_headline['description'], current_headline['content'], current_headline['publishedAt'], current_headline['url'] 
        print()
        print()
        print('  (S) - Save Article For Later    |     (M) - Main Menu.    |     (P) - Previous Menu.     |     (exit) - Exit.  ')
        print('')
        print('')
    
        menuSel = input('Select Option : ')
        if menuSel in ('S','s'):
            Save(sourceName, title, description, content, publishedAt, url)
        elif menuSel in ('M','m'):
            init()
        elif menuSel in ('P','p'):
            breaking_news()

        elif menuSel in ('exit','Exit', 'EXIT'):
            sys.exit(1)
        else:
            print('Wrong Input Try Again...')
            SingleHeadline(n)
        

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
        sourceName, title, description, content, url, publishedAt = SingleHeadline(int(Options))
        

    
    else:
        init()


def search():
    global india, health, sports, breaking, searching, query
    searching=True
    breaking=False
    india=False
    health=False 
    sports=False
    print()
    print()
    print()
    print('````````````````````````````````')
    searchWords = input('Search Topic : ')
    print('````````````````````````````````')
    print()
    print()
    print()
    query=searchWords
    breaking_news()





def news_of_india():
    global india, health, sports, breaking, searching
    searching=False    
    breaking=False
    india=True
    health=False 
    sports=False
    breaking_news()


def health_news():
    global india, health, sports, breaking, searching
    searching=False
    breaking=False
    india=False
    health=True 
    sports=False
    breaking_news()
    
def sports_news():
    global india, health, sports, breaking, searching
    searching=False
    breaking=False
    india=False
    health=False 
    sports=True
    breaking_news()


def init():
    print()
    print(' ~~~ Main Menu ~~~')
    print()
    print('1. World News')
    print('2. News of India')
    print('3. Health News')
    print('4. Sports News')
    print('5. Search Articles and News')
    print('6. Weather Updates (Beta)')
    print('7. Saved Articles')
    print()
    close = False
    try:
        option = input('Select Any Option : ')
        if option == 'exit':
            close = True
        elif int(option) in [1,2,3,4,5,6,7]:
            print()
            if option == '1':
                global breaking
                breaking = True
                breaking_news()
                
            elif option == '2':
                news_of_india()
            elif option == '3':
                health_news()
            elif option == '4':
                sports_news()
            elif option == '5':
                search()
            elif option == '6':
                weatherNews()
                init()
            elif option == '7':
                SavedNews()
        
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
    print()
    print('                NEWSFEED                ')
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()
    print()
    init()
    