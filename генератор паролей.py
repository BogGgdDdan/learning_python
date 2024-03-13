import random

small = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
         'x', 'c', 'v', 'b', 'n', 'm']
big = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
       'C', 'V', 'B', 'N', 'M']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols2 = ['+', '-', '*', '/', '=', '_', '#', '!', '?']
list_passwords = ["9q!j!e3H", 'VJBngn4+', 'JpwxIN1?', 'p7iVj0y!', 'O2Ap?FMp', '5hIqeb6?', 'ON2MxN%K',
                          'K+N3cCDE',
                          'NowHfm4+', 'pYw%S0Nz']
def generaiton():
    new_password = ''
    list_symbols = small, big, digits, symbols2
    for i in range(8):
        choise_list = random.choice(list_symbols)
        random_symbol = random.choice(choise_list)
        new_password += random_symbol
    choise_password = random.choice(list_passwords)
    password = new_password
    print(f' ваш пароль {new_password}')
    return password

def check_password(password):
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
        print("Отличный пароль")
        return True
    else:
        print("Пароль не надёжен,но вы сможете его поменять")
        return False

while True:
    password = generaiton()
    if check_password(password):
        break