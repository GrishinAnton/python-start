# ДЗ. Тема 7. Полезные инструменты. Обработка исключений.
# Решить с помощью генераторов списка.
#
# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.

arr1 = ['apple', 'orange', 'avocado', 'date']
arr2 = ['apricot', 'date','banana', 'avocado']

new_arr = [item for item in arr1 if item in arr2]
print(new_arr)

# 2
list = [-2,-3, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
result3 = []
resultPlus= []
result4 = []

for i in range(len(list)):
    if list[i]%3 ==0 :
         result3.append(list[i])
    if list[i]%4 != 0 :
         result4.append(list[i])
    if list[i] >= 0 :
         resultPlus.append(list[i])

print(result3)
print(result4)
print(resultPlus)

# 3. Напишите функцию которая принимает на вход список. Функция создает из этого списка новый список из квадратных корней чисел (если число положительное) и самих чисел (если число отрицательное) и возвращает результат (желательно применить генератор и тернарный оператор при необходимости). В результате работы функции исходный список не должен измениться.
# Например:
old_list = [1, -3, 4]
result = [1, -3, 2]

def squ(list):
    arr = []
    for i in range(len(list)):
        arr.append(list[i]**2 if list[i] >= 0 else list[i] )
    return arr

print(squ(old_list))
print(squ(result))

# 4.

number = int(input('Введите число'))


def fn(number):
    if number == 13:
        raise Exception('ValueError')
    return number ** 2


if(1 <= number <= 100):
    try:
        print('try')
        print(fn(number))
    except Exception:
        print('ValueError')
        print(number)




