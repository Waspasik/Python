# Средняя зарплата
# Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах
# сотрудников в различных компаниях. В первом столбце записано название компании, а во
# втором — зарплата очередного сотрудника:

# company_name;salary
# Atos;135000
# ХайТэк;24400
# Philax;128600
# Инлайн Груп;43900
# IBS;70600
# Oracle;131600
# Atos;91000
# ...

# Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее
# сотрудников и выводит их названия, каждое на отдельной строке. Если две компании имеют
# одинаковые средние зарплаты, они должны быть расположены в лексикографическом порядке
# их названий.

# Примечание 1. Средняя зарплата компании определяется как отношение суммы всех зарплат
# к их количеству.

# Примечание 2. Разделителем в файле salary_data.csv является точка с запятой, при этом
# кавычки не используются.

# Примечание 3. Начальная часть ответа выглядит так:

# Информзащита
# Форс
# OFT group
# ...

# Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.

import csv
import statistics as st

with open('salary_data.csv', encoding='utf-8') as file:
    salary_companies = {}
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        salary_companies[row['company_name']] = salary_companies.get(row['company_name'], []) + [int(row['salary'])]
    for key, value in dict(sorted(salary_companies.items(), key=lambda x: st.mean(x[1]))).items():
        print(key)



# Функция csv_columns()
# Реализуйте функцию csv_columns(), которая принимает один аргумент:

# filename — название csv файла, например, data.csv

# Функция должна возвращать словарь, в котором ключом является название столбца
# файла filename, а значением — список элементов этого столбца.

# Примечание 1. Гарантируется, что в передаваемом в функцию файле разделителем
# является запятая, при этом кавычки не используются.

# Примечание 2. Гарантируется, что у передаваемого в функцию файла первая строка
# содержит названия столбцов.

# Примечание 3. Например, если бы файл exam.csv имел вид:

# name,grade
# Timur,5
# Arthur,4
# Anri,5

# то следующий вызов функции csv_columns():

# csv_columns('exam.csv')

# должен был бы вернуть:

# {'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4', '5']}

# Примечание 4. Ключи в словаре, а также элементы в списках должны располагаться
# в своем исходном порядке.

# Примечание 5. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию csv_columns(), но не код, вызывающий ее.

import csv

def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        result_dict = {}
        reader = list(csv.reader(file, delimiter=','))
        for i in range(len(reader[0])):
            for j in range(1, len(reader)):
                result_dict[reader[0][i]] = result_dict.get(reader[0][i], []) + [reader[j][i]]
        return result_dict



# Популярные домены
# Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях
# некоторого ресурса. В первом столбце записано имя пользователя, во втором — фамилия,
# в третьем — адрес электронной почты:

# first_name,surname,email
# John,Wilson,johnwilson@outlook.com
# Mary,Wilson,marywilson@list.ru
# ...

# Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:

# domain,count
# rambler.ru,24
# iCloud.com,29
# ...

# где в первом столбце записано название почтового домена, а во втором — количество
# пользователей, использующих данный домен. Домены в файле должны быть расположены в
# порядке возрастания количества их использований, при совпадении количества использований
# — в лексикографическом порядке.

# Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не
# используются.

# Примечание 2. Начальная часть файла domain_usage.csv выглядит так:

# domain,count
# rambler.ru,24
# iCloud.com,29
# ...

import csv

with open('data.csv', encoding='utf-8') as file:
    reader = list(csv.reader(file, delimiter=','))
    domain_usage_dict = {}
    for i in range(1, len(reader)):
        domain_usage = reader[i][-1].split('@')[-1]
        domain_usage_dict[domain_usage] = domain_usage_dict.get(domain_usage, 0) + 1
        
    sorted_domain_usage_dict = dict(sorted(domain_usage_dict.items(), key=lambda x: (x[1], x[0])))
    
    with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['domain', 'count'])
        for domain_name, count in sorted_domain_usage_dict.items():
            writer.writerow([domain_name, count])



# Wi-Fi Москвы
# Вам доступен файл wifi.csv, который содержит данные о городском Wi-Fi Москвы. В
# первом столбце записано название округа, во втором – название района, в третьем
# — адрес, в четвертом — количество точек доступа по этому адресу:

# adm_area;district;location;number_of_access_points
# Центральный административный округ;район Якиманка;город Москва, улица Серафимовича,
# дом 5/16;5
# Центральный административный округ;район Якиманка;город Москва, Болотная набережная,
# дом 11, строение 1;2
# ...

# Напишите программу, которая определяет количество точек доступа в каждом районе
# Москвы и выводит названия всех районов, для каждого указывая соответствующее
# количество точек доступа, каждое на отдельной строке, в следующем формате:

# <название района>: <количество точек доступа>

# Названия районов должны быть расположены в порядке убывания количества точек доступа,
# при совпадении количества точек доступа — в лексикографическом порядке.

# Примечание 1. Разделителем в файле wifi.csv является точка с запятой, при этом кавычки
# не используются.

