import requests
import json

# Для двух городов
# from_city = input('Введите из какого города вы вылетаете: ')
# to_city = input('Введите в какой город направляетесь: ')
#
# link = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20" + from_city + "%20в%20" + to_city
# req = requests.get(link)
# text = req.text
#
# response = json.loads(text)
# print(response)
#
# for item in response:
#     if item == 'origin':
#         print("IATA города отправления: ", response[item]['iata'])
#     if item == 'destination':
#         print("IATA города прибывания: ", response[item]['iata'])


# Для одного города
# city = input('Введите название города: ')
# link = "http://autocomplete.travelpayouts.com/places2?term=" + city + "&locale=ru"
#
# req = requests.get(link)
# text = req.text
#
# response = json.loads(text)
#
# for item in response[0]:
#     if item == 'code':
#         print('IATA код города: ', response[0][item])


# 1. Напишите функцию получения IATA-кода города из его названия, используя API Aviasales для усовершенствования приложения по парсингу информации об авиабилетах, созданного нами в ходе урока.
# Примечание: воспользуйтесь документацией по API, которая доступна на странице www.aviasales.ru/API (ссылка на значке «API-документация»). Вам необходимо изучить раздел «API для определения IATA-кода».

# https://support.travelpayouts.com/hc/ru/articles/360002755812-API-%D0%B4%D0%BB%D1%8F-%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-IATA-%D0%BA%D0%BE%D0%B4%D0%B0
# https://www.travelpayouts.com/widgets_suggest_params?q=Из%20Москвы%20в%20Лондон