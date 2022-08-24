import time
import os
from bs4 import BeautifulSoup as bs
import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


path_of_program_folder = os.path.dirname(os.path.abspath(__file__))
Path_of_Chromedriver = path_of_program_folder+"\Chrome Beta\chromedriver.exe"
Path_of_ChromeBeta = path_of_program_folder+"\Chrome Beta\Application\chrome.exe"
Path_of_output_file = path_of_program_folder+"\search_result.txt"



print("News titles in the following websites will be searched - ")
print("Chi: (1) MingPao (2) RTHK (3) SingTao (4) HK01  (5) ET  (6) EJ (7)AM730")
print("     (8)商台 (9)TVB (10)Cable (11)NowTV (12)文匯網 (13)商報 (14)點新聞 (15)中通社 (16)東網")
print(" ")
print("Eng: (1) RTHK English (2) Hong Kong Free Press (3) the Standard (4) SCMP Main page (5)SCMP Hong Kong news ")
language_option = input("Search for (a) chi / (b) eng: ")

if language_option != "a":
    if language_option!="b":
        time.sleep(1)
        print("Exiting program.")
        time.sleep(3)
        quit()

number_of_keyword = int(input("How many keyword you would like to search for: "))

list_of_keyword = []
for i in range(number_of_keyword):
    list_of_keyword.append(input("Please enter keyword no. "+ str(i+1) + " : "))
all_keyword = '|'.join(list_of_keyword)


start = time.time()

testing_file = open(str(Path_of_output_file), "w", encoding='UTF-8')

testing_file.write("\n" + "Searched for the following keywords - " + all_keyword + "\n"+"\n")

def news_scraping (myList_BS):
    for k in range(len(myList_BS)):
        testing_file.write("\n" + myList_BS[k]['media'] + "\n" + "\n")
        result = requests.get(myList_BS[k]['url'] )
        soup = bs(result.content, "html.parser")

        list_of_tag_title = soup.find_all("a",attrs={"title" : re.compile(all_keyword)})
        list_of_tag = soup.find_all("a",string=re.compile(all_keyword))
        news_dict = {}
        for i in range(len(list_of_tag_title)):
            news_dict.update({"News title "+str(i+1)+"" : list_of_tag_title[i]["title"]})
            if not list_of_tag_title[i]['href'].startswith("https://"):
                news_dict.update({"News url "+str(i+1)+"" : myList_BS[k]['main_url'] +list_of_tag_title[i]["href"]})
            else:
                news_dict.update({"News url "+str(i+1)+"" : list_of_tag_title[i]["href"]})

        for i in range(len(list_of_tag)):
            news_dict.update({"News title "+str(i+1)+"" : list_of_tag[i].string})
            if not list_of_tag[i]['href'].startswith("https://"):
                news_dict.update({"News url "+str(i+1)+"" : myList_BS[k]['main_url'] +list_of_tag[i]["href"]})
            else:
                news_dict.update({"News url "+str(i+1)+"" : list_of_tag[i]["href"]})

        temp = {val: key for key, val in news_dict.items()}
        removed_duplicates = {val: key for key, val in temp.items()}
        i=1
        for value in removed_duplicates.values():
            if (i%2)== 0:
                testing_file.write('{}\n'.format(value))
                testing_file.write("\n")
            else:
                testing_file.write('{}\n'.format(value))
            i = i+1

myList_BS = [{"media": "MingPao","url":"https://news.mingpao.com/ins/%E5%8D%B3%E6%99%82%E6%96%B0%E8%81%9E/main", "main_url":"https://news.mingpao.com/"},
             {"media": "RTHK","url":"https://news.rthk.hk/rthk/ch/latest-news.htm", "main_url":""},
             {"media": "SingTao","url":"https://std.stheadline.com/realtime/hongkong/%E5%8D%B3%E6%99%82-%E6%B8%AF%E8%81%9E", "main_url":""},
             {"media": "HK01 港聞","url":"https://www.hk01.com/zone/1/%E6%B8%AF%E8%81%9E", "main_url":"https://www.hk01.com"},
             {"media": "HK01 社會新聞","url":"https://www.hk01.com/channel/2/%E7%A4%BE%E6%9C%83%E6%96%B0%E8%81%9E", "main_url":"https://www.hk01.com"},
             {"media": "HK01 政情","url":"https://www.hk01.com/channel/310/%E6%94%BF%E6%83%85", "main_url":"https://www.hk01.com"},
             {"media": "HKET","url":"https://topick.hket.com/srat006/%E6%96%B0%E8%81%9E", "main_url":"https://topick.hket.com"},
             {"media": "EJ","url":"https://www2.hkej.com/instantnews/current", "main_url":"https://www2.hkej.com/"},
             {"media": "AM730 港聞","url":"https://www.am730.com.hk/%E6%9C%AC%E5%9C%B0", "main_url":"https://www.am730.com.hk"}]

def search_by_XPATH(myList_XPATH):
    for k in range(len(myList_XPATH)):
        options = Options()
        options.binary_location = Path_of_ChromeBeta
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options, service=Service(Path_of_Chromedriver))
        try:
            driver.set_page_load_timeout(20)
            try:
                driver.get(myList_XPATH[k]['url'])
            except TimeoutException:
                testing_file.write("The page was not fully loaded - " )

            driver.execute_script("window.scrollTo(0, 10000)")
            time.sleep(1)
            elem = driver.find_elements(By.XPATH, myList_XPATH[k]['XPATH'])
            testing_file.write(myList_XPATH[k]['media'] + "\n" + "\n")
            for i in elem:
                for y in range(len(list_of_keyword)):
                    if list_of_keyword[y] in i.text:
                        testing_file.write(i.text + "\n")
                        testing_file.write(i.get_attribute("href") + "\n" + "\n")
            testing_file.write("\n")
        finally:
            driver.quit()


