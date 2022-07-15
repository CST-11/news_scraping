

from bs4 import BeautifulSoup as bs
import requests
import re

Keyword = input("Please enter keyword: ")

#MingPao

testing_file = open(r"C:\Users\user\Desktop\testing.txt", "a", encoding='UTF-8')

testing_file.write("MingPao - " + "\n" + "\n")

Mingpao_result = requests.get("https://news.mingpao.com/ins/%E6%B8%AF%E8%81%9E/section/20220714/s00001")
Mingpao_soup = bs(Mingpao_result.content, "html.parser")

Mingpao_list_of_tag_title = Mingpao_soup.find_all("a",attrs={"title" : re.compile(Keyword)}) #
Mingpao_list_of_tag = Mingpao_soup.find_all("a",string=re.compile(Keyword))


for i in range(len(Mingpao_list_of_tag_title)):
    if Mingpao_list_of_tag_title[i]['href'].startswith("../"):
        Mingpao_list_of_tag_title[i]['href'] = "https://news.mingpao.com/" + Mingpao_list_of_tag_title[i]['href'][3:]

for i in range(len(Mingpao_list_of_tag_title)):
    testing_file.write(Mingpao_list_of_tag_title[i]["title"] + "\n")
    testing_file.write(Mingpao_list_of_tag_title[i]["href"] + "\n")

for i in range(len(Mingpao_list_of_tag)):
    testing_file.write(Mingpao_list_of_tag[i].string + "\n")
    testing_file.write(Mingpao_list_of_tag[i]["href"] + "\n" + "\n")

#RTHK

RTHK_result = requests.get("https://news.rthk.hk/rthk/ch/latest-news.htm")
RTHK_soup = bs(RTHK_result.content, "html.parser")

RTHK_all_related_news = RTHK_soup.find_all("a", string = re.compile(Keyword))

# testing_file.write("RTHK - " + "\n" + "\n")

for i in range(len(RTHK_all_related_news)):
    testing_file.write(RTHK_all_related_news[i].string + "\n") # <a title=> xxxx </a>
    testing_file.write(RTHK_all_related_news[i]["href"] + "\n" + "\n")

testing_file.close()







