from selenium import webdriver
from bs4 import BeautifulSoup


def search_engine(text) :
    driver = webdriver.Chrome(r'C:\Users\KIH\Desktop\chromedriver.exe')
    driver.implicitly_wait(30) # 을지로3가 맛집 검색의 경우 -> 카페 키워드를 이용한 검색보다 정보를 찾는데 더 많은 시간이 걸리게됨. 따라서 wait 시간이 짧을경우 데이터를 못받아오는 경우가 있음.  (3 -> 30 으로 늘려주었음)
    driver.get('https://map.naver.com/')
    driver.find_element_by_id('search-input').send_keys(text)
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/fieldset/button').click()

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    shop = soup.select('dl > dt > a')
    
    c = 1
    for i in shop :        # 해당 장소 이름 출력 for문 
        print(str(c) + ". " + i.text)
        c += 1
    
    shop_id = []
    for i in range(len(shop)) :   # find의 attrs 속성을 이용하면 특정 elements에 접근가능하다. 크롤링하고자하는 html은 data-id에 찾고자하는 장소의 id번호가 담겨있음. 접근한 최종 데이터에 [1:] 슬라이싱을 통해 앞에 's'를 삭제해줌 
        shop_id.append( soup.find("ul",{"class" : "lst_site"}).find_all("li", attrs = {"data-id" : True})[i]["data-id"][1:] )    
   
   
    return shop_id

        
txt = input('검색어를 입력하세요 : ')       

shop_id = search_engine(txt)   

choice = int( input("원하시는 장소를 선택하세요 : " ) )

print("https://map.naver.com/local/siteview.nhn?code=" +shop_id[choice - 1])
