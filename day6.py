from bs4 import BeautifulSoup
import requests

bbc_url = 'https://www.bbc.com/news'
raw = requests.get(bbc_url)

soup = BeautifulSoup(raw.text, 'html.parser')

mostRead = soup.find_all('span', class_='gs-c-promo-heading__title gel-pica-bold')
#가장 많이 본 기사의 제목이 들어있는 span 태그를 변수에 저장

for title in mostRead:
    print(title.text)
#가장 많이 본 기사의 제목 출력하기
