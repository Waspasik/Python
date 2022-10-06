# Форматированный вывод
# Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу,
# которая выводит названия всех файлов из этого архива в лексикографическом порядке,
# указывая для каждого его дату изменения, а также объем до и после сжатия, в следующем
# формате:

# <название файла>
#   Дата модификации файла: <дата изменения>
#   Объем исходного файла: <объем до сжатия> байт(а)
#   Объем сжатого файла: <объем после сжатия> байт(а)

# Между данными о двух файлах должна располагаться пустая строка.

# Примечание 1. Если файл находится в папке, вывести следует только название без пути.

# Примечание 2. Начальная часть ответа выглядит так (в качестве отступов используйте два
# пробела):

# Alexandra Savior – Crying All the Time.mp3
#   Дата модификации файла: 2021-11-30 13:27:02
#   Объем исходного файла: 5057559 байт(а)
#   Объем сжатого файла: 5051745 байт(а)

# code.jpeg
#   Дата модификации файла: 2021-11-30 13:18:26
#   Объем исходного файла: 412414 байт(а)
#   Объем сжатого файла: 410006 байт(а)

# ...

from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    result = []
    for file in sorted(zip_file.infolist(), key=lambda item: item.filename.lower().split('/')[-1]):
        if not file.is_dir():
            info_file = [file.filename.split('/')[-1], 
                         f'  Дата модификации файла: {datetime(*file.date_time).strftime("%Y-%m-%d %H:%M:%S")}',
                         f'  Объем исходного файла: {file.file_size} байт(а)',
                         f'  Объем сжатого файла: {file.compress_size} байт(а)',
                         '']
            result.append(info_file)
    
    for lst in result:
        print(*lst, sep='\n')



# Шахматы были лучше 🌶️
# Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть
# несколько JSON файлов, каждый из которых содержит информацию о каком-либо футболисте:

# {
#    "first_name": "Gary",
#    "last_name": "Cahill",
#    "team": "Chelsea",
#    "position": "Defender"
# }

# У футболиста имеются следующие атрибуты: 

# first_name — имя
# last_name — фамилия
# team — название футбольного клуба
# position — игровая позиция

# Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и
# фамилии футболистов, выступающих за футбольный клуб Arsenal. Футболисты должны быть
# расположены в лексикографическом порядке имен, а при совпадении — в лексикографическом
# порядке фамилий, каждый на отдельной строке.

# Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует,
# что он является корректным текстовым файлом в формате JSON. Для того чтобы определить,
# является ли файл корректным текстовым файлом в формате JSON, воспользуйтесь конструкцией
# try-except и функцией is_correct_json().

# Примечание 2. Начальная часть ответа выглядит так:

# Alex Iwobi
# Alexis Sanchez
# ...

from zipfile import ZipFile
import json


def is_correct_json(f):
    try:
        data = json.loads(f)
        if bool(data):
            return True
    except json.decoder.JSONDecodeError:
        return False


def is_correct_decode(f):
    try:
        with zip_file.open(f.filename) as file:
            file_read = file.read().decode('utf-8')
            if is_correct_json(file_read):
                return creat_set_players(file_read)
    except:
        return False


def creat_set_players(file):
    data = json.loads(file)
    if data['team'] == 'Arsenal':
        player = f'{data["first_name"]} {data["last_name"]}'
        result.add(player)


with ZipFile('data.zip') as zip_file:
    result = set()
    for file in zip_file.infolist():
        if not file.is_dir():
            is_correct_decode(file)
    print(*sorted(result), sep='\n')
