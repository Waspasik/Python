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
    reader = list(csv.reader(file))
    reader_dict = {}
    email_users_dict = {}
    columns = reader[0]
    for i in range(1, len(reader)):
        reader_dict[datetime.strptime(reader[i][-1], '%d/%m/%Y %H:%M')] = reader_dict.get(datetime.strptime(reader[i][-1], '%d/%m/%Y %H:%M'), reader[i][:-1])

    for i in range(1, len(reader)):
        email_users_dict[reader[i][1]] = email_users_dict.get(reader[i][1], []) + [datetime.strptime(reader[i][-1], '%d/%m/%Y %H:%M')]
    
    with open('D:/Python/Stepik/new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        for key, value in email_users_dict.items():
            writer.writerow([reader_dict[max(value)], max(value).strftime('%d/%m/%Y %H:%M')])
