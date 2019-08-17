import re
from bs4 import BeautifulSoup as BS
with open('index.html') as f:
    s = f.read()

# Используя навыки работы с текстом, получите количество студентов GeekBrains со стартовой страницы сайта geekbrains.ru.
# <span class="total-users">Нас уже 3 826 114 человек</span>
# Решите задачу двумя способами:
# a) используя регулярные выражения (библиотеку re),

# comments = re.compile("<!--.*?-->", re.DOTALL)
# scripts = re.compile("<script.*?</script>", re.DOTALL)
# tags = re.compile("<[^<]*>")
total = re.compile("<span class=\"total-users\">(.+)</span>")

# s = comments.sub("",s)
# s = scripts.sub("",s)
# s = tags.sub("",s)
li = total.findall(s)[0]
#
# s = re.sub("[ ]+", " ", s)
# s = re.sub("\s{2,}", "\n", s)

print(li)

# b) используя библиотеку BeautifulSoup.

soup = BS(s, "html.parser")

li = soup.select(".total-users")[0].get_text()

print(li)