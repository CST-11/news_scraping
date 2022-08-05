from bs4 import BeautifulSoup as bs
import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

print("Please select (a) ChromeBeta in usb / (b) ChromeBeta in other directory")
usb_or_other_directory = input("a / b: ")
if usb_or_other_directory == "a":
    usb_root_directory = input("Please enter the root directory of usb drive(e.g C/D): ")
    Path_of_Chromedriver = usb_root_directory+":\Chrome Beta\chromedriver.exe"
    Path_of_ChromeBeta = usb_root_directory+":\Chrome Beta\Application\chrome.exe"
elif usb_or_other_directory =="b":
    Path_of_Chromedriver =input("Please enter path of chromedriver: ")
    Path_of_ChromeBeta = input("Please enter path of ChromeBeta: ")
else:
    print("Invalid option.")

print("Write search results in (a) usb / (b) other directory")
search_result_directory = input("a / b: ")
if search_result_directory == "a":
    usb_root_directory = input("Please enter the root directory of usb drive(e.g C/D): ")
    Path_of_output_file = usb_root_directory + ":\search_results.txt"
elif usb_or_other_directory == "b":
    Path_of_output_file = input("Please enter path of output file: ")
else:
    print("Invalid option.")

print("The following news websites can be searched - ")
print("Chi: (1) MingPao (2) RTHK (3) SingTao (4) HK01  (5) ET  (6) EJ")
print("     (7)商台 (8)TVB (9)Cable (10)NowTV (11)文匯網 (12)商報 (13)點新聞 (14)中通社 (15)東網")
print(" ")
print("Eng: (1) RTHK English (2) Hong Kong Free Press (3) the Standard (4) SCMP Main page (5)SCMP Hong Kong news ")
language_option = input("Search for chi or eng news: ")
keyword = input("Please enter keyword: ")
start = time.time()


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
             {"media": "EJ","url":"https://www2.hkej.com/instantnews/current", "main_url":"https://www2.hkej.com/"}]

def search_by_XPATH(myList_XPATH):
    for k in range(len(myList_XPATH)):
        options = Options()
        options.binary_location = Path_of_ChromeBeta
        driver = webdriver.Chrome(options=options, service=Service(Path_of_Chromedriver))
        try:
            driver.set_page_load_timeout(15)
            try:
                driver.get(myList_XPATH[k]['url'])
            except TimeoutException:
                testing_file.write("The page was expired or not fully loaded - " )

            elem = driver.find_elements(By.XPATH, myList_XPATH[k]['XPATH'])
            testing_file.write(myList_XPATH[k]['media'] + "\n" + "\n")
            for i in elem:
                if keyword in i.text:
                    testing_file.write(i.text + "\n")
                    testing_file.write(i.get_attribute("href") + "\n" + "\n")
            testing_file.write("\n")
        finally:
            driver.quit()


myList_XPATH = [{"media": "商台","url":"https://www.881903.com/news/local", "XPATH":"//a[@class='news-grid__headline']"},
                {"media": "TVB","url":"https://news.tvb.com/tc/local", "XPATH":"//a[.//h3]"},
                {"media": "Cable TV","url":"https://www.i-cable.com/category/%E6%96%B0%E8%81%9E%E8%B3%87%E8%A8%8A/%E6%B8%AF%E8%81%9E/", "XPATH":"//h4[@class='post-title']/a"},
                {"media": "Now TV","url":"https://news.now.com/home/local", "XPATH":"//a[@class='newsWrap clearfix']"},
                {"media": "文匯網","url":"https://www.wenweipo.com/immed/hongkong", "XPATH":"//div[@class='story-item-title text-overflow']/a"},
                {"media": "商報","url":"http://www.hkcd.com/hkcdweb/hongkongMacao.list.html", "XPATH":"//a[.//h6]"},
                {"media": "點新聞","url":"https://www.dotdotnews.com/immed/hknews", "XPATH":"//div[@class='text']/h2/a"},
                {"media": "中通社","url":"http://www.hkcna.hk/index_col.jsp?channel=2804", "XPATH":"//a"}]

