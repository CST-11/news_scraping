
from newspaper import Article
from snownlp import SnowNLP
import os
import sys
import time

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

Path_of_search_result = os.path.join(application_path, "search_result.txt")
Path_of_other_articles = os.path.join(application_path, "other_articles.txt")
Path_of_content_analysis_file = os.path.join(application_path, "content_analysis.txt")


print("This program will analyse and extract the keywords and summary of Chinese news articles." )
print("Conduct content analysis on (a) search_result.txt or (b) other_ariticles.txt ? " )
option_of_analysis_file = input("a/b:  ")
if option_of_analysis_file == "a":
    Path_of_input_file = Path_of_search_result
elif option_of_analysis_file == "b":
    print("Please paste the urls of the articles that you would like to analyse into other_ariticles.txt.")
    input("Press Enter to continue...")
    Path_of_input_file = Path_of_other_articles
else:
    print("Invalid option. Exiting program.")
    time.sleep(3)
    quit()


with open(Path_of_input_file,'r', encoding='UTF-8') as search_result_file, open(Path_of_content_analysis_file,'w', encoding='UTF-8') as content_analysis_file:
    list_of_url_result = []
    for line in search_result_file:
        if line.startswith("https://"):
            if line not in list_of_url_result:
                list_of_url_result.append(line)
    list_of_url_withoutCR = [x for x in list_of_url_result if "881903" not in x]
    for url in list_of_url_withoutCR:
        news_article = Article(url, language='zh')
        news_article.download()
        news_article.parse()
        content_analysis_file.write(("Title: " + news_article.title)+"\n")
        content_analysis_file.write(url+ "\n")
        full_article = news_article.text

        a = SnowNLP(u'{}'.format(full_article))
        simplified_chi_text = a.han
        s = SnowNLP(u'{}'.format(simplified_chi_text))
        content_analysis_file.write("Keywords- ")
        for NLP_keyword in s.keywords(6):
            content_analysis_file.write(NLP_keyword + " ")
        content_analysis_file.write("\n" + "Summary- " + "\n")
        for NLP_summary in s.summary(4):
            content_analysis_file.write(NLP_summary +"\n"+ "\n")
        sent = s.sentences
        sentiment_score = []
        for sen in sent:
            s = SnowNLP(sen)
            sentiment_score.append(s.sentiments)
        average_sentiment_score = str((sum(sentiment_score) / len(sentiment_score)))
        content_analysis_file.write("Average sentiment on a scale from 0 to 1 (0 being the most negative): "+ average_sentiment_score + "\n" + "\n" + "\n"+ "\n")


print("Finished analysis. Please take a look at content_analysis.txt!")
time.sleep(3)
quit()
