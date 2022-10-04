# Количество файлов
# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит единственное число — количество
# файлов в этом архиве.

# Примечание 1. Обратите внимание, что папка не считается файлом.

from zipfile import ZipFile

print(len(list(filter(lambda f: not f.is_dir(), ZipFile('workbook.zip').infolist()))))



# Объем файлов
# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит суммарный объем файлов этого архива
# в сжатом и не сжатом видах в байтах, в следующем формате:

# Объем исходных файлов: <объем до сжатия> байт(а)
# Объем сжатых файлов: <объем после сжатия> байт(а)

from zipfile import ZipFile
from functools import reduce

with ZipFile('workbook.zip') as zip_file:
    files_size = reduce(lambda x, y: x + y.file_size, zip_file.infolist(), 0)
    files_compress_size = reduce(lambda x, y: x + y.compress_size, zip_file.infolist(), 0)
    print(f'Объем исходных файлов: {files_size} байт(а)')
    print(f'Объем сжатых файлов: {files_compress_size} байт(а)')



# Наилучший показатель
# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит название файла из этого архива,
# который имеет наилучший показатель степени сжатия.

# Примечание 1. Если файл находится в папке, вывести следует только
# название без пути.

# Примечание 2. Гарантируется, что в исходном архиве только один файл
# имеет наилучший показатель степени сжатия.

from zipfile import ZipFile

def canculation_compression_ratio(file_size, compress_size):
    return (file_size / compress_size) * 100

with ZipFile('workbook.zip') as zip_file:
    compression_ratio = {}
    for file in zip_file.infolist():
        if not file.is_dir():
            compression_ratio[file.filename] = compression_ratio.get(file.filename, canculation_compression_ratio(file.file_size, file.compress_size))
    
    print(max(compression_ratio, key=compression_ratio.get).split('/')[-1])



# Избранные
# Вам доступен архив workbook.zip, содержащий различные папки и файлы.
# Напишите программу, которая выводит названия файлов из этого архива,
# которые были созданы или изменены позднее 2021-11-30 14:22:00. Названия
# файлов должны быть расположены в лексикографическом порядке, каждое на
# отдельной строке.

# Примечание 1. Если файл находится в папке, вывести следует только название
# без пути.

# Примечание 2. Начальная часть ответа выглядит так:

# countries.json
# data_sample.csv
# ...

from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    result = []
    for file in zip_file.infolist():
        if not file.is_dir() and datetime(*file.date_time) >= datetime(2021,11, 30, 14, 22, 0):
            result.append(file.filename.split('/')[-1])
    
    print(*sorted(result), sep='\n')



# Вам доступен набор различных файлов, названия которых представлены в списке
# file_names. Дополните приведенный ниже код, чтобы он создал архив files.zip
# и добавил в него все файлы из данного списка.

# Примечание. Считайте, что файлы из списка file_names находятся в папке с
# программой.

from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']

with ZipFile('files.zip', mode='w') as zip_file:
    for file in file_names:
        zip_file.write(file)



# Вам доступен набор различных файлов, названия которых представлены в списке
# file_names. Также вам доступен архив files.zip. Дополните приведенный ниже
# код, чтобы он добавил в архив files.zip только те файлы из списка file_names,
# объем которых не превышает 100100 байт.

# Примечание 1. Получить объем файла в байтах позволяет функция getsize() из
# модуля os.path. Данная функция принимает в качестве аргумента путь к файлу
# и возвращает размер указанного файла в байтах.

# Примечание 2. Считайте, что файлы из списка file_names и архив files.zip
# находятся в папке с программой.

from zipfile import ZipFile
import os.path

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']

with ZipFile('files.zip', mode='w') as zip_file:
    for file in file_names:
        if os.path.getsize(file) <= 100:
            zip_file.write(file)



# Функция extract_this()
# Реализуйте функцию extract_this(), которая принимает один или более аргументов
# в следующем порядке:

# zip_name — название zip архива, например, data.zip
# *args — переменное количество позиционных аргументов, каждый из которых является
# названием некоторого файла

# Функция должна извлекать файлы *args из архива zip_name в папку с программой.
# Если в функцию не передано ни одного названия файла для извлечения, то функция
# должна извлечь все файлы из архива.

# Примечание 1. Например, следующий вызов функции

# extract_this('workbook.zip', 'earth.jpg', 'exam.txt')

# должен извлечь из архива workbook.zip файлы earth.jpg и exam.txt в папку с программой.

# Вызов функции

# extract_this('workbook.zip')

# должен извлечь из архива workbook.zip все файлы в папку с программой.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию extract_this(), но не код, вызывающий ее.

from zipfile import ZipFile

def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if args:
            for file_name in args:
                zip_file.extract(file_name)
        else:
            zip_file.extractall()