
# Author: CHOI SHEUNG TING / CHIANG RUI
from bs4 import BeautifulSoup as bs
import requests
import re


Keyword = input("Please enter keyword: ")


testing_file = open(r"C:\Users\user\PycharmProjects\web_scraping\testing.txt", "w", encoding='UTF-8')


def news_scraping (myList):
    for k in range(len(myList)):
        testing_file.write(myList[k]['media'] + "\n" + "\n")
        result = requests.get(myList[k]['url'] )
        soup = bs(result.content, "html.parser")

        list_of_tag_title = soup.find_all("a",attrs={"title" : re.compile(Keyword)})
        list_of_tag = soup.find_all("a",string=re.compile(Keyword))

        for i in range(len(list_of_tag_title)):
            testing_file.write(list_of_tag_title[i]["title"] + "\n")
            if not list_of_tag_title[i]['href'].startswith("https://"):
               testing_file.write(myList[k]['main_url'] +list_of_tag_title[i]["href"] + "\n" + "\n")
            else:
                testing_file.write(list_of_tag_title[i]["href"] + "\n" + "\n")
        for i in range(len(list_of_tag)):
            testing_file.write(list_of_tag[i].string + "\n")
            if not list_of_tag[i]['href'].startswith("https://"):
                testing_file.write(myList[k]['main_url']  + list_of_tag[i]["href"] + "\n" + "\n")
            else:
                testing_file.write(list_of_tag[i]["href"] + "\n" + "\n")






myList = [{"media": "MingPao","url":"https://news.mingpao.com/ins/%E5%8D%B3%E6%99%82%E6%96%B0%E8%81%9E/main", "main_url":"https://news.mingpao.com/"},
          {"media": "RTHK","url":"https://news.rthk.hk/rthk/ch/latest-news.htm", "main_url":""},
          {"media": "SingTao","url":"https://std.stheadline.com/realtime/hongkong/%E5%8D%B3%E6%99%82-%E6%B8%AF%E8%81%9E", "main_url":""},
<<<<<<< HEAD
          {"media": "HK01","url":"https://std.stheadline.com/realtime/hongkong/%E5%8D%B3%E6%99%82-%E6%B8%AF%E8%81%9E", "main_url":""},
          {"media":"Oriental_Daily", "url": "https://hk.on.cc/hk/news/mobile/index.html","main_url":""}]
=======
          {"media": "HK01","url":"https://www.hk01.com/zone/1/%E6%B8%AF%E8%81%9E", "main_url":""},
          {"media": "HKET","url":"https://topick.hket.com/srat006/%E6%96%B0%E8%81%9E", "main_url":"https://topick.hket.com"},
          {"media": "EJ","url":"https://www2.hkej.com/instantnews/current", "main_url":"https://www2.hkej.com/"}]

>>>>>>> 8babf7e40b4e95007fab53aab0ea46e1b78100fb


testing_file.close()




