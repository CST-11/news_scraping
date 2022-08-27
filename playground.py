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
from concurrent.futures import ThreadPoolExecutor


path_of_program_folder = os.path.dirname(os.path.abspath(__file__))
Path_of_Chromedriver = path_of_program_folder+"\Chrome Beta\chromedriver.exe"
Path_of_ChromeBeta = path_of_program_folder+"\Chrome Beta\Application\chrome.exe"
Path_of_output_file = path_of_program_folder+"\search_result.txt"

list_of_keyword = []

path_of_keyword_file = path_of_program_folder+"\keyword_chi.txt"
keyword_file= open(path_of_keyword_file,'r', encoding='UTF-8')
for line in keyword_file:
    line = line.replace("\n", "")
    list_of_keyword.append(line)
keyword_file.close()
all_keyword = '|'.join(list_of_keyword)



start = time.time()

testing_file = open(str(Path_of_output_file), "w", encoding='UTF-8')

testing_file.write("\n" + "Searched for the following keywords - " + all_keyword + "\n"+"\n")

'''
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(square, list_1)
'''
# {"media": "東網","url":"https://hk.on.cc/hk/news/index.html", "XPATH":"//a"}
def search_by_XPATH(dict_media):
    options = Options()
    options.binary_location = Path_of_ChromeBeta
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=Service(Path_of_Chromedriver))
    try:
        driver.set_page_load_timeout(40)
        try:
            driver.get(dict_media['url'])
        except TimeoutException:
            print("The page was not fully loaded.")

        driver.execute_script("window.scrollTo(0, 10000)")
        time.sleep(1)
        elem = driver.find_elements(By.XPATH, dict_media['XPATH'])
        print(dict_media['media'] + "\n" + "\n")
        # {"media":apple daily, "title":hi you, "url":https://},{}
        for i in elem:
            for y in range(len(list_of_keyword)):
                if list_of_keyword[y] in i.text:
                    print(i.text + "\n")
                    print(i.get_attribute("href") + "\n" + "\n")
        print("\n")
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


with ThreadPoolExecutor() as executor:
    futures = [executor.submit(search_by_XPATH, i) for i in myList_XPATH]
    for future in futures:
        # retrieve the result
        print(future.result())




end = time.time()
time_taken = (end - start)/60
testing_file.write("It took " + str(round(time_taken, 3)) + " minutes to finish searching.")

testing_file.close()

print("Search completed. Please take a look at search_result.txt !")
time.sleep(3)
quit()