myList_XPATH = [{"media": "商台","url":"https://www.881903.com/news/local", "XPATH":"//a[@class='news-grid__headline']"},
                {"media": "TVB","url":"https://news.tvb.com/tc/local", "XPATH":"//a[.//h3]"},
                {"media": "Cable","url":"https://www.i-cable.com/category/%E6%96%B0%E8%81%9E%E8%B3%87%E8%A8%8A/%E6%B8%AF%E8%81%9E/", "XPATH":"//h4[@class='post-title']/a"},
                {"media": "Now TV","url":"https://news.now.com/home/local", "XPATH":"//a[@class='newsWrap clearfix']"},
                {"media": "文匯網","url":"https://www.wenweipo.com/immed/hongkong", "XPATH":"//div[@class='story-item-title text-overflow']/a"},
                {"media": "商報","url":"http://www.hkcd.com/hkcdweb/hongkongMacao.list.html", "XPATH":"//a[.//h6]"},
                {"media": "點新聞","url":"https://www.dotdotnews.com/immed/hknews", "XPATH":"//div[@class='text']/h2/a"},
                {"media": "中通社","url":"http://www.hkcna.hk/index_col.jsp?channel=2804", "XPATH":"//a"},
                {"media": "東網","url":"https://hk.on.cc/hk/news/index.html", "XPATH":"//a"}]

def news_scraping_Eng (myList_BS_Eng):
    for k in range(len(myList_BS_Eng)):
        testing_file.write("\n" + myList_BS_Eng[k]['media'] + "\n" + "\n")
        result = requests.get(myList_BS_Eng[k]['url'] )
        soup = bs(result.content, "html.parser")

        list_of_tag_title = soup.find_all("a",attrs={"title" : re.compile(all_keyword)})
        list_of_tag = soup.find_all("a",string=re.compile(all_keyword))
        news_dict = {}
        for i in range(len(list_of_tag_title)):
            news_dict.update({"News title "+str(i+1)+"" : list_of_tag_title[i]["title"]})
            if not list_of_tag_title[i]['href'].startswith("https://"):
                news_dict.update({"News url "+str(i+1)+"" : myList_BS_Eng[k]['main_url'] +list_of_tag_title[i]["href"]})
            else:
                news_dict.update({"News url "+str(i+1)+"" : list_of_tag_title[i]["href"]})

        for i in range(len(list_of_tag)):
            news_dict.update({"News title "+str(i+1)+"" : list_of_tag[i].string})
            if not list_of_tag[i]['href'].startswith("https://"):
                news_dict.update({"News url "+str(i+1)+"" : myList_BS_Eng[k]['main_url'] +list_of_tag[i]["href"]})
            else:
                news_dict.update({"News url "+str(i+1)+"" : list_of_tag[i]["href"]})

        temp = {val: key for key, val in news_dict.items()}
        removed_duplicates = {val: key for key, val in temp.items()}
        i=1
        for value in removed_duplicates.values():
            if (i%2)== 0:
                testing_file.write('{}\n'.format(value))
                testing_file.write("\n")
            else:
                testing_file.write('{}\n'.format(value))
            i = i+1

myList_BS_Eng = [{"media": "RTHK","url":"https://news.rthk.hk/rthk/en/latest-news.htm", "main_url":""},
                 {"media": "Hong Kong Free Press","url":"https://hongkongfp.com/hong-kong-news/", "main_url":""}]

def search_by_XPATH_Eng(myList_XPATH_Eng):
    for k in range(len(myList_XPATH_Eng)):
        options = Options()
        options.binary_location = Path_of_ChromeBeta
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options, service=Service(Path_of_Chromedriver))
        try:
            driver.set_page_load_timeout(20)
            try:
                driver.get(myList_XPATH_Eng[k]['url'])
            except TimeoutException:
                testing_file.write("The page was not fully loaded - " )

            driver.execute_script("window.scrollTo(0, 10000)")
            time.sleep(1)
            elem = driver.find_elements(By.XPATH, myList_XPATH_Eng[k]['XPATH'])
            testing_file.write(myList_XPATH_Eng[k]['media'] + "\n" + "\n")
            for i in elem:
                for y in range(len(list_of_keyword)):
                    if list_of_keyword[y] in i.text:
                        testing_file.write(i.text + "\n")
                        testing_file.write(i.get_attribute("href") + "\n" + "\n")
            testing_file.write("\n")
        finally:
            driver.quit()

myList_XPATH_Eng = [{"media": "The Standard","url":"https://www.thestandard.com.hk/section-news-list/section/local/", "XPATH":"//h1/a"},
                    {"media": "SCMP Main Page","url":"https://www.scmp.com/", "XPATH":"//a"},
                    {"media": "SCMP Hong Kong News","url":"https://www.scmp.com/news/hong-kong?module=mega_menu_news_int&pgtype=homepage", "XPATH":"//a"}]

if language_option =="a" :
    news_scraping(myList_BS)
    testing_file.write("\n")
    search_by_XPATH(myList_XPATH)
elif language_option == "b" :
    news_scraping_Eng(myList_BS_Eng)
    testing_file.write("\n")
    search_by_XPATH_Eng(myList_XPATH_Eng)
else:
    print("Invalid option.")
    time.sleep(1)
    print("Exiting program.")
    time.sleep(3)
    quit()

end = time.time()
time_taken = (end - start)/60
testing_file.write("It took " + str(round(time_taken, 3)) + " minutes to finish searching.")

testing_file.close()

print("Search completed. Please take a look at search_result.txt !")
time.sleep(3)
quit()



