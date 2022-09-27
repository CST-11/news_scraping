This project aims to scrape instant news articles from major news websites in Hong Kong. The program will search for news title which contain a specific keyword, and scrape the title and url of the article. Results will be written in a separate text file. Users can enter multiple keywords or save a set of keywords in the text files named by “keyword_chi” and “keyword_eng”. It is recommended to convert this python program to exe file by auto-py-to-exe.

The program mainly consists of two parts. The first part uses Beautifulsoup4 and requests module to parse non-dynamic news websites and search for <a> tag, then re module will be used to check whether the link-text of <a>tag contains a specific keyword; the second part uses Selenium together with Chrome driver to open and load dynamic news websites, news titles will be located by using their direct XPATH. As Chrome version 1.04 is more stable for scraping, the application folder of Chrome Beta is set to be placed in the root directory of the program. Chrome driver 1.04 should also be placed in the application folder of Chrome Beta. 

To facilitate automation, there is a version designed for using in combination with windows task scheduler. This version will not ask user to enter keyword, it will search for the keywords as specified in the two keyword text files and send the search results to a specified gmail account. Users can use windows task scheduler to create an automated task on a routine basis.

List of target news websites – 

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