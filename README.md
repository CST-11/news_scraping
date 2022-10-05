**Getting started**

This project aims to scrape instant news articles from major news websites in Hong Kong. The program will search for news title which contain specific keyword(s), and scrape the title and url of the articles. Results will be written in a separate text file. Users can enter multiple keywords, or save their own set of keywords in a text file which will be automatically read by the program. 

**Dependencies**

Python modules - 
[beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
[requests](https://pypi.org/project/requests/)
[selenium](https://pypi.org/project/selenium/)

Chrome Beta (Chrome version 104)

Chrome driver 104

**How to use**

An application folder of Chrome Beta should be placed in the root directory of the program. You may install Chrome Beta version 104 on your Windows PC, and make a copy of the application folder to the root directory of this program. Chrome driver 104 should also be placed inside the application folder. 

The program will ask the user to select a set of websites to be scraped (classified by Chinese or English). Then the user need to choose whether they would like to search for specific keywords, or the keywords saved in text files named by “keyword_chi” or “keyword_eng”.

The program mainly consists of two parts. The first part uses Beautifulsoup4 and requests module to parse non-dynamic news websites and search for "a" tag, then re module will be used to check whether the link-text of "a" tag contains a specific keyword; the second part uses Selenium together with Chrome driver to open and load dynamic news websites, news titles will be located by using their direct XPATH. 

Results will be written in a text file named by "search_result". It will be saved in the root directory of the program.

To facilitate usage on Windows PC without Python, it is recommended to convert this python program to exe file by [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/).

**Automation**

To facilitate automation, there is a version designed for using in combination with windows task scheduler. This version will not ask user to enter any keyword, it will only search for the keywords in the keyword text files. After scraping, the results in the text file will extracted, then sent as plain texts to a specified email account. Users can use windows task scheduler to create automated and scheduled task.

**List of target news websites**

Chinese:
1.	MingPao Daily
2.	RTHK
3.	SingTao Daily
4.	HK01
5.	HKET
6.	HKEJ
7.	AM730
8.	Hong Kong China News Agency
9.	Commercial Radio
10.	TVB
11.	Cable TV
12.	Now TV
13.	Wen Wei Po
14.	Dotdot news
15.	Hong Kong Commercial Daily
16.	On.cc

English:
1.	South China Morning Post
2.	The Standard
3.	Hong Kong Free Press
4.	RTHK English