def search_by_xpath_contain(myList_xpath_contain):
    for k in range(len(myList_xpath_contain)):
        options = Options()
        options.binary_location = Path_of_ChromeBeta
        driver = webdriver.Chrome(options=options, service=Service(Path_of_Chromedriver))
        try:
            driver.set_page_load_timeout(15)
            try:
                driver.get(myList_xpath_contain[k]['url'])
            except TimeoutException:
                testing_file.write("The page was expired or not fully loaded - ")

            elem = driver.find_elements(By.XPATH, myList_xpath_contain[k]['XPATH'])
            testing_file.write(myList_xpath_contain[k]['media'] + "\n" + "\n")
            for i in elem:
                testing_file.write(i.text + "\n")
                testing_file.write(i.get_attribute("href") + "\n" + "\n")
            testing_file.write("\n")
        finally:
            driver.quit()

myList_xpath_contain = [{"media": "東網","url":"https://hk.on.cc/hk/news/index.html", "XPATH":"//h1/a[contains(text(), '" + keyword + "')]"}]


def news_scraping_Eng (myList_BS_Eng ):
    for k in range(len(myList_BS_Eng )):
        testing_file.write(myList_BS_Eng[k]['media'] + "\n" + "\n")
        result = requests.get(myList_BS_Eng[k]['url'] )
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
                testing_file.write(myList_BS_Eng[k]['main_url']  + list_of_tag[i]["href"] + "\n" + "\n")
            else:
                testing_file.write(list_of_tag[i]["href"] + "\n" + "\n")

myList_BS_Eng = [{"media": "RTHK","url":"https://news.rthk.hk/rthk/en/latest-news.htm", "main_url":""},
                 {"media": "Hong Kong Free Press","url":"https://hongkongfp.com/hong-kong-news/", "main_url":""}]

def search_by_xpath_contain_Eng(myList_xpath_contain_Eng):
    for k in range(len(myList_xpath_contain_Eng)):
        options = Options()
        options.binary_location = Path_of_ChromeBeta
        driver = webdriver.Chrome(options=options, service=Service(Path_of_Chromedriver))
        try:
            driver.set_page_load_timeout(15)
            try:
                driver.get(myList_xpath_contain_Eng[k]['url'])
            except TimeoutException:
                testing_file.write("The page was expired or not fully loaded - " )

            elem = driver.find_elements(By.XPATH, myList_xpath_contain_Eng[k]['XPATH'])
            testing_file.write(myList_xpath_contain_Eng[k]['media'] + "\n" + "\n")
            for i in elem:
                testing_file.write(i.text + "\n")
                testing_file.write(i.get_attribute("href") + "\n" + "\n")
            testing_file.write("\n")
        finally:
            driver.quit()

myList_xpath_contain_Eng = [{"media": "The Standard","url":"https://www.thestandard.com.hk/section-news-list/section/local/", "XPATH":"//h1/a[contains(text(), '" + keyword + "')]"},
                            {"media": "SCMP Main Page","url":"https://www.scmp.com/", "XPATH":"//a[contains(text(), '" + keyword+ "')]"},
                            {"media": "SCMP Hong Kong News","url":"https://www.scmp.com/news/hong-kong?module=mega_menu_news_int&pgtype=homepage", "XPATH":"//a[contains(text(), '" + keyword+ "')]"}]



if language_option =="chi" :
    news_scraping(myList_BS)
    search_by_XPATH(myList_XPATH)
    search_by_xpath_contain(myList_xpath_contain)
elif language_option == "eng" :
    news_scraping_Eng(myList_BS_Eng)
    search_by_xpath_contain_Eng(myList_xpath_contain_Eng)
else:
    print("Invalid instruction.")

end = time.time()
testing_file.write("It took " + str(end - start) + " seconds to finish searching.")

testing_file.close()


# [{'title': xxx, 'href':xxx}, {}, {}]
