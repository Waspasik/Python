# Снова не успел
# Дан режим работы магазина:

# Понедельник	9:00 - 21:00
# Вторник	    9:00 - 21:00
# Среда	        9:00 - 21:00
# Четверг	    9:00 - 21:00
# Пятница	    9:00 - 21:00
# Суббота	    10:00 - 18:00
# Воскресенье	10:00 - 18:00

# Напишите программу, которая принимает на вход текущие дату и время и определяет
# количество минут, оставшееся до закрытия магазина.

# Формат входных данных
# На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

# Формат выходных данных
# Программа должна вывести количество минут, которое осталось до закрытия магазина,
# или текст Магазин не работает, если он закрыт.

from datetime import datetime, timedelta


timetable = {
    1: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    2: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    3: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    4: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    5: {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    6: {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
    7: {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
    }

datetime_input = input().split(' ')
day_of_the_week = datetime.strptime(datetime_input[0], '%d.%m.%Y').isoweekday()
hours, minutes = datetime_input[1].split(':')
tm = timedelta(hours=int(hours), minutes=int(minutes))

if timetable[day_of_the_week]['start'] <= tm < timetable[day_of_the_week]['end']:
    minutes_before_closing = timetable[day_of_the_week]['end'] - tm
    print(minutes_before_closing.seconds // 60)
else:
    print('Магазин не работает')



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
