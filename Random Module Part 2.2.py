# Тайный друг 🌶️
# Напишите программу, которая случайным образом назначает каждому ученику его тайного
# друга, который будет вместе с ним решать задачи по программированию.

# Формат входных данных
# На вход программе в первой строке подается число nn – общее количество учеников.
# Далее идут n строк, содержащих имена и фамилии учеников.

# Формат выходных данных
# Программа должна вывести имя и фамилию ученика (в соответствии с исходным порядком)
# и имя и фамилию его тайного друга, разделённые дефисом.

# Примечание 1. Обратите внимание, что нельзя быть тайным другом самому себе и нельзя
# быть тайным другом для нескольких учеников.

from random import*

name_list = [input() for i in range(int(input()))]
couples_students = []

def choice_name(name):
    while True:
        copy_name_list = name_list.copy()
        copy_name_list.remove(name)
        partner = choice(copy_name_list)
        if partner not in couples_students:
            couples_students.append(partner)
            return partner
        else:
            continue

for name in name_list:
    print(f'{name} - {choice_name(name)}')



# Генератор паролей 1
# Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов,
# состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать
# между собой:

# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
# Формат входных данных
# На вход программе подаются два числа n и m, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести nn паролей длиной m символов в соответствии с условием задачи,
# каждый на отдельной строке.

# Примечание 1. Считать, что числа n и m всегда таковы, что требуемые пароли сгенерировать
# возможно.

# Примечание 2. В каждом пароле необязательно должна присутствовать хотя бы одна цифра и буква
# в верхнем и нижнем регистре.

from random import*
from string import*

def generate_password(length):
    valid_chars = ' '.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
    return sample(valid_chars.split(), length)
    
def generate_passwords(count, length):
    for _ in range(count):
        print(''.join(generate_password(length)))

n, m = int(input()), int(input())

generate_passwords(n, m)



# Генератор паролей 2 🌶️
# Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов,
# состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать
# между собой:

# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
# Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра
# и как минимум по одной букве в верхнем и нижнем регистре.

# Формат входных данных
# На вход программе подаются два числа n и m, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести n паролей длиной m символов в соответствии с условием задачи,
# каждый на отдельной строке.

# Примечание 1. Считать, что числа n и m всегда таковы, что требуемые пароли сгенерировать
# возможно.

from random import*
from string import*

def generate_password(length):
    while True:
        valid_chars = ' '.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))
        password = sample(valid_chars.split(), length)
        if set(password) & set(ascii_uppercase) and set(password) & set(ascii_lowercase) and set(password) & set(digits):
            return password
        else:
            continue
    
def generate_passwords(count, length):
    for _ in range(count):
        print(''.join(generate_password(length)))

n, m = int(input()), int(input())

generate_passwords(n, m)