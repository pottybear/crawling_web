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
    shop = {}
    driver.get(url)
    wait(driver, By.CSS_SELECTOR, '.list_wrapper')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    sh = soup.select("a.name")

    c = 1
    for i in sh:
        shop[c] = [i.get("title"), i.get("href")]
        print(str(c) + ". " + i.get("title"))
        c += 1
    return shop

def select_shop():
    n = int(input('원하시는 장소의 번호를 입력하세요 : '))
    # 한 페이지에 가게는 20개이므로, 입력 받은 수가 20을 넘으면 재입력
    while n > 20:
        print('리스트 안의 번호를 선택해주세요')
        n = int(input('원하시는 장소의 번호를 입력하세요 : '))
    print(shop[n][0] + ' : ' + shop[n][1])

# headless Chrome 사용 위한 옵션
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe', chrome_options=options)

s = input('검색어를 입력하세요 : ')
url = 'https://store.naver.com/restaurants/list?page=1&query=' + parse.quote(s)

shop = search_engine(url)
select_shop()

while True:
    c = input('종료하시려면 n, 다른 가게를 보려면 y, 가게 목록을 다시 보려면 s을 입력해주세요 : ')
    if c == 'n':
        driver.quit()
        break
    elif c == 'y':
        select_shop()
    elif c == 's':
        for n in range(1, len(shop) + 1):
            print(str(n) + '. ' + shop[n][0])
    else:
        print('잘못 입력하셨습니다')