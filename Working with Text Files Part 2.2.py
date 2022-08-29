# Статистика по файлу
# Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу,
# которая выводит количество букв латинского алфавита, слов и строк. Выведите три
# найденных числа в формате, приведенном в примере.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести три найденных числа в формате, приведенном в примере.

# Примечание 1. Если бы файл file.txt содержал строки:

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# то результатом было бы:

# Input file contains:
# 108 letters 
# 20 words 
# 4 lines 

# Примечание 2. Словом называется последовательность из непробельных символов.
# Например, строка

# abc a21 67pop    qwert bo7ok 83456
# содержит 66 слов: abc, a21, 67pop, qwert, bo7ok, 83456.

with open('file.txt', 'r', encoding='utf-8') as file:
    file_list = list(map(str.strip, file.readlines()))
    count_letters = 0
    for line in file_list:
        for char in line:
            if char.isalpha():
                count_letters += 1
    count_words = sum(map(lambda line: len(line.split()), file_list))
    count_lines = len(file_list)
    print (f"""Input file contains:
{count_letters} letters 
{count_words} words 
{count_lines} lines""")



# Random name and surname
# Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами,
# другой с фамилиями.

# Напишите программу, которая c помощью модуля random создает 33 случайные пары имя
# + фамилия, а затем выводит их, каждую на отдельной строке.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести текст в формате, приведенном в примере.

# Примечание 1. Если бы файлы first_names.txt и last_names.txt содержали строки:

# Aaron
# Abdul
# Abe
# Abel
# Abraham
# Albert

# и

# Abramson
# Adamson
# Adderiy
# Addington
# Adrian
# Albertson
# Einstein

# то результатом могло быть:

# Abdul Albertson
# Abel Adamson
# Albert Einstein

from random import *

with open('first_names.txt', 'r', encoding='utf-8') as first_names, open('last_names.txt', 'r', encoding='utf-8') as last_names:
    random_names = []
    first_names_list = list(map(str.strip, first_names.readlines()))
    last_names_list = list(map(str.strip, last_names.readlines()))
    for i in range(3):
        random_names.append([choice(first_names_list), choice(last_names_list)])
    [print(*random_names[i]) for i in range(len(random_names))]



# Необычные страны
# Вам доступен текстовый файл population.txt с названиями стран и численностью их
# населения, разделенными символом табуляции '\t'.

# Напишите программу выводящую все страны, название которых начинается с буквы 'G',
# численность населения которых больше чем 500 \, 000500000 человек, не меняя их
# порядок.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести названия стран, удовлетворяющие условиям задачи, каждое
# на отдельное строке.

# Решение через словарь
with open('population.txt', 'r', encoding='utf-8') as population:
    population_list = [line.strip().split() for line in population.readlines()]
    population_dict = {}

    for city_info in population_list:
        population_dict[city_info[-1]] = population_dict.get(city_info[-1], []) + [city_info[0:-1]]
    
    for key, value in population_dict.items():
        if value[0][0][0] == 'G' and int(key) > 500000:
            print(*value[0])

# Стандартное решение
with open('population.txt', 'r', encoding='utf-8') as population:
    for line in population:
        city_name, pop = line.split('\t')
        if city_name[0] == 'G' and int(pop) > 500000:
            print(city_name)