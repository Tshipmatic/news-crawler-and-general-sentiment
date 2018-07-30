import requests
from bs4 import BeautifulSoup

def get_time(suburl):
    url = requests.get(suburl).text
    soup = BeautifulSoup(url, 'lxml')
    time = soup.find("div",class_="article-pub-date").contents[0].strip()
    return time

def sentiment(suburl):
    url = requests.get(suburl).text
    soup = BeautifulSoup(url, 'lxml')
    
    texts = soup.find('div', class_='text').text.strip()
    from textblob import TextBlob  
    
    total = len(TextBlob(texts).sentences)
    pos,neg,neu = 0,0,0
    
    for sentence in TextBlob(texts).sentences:
        polar = TextBlob(str(sentence)).sentiment.polarity
        
        if polar<0:
            neg += 1 
        
        elif polar>0:
            pos +=1
            
        else:
            neu +=1
    positive = pos/total
    negative = neg/total
    neutral = neu/total
    print('Overall sentiment of is')
    print("pos:",round(positive,2),"\t","neg:",round(negative,2),"\t","neu:",
          round(neutral,2))
    print(20*"===")
        
        









root_url = "https://www.businesslive.co.za/markets"
url = requests.get("https://www.businesslive.co.za/markets").text
soup = BeautifulSoup(url, 'lxml')
print("FEARURED")
#featured_news = soup.find("span",class_="featured_story")
featured_news = soup.find("span",class_="featured-title")
featured_url = root_url+featured_news.find('a')["href"]

print(" ".join(featured_news.a.text.split())+".")
print(get_time(featured_url))
print(featured_url)
print( sentiment(featured_url))
print("=================end of featured===================\n")

#headlines
headlines = soup.find_all('div',class_='article-text col-md-8')

print("\t HEADLINES:")
for headline in headlines:
    print(" ".join(headline.text.split())+".")
    print(get_time(root_url + headline.find('a')['href']))
    print(root_url + headline.find('a')['href'])
    print( sentiment(root_url + headline.find('a')['href']))
    print('\n') 




def get_time(suburl):
    url = requests.get(suburl).text
    soup = BeautifulSoup(url, 'lxml')
    time = soup.find("div",class_="article-pub-date").contents[0].strip()
    return time

def sentiment(suburl):
    url = requests.get(suburl).text
    soup = BeautifulSoup(url, 'lxml')
    
    texts = soup.find('div', class_='text').text.strip()
    from textblob import TextBlob  
    
    total = len(TextBlob(texts).sentences)
    pos,neg,neu = 0,0,0
    
    for sentence in TextBlob(texts).sentences:
        polar = TextBlob(str(sentence)).sentiment.polarity
        
        if polar<0:
            neg += 1 
        
        elif polar>0:
            pos +=1
            
        else:
            neu +=1
    positive = pos/total
    negative = neg/total
    neutral = neu/total
    print('Overall sentiment of is')
    print("pos:",round(positive,2),"\t","neg:",round(negative,2),"\t","neu:",
          round(neutral,2))
    print(20*"===")
        
        
        
        
        
    
    
    
    






