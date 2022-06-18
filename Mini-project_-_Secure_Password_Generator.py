# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на
# длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

# От автора кода: программа написана по тем шагам, которые были указаны авторами курса. Доработка программы
# будет сделана в ближайшее время :)

from random import*
from string import*

chars = ''
ambiguous_ch = 'il1Lo0O'


def digit_password():
    print('Нужно ли включать цифры?')
    while True:
        digit_pass = input()
        digit_pass = digit_pass.lower()
        if digit_pass.lower() == 'да':
            return True
        elif digit_pass.lower() == 'нет':
            return False
        else:
            print('Введите "Да" или "Нет"')
            continue

def lowercase_password():
    print('Нужно ли включать строчные буквы?')
    while True:
        lowercase_pass = input()
        lowercase_pass = lowercase_pass.lower()
        if lowercase_pass.lower() == 'да':
            return True
        elif lowercase_pass.lower() == 'нет':
            return False
        else:
            print('Введите "Да" или "Нет"')
            continue

def uppercase_password():
    print('Нужно ли включать прописные буквы?')
    while True:
        uppercase_pass = input()
        uppercase_pass = uppercase_pass.lower()
        if uppercase_pass.lower() == 'да':
            return True
        elif uppercase_pass.lower() == 'нет':
            return False
        else:
            print('Введите "Да" или "Нет"')
            continue

def punctuation_password():
    print('Нужно ли включать символы?')
    while True:
        punctuation_pass = input()
        punctuation_pass = punctuation_pass.lower()
        if punctuation_pass.lower() == 'да':
            return True
        elif punctuation_pass.lower() == 'нет':
            return False
        else:
            print('Введите "Да" или "Нет"')
            continue

def ambiguous_chars():
    print('Нужно ли исключить неоднозначные символы "il1Lo0O"?')
    while True:
        ambiguous_ch = input()
        ambiguous_ch = ambiguous_ch.lower()
        if ambiguous_ch.lower() == 'да':
            return True
        elif ambiguous_ch.lower() == 'нет':
            return False
        else:
            print('Введите "Да" или "Нет"')
            continue

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += choice(chars)
    print(password)


print('Добро пожаловать в Генератор безопасных паролей.')
print('Введите количество паролей, которые вам нужно сгенерировать')
while True:
    count_pass = input()
    if count_pass.isdigit():
        break
    elif count_pass.isalnum() or count_pass.isalpha():
        print('Введите количество требуемых паролей числом')
        continue
print('Какая длинна пароля вам необходима?')
while True:
    len_pass = input()
    if len_pass.isdigit():
        break
    elif len_pass.isalnum() or len_pass.isalpha():
        print('Введите требуемую длинну пароля числом')
        continue
if digit_password():
    chars += digits
if lowercase_password():
    chars += ascii_lowercase
if uppercase_password():
    chars += ascii_uppercase
if punctuation_password():
    chars += punctuation
if ambiguous_chars():
    for i in ambiguous_ch:
        chars = chars.replace(i, '')

for _ in range(int(count_pass)):
    generate_password(int(len_pass), chars)