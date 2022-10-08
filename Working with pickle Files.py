# Найдите и исправьте ошибки, допущенные в приведенной ниже программе, чтобы
# она сериализовала словарь dogs и записала результат в файл dogs.pkl.

import pickle

dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}

with open('dogs.pkl', mode='wb') as file:
    pickle.dump(dogs, file)



# Одинокая функция
# Дан pickle файл, содержащий единственную сериализованную функцию. Напишите
# программу, которая вызывает данную функцию с заданными аргументами и выводит
# возвращаемое значение функции.

# Формат входных данных
# На вход программе в первой строке подается название pickle файла, в котором
# содержится единственная сериализованная функция. Далее подается произвольное
# количество строк, каждая из которых содержит позиционный аргумент для этой
# функции.

# Формат выходных данных
# Программа должна вызвать функцию из указанного pickle файла со всеми введенными
# строковыми аргументами, и вывести возвращаемое значение функции. Причем аргументы
# должны быть переданы в том порядке, в котором они были введены.

# Примечание 1. Аргументы, передаваемые в функцию, должны иметь тип str.

# Примечание 2. Рассмотрим первый тест. Сначала подается название файла — func.pkl,
# в котором содержится сериализованная функция:

# def func(*args):
#     return ' '.join(args)

# затем аргументы для этой функции: Hello,, how, are, you и today?.

# Программа выводит результат следующего вызова:

# func('Hello,', 'how', 'are', 'you', 'today?')

# Примечание 3. Для считывания произвольного количества строк используйте потоковый
# ввод sys.stdin.

# Примечание 4. Считайте, что вводимый файл находится в папке с программой.

import pickle
import sys

with open(input(), 'rb') as file:
    obj = pickle.load(file)
    args = [str(arg).strip() for arg in sys.stdin]
    print(obj(*args))



# Ты не пройдешь
# Реализуйте функцию filter_dump(), которая принимает три аргумента в следующем
# порядке:

# filename — название pickle файла, например, data.pkl
# objects — список произвольных объектов
# typename — тип данных

# Функция должна создавать pickle файл с названием filename, который содержит
# сериализованный список только тех объектов из списка objects, тип которых равен
# typename.

# Примечание 1. Например, вызов функции filter_dump() следующим образом:

# filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)

# должен создавать файл numbers.pkl, содержащий сериализованный список [1, 3, 4].

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию filter_dump(), но не код, вызывающий ее.

import pickle

def filter_dump(filename , objects, typename):
    with open(filename, 'wb') as file:
        pickle.dump(list(filter(lambda x: type(x) == typename, objects)), file)



# Контрольная сумма
# По каналу связи передаются pickle файл, содержащий сериализованный словарь или
# список, и целое число — контрольная сумма, которая вычисляется по следующему
# правилу:

# для словаря — сумма всех целочисленных ключей (тип int)
# для списка — произведение минимального и максимального целочисленных элементов
# (тип int)

# Напишите программу, которая вычисляет контрольную сумму для объекта, содержащегося
# в pickle файле, и сравнивает ее с данным целым числом.

# Формат входных данных
# На вход программе в первой строке подается название pickle файла, в котором
# содержится сериализованный словарь или список, в следующей — целое число.

# Формат выходных данных
# Программа должна вычислить контрольную сумму для объекта, который содержится в
# данном pickle файле, и

# если она совпадает с введенным числом, вывести текст:
# Контрольные суммы совпадают
# если она не совпадает с введенным числом, вывести текст:
# Контрольные суммы не совпадают

# Примечание 1. Если список (словарь) не содержит целочисленных элементов (ключей),
# то считайте, что контрольная сумма равна 00.

# Примечание 2. Рассмотрим первый тест. Подается название файла — data.pkl, в котором
# содержится сериализованный список:

# ['a', 'b', 3, 4, 'f', 'g', 7, 8]

# затем число — 3023. Контрольная сумма для данного списка равна 3 ⋅ 8 = 24. Так как
# 3023 != 24, программа выводит:

# Контрольные суммы не совпадают

import pickle

file_name, sm = input(), int(input())
with open(file_name, 'rb') as file:
    obj = pickle.load(file)
    filtered_obj = [elem for elem in obj if type(elem) == int] or [0]
    check = sum(filtered_obj) if type(obj) == dict else max(filtered_obj) * min(filtered_obj)
    print(['Контрольные суммы не совпадают', 'Контрольные суммы совпадают'][sm == check])