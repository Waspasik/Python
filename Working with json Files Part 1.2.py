# Спортивные площадки
# Вам доступен файл playgrounds.csv с информацией о спортивных площадках Москвы. В
# первом столбце записан тип площадки,  во втором — административный округ, в третьем
# — название района, в четвертом — адрес:

# ObjectName;AdmArea;District;Address
# Парк, озелененная городская территория «Лианозовский парк культуры и отдыха»;Северо-Восточный административный округ;район Лианозово;Угличская улица, дом 13
# ...

# Напишите программу, создающую JSON-объект, ключом в котором является административный
# округ, а значением — JSON-объект, в котором, в свою очередь, ключом является название
# района, относящийся к этому административному округу, а значением — список адресов всех
# площадок в этом районе. Полученный JSON-объект программа должна записать в файл addresses.json.

# Примечание 1. Адреса в списках должны располагаться в своем исходном порядке.

# Примечание 2. Разделителем в файле playgrounds.csv является точка с запятой, при этом
# кавычки не используются.

# Примечание 3. Начальная часть файла addresses.json выглядит так:

# {
#    "Северо-Восточный административный округ": {
#       "район Лианозово": [
#          "Угличская улица, дом 13",
#          "Алтуфьевское шоссе, дом 147А"
#       ],
#       "район Отрадное": [
#          "Алтуфьевское шоссе, дом 20А",
#          "Юрловский проезд, дом 8, строение 1",
#          "Юрловский проезд, дом 8, строение 1"
#       ],
#       ...
#    },
#    ...
# }

import csv
import json

with open('D:/Python/Stepik/playgrounds.csv', 'r', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';')
    sports_grounds_dict = {}
    for row_data in data:
        sports_grounds_dict[row_data['AdmArea']] = sports_grounds_dict.get(row_data['AdmArea'], {})
        sports_grounds_dict[row_data['AdmArea']][row_data['District']] = sports_grounds_dict[row_data['AdmArea']].get(row_data['District'], []) + [row_data['Address']]
    
    with open('D:/Python/Stepik/addresses.json', 'w', encoding='utf-8') as new_file:
        json.dump(sports_grounds_dict, new_file, indent=3)



# Студенты курса
# Вам доступен файл students.json, содержащий список JSON-объектов, которые представляют
# данные о студентах некоторого курса:

# [
#    {
#       "name": "Holly-Anne",
#       "city": "Abilene",
#       "age": 29,
#       "progress": 85,
#       "phone": "(802) 983-9126"
#    },
#    ...
# ]

# Под «студентом» мы будем подразумевать один JSON-объект из этого списка. У студента
# имеются следующие атрибуты:

# name — имя 
# city — город проживания
# age — возраст
# progress — прогресс по курсу в процентах
# phone— контактный номер

# Напишите программу, которая определяет студентов, удовлетворяющих следующим условиям:

# возраст 18 лет или более
# прогресс по курсу 75 % или более

# Программа должна создать файл data.csv с двумя столбцами — name (имя) и phone (номер),
# и записать в него данные выбранных студентов, расположив их в лексикографическом порядке
# имён. В качестве разделителя в файле data.csv должна быть использована запятая.

# Примечание 1. Гарантируется, что все студенты имеют различные имена.

# Примечание 2. Начальная часть файла data.csv выглядит так:

# name,phone
# Cary,(580) 476-8517
# Catarina,(237) 608-2757
# Catherin,(876) 215-3666
# ...

import csv
import json

with open('D:/Python/Stepik/students.json', encoding='utf-8') as file:
    data = json.load(file)
    students_list = []

    for elem in data:
        if elem['progress'] >= 75 and elem['age'] >= 18:
            student_info = [elem['name'], elem['phone']]
            students_list.append(student_info)

    with open('D:/Python/Stepik/data.csv', 'w', encoding='utf-8', newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(['name', 'phone'])
        for name, phone in sorted(students_list):
            writer.writerow([name, phone])