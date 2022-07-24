
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

keyword= input("Please enter keyword:")

def search_by_direct_XPATH(myList_1):
    for k in range(len(myList_1)):
        driver = webdriver.Chrome(r"C:\Users\user\PycharmProjects\web_scraping\chromedriver.exe")
        driver.get(myList_1[k]['url'])
        driver.implicitly_wait(15)
        elem = driver.find_elements(By.XPATH, myList_1[k]['XPATH'])
        links_and_titles = []
        for i in elem:
            links_and_titles.append(i.text + " " + i.get_attribute('href'))
        match = [s for s in links_and_titles if keyword in s]
        print(myList_1[k]['media'])
        print(match)
        print('')
        driver.quit()

myList_1 = [{"media": "Cable","url":"https://www.i-cable.com/category/%E6%96%B0%E8%81%9E%E8%B3%87%E8%A8%8A/%E6%B8%AF%E8%81%9E/", "XPATH":"//h4[@class='post-title']/a"},
            {"media": "文匯網","url":"https://www.wenweipo.com/immed/hongkong", "XPATH":"//div[@class='story-item-title text-overflow']/a"},
            {"media": "點新聞","url":"https://www.dotdotnews.com/immed/hknews", "XPATH":"//div[@class='text']/h2/a"}]

search_by_direct_XPATH(myList_1)

def search_by_two_XPATH(myList_2):
    for k in range(len(myList_2)):
        driver = webdriver.Chrome(r"C:\Users\user\PycharmProjects\web_scraping\chromedriver.exe")
        driver.get(myList_2[k]['url'])
        driver.implicitly_wait(15)
        elem = driver.find_elements(By.XPATH, myList_2[k]["XPATH_LINK"]) + driver.find_elements(By.XPATH, myList_2[k]["XPATH_TITLE"])
        links_and_titles  = []
        for i in elem:
            links_and_titles.append(i.text)
            links_and_titles.append(str(i.get_attribute('href')))
        matches = [s for s in links_and_titles if keyword in s]
        print(myList_2[k]["media"])
        for match in matches:
            index_of_match = links_and_titles.index(match)
            index_of_match_link = index_of_match + 1
            print(match)
            print(links_and_titles[index_of_match_link])
        print('')
    driver.quit()

myList_2 = [{"media": "商台即時","url":"https://www.881903.com/news/local", "XPATH_LINK":"//a[@class='news-grid__headline']", "XPATH_TITLE":"//a[@class='news-grid__headline']/span"},
            {"media": "NowTV","url":"https://news.now.com/home/local", "XPATH_LINK":"//a[@class='newsWrap clearfix']", "XPATH_TITLE":"//div[@class='newsTitle']"}]

search_by_two_XPATH(myList_2)



def TVB():
    driver = webdriver.Chrome(r"C:\Users\user\PycharmProjects\web_scraping\chromedriver")
    driver.get("https://news.tvb.com/tc/local")
    driver.implicitly_wait(25)
    elem = driver.find_elements(By.TAG_NAME, "a") + driver.find_elements(By.XPATH, "//div[@class='entryContent']/h3")
    for i in elem:
        print(i.text)
        print(i.get_attribute("href"))
    driver.quit()

