from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(login_url)
time.sleep(3)

my_id = 'sue555'
my_pw = 'navsue980329!'

#아이디와 비밀번호 입력(자바스크립로 값을 넘겨줘서 우회하여 로그인)
driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")
time.sleep(1)

driver.find_element_by_id('log.login').click()
time.sleep(1)

comu_url = 'https://cafe.naver.com/codeuniv'
driver.get(comu_url)
time.sleep(3)

driver.find_element_by_id('menuLink90').click()
time.sleep(1)

#프레임 전환
driver.switch_to.frame('cafe_main')
time.sleep(1)

#게시물 클릭
driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a[1]').click()
time.sleep(1)

#게시물 내용 출력 ~ '다음글'버튼 클릭 반복
for i in range(1,21):
    content = driver.find_element_by_css_selector('div.se-component-content').text
    print('<', i, '번째 글>')
    print(content)
    driver.find_element_by_css_selector('a.BaseButton.btn_next.BaseButton--skinGray.size_default').click()
    time.sleep(1)

driver.close()