# Примечание 2. Начальная часть ответа выглядит так:

# Тверской район: 480
# район Хамовники: 386
# Пресненский район: 349
# ...

import csv

with open('wifi.csv', encoding='utf-8') as file:
    reader = list(csv.reader(file, delimiter=';'))
    access_points = {}

    for i in range(1, len(reader)):
        access_points[reader[i][1]] = access_points.get(reader[i][1], 0) + int(reader[i][-1])

    for district, count in sorted(access_points.items(), key=lambda x: [-x[1], x[0]]):
        print(f'{district}: {count}')



# Последний день на Титанике
# Вам доступен файл titanic.csv, который содержит данные о пассажирах, присутствовавших
# на борту парохода Титаник. В первом столбце указана единица, если пассажир выжил, и
# ноль в противном случае, во втором столбце записано полное имя пассажира, в третьем
# — пол, в четвертом — возраст:

# survived;name;sex;age
# 0;Mr. Owen Harris Braund;male;22
# 1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
# ...

# Напишите программу, которая выводит имена выживших пассажиров, которым было менее 18
# лет, каждое на отдельной строке. Причем сначала должны быть расположены имена всех
# пассажиров мужского пола, а затем — женского, имена же непосредственно в мужском и
# женском списках должны быть расположены в своем исходном порядке.

# Примечание 1. Разделителем в файле titanic.csv является точка с запятой, при этом
# кавычки не используются.

# Примечание 2. Часть ответа выглядит так:

# Master. Gerios Moubarek
# Master. Alden Gates Caldwell
# ...
# Master. Harold Theodor Johnson
# Mrs. Nicholas (Adele Achem) Nasser
# Miss. Marguerite Rut Sandstrom
# ...

import csv

with open('titanic.csv', encoding='utf-8') as file:
    reader = list(csv.reader(file, delimiter=';'))
    survived_males = []
    survived_females = []

    for i in range(1, len(reader)):
        if int(reader[i][0]) == 1 and reader[i][-2] == 'male' and float(reader[i][-1]) < 18.0:
            survived_males.append(reader[i][1])
        elif int(reader[i][0]) == 1 and reader[i][-2] == 'female' and float(reader[i][-1]) < 18.0:
            survived_females.append(reader[i][1])

    print(*survived_males, sep='\n')
    print(*survived_females, sep='\n')

    
    
# Лог-файл
# Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя.
# В первом столбце записано измененное имя пользователя, во втором — адрес электронной
# почты, в третьем — дата и время изменения. При этом email пользователь менять не может,
# только имя:

# username,email,dtime
# rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
# busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
# ...

# Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи
# для каждого пользователя и записывает их в файл new_name_log.csv. В файле new_name_log.csv
# первой строкой должны быть заголовки столбцов такие же, как в файле name_log.csv. Логи
# в итоговом файле должны быть расположены в лексикографическом порядке названий электронных
# ящиков пользователей.

# Примечание 1. Для части пользователей в исходном файле запись только одна, и тогда в
# итоговый файл следует записать только ее, для некоторых пользователей есть несколько
# записей с разными именами.

# Например, пользователь с электронной почтой c3po@gmail.com несколько раз менял имя:

# C=3PO,c3po@gmail.com,16/11/2021 17:10
# C3PO,c3po@gmail.com,16/11/2021 17:15
# C-3PO,c3po@gmail.com,16/11/2021 17:24

# Из этих трех записей в итоговый файл должна быть записана только одна — самая свежая:

# C-3PO,c3po@gmail.com,16/11/2021 17:24

# Примечание 2. Разделителем в файле name_log.csv является запятая, при этом кавычки
# не используются.

# Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

# Примечание 4. Начальная часть файла new_name_log.csv выглядит так:

# username,email,dtime
# angry-barbara2,barbaraanderson@bk.ru,17/11/2021 01:17
# dead-barbara6,barbarabrown@rambler.ru,27/11/2021 08:27
# busy_barbara7,barbaradavis@aol.com,24/11/2021 08:24
# ...

# Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.

import csv
from datetime import datetime


