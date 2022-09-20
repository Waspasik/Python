# Сотрудники организации 😄
# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения.
# Напишите программу, которая определяет самого старшего сотрудника из данного списка.

# Формат входных данных
# На вход программе в первой строке подается натуральное число nn — количество сотрудников,
# работающих в организации. В последующих nn строках вводятся данные о каждом сотруднике:
# фамилия, имя и дата рождения, разделённые пробелом. Дата рождения указывается в формате
# DD.MM.YYYY.

# Формат выходных данных
# Программа должна определить самого старшего сотрудника и вывести его дату рождения, имя
# и фамилию, разделив пробелом. Если таких сотрудников несколько, программа должна вывести
# их дату рождения, а также их количество, разделив пробелом.

from datetime import datetime

employee_dict = {}
min_birthday = datetime(2020, 1, 1)

for i in range(int(input())):
    employee_info = input().split(' ')
    birthday_employe = datetime.strptime(employee_info[2], '%d.%m.%Y')
    employee_dict[birthday_employe] = employee_dict.get(birthday_employe, []) + [' '.join(employee_info[:2])]

for key, value in employee_dict.items():
    if key < min_birthday:
        min_birthday = key

if len(employee_dict[min_birthday]) > 1:
    print(min(employee_dict).strftime('%d.%m.%Y'), len(employee_dict[min_birthday]))
else:
    print(min(employee_dict).strftime('%d.%m.%Y'), ''.join(employee_dict[min_birthday]))