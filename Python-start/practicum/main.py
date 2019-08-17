import os
import sys
from g_random import g_random
from core import create_file, getList, delete_file, copy_file, save_info

change_dir = input('Работаем в этой директории {}  или изменим? | Да иди Нет'.format(os.getcwd()))
if change_dir == 'Да':
    dir = input('Введите директрию')
    os.chdir(dir)
    print('Директория изменена на {}'.format(dir))


save_info('Начало')

try:
    command = sys.argv[1]
except IndexError:
    command = ''
    print('Введите команду для консольного менеджера')


if command == 'list':
    getList()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название файла')
    else:
        create_file(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название файла или папки')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Требуется ввести название копируемого файла или папки и название файла или папки копии')
    else:
        copy_file(name, new_name)
elif command == 'game':
    g_random()
elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление фала или папки')
    print('copy - копирование файла или папки')
    print('game - поиграть в игру - УгадайЧисло')

save_info('Конец')