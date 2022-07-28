from bs4 import BeautifulSoup as bs
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


Path_of_Chromedriver = input("Please enter path of Chromedriver: ")
Path_of_output_file = input("Please enter path of output doc: ")
keyword = input("Please enter keyword: ")



testing_file = open(str(Path_of_output_file), "w", encoding='UTF-8')


def news_scraping (myList_BS):
    for k in range(len(myList_BS)):
        testing_file.write(myList_BS[k]['media'] + "\n" + "\n")
        result = requests.get(myList_BS[k]['url'] )
        soup = bs(result.content, "html.parser")

        list_of_tag_title = soup.find_all("a",attrs={"title" : re.compile(keyword)})
        list_of_tag = soup.find_all("a",string=re.compile(keyword))

        for i in range(len(list_of_tag_title)):
            testing_file.write(list_of_tag_title[i]["title"] + "\n")
            if not list_of_tag_title[i]['href'].startswith("https://"):
               testing_file.write(myList_BS[k]['main_url'] +list_of_tag_title[i]["href"] + "\n" + "\n")
            else:
                testing_file.write(list_of_tag_title[i]["href"] + "\n" + "\n")
        for i in range(len(list_of_tag)):
            testing_file.write(list_of_tag[i].string + "\n")
            if not list_of_tag[i]['href'].startswith("https://"):
                testing_file.write(myList_BS[k]['main_url']  + list_of_tag[i]["href"] + "\n" + "\n")
            else:
                testing_file.write(list_of_tag[i]["href"] + "\n" + "\n")

myList_BS = [{"media": "MingPao","url":"https://news.mingpao.com/ins/%E5%8D%B3%E6%99%82%E6%96%B0%E8%81%9E/main", "main_url":"https://news.mingpao.com/"},
             {"media": "RTHK","url":"https://news.rthk.hk/rthk/ch/latest-news.htm", "main_url":""},
             {"media": "SingTao","url":"https://std.stheadline.com/realtime/hongkong/%E5%8D%B3%E6%99%82-%E6%B8%AF%E8%81%9E", "main_url":""},
             {"media": "HK01","url":"https://www.hk01.com/zone/1/%E6%B8%AF%E8%81%9E", "main_url":"https://www.hk01.com/"},
             {"media": "HKET","url":"https://topick.hket.com/srat006/%E6%96%B0%E8%81%9E", "main_url":"https://topick.hket.com"},
             {"media": "EJ","url":"https://www2.hkej.com/instantnews/current", "main_url":"https://www2.hkej.com/"},
             {"media": "商報","url":"http://www.hkcd.com/hkcdweb/hongkongMacao.list.html", "main_url":""},
             {"media": "Hong Kong Free Press","url":"https://hongkongfp.com/hong-kong-news/", "main_url":""}]

news_scraping(myList_BS)

def search_by_XPATH(myList_XPATH):
    for k in range(len(myList_XPATH)):
        driver = webdriver.Chrome(Path_of_Chromedriver)
        driver.get(myList_XPATH[k]['url'])
        driver.implicitly_wait(15)
        elem = driver.find_elements(By.XPATH, myList_XPATH[k]['XPATH'])
        testing_file.write(myList_XPATH[k]['media'] + "\n" + "\n")
        for i in elem:
            if keyword in i.text:
                testing_file.write(i.text + "\n")
                testing_file.write(i.get_attribute("href") + "\n" + "\n")
        testing_file.write("\n")
        driver.quit()

myList_XPATH = [{"media": "商台","url":"https://www.881903.com/news/local", "XPATH":"//a[@class='news-grid__headline']"},
                {"media": "TVB","url":"https://news.tvb.com/tc/local", "XPATH":"//a[.//h3]"},
                {"media": "Cable TV","url":"https://www.i-cable.com/category/%E6%96%B0%E8%81%9E%E8%B3%87%E8%A8%8A/%E6%B8%AF%E8%81%9E/", "XPATH":"//h4[@class='post-title']/a"},
                {"media": "Now TV","url":"https://news.now.com/home/local", "XPATH":"//a[@class='newsWrap clearfix']"},
                {"media": "文匯網","url":"https://www.wenweipo.com/immed/hongkong", "XPATH":"//div[@class='story-item-title text-overflow']/a"},
                {"media": "點新聞","url":"https://www.dotdotnews.com/immed/hknews", "XPATH":"//div[@class='text']/h2/a"}]

search_by_XPATH(myList_XPATH)

def search_by_xpath_contain(myList_xpath_contain):
    for k in range(len(myList_xpath_contain)):
        driver = webdriver.Chrome(Path_of_Chromedriver)
        driver.get(myList_xpath_contain[k]['url'])
        driver.implicitly_wait(15)
        elem = driver.find_elements(By.XPATH, myList_xpath_contain[k]['XPATH'])
        testing_file.write(myList_xpath_contain[k]['media'] + "\n" + "\n")
        for i in elem:
            testing_file.write(i.text + "\n")
            testing_file.write(i.get_attribute("href") + "\n" + "\n")
        testing_file.write("\n")
        driver.quit()

myList_xpath_contain = [{"media": "On.cc","url":"https://hk.on.cc/hk/news/index.html", "XPATH":"//h1/a[contains(text(), '" + keyword + "')]"},
                        {"media": "The Standard","url":"https://www.thestandard.com.hk/section-news-list/section/local/", "XPATH":"//h1/a[contains(text(), '" + keyword + "')]"}]

search_by_xpath_contain(myList_xpath_contain)

testing_file.close()