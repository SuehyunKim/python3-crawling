from selenium import webdriver
import time

keyword = input('뉴스 검색 키워드 : ')

driver = webdriver.Chrome('./chromedriver')
news_url = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword
driver.get(news_url)
time.sleep(2)

#뉴스마다 번호를 붙여주는 변수
count = 0

for i in range(1,4):
    if i > 1:
        page = driver.find_element_by_xpath("//*[@id='content']/div[1]/div[2]/div[2]/div/span/a[" + str(i) + "]")
        page.click()
        time.sleep(2)

    ten_articles = driver.find_elements_by_css_selector('em.tit')

    for article in ten_articles:

        #'article'은 뉴스 기사 제목을 나타내는 HTML 요소이므로, text는 제목
        title = article.text
        #'article' 클릭하면 뉴스 기사 본문 페이지로 이동
        article.click()
        time.sleep(1)
        #'driver'를 뉴스 기사 본문 탭으로 전환
        driver.switch_to.window(driver.window_handles[-1])
        #기사 본문을 'content' 변수에 저장
        content = driver.find_element_by_id('articletxt').text
        #'content'를 '\n' 줄단위로 나누어 'seperate' 변수에 저장
        seperate = content.split('\n')
        count += 1
        print(f'< {count}번 뉴스 - {title} >') # 문자열 포매팅 - f'문자열{변수}문자열'
        for sep in seperate:
            # 공백은 출력하지 않음
            if sep != '':
                # 모든 sep 사이에 공백 한 칸씩 삽입하여 출력
                print(sep, end=' ')
            # 하나의 본문 내용을 출력하면 줄 바꿈
            print('\n')
        #새 탭 닫기
        driver.close()
        #처음 탭으로 다시 이동
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

driver.close()