from bs4 import BeautifulSoup
import requests
import datetime

today = datetime.date.today()

keywords = [keyword.strip() for keyword in input("Enter keywords that you want, separated by commas:").replace("，",",").replace("/",",").replace("\\",",").split(",") if keyword.strip()]

check=0
for i in range((today - datetime.timedelta(days=30)).toordinal(), today.toordinal()):
    fetch_date = datetime.date.fromordinal(i)
    link = f"http://www.macaodaily.com/html/{fetch_date.year}-{str(fetch_date.month).zfill(2)}/{str(fetch_date.day).zfill(2)}/node_1.htm"
    res = requests.get(link)
    if res.status_code == 404:
        continue
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, features="html.parser")
    all_articles = soup.find('div',{'id':'all_article_list'}).find_all('div', {"class": 'listblock'})
    for article_box in all_articles:
        this_titles = article_box.find_all('a')
        for this_title in this_titles:
            if any(keyword in this_title.text for keyword in keywords):
                print(f"{fetch_date}: {this_title.text}")
                check = 1
if check == 0:
    print("No news with given keywords found")