with open('D:/Python/Stepik/name_log.csv', encoding='utf-8') as file:
    dict_reader = csv.DictReader(file)  
    email_users_dict = {}
    latest_data_dict = {}
    for info_dict in dict_reader:
        email_users_dict[info_dict['email']] = email_users_dict.get(info_dict['email'], {})
        dtime_change = datetime.strptime(info_dict['dtime'], '%d/%m/%Y %H:%M')
        email_users_dict[info_dict['email']][dtime_change] = email_users_dict[info_dict['email']].get(dtime_change, []) + [info_dict['username']]

    with open('D:/Python/Stepik/new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'email', 'dtime'])
        for email, dtime_change in sorted(email_users_dict.items(), key=lambda x: x[0]):
            dtime_last_changed = max(dtime_change)
            writer.writerow([dtime_change[dtime_last_changed][0], email, dtime_last_changed.strftime('%d/%m/%Y %H:%M')])

            
            
# Проще, чем кажется 🌶️
# Рассмотрим следующий текстовый фрагмент:

# ball,color,purple
# ball,size,4
# ball,notes,it's round
# cup,color,blue
# cup,size,1
# cup,notes,none

# Каждая строка этого фрагмента содержит три значения через запятую: имя объекта, свойство этого
# объекта, значение свойства. Например, в первой строке указан объект ball, имеющий свойство color,
# значение которого равно purple. Также у объекта ball есть свойства size и notes, имеющие значения
# 4 и it's round соответственно. Помимо объекта ball имеется объект cup, имеющий те же свойства и в
# том же количестве. Дадим этим объектам общее название object и сгруппируем строки данного текстового
# фрагмента по первому столбцу:

# object,color,size,notes
# ball,purple,4,it's round
# cup,blue,1,none

# Мы получили запись в привычном CSV формате, в котором в первом столбце указывается имя объекта, а
# в последующих — значения соответствующих свойств этого объекта.

# Реализуйте функцию condense_csv(), которая принимает два аргумента в следующем формате:

# filename — название csv файла, например, data.csv; формат содержимого файла аналогичен формату
# текстового фрагмента, рассмотренного в условии задачи: каждая строка файла содержит три значения
# через запятую, а именно имя объекта, свойство этого объекта, значение свойства; все объекты имеют
# равные свойства и в равных количествах
# id_name — общее название для объектов

# Функция должна привести содержимое файла в привычный CSV формат, сгруппировав строки по первому
# столбцу и назвав первый столбец id_name. Полученный результат функция должна записать в файл
# condensed.csv.

# Примечание 1. Например, если бы файл data.csv имел следующий вид:

# 01,Title,Ran So Hard the Sun Went Down
# 02,Title,Honky Tonk Heroes (Like Me)

# то вызов функции condense_csv():

# ondense_csv('data.csv', id_name='ID')

# должен был бы создать файл condensed.csv со следующим содержанием:

# ID,Title
# 01,Ran So Hard the Sun Went Down
# 02,Honky Tonk Heroes (Like Me)

# Примечание 2. Гарантируется, что в передаваемом в функцию csv файле разделителем является запятая,
# при этом кавычки не используются.

import csv


def condense_csv(filename, id_name):
    columns = [id_name]
    objects_and_properties = {}

    with open(filename, encoding='utf-8') as file:
        file_reader = csv.reader(file)
        for obj, property, value in file_reader:
            objects_and_properties[obj] = objects_and_properties.get(obj, {})
            objects_and_properties[obj][property] = value
            if property not in columns:
                columns.append(property)

    with open('D:/Python/Stepik/condensed.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        for id, obj_and_prop in objects_and_properties.items():
            writer.writerow([id, *obj_and_prop.values()])

            
            
# Возрастание классов 🌶️
# Вам доступен файл student_counts.csv, который содержит данные о количестве учеников в некотором
# учебном заведении за период 20002000 — 20212021 г. В первом столбце записан год, в последующих
# столбцах записан класс и количество учеников в данном классе в этом году:

# year,5-Б,3-Б,8-А,2-Г,7-Б,1-Б,3-Г,3-А,2-В,6-Б,6-А,8-Б,8-Г,11-А,2-А,7-А,5-А,2-Б,10-А,11-Б,8-В,4-А,7-В,3-В,1-А,9-А,11-В
# 2000,19,15,18,29,19,17,26,29,28,30,26,27,27,22,29,19,27,20,16,18,15,27,19,29,22,20,23
# 2001,21,30,22,19,26,20,24,27,20,30,24,30,29,21,20,19,29,27,23,25,30,30,23,22,22,18,22
# ...

# Напишите программу, которая записывает данную таблицу в файл sorted_student_counts.csv, располагая
# все столбцы в порядке возрастания классов, при совпадении классов — в порядке возрастания букв.

# Примечание 1. Каждый класс содержит номер и букву и записывается в следующем формате:

# <номер класса>-<буква класса>

# Примечание 2. Разделителем в файле student_counts.csv является запятая, при этом кавычки не
# используются.

# Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

# Примечание 4. Начальная часть файла sorted_student_counts.csv выглядит так:

# year,1-А,1-Б,2-А,2-Б,...
# 2000,22,17,29,20,...
# 2001,22,20,20,27,...
# ...

import csv
from re import findall


with open('D:/Python/Stepik/student_counts.csv', encoding='utf-8') as file:
    file_reader = csv.DictReader(file)
    sorted_columns = sorted(file_reader.fieldnames[1:], key=lambda x: (int(findall(r'(\d+)', x)[0]), x[-1]))     
    with open('D:/Python/Stepik/sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['year'] + sorted_columns)
        for counts_year in file_reader:
            writer.writerow([counts_year['year']] + [counts_year[column] for column in sorted_columns])
