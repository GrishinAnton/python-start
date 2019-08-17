# Знаки “=”, “>” и “<” пользователь вводит с к
import math
#Условия игры. Максимальное число можно спрашивать в начале.


def g_random():
    min_number = 1
    max_number = 100
    rest = 0

    while True:
        ranges = range(min_number, max_number)
        rest = math.ceil(len(list(ranges)) / 2)
        if len(list(ranges)) < 2:
            if list(ranges)[0] > 50:
                print(f'Загаданное число: {max_number} ?')
            else:
                print(f'Загаданное число: {min_number} ?')
        else:
            print(f'Загаданное число: {list(ranges)[rest]} ?')

        answer = input('Введите ответ = - если значение угадано, > - если значение больше < - если значение меньше: ')

        if answer == '>':
            min_number = list(ranges)[rest]
        if answer == '<':
            max_number = list(ranges)[rest]
        if answer == '=':
            print('Спасибо за игру!')
            break
