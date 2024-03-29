# Входная строка

# Напишите программу, которая считывает строку текста и записывает её в текстовый
# файл output.txt.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна создать файл с именем output.txt и записать в него считанную
# строку текста.

# Примечание. Считайте, что исполняемая программа и указанный файл находятся в
# одной папке.

with open('output.txt', 'w') as output:
    print(input(), file=output)



# Случайные числа

# Напишите программу, записывающую в текстовый файл random.txt 25 случайных чисел
# в диапазоне от 111 до 777 (включительно), каждое с новой строки.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна создать файл с именем random.txt и записать в него случайные
# числа в соответствии с условием задачи.

# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся
# в одной папке.

# Примечание 2. Для генерации случайных чисел используйте модуль random.

from random import *

with open('random.txt', 'w') as output:
    for _ in range(25):
        print(randint(111, 777), file=output)
    


# Нумерация строк

# Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите
# программу для записи содержимого этого файла в файл output.txt в виде нумерованного
# списка, где перед каждой строкой стоит ее номер, символ ) и пробел. Нумерация строк
# должна начинаться с 1.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна создать файл с именем output.txt и записать в него пронумерованные
# строки файла input.txt.

# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной
# папке.

# Примечание 2. Используйте встроенную функцию enumerate().

# Примечание 3. Если бы файл input.txt содержал строки:

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# то файл output.txt имел бы вид:

# 1) Beautiful is better than ugly.
# 2) Explicit is better than implicit.
# 3) Simple is better than complex.
# 4) Complex is better than complicated.

with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w') as output_file:
    lines_list = list(map(str.strip, input_file.readlines()))
    for line in enumerate(lines_list, 1):
        print(f'{line[0]}) {line[1]}', file=output_file)



# Подарок на новый год

# Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках
# вида: фамилия оценка (фамилия и оценка разделены пробелом). Оценка - целое число от
# 0 до 100 включительно.

# Напишите программу для добавления 5 баллов к каждому результату теста и вывода фамилий
# и новых результатов тестов в файл new_scores.txt.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна создать файл с именем new_scores.txt в соответствии с условием задачи.

# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной
# папке.

# Примечание 2. Если бы файл class_scores.txt содержал строки:

# Washington 83
# Adams 86
# Kingsman 100
# MacDonald 95
# Thomson 98

# то файл new_scores.txt имел бы вид:

# Washington 88
# Adams 91
# Kingsman 100
# MacDonald 100
# Thomson 100

with open('class_scores.txt', 'r', encoding='utf-8') as class_scores, open('new_scores.txt', 'w') as new_scores:
    for line in class_scores:
        new_line = line.strip().split()
        if int(new_line[1]) + 5 <= 100:
            new_mark = int(new_line[1]) + 5
        else:
            new_mark = 100
        print(f'{new_line[0]} {new_mark}', file=new_scores)



# Загадка от Жака Фреско 🌶️

# Однажды Жака Фреско спросили:

# "Если ты такой умный, почему не богатый?"

# Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку
# спрашивающему:

# "Были разноцветные козлы. Сколько?"

# "Сколько чего?"

# "Сколько из них составляет более 7% от общего количества козлов?"

# Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS,
# далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS, и
# далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только
# строки из первого списка.

# Напишите программу создания файла answer.txt и вывода в него списка козлов, которые
# удовлетворяют условию загадки от Жака Фреско.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна создать файл с именем answer.txt и вывести в него в алфавитном порядке
# названия цветов козлов, которые удовлетворяют условию загадки Жака Фреско.

# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной
# папке.

# Примечание 2. Если бы файл goats.txt содержал строки:

# COLOURS
# Pink goat
# Green goat
# Black goat
# GOATS
# Pink goat
# Pink goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# Green goat
# Pink goat
# Black goat
# Black goat
# Pink goat
# Pink goat
# Black goat
# 3Black goat
# Pink goat

# то файл answer.txt имел бы вид:

# Black goat
# Pink goat

with open('goats.txt', 'r', encoding='utf-8') as goats, open('answer.txt', 'w') as answer:
    goats_list = list(map(str.strip, goats.readlines()))
    goats_list = goats_list[len(set(goats_list)):]

    result = {}

    for colour in goats_list:
        result[colour] = result.get(colour, 0) + 1
    
    for key, value in result.items():
        if value > len(goats_list) * 0.07:
            print(key, file=answer)



# Конкатенация файлов 🌶️

# На вход программе подается натуральное число n и n строк с названиями файлов.
# Напишите программу, которая создает файл output.txt и выводит в него содержимое
# всех файлов с указанными именами, не меняя их порядка.

# Формат входных данных
# На вход программе подается натуральное число n и n строк названий существующих
# файлов.

# Формат выходных данных
# Программа должна создать файл с именем output.txt в соответствии с условием задачи.

# Примечание. Считайте, что исполняемая программа и указанные файлы находятся в
# одной папке.

with open('output.txt', 'w') as output:
    for _ in range(int(input())):
        with open(input()) as other_file:
            output.write(other_file.read())



# Лог файл 🌶️

# Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя
# в систему и выхода из нее. Каждая строка файла содержит три значения, разделенные
# запятыми и символом пробела: имя пользователя, время входа, время выхода, где время
# указано в 24-часовом формате.

# Напишите программу, которая создает файл output.txt и выводит в него имена всех
# пользователей (не меняя порядка следования), которые были в сети не менее часа.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна создать файл с именем output.txt в соответствии с условием задачи.

# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в
# одной папке.

# Примечание 2. Считайте, что каждый пользователь был только раз в системе, то есть
# в файле нет двух строк с одинаковым пользователем.

# Примечание 3. Если бы файл logfile.txt содержал строки:

# Тимур Гуев, 14:10, 15:50
# Руслан Гриценко, 12:00, 12:59
# Роман Гацалов, 09:10, 17:45
# Габолаев Георгий, 11:10, 12:10

# то файл output.txt имел бы вид:

# Тимур Гуев
# Роман Гацалов
# Габолаев Георгий

with open('logfile.txt', 'r', encoding='utf-8') as logfile, open('output.txt', 'w') as output:
    def minutes(x):
        res=[int(i) for i in x.split(':')]
        return res[0]*60+res[1]
    
    for line in logfile.readlines():
        line = line.strip().split(', ')
        if minutes(line[1]) + 60 <= minutes(line[2]):
            print(line[0], file=output)