# Открытие файла
# file = open('test.txt','r')
# Действия с файлом

# Закрытие файла
# file.close()

# Режим записи в файл
# file = open('todo.txt','w',encoding='utf-8')
# file.write('Сходить в магазин')
# file.close()

# Режим чтения
# file = open('todo.txt','r',encoding='utf-8')
# info = file.read
# print(info)
# file.close()

# Режим добавления
# file = open('todo.txt','a',encoding='utf-8')
# file.write('Сходить в магазин\n')
# file.close()

import pyttsx3

jork = pyttsx3.init("sapi5")


def see_todo_list():
    print('Дела:')
    file = open('todo.txt', 'r', encoding='utf-8')
    index = 1
    info = file.read()
    todo_list = info.split('\n')
    todo_list.pop()
    for i in todo_list:
        print(f'{index}: {i}')
        index += 1
    file.close()


menu = ('1: Добавить дело',
        '2: Удалить дело',
        '3: Вывести список',
        '4: Изменить дело',
        '5: Выйти')

while True:
    for i in menu:
        print(i)
    jork.say('Введите номер желаемого действия: ')
    jork.runAndWait()
    num = int(input('Введите номер желаемого действия: '))
    if num == 5:
        jork.say('Завершение работы')
        jork.runAndWait()
        break
    elif num == 1:
        jork.say('Сколько у вас новых дел? ')
        jork.runAndWait()
        count = int(input('Сколько у вас новых дел? '))
        for i in range(count):
            jork.say('Введите новое дело: ')
            jork.runAndWait()
            delo = input('Введите новое дело: ')
            file = open('todo.txt', 'a', encoding='utf-8')
            file.write(delo + '\n')
            file.close()
    elif num == 2:
        see_todo_list()
        jork.say("Какое действие удалить?  ")
        jork.runAndWait()
        del_num = int(input("Какое действие удалить?  "))
        file = open('todo.txt', 'r', encoding='utf-8')
        info = file.read()
        todo_list = info.split('\n')
        todo_list.pop(del_num - 1)
        file.close()
        print(todo_list)
        file = open('todo.txt', 'w', encoding='utf-8')
        for i in todo_list:
            file.write(i + '\n')
        file.close()
    elif num == 3:
        see_todo_list()
    elif num == 4:
        see_todo_list()
        jork.say('Какое действие изменить?')
        jork.runAndWait()
        num_replace = count = int(input('Какое действие изменить?  '))
        jork.say('Введите новое дело: ')
        jork.runAndWait()
        delo = input('Введите новое дело: ')
        file = open('todo.txt', 'r', encoding='utf-8')
        info = file.read()
        todo_list = info.split('\n')
        todo_list.pop(del_num - 1)
        file.close()
        todo_list[num_replace - 1] = delo
        file = open('todo.txt', 'w', encoding='utf-8')
        for i in todo_list:
            file.write(i + '\n')
        file.close()
    else:
        jork.say('Такого действия нет')
        jork.runAndWait()
        print('Такого действия нет')