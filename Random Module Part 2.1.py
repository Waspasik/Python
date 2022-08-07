# IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных
# точкой.

# Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает
# случайный корректный IP адрес.

from random import*

def generate_ip():
    ip = [0, 0, 0, 0]
    
    for i in range(len(ip)):
        ip[i] = str(randint(0, 255))
    
    return '.'.join(ip)

generate_ip()



# Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter
# – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).

# Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает
# случайный корректный почтовый индекс Латверии.

from random import*
from string import*

def generate_postcode():
    postcode = ''
    
    for i in range(7):
        if i not in [2, 3, 4]:
            postcode += choice(ascii_uppercase)
        elif i in [2, 4]:
            postcode += str(randint(0, 99))
        else:
            postcode += '_'
    
    return print(postcode)

generate_postcode()



# Напишите программу, которая с помощью модуля random перемешивает случайным образом
# содержимое матрицы (двумерного списка).

# Примечание. Выводить содержимое матрицы не нужно.

from random import*

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

for lst in matrix:
    shuffle(lst)



# Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров
# лотерейных билетов и выводит их каждый на отдельной строке. Обратите внимание, вы
# должны придерживаться следующих условий:

# номер не может начинаться с нулей;
# номер лотерейного билета должен состоять из 7 цифр;
# все 100 лотерейных билетов должны быть различными.

from random import *

counter = 0

while counter != 100:
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    number_ticket = sample(numbers, 7)
    if number_ticket[0] != '0':
        print(''.join(number_ticket))
    else:
        continue
    counter += 1



# Анаграмма – это слово образованное путём перестановки букв, составляющих другое слово.

# Например, слова пила и липа или пост и стоп – анаграммы.

# Напишите программу, которая считывает одно слово и выводит с помощью модуля random его
# случайную анаграмму.

# Примечание. Обратите внимание на то, что метод shuffle() работает со списком, а не со
# строкой.

from random import*

word = ' '.join(input()).split()
shuffle(word)
print(''.join(word))



# Для игры в бинго требуется карточка размером 5 × 5, содержащая различные (уникальные)
# целые числа от 1 до 75 (включительно), при этом центральная клетка является пустой
# (она заполняется числом 0).

# Напишите программу, которая с помощью модуля random генерирует и выводит случайную
# карточку для игры в бинго.

# Примечание 1. Для наглядности рекомендуем отводить на вывод каждого числа ровно 3
# символа. Для этого используйте строковый метод ljust().

from random import*

numbers = [i for i in range(1, 76)]
matrix = []
numbers = sample(numbers, 25)

for i in range(0, len(numbers), 5):
    matrix.append(numbers[i:i + 5])

matrix[2][2] = 0

for rows in range(5):
    for cols in range(5):
        print(str(matrix[rows][cols]).ljust(3), end='')
    print()