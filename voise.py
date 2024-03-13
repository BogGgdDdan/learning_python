import pyttsx3
from webbrowser import open  # Открытие ссылок
from subprocess import run  # Открытие приложений
import random

# print(list('qwertyuiopasdfghjklzxcvbnm'))
# print(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
# print(list('1234567890'))
# print(list('+-*/=_#!?'))

jork = pyttsx3.init("sapi5")
jork.say("Голосовой помощник джорк на связи!Как к вам обращаться?")
jork.runAndWait()

name = input("Введите имя: ")
hello = ["Рад вас приветствовать", "Доброго времени суток", "Вас приветствует голосовой помощник джорк",
         "Здравствуйте,вы обратились к голосовому помощнику джорк"]
jork.say(f"{random.choice(hello)},{name}")
jork.runAndWait()

jork.say("Придумайте пароль для входа в приложения")
jork.runAndWait()
password = input("Ваш пароль: ")
jork.say(f"{name},ваш пароль {password}")
if len(password) <= 7:
    print("Слишком короткий пароль")
count_big = 0
count_litter = 0
count_digits = 0
symbols = ["?", "!", "%", "+"]
count_symbols = 0

for i in password:
    if i.isupper():
        count_big += 1
    if i.islower():
        count_litter += 1
    if i.isdigit():
        count_digits += 1
    if i in symbols:
        count_symbols += 1

if count_big == 0:
    print("Нехватает заглавных букв")
if count_litter == 0:
    print("Нехватает строчных букв")
if count_digits == 0:
    print("Нехватает цифр")
if count_symbols == 0:
    print("Нехватает специальных символов")

if count_big != 0 and count_litter != 0 and count_symbols != 0 and count_digits != 0:
    jork.say("Отличный пароль")
else:
    jork.say("Пароль не надёжен,но вы сможете его поменять")

jork.say("Как у вас дела?")
jork.runAndWait()

dela = input("хорошо,нормально или плохо: ")
if dela == ("хорошо"):
    jork.say("У меня тоже ")
elif dela == ("нормально"):
    jork.say("Почаще улыбайся и всё будет хорошо")
else:
    jork.say(f"Сочувствую тебе ,{name}")
jork.runAndWait()

while True:
    jork.say("Какое действие вы хотите сделать?")
    jork.runAndWait()
    print('Доступны следующие действия: ')
    menu = ("посчитай", "стоп", "рандомный пароль", "поменять пароль", "открыть ютуб", "открыть роблокс")
    for i in menu:
        print(i)
    action = input("Введите действие: ")

    if action == ("посчитай"):
        jork.say("Какой пример хотите посчитать?")
        jork.runAndWait()
        example = input("Ваш пример: ")
        result = eval(example)
        jork.say(f"{example} = {result}")
        jork.runAndWait()
        print(f"{example} = {result}")

    elif action == "стоп":
        jork.say("Остановление работы")
        jork.runAndWait()
        break

    elif action == 'посмотреть список дел':
        menu = ('1: Добавить дело',
                '2: Удалить дело',
                '3: Вывести список',
                '4: Изменить дело',
                '5: Выйти')

        for i in menu:
            print(i)
        todo = []
        while True:
            num = int(input('Введите номер желаемого действия: '))
            if num == 5:
                print('Завершение работы')
                break
            elif num == 1:
                count = int(input('Сколько у вас новых дел? '))
                for i in range(count):
                    delo = input('Введите новое дело: ')
                    todo.append(delo)
            elif num == 2:
                del_num = int(input('Какое действие удалить?  '))
                todo.pop(del_num - 1)
            elif num == 3:
                print('Дела: ')
                for i in todo:
                    print(f'{todo.index(i) + 1}: {i}')
            elif num == 4:
                num_replace = count = int(input('Какое действие изменить?  '))
                delo = input('Введите новое дело: ')
                todo[num_replace - 1] = delo
            else:
                print('Такого действия нет')

    elif action == "рандомный пароль":
        small = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
                 'x', 'c', 'v', 'b', 'n', 'm']
        big = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
               'C', 'V', 'B', 'N', 'M']
        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        symbols2 = ['+', '-', '*', '/', '=', '_', '#', '!', '?']
        while True:
            jork.say('Чтобы выбрать рандомный пароль введите старый пароль')
            jork.runAndWait()
            proverka = input("Введите старый пароль:")
            if proverka == password:
                break
            else:
                jork.say("Неверный пароль")
                jork.runAndWait()
        list_passwords = ["9q!j!e3H", 'VJBngn4+', 'JpwxIN1?', 'p7iVj0y!', 'O2Ap?FMp', '5hIqeb6?', 'ON2MxN%K',
                          'K+N3cCDE',
                          'NowHfm4+', 'pYw%S0Nz']
        new_password = ''
        list_symbols = small, big, digits, symbols2
        for i in range(8):
            choise_list = random.choice(list_symbols)
            random_symbol = random.choice(choise_list)
            new_password += random_symbol
        choise_password = random.choice(list_passwords)
        password = new_password
        jork.say(f'{name},ваш пароль{new_password}')
        print(f'{name}, ваш пароль {new_password}')
        jork.runAndWait()

    elif action == "поменять пароль":
        jork.say("Для смены пароля введите старый пароль")
        jork.runAndWait()
        while True:
            proverka = input("Введите пароль:")
            if proverka == password:
                jork.say("Введите новый пароль")
                jork.runAndWait()
                password = input("Введите новый пароль:")
                jork.say(f"{name},ваш пароль {password}")
                if len(password) <= 7:
                    print("Слишком короткий пароль")
                count_big = 0
                count_litter = 0
                count_digits = 0
                symbols = ["?", "!", "%", "+"]
                count_symbols = 0

                for i in password:
                    if i.isupper():
                        count_big += 1
                    if i.islower():
                        count_litter += 1
                    if i.isdigit():
                        count_digits += 1
                    if i in symbols:
                        count_symbols += 1

                if count_big == 0:
                    print("Нехватает заглавных букв")
                if count_litter == 0:
                    print("Нехватает строчных букв")
                if count_digits == 0:
                    print("Нехватает цифр")
                if count_symbols == 0:
                    print("Нехватает специальных символов")

                if count_big != 0 and count_litter != 0 and count_symbols != 0 and count_digits != 0:
                    jork.say("Отличный пароль")
                else:
                    jork.say("Пароль не надёжен,но вы сможете его поменять")
                break
            else:
                jork.say("Неверный пароль")
                jork.runAndWait()

    elif action == "открыть ютуб":
        jork.say("Открываю ютуб")
        jork.runAndWait()
        open("https://www.youtube.com/")

    elif action == "открыть роблокс":
        jork.say("Введите пароль")
        jork.runAndWait()
        while True:
            proverka = input("Введите пароль:")
            if proverka == password:
                jork.say("Открываю роблокс")
                jork.runAndWait()
                run(r"C:\Users\user\AppData\Local\Roblox\Versions\version-48a28da848b7420d\RobloxPlayerBeta.exe")
                break
            else:
                jork.say("Неверный пароль")
                jork.runAndWait()
