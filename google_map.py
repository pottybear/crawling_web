from urllib import parse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait(driver, selector, name):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((selector, name))
        )        
    except TimeoutException:
        print('Time Out')

def search_engine(url) :
    shop = []
    driver.get(url)
    wait(driver, By.CSS_SELECTOR, '.section-listbox')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    sh = soup.select('h3.section-result-title > span')

    c = 1
    for i in sh:
        shop.append(i.text)
        print(str(c) + ". " + i.text)
        c += 1
    
    return shop


s = input('검색어를 입력하세요 : ')

# 구글은 url 파라미터로 검색어를 넘기는 방식
# 입력값에 url인코딩을 적용해서 url 값으로 입력
url = 'https://www.google.co.kr/maps/search/' + parse.quote(s)

driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe')
shop = search_engine(url)   

n = int(input('원하시는 장소의 번호를 입력하세요 : '))
while n > 20:
    print('리스트 안의 번호를 선택해주세요')
    n = int(input('원하시는 장소의 번호를 입력하세요 : '))

# 음식점 div를 클릭했을 때 동적으로 페이지가 넘어감
# 각 음식점 링크가 걸린 div의 xpath는 //*[@id="pane"]/div/div[1]/div/div/div[3]/div[n]
# n은 1부터 홀수로 증가
driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[3]/div[' + str(n * 2 - 1) + ']').click()