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
            
            
            
# Бассейны
# Тимур планирует пойти в бассейн. Среди всех бассейнов ему подходят те, которые открыты
# в понедельник в период с 10:00 до 12:00. Также ему нравится плавать по длинным дорожкам,
# поэтому из всех работающих в это время бассейнов нужно выбрать бассейн с наибольшей
# длиной дорожки, при равных значениях — c наибольшей шириной.

# Вам доступен файл pools.json, содержащий список JSON-объектов, которые представляют
# данные о крытых плавательных бассейнах:

# [
#    {
#       "ObjectName": "Физкультурно-оздоровительный комплекс с бассейном «ГБУ «СШОР № 82» Москомспорта»",
#       "AdmArea": "Северо-Восточный административный округ",
#       "District": "Алтуфьевский район",
#       "Address": "Инженерная улица, дом 5, корпус 1",
#       "WorkingHoursSummer": {
#          "Понедельник": "10:00-11:00",
#          "Вторник": "10:00-11:00",
#          "Среда": "10:00-11:00",
#          "Четверг": "10:00-11:00",
#          "Пятница": "10:00-11:00",
#          "Суббота": "10:00-11:00",
#          "Воскресенье": "09:00-15:00",
#       },
#       "DimensionsSummer": {
#          "Square": 350,
#          "Length": 25,
#          "Width": 14,
#          "Depth": 1.8
#       }
#    },
#    ...
# ]

# Под «бассейном» будем подразумевать один JSON-объект из этого списка. У бассейна имеются
# следующие атрибуты:

# ObjectName — название, будь то фитнес клуб или спортивный комплекс
# AdmArea — административный округ
# District — название района
# Address — адрес
# WorkingHoursSummer — график работы, время начала и закрытия указываются в формате HH:MM
# DimensionsSummer — размеры бассейна, где Square — площадь, Length — длина, Width — ширина, Depth — глубина

# Напишите программу, которая определяет бассейн, подходящий Тимуру. Программа должна вывести
# его размеры и адрес в следующем формате:

# <длина>x<ширина>
# <адрес>

# Примечание 1. Пример вывода:

# 25x16
# Писцовая улица, дом 12, строение 1

# Примечание 2. Бассейн должен быть открыт во время всего периода с 10:00 до 12:00. Например,
# если бассейн работает в 10:00, но не работает в 11:30, он не подходит.

import json
from datetime import datetime


def pool(length, width, address):
        return [f'{length}x{width}', address]


with open('D:/Python/Stepik/pools.json', encoding='utf-8') as file:
    data = json.load(file)
    min_length = 1
    min_width = 1

    for elem in data:
        working_hours = list(map(lambda x: datetime.strptime(x, '%H:%M'), elem['WorkingHoursSummer']['Понедельник'].split('-')))
        if working_hours[0] <= datetime.strptime('10:00', '%H:%M') and working_hours[1] >= datetime.strptime('12:00', '%H:%M'):
            if elem['DimensionsSummer']['Length'] > min_length:
                min_length = elem['DimensionsSummer']['Length']
                min_width = elem['DimensionsSummer']['Width']
                needed_pool = pool(min_length, min_width, elem['Address'])
            elif elem['DimensionsSummer']['Length'] == min_length:
                if elem['DimensionsSummer']['Width'] >= min_width:
                    min_length = elem['DimensionsSummer']['Length']
                    min_width = elem['DimensionsSummer']['Width']
                    needed_pool = pool(min_length, min_width, elem['Address'])
    
    print(*needed_pool, sep='\n')



# Результаты экзамена 🌶️
# Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене в некотором
# учебном заведении. В первом столбце записано имя студента, во втором — фамилия, в третьем — оценка
# за экзамен, в четвертом — дата и время сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес
# электронной почты:

# name,surname,score,date_and_time,email
# Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
# April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
# ...

# Каждый студент имеет право пересдать экзамен два раза, поэтому он может встречаться в исходном
# файле до трёх раз с различной оценкой и различными датой и временем сдачи.

# Напишите программу, которая для каждого студента определяет его максимальную оценку, а также дату
# и время ее получения. Программа должна создать список словарей, каждый из которых содержит следующие
# пары ключ-значение:

# name — имя студента
# surname — фамилия студента
# best_score — максимальная оценка за экзамен
# date_and_time — дата и время получения максимальной оценки в исходном формате
# email — адрес электронной почты

# Полученный список программа должна записать в файл best_scores.json, причем словари в списке должны
# быть расположены в лексикографическом порядке названий электронных почт.

# Примечание 1. Если при пересдаче студент получил такую же оценку, что и в прошлый раз, то в качестве
# даты следует указать дату пересдачи.

# Примечание 2. В качестве разделителя в файле exam_results.csv используется запятая, при этом кавычки
# не используются.

# Примечание 3. Начальная часть файла best_scores.json выглядит так:

[
   {
      "name": "Stephen",
      "surname": "Farley",
      "best_score": 3,
      "date_and_time": "2021-11-12 12:00:00",
      "email": "aardo@mac.com"
   },
   {
      "name": "Kaylen",
      "surname": "Horne",
      "best_score": 4,
      "date_and_time": "2021-11-09 11:00:00",
      "email": "aaribaud@att.net"
   },
   ...
]

import csv
import json
from datetime import datetime


with open('D:/Python/Stepik/exam_results.csv', 'r', encoding='utf-8') as file:
    file_reader_list = list(csv.DictReader(file))
    students_scores = {}
    result_dict = {}
    
    for student_info in file_reader_list:
        students_scores[student_info['email']] = students_scores.get(student_info['email'], {})
        exam_dtime = datetime.strptime(student_info['date_and_time'], '%Y-%m-%d %H:%M:%S')
        students_scores[student_info['email']][int(student_info['score'])] = students_scores[student_info['email']].get(int(student_info['score']), []) + [exam_dtime]
    
    for email, scores_dtime in students_scores.items():
        best_score = max(scores_dtime)
        last_dtime = max(scores_dtime[best_score]).strftime('%Y-%m-%d %H:%M:%S')
        for info in file_reader_list:
            if info['email'] == email:
                final_info = {'name': info['name'], 'surname': info['surname'], 'best_score': best_score,'date_and_time': last_dtime, 'email': info['email']}
                result_dict[email] = result_dict.get(email, final_info)
                break
    
    with open('D:/Python/Stepik/best_scores.json', 'w', encoding='utf-8') as new_file:
        exam_results_json = [info for _, info in sorted(result_dict.items(), key=lambda x: x[0])]
        json.dump(exam_results_json, new_file, indent=3)
    
    
    
# Общественное питание 😥
# Вам доступен файл food_services.json, содержащий список JSON-объектов, которые
# представляют данные о заведениях общественного питания:

# [
#    {
#       "Name": "СМЕТАНА",
#       "IsNetObject": "нет",
#       "OperatingCompany": "",
#       "TypeObject": "кафе",
#       "AdmArea": "Северо-Восточный административный округ",
#       "District": "Ярославский район",
#       "Address": "город Москва, улица Егора Абакумова, дом 9",
#       "SeatsCount": 48
#    },
#    ...
# ]

# Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения
# имеются следующие атрибуты:

# Name — название 
# IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
# OperatingCompany — название сети
# TypeObject — вид (кафе, столовая, ресторан и т.д.)
# AdmArea — административная зона
# District — район
# Address — полный адрес
# SeatsCount — количество мест

# Напишите программу, которая:
# определяет район Москвы, в котором находится больше всего заведений, и выводит название
# этого района и количество заведений в нем
# определяет сеть с самым большим числом заведений и выводит название этой сети и количество
# заведений этой сети

# Полученные значения программа должна вывести в следующем формате:

# <район>: <количество заведений>
# <название сети>: <количество заведений>

# Примечание 1. Гарантируется, что искомая сеть единственная.

# Примечание 2. Пример вывода:

# район Метрогородок: 456
# Французская пекарня SeDelice: 144

import json

with open('D:/Python/Stepik/food_services.json', encoding='utf-8') as file:
    data = json.load(file)
    amount_net_object = {}
    amount_objects = {}

    for elem in data:
        amount_objects[elem['District']] = amount_objects.get(elem['District'], 0) + 1
        if elem['IsNetObject'] == 'да':
            amount_net_object[elem['OperatingCompany']] = amount_net_object.get(elem['OperatingCompany'], 0) + 1
    
    max_objects = max(amount_objects, key=amount_objects.get)
    max_net_object = max(amount_net_object, key=amount_net_object.get)

    print(f'{max(amount_objects, key=amount_objects.get)}: {amount_objects[max_objects]}')
    print(f'{max(amount_net_object, key=amount_net_object.get)}: {amount_net_object[max_net_object]}')



# Общественное питание 😰
# Вам доступен файл food_services.json, содержащий список JSON-объектов, которые
# представляют данные о заведениях общественного питания:

# [
#    {
#       "Name": "СМЕТАНА",
#       "IsNetObject": "нет",
#       "OperatingCompany": "",
#       "TypeObject": "кафе",
#       "AdmArea": "Северо-Восточный административный округ",
#       "District": "Ярославский район",
#       "Address": "город Москва, улица Егора Абакумова, дом 9",
#       "SeatsCount": 48
#    },
#    ...
# ]

# Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения
# имеются следующие атрибуты:

# Name — название 
# IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
# OperatingCompany — название сети
# TypeObject — вид (кафе, столовая, ресторан и т.д.)
# AdmArea — административная зона
# District — район
# Address — полный адрес
# SeatsCount — количество мест

# Напишите программу, которая определяет все виды заведений и для каждого вида находит
# самое большое заведение этого вида (имеет наибольшее количество посадочных мест).
# Программа должна вывести все виды заведений в лексикографическом порядке, указав для
# каждого самое большое заведение и количество посадочных мест в нем. Данные о заведениях
# должны быть расположены каждые на отдельной строке, в следующем формате:

# <вид заведения>: <название заведения>, <количество посадочных мест>

# Примечание 1. Начальная часть ответа выглядит так:

# бар: Барное объединение ПРОФСОЮЗ, 800
# буфет: СТОЛОВАЯ - КАНТИНАСИТИ, 320
# закусочная: Бургерная FARШ, 74
# ...

import json

with open('D:/Python/Stepik/food_services.json', encoding='utf-8') as file:
    data = json.load(file)
    type_objects = {}
    result = []

    for elem in data:
        type_objects[elem['TypeObject']] = type_objects.get(elem['TypeObject'], []) + [[elem['SeatsCount'], elem['Name']]]
        
    for type, object in type_objects.items():
        bigest_type = f'{type}: {max(object)[1]}, {max(object)[0]}'
        result.append(bigest_type)

    print(*sorted(result), sep='\n')
