import re
import collections

f = open('text.txt', 'r')
filetext = f.read()
f.close()

# 2. Разбейте полученные текст на предложения.
# Примечание: Напоминаем, что в русском языке предложения заканчиваются на ., ! или ?.

# Решение:
li = re.split('\. |\.\n|\!|\?', filetext)

for item in li:
    print(item)

# print(li)


# 3. Найдите слова, состоящие из 4 букв и более. Выведите на экран 10 самых часто используемых слов.
# Пример вывода: [(“привет”, 3), (“люди”, 3), (“город”, 2)].

li = re.findall('\w{4,}', filetext)
counter=collections.Counter(li).most_common(10)
print(counter)

# 4. Отберите все ссылки.
# Примечание: Для поиска воспользуйтесь методом compile, в который вы вставите свой шаблон для поиска ссылок в тексте.

pattern = re.compile('(\w+.\w+.ru|\w+.\w+.ru/\w+)\. ')
print(pattern.findall(filetext))

# 5. Ссылки на страницы какого домена встречаются чаще всего?
# Напоминаем, что доменное имя — часть ссылки до первого символа «слеш». Например в ссылке вида travel.mail.ru/travel?id=5 доменным именем является travel.mail.ru.
# Подсчет частоты сделайте по аналогии с заданием 3, но верните только одну самую частую ссылку.

pattern = re.compile('\w+.\w+.ru')
li = pattern.findall(filetext)
print(li)
link =  collections.Counter(li).most_common(1)
print(link)


# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».

pattern = re.compile('(\w+.\w+.ru|\w+.\w+.ru/\w+)\. ')
li = re.sub(pattern, 'Ссылка отобразится после регистрации. ', filetext)
print(li)