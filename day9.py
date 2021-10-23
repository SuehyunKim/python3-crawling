import requests
from bs4 import BeautifulSoup

keyword = input("뉴스 검색 키워드 : ")
count = 0

for page in range(1, 3):
    news_url = 'https://search.hankyung.com/apps.frm/search.news?query='+keyword+'&sort=DATE%2FDESC%2CRANK%2FDESC&period=ALL&area=ALL&mediaid_clust=HKPAPER&exact=&include=&except=&page=' + str(page)
    raw = requests.get(news_url)

    soup = BeautifulSoup(raw.text, 'html.parser')

    box = soup.find('ul', {'class' : 'article'})
    all_title = box.find_all('em', {'class' : 'tit'})
    all_date = soup.find_all('span', {'class' : 'date_time'})


    for title,date in zip(all_title,all_date):
        count += 1
        t = title.text
        print(count, '-', '[', date.text, ']', t.strip())
    print()