from bs4 import BeautifulSoup
import requests
from datetime import datetime


URL = "https://www.securitylab.ru/news/"

HEADERS = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36"
}

def get_request(url,params=''):
    req=requests.get(url=URL,headers=HEADERS, params=params)
    return req

def get_data(html):
    soup=BeautifulSoup(html, "html.parser")
    items=soup.find_all("a", class_= 'artical-card')
    news = []
    date_time = datetime
    for item in items:
        news.append(
            {
                "title": item.find("h2", class_='artical-card-title').get_text(),
                "link": URL + item.find("a", class_='an').get('href'),
                "des": item.find("p").get_text(),
                "date_time": item.find("time").get("datetime"),


            }
        )
    print(news)
def news_script():
    html=get_request(URL)
    if html.status_code == 200:
        anime=[]
        for page in range(0,1):
            html = get_request(f"{URL}latest/{page}")
            anime.extend(get_data(html.text))
            return anime
    else:
        raise Exception('Error in parser!')
print(news_script)