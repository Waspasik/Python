# Функция get_weekday()
# Реализуйте функцию get_weekday(), которая принимает один аргумент:

# number — целое число (от 1 до 7 включительно)

# Функция должна возвращать полное название дня недели на русском, который
# соответствует числу number, при этом:

# если number не является целым числом, функция должна возбуждать исключение: 
# TypeError('Аргумент не является целым числом')

# если number является целым числом, но не принадлежит отрезку [1;7], функция
# должна возбуждать исключение: 
# ValueError('Аргумент не принадлежит требуемому диапазону')

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию get_weekday(), но не код, вызывающий ее.

import calendar, locale

def get_weekday(number):
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    day_names = calendar.day_name
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    if isinstance(number, int) and number not in [i for i in range(1, 8)]:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        return day_names[number - 1]



# Функция get_id()
# В онлайн-школе BEEGEEK имя ученика считается корректным, если оно начинается с
# заглавной латинской буквы, за которой следуют строчные латинские буквы. Например,
# имена Timur и Yo считаются корректными, а имена timyrik, Yo17, TimuRRR нет. Также
# у каждого ученика имеется идентификационный номер, представленный натуральным числом,
# который выдается при поступлении в школу. К примеру, если в школе обучается 10
# учеников, то новый прибывший ученик получит идентификационный номер равный 11.

# Реализуйте функцию get_id(), которая принимает два аргумента:

# names — список имен учеников, обучающихся в школе
# name — имя поступающего ученика

# Функция должна возвращать идентификационный номер, который получит поступающий в школу
# ученик, при этом

# если имя ученика name не является строкой (тип str), функция должна возбуждать исключение:
# TypeError('Имя не является строкой')

# если имя ученика name является строкой (тип str), но не представляет собой корректное
# имя, функция должна возбуждать исключение:
# ValueError('Имя не является корректным')

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию get_id(), но не код, вызывающий ее. 

def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    if not (name[0].isupper() and name[1:].islower() and name.isalpha()):
        raise ValueError('Имя не является корректным')
    return len(names) + 1



# Десериализация
# Напишите программу, которая принимает на вход название JSON файла, десериализует
# содержащийся в этом файле объект и выводит его.

# если файла с данным названием нет в папке с программой, программа должна вывести
# текст:
# Файл не найден

# если файл с данным названием содержит некорректные данные (то есть не удовлетворяющие
# формату JSON), программа должна вывести текст:
# Ошибка при десериализации

# Формат входных данных
# На вход программе подается название JSON файла.

# Формат выходных данных
# Программа должна десериализовать объект, содержащийся в файле с введенным названием,
# и вывести его. Если при поиске файла или десериализации его содержимого произошла
# ошибка, программа должна вывести соответствующий текст.

# Примечание 1. Название подаваемого файла уже содержит расширение.

import json

try:
    file = open(input(), 'r', encoding='utf-8')
    try:
        read_file = json.load(file)
        print(read_file)
    except:
        print('Ошибка при десериализации')
except FileNotFoundError:
    print('Файл не найден')