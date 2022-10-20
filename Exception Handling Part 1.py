# Ревью кода 😤
# Дан файл data.txt. Требовалось написать программу, которая определяет, сколько
# строк содержится в данном файле, и выводит полученный результат. Программист
# торопился и написал программу неправильно.

# айдите и исправьте все ошибки, допущенные в этой программе (их ровно 3).

# Примечание. Известно, что каждая ошибка затрагивает только одну строку и может
# быть исправлена без изменения других строк.

# code before review

total = 0

with open(data.txt, encoding='utf-8') as file:
    for _ in file.readlines:
        total == total + 1

print(total)

# code after review

total = 0

with open('data.txt', encoding='utf-8') as file:
    for _ in file.readlines():
        total = total + 1

print(total)



# Ревью кода 😠
# ребовалось реализовать функцию swapcase_vowels(), которая принимает в качестве
# аргумента строку, заменяет в ней все гласные латинские буквы на заглавные и возвращает
# полученную новую строку. Программист торопился и реализовал функцию неправильно.

# Найдите и исправьте все ошибки, допущенные в реализации этой функции (их ровно 3).

# Примечание. Известно, что каждая ошибка затрагивает только одну строку и может быть
# исправлена без изменения других строк.

# code before review

def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        if char == vowels:
            char.upper()
        swapped_string += char

    return print(swapped_string)

# code after review

def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        if char in vowels:
            char = char.upper()
        swapped_string += char

    return swapped_string



# Ревью кода 😡
# Требовалось написать программу, которая принимает на вход два целых числа a и b,
# каждое на отдельной строке, и выводит список всех целых чисел от a до b включительно,
# которые делятся на 7 без остатка. Программист торопился и написал программу неправильно.

# Найдите и исправьте все ошибки, допущенные в этой программе (их ровно 5).

# Примечание. Известно, что каждая ошибка затрагивает только одну строку и может быть
# исправлена без изменения других строк.

# code before review

a = input()
b = input()
numbers = []

for i in range(a, b):
    if i // 7 == 0:
        numbers = numbers.append(i)

print(numbers)

# code after review

a = int(input())
b = int(input())
numbers = []

for i in range(a, b+1):
    if i % 7 == 0:
        numbers.append(i)

print(numbers)



# Ревью кода 🤬
# Требовалось реализовать функцию get_max_index(), которая принимает в качестве аргумента
# список различных целых чисел и возвращает индекс наибольшего числа из этого списка
# (начиная с 0). Программист торопился и реализовал функцию неправильно.

# Найдите и исправьте все ошибки, допущенные в реализации этой функции (их ровно 4).

# Примечание. Известно, что каждая ошибка затрагивает только одну строку и может быть
# исправлена без изменения других строк.

# code before review

def get_max_index(numbers):
    max_index = 0
    max_value = numbers[-1] 

    for index, value in enumerate(numbers, 1): 
        if index > max_index: 
            max_index = index
            max_value = value

    return max_value

# code after review

def get_max_index(numbers):
    max_index = 0
    max_value = numbers[0] 

    for index, value in enumerate(numbers): 
        if value > max_value: 
            max_index = index
            max_value = value

    return max_index