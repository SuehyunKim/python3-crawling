from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('./chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

driver.find_element_by_css_selector('button.btn_switch___x4Tcl').click()
time.sleep(1)

f = open('./my_papago.csv', 'r', encoding='CP949')
rdr = csv.reader(f)
next(rdr)
my_dict = {}
for row in rdr:
    keyword = row[1]
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    output = driver.find_element_by_css_selector('div#txtTarget').text
    my_dict[keyword] = output

    driver.find_element_by_css_selector('textarea#txtSource').clear()

    print(my_dict[keyword], ':', keyword)

driver.close()
f.close()