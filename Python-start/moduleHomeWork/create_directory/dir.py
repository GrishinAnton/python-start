# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код. Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
import os


def create_directories():
    for i in range(1, 10):
        name = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.mkdir(name)

def remove_directories():
    for i in os.listdir():
        if os.path.isdir(i) and i[0:3] == 'dir':
           os.rmdir(i)
