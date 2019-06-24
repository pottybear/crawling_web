from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def search_engine(text) :
    driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe')
    driver.get('https://map.naver.com/')
    driver.find_element_by_id('search-input').send_keys(text)
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/fieldset/button').click()
    
    # WebDriverWait를 이용해 class명이 lst_site인 태그가 로드 될 때까지 10초 대기
    # 로드 불가한 경우엔 TimeOut 오류 출력
    # 완료한 뒤에는 driver 종료
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.lst_site'))
        )
        #받아온 내용을 BS로 파싱
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    except TimeoutException:
        print('Time Out')
    finally:
        driver.quit()
    
    shop = soup.select('dl > dt > a')
    
    c = 1
    for i in shop :        # 해당 장소 이름 출력 for문 
        print(str(c) + ". " + i.text)
        c += 1
    
    shop_id = []
    for i in range(len(shop)) :
        # find의 attrs 속성을 이용하면 특정 elements에 접근가능하다. 크롤링하고자하는 html은 data-id에 찾고자하는 장소의 id번호가 담겨있음.
        # 접근한 최종 데이터에 [1:] 슬라이싱을 통해 앞에 's'를 삭제해줌 
        #shop_id.append( soup.find("ul",{"class" : "lst_site"}).find_all("li", attrs = {"data-id" : True})[i]["data-id"][1:] )    
        # CSS selector로 좀 더 간단하게 구현
        shop_id.append(soup.select('ul.lst_site > li')[i].get('data-id')[1:])
    return shop_id

txt = input('검색어를 입력하세요 : ')       

shop_id = search_engine(txt)   

choice = int( input("원하시는 장소를 선택하세요 : " ) )

print("https://map.naver.com/local/siteview.nhn?code=" +shop_id[choice - 1])