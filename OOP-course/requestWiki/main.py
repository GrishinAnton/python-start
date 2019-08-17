from wiki_requests import get_topic_page
import re
from bs4 import BeautifulSoup as BS

def get_topic_words(topic):
    html_content = get_topic_page(topic)

    more_link_word = get_some_more_links_word(html_content)

    if len(more_link_word):
        #Ограничение тремя ссылками, чтобы быстрее было
        for word in more_link_word[0:3]:
            html_content+= get_topic_page(word)

    words = re.findall("[а-яА-я\-\']{3,}", html_content)
    return words

def get_some_more_links_word(content):
    soup = BS(content, 'html.parser')

    def is_none(attr):
        return attr is None
    # Можно еще улучшить выборку. У меня остались ссылка на снутренние страницы, которые разделены :
    # Так же остались ссылки на языки
    li = soup.find_all('a', href=re.compile("^/wiki/"), class_=is_none, accesskey=is_none)

    strArr=[]

    for a in li:
        str1 = re.findall('>([а-яА-Я].+)</', str(a))
        if len(str1):
            strArr.append(str1[0])

    return strArr

def get_common_words(topic):
    words_list = get_topic_words(topic)
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1

    rate_list = list(rate.items())
    rate_list.sort(key = lambda x: -x[1])
    return rate_list

def visualize_common_words(topic):
    words = get_common_words(topic)

    print("Список: ", words)



def main():
    topic = input("Topic")
    visualize_common_words(topic)