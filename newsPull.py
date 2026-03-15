from bs4 import BeautifulSoup as bs 
import requests


#pull data from wsvn news for testing

news_url = "https://wsvn.com/"
req = requests.get(news_url)
if req.status_code <= 200:
    html = bs(req.content,'html.parser')
    divs = html.find_all('div')
    
    title = html.find_all('a',class_='wp-block-article-list__link')
    re_link_list = []
    for linkz in title:
        re_link_list.append(linkz.get('href'))
    for titles, links in zip(title,re_link_list):
        print(f"title:{titles}-->{links}")
    #for titles in title:
    #    print(titles.get('href'))
    #for titles in title:
    #    print(titles.get('href')) 
else:
    print('something went wrong')
