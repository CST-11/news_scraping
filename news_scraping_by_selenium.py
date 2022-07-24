
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

keyword= input("Please enter keyword:")


def search_by_XPATH(myList_1):
    for k in range(len(myList_1)):
        driver = webdriver.Chrome(r"C:\Users\user\PycharmProjects\web_scraping\chromedriver.exe")
        driver.get(myList_1[k]['url'])
        driver.implicitly_wait(15)
        elem = driver.find_elements(By.XPATH, myList_1[k]['XPATH'])
        print(myList_1[k]['media'])
        for i in elem:
            if keyword in i.text:
                print(i.text)
                print(i.get_attribute("href"))
        print('')
        driver.quit()

myList_1 = [{"media": "商台","url":"https://www.881903.com/news/local", "XPATH":"//a[@class='news-grid__headline']"},
            {"media": "TVB","url":"https://news.tvb.com/tc/local", "XPATH":"//a[.//h3]"},
            {"media": "Cable TV","url":"https://www.i-cable.com/category/%E6%96%B0%E8%81%9E%E8%B3%87%E8%A8%8A/%E6%B8%AF%E8%81%9E/", "XPATH":"//h4[@class='post-title']/a"},
            {"media": "Now TV","url":"https://news.now.com/home/local", "XPATH":"//a[@class='newsWrap clearfix']"},
            {"media": "文匯網","url":"https://www.wenweipo.com/immed/hongkong", "XPATH":"//div[@class='story-item-title text-overflow']/a"},
            {"media": "點新聞","url":"https://www.dotdotnews.com/immed/hknews", "XPATH":"//div[@class='text']/h2/a"}]

#myList_3 = [{"media": "東方","url":"https://hk.on.cc/hk/news/index.html", "XPATH":"//div/h1/a"}]

search_by_XPATH(myList_1)

