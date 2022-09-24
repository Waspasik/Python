# Сотрудники организации 🙂
# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты
# рождения. Напишите программу, которая определяет, в какую из дат родилось больше
# всего сотрудников.

# Формат входных данных
# На вход программе в первой строке подается натуральное число nn — количество
# сотрудников, работающих в организации. В последующих nn строках вводятся данные
# о каждом сотруднике: фамилия, имя и дата рождения, разделённые пробелом. Дата
# рождения указывается в формате DD.MM.YYYY.

# Формат выходных данных
# Программа должна вывести дату, в которую наибольшее количество сотрудников отмечает
# день рождения, в формате DD.MM.YYYY. Если таких дат несколько, программа должна
# вывести их все в порядке возрастания, каждую на отдельной строке, в том же формате.

from datetime import datetime


employee_dict = {}
amount_birthdays = {}
max_amount_birthday = 0
result = []

for i in range(int(input())):
    employee_info = input().split(' ')
    birthday_employe = datetime.strptime(employee_info[2], '%d.%m.%Y')
    employee_dict[birthday_employe] = employee_dict.get(birthday_employe, []) + [' '.join(employee_info[:2])]
    
for key, value in employee_dict.items():
    amount_birthdays[key] = amount_birthdays.get(key, len(value))
    if len(value) > max_amount_birthday:
        max_amount_birthday = len(value)

for key, value in amount_birthdays.items():
    if value == max_amount_birthday:
        result.append(key.strftime('%d.%m.%Y'))

print(*sorted(result, key=lambda dt: datetime.strptime(dt, '%d.%m.%Y')), sep='\n')



# Сотрудники организации 😔
# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты
# рождения. Напишите программу, которая определяет самого молодого сотрудника,
# празднующего свой день рождения в течение ближайших семи дней от текущей даты.

# Формат входных данных
# На вход программе в первой строке подается текущая дата в формате DD.MM.YYYY,
# в следующей строке вводится натуральное число n — количество сотрудников,
# работающих в организации. В последующих n строках вводятся данные о каждом
# сотруднике: фамилия, имя и дата рождения, разделённые пробелом. Дата рождения
# указывается в формате DD.MM.YYYY.

# Формат выходных данных
# Программа должна определить самого молодого сотрудника, празднующего свой день
# рождения в течение ближайших семи дней, и вывести его фамилию и имя, разделив
# пробелом. Если таких сотрудников нет, программа должна вывести текст:

# Дни рождения не планируются
# Примечание 1. Гарантируется, что у всех сотрудников даты рождения различны.

# Примечание 2. Например, для даты 01.11.2021 ближайшими семью днями являются:

# 02.11.2021, 03.11.2021, 04.11.2021, 05.11.2021, 06.11.2021, 07.11.2021, 08.11.2021

from datetime import datetime, timedelta


yunger_employees = {}
today_input = input()

for _ in range(int(input())):
    employee_info = input().split(' ')
    birthday_employee = employee_info[2]
    todays_changed_year = today_input.replace(today_input[-4::], birthday_employee[-4::])
    begining_period = datetime.strptime(todays_changed_year, '%d.%m.%Y')
    birthday_employee = datetime.strptime(birthday_employee, '%d.%m.%Y')
    end_period = begining_period + timedelta(days=7)
    if birthday_employee.year == end_period.year:
        if begining_period < birthday_employee <= end_period:
            yunger_employees[birthday_employee] = yunger_employees.get(birthday_employee, ' '.join(employee_info[:2]))
    else:
        if begining_period < (birthday_employee + timedelta(days=365)) <= ((birthday_employee + timedelta(days=365)) + timedelta(days=7)):
            yunger_employees[birthday_employee] = yunger_employees.get(birthday_employee, ' '.join(employee_info[:2]))       
        
if bool(yunger_employees):
    print(yunger_employees[max(yunger_employees)])
else:
    print('Дни рождения не планируются')



# FAKE NEWS 🌶️
# Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00.
# Напишите программу, которая принимает на вход текущие дату и время и определяет,
# сколько времени осталось до выхода курса.

# Формат входных данных
# На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

# Формат выходных данных
# Программа должна вывести текст с указанием количества дней и часов, оставшихся
# до выхода курса, в следующем формате:

# До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов
# Если в данном случае количество часов равно нулю, то вывести нужно только дни.

# Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем
# формате:

# До выхода курса осталось: <кол-во часов> часов и <кол-во минут> минут
# Если в данном случае количество минут равно нулю, то вывести нужно только часы.
# Аналогично, если количество часов равно нулю, то вывести нужно только минуты.

# Если введенные дата и время больше либо равны 08.11.2022 12:00, программа должна
# вывести текст: 

# Курс уже вышел!

from datetime import datetime, timedelta


def days_before_start_course(start, dn):
    if dn > start:
        return 'Курс уже вышел!'
    else:
        datetime_range = start - dn

        if datetime_range > timedelta(days=1):
            date_range, time_range = int(str(datetime_range).split(' ')[0]), str(datetime_range).split(' ')[-1]
            hours = None
            if int(time_range.split(':')[0]) > 0:
                hours = int(time_range.split(':')[0])
            if hours != None:
                return f"До выхода курса осталось: {choose_plural(date_range, ('день', 'дня', 'дней'))} и {choose_plural(hours, ('час', 'часа', 'часов'))}"
            elif hours == None:
                return f"До выхода курса осталось: {choose_plural(date_range, ('день', 'дня', 'дней'))}"
        else:
            time_range = str(datetime_range)
            hours, minutes = None, None
            if int(time_range.split(':')[0]) > 0:
                hours = int(time_range.split(':')[0])
            if int(time_range.split(':')[1]) > 0:
                minutes = int(time_range.split(':')[1])
            if hours != None and minutes != None:
                return f"До выхода курса осталось: {choose_plural(hours, ('час', 'часа', 'часов'))} и {choose_plural(minutes, ('минута', 'минуты', 'минут'))}"
            elif hours != None and minutes == None:
                return f"До выхода курса осталось: {choose_plural(hours, ('час', 'часа', 'часов'))}"
            elif hours == None and minutes != None:
                return f"До выхода курса осталось: {choose_plural(minutes, ('минута', 'минуты', 'минут'))}"


def choose_plural(amount, declensions):
    suffixes = {
        1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2,
        11: 2, 12: 2, 13: 2, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 2, 20: 2, 0: 2,
    }
    for key, value in suffixes.items():
        if len(str(amount)) >= 2 and str(amount)[-2:] in ['11', '12', '13', '14']:
            return f'{amount} {declensions[suffixes[11]]}'
        elif len(str(amount)) >= 2 and str(amount)[-2:] == str(key):
            return f'{amount} {declensions[value]}'
        elif len(str(amount)) >= 2 and str(amount)[-1] == str(key):
            return f'{amount} {declensions[value]}' 
        elif len(str(amount)) == 1 and str(amount)[-1] == str(key):
            return f'{amount} {declensions[value]}'


start_day = datetime.strptime('08.11.2022 12:00', '%d.%m.%Y %H:%M')
day_now = datetime.strptime(input(), '%d.%m.%Y %H:%M')

print(days_before_start_course(start_day, day_now))
