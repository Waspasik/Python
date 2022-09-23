# Високосный год
# Напишите программу, которая определяет, является ли год високосным.

# Формат входных данных
# На вход программе в первой строке подается целое число n, в последующих n строках
# вводятся натуральные числа, представляющие года.

# Формат выходных данных
# Программа должна для каждого введенного года вывести True, если он является
# високосным, или False в противном случае.

from calendar import*

for _ in range(int(input())):
    print(isleap(int(input())))



# Календарь на месяц
# Напишите программу, которая выводит календарь на заданные год и месяц.

# Формат входных данных
# На вход программе подаются год и сокращенное название месяца на английском, разделенные
# пробелом.

# Формат выходных данных
# Программа должна вывести календарь на введенные год и месяц.

from calendar import*

y, m = input().split(' ')
print(month(int(y), list(month_abbr).index(m)))



# День недели
# Напишите программу, которая определяет день недели, соответствующий заданной дате.

# Формат входных данных
# На вход программе подается дата в формате YYYY-MM-DD.

# Формат выходных данных
# Программа должна вывести полное название дня недели на английском, который соответствует
# введенной дате.

from datetime import date, datetime
from calendar import*

date_input = datetime.strptime(input(), '%Y-%m-%d')
number_week = date_input.weekday()
print(list(day_name)[number_week])



# Количество дней 😉
# Напишите программу, которая определяет количество дней в заданном месяце.

# Формат входных данных
# На вход программе подаются год и порядковый номер месяца (начиная с 1), разделенные
# пробелом.

# Формат выходных данных
# Программа должна вывести единственное число — количество дней в введенном месяце.

# Примечание 1. Январь имеет порядковый номер 1, Февраль — 2, Март — 3, и так далее.

from calendar import*

y, m = map(int, input().split(' '))
print(monthrange(y, m)[1])



# Количество дней 😎
# Напишите программу, которая определяет количество дней в заданном месяце.

# Формат входных данных
# На вход программе подаются год и полное название месяца на английском, разделенные
# пробелом.

# Формат выходных данных
# Программа должна вывести единственное число — количество дней в введенном месяце.

from calendar import*

y, m = input().split(' ')
number_month = list(month_name).index(m)
print(monthrange(int(y), number_month)[1])



# Функция get_days_in_month()   
# Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем
# порядке:

# year — натуральное число
# month — полное название месяца на английском

# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date)
# месяца month и года year.

# Примечание 1. Например, вызов:

# get_days_in_month(2021, 'December')

#должен вернуть список:

# [datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ..., datetime.date(2021, 12, 30),
# datetime.date(2021, 12, 31)]

#Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию get_days_in_month(), но не код, вызывающий ее.

from datetime import datetime, timedelta
from calendar import*

def get_days_in_month(year, month):
    number_month = list(month_name).index(month)
    days_in_month = monthrange(int(year), number_month)[1]
    
    return [date(year, number_month, i) for i in range(1, days_in_month+1)]



# Функция get_all_mondays()
# Реализуйте функцию get_all_mondays(), которая принимает один аргумент:

# year — натуральное число

# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date)
# года year, выпадающих на понедельник.

# Примечание 1. Например, вызов:

# get_all_mondays(2021)

# должен вернуть список:

# [datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., datetime.date(2021, 12, 20),
# datetime.date(2021, 12, 27)]

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию get_all_mondays(), но не код, вызывающий ее.

from datetime import datetime, date
from calendar import*


def get_all_mondays(year):
    result = []

    for i in range(1, 13):
        days_in_month = monthrange(year, i)[1]
        for j in range(1, days_in_month+1):
            check_date = date(year, i, j)
            y, m, d = list(map(int, check_date.strftime('%Y %m %d').split(' ')))
            if weekday(y, m, d) == MONDAY:
                result.append(check_date)

    return result



# ТЧМ 🌶️
# Во многих музеях существует один день месяца, когда посещение музея для всех лиц или
# отдельных категорий граждан происходит без взимания платы. Например, в Эрмитаже это
# третий четверг месяца.

# Напишите программу, которая определяет даты бесплатных дней посещения Эрмитажа в заданном
# году.

# Формат входных данных
# На вход программе подается натуральное число, представляющее год.

# Формат выходных данных
# Программа должна определить все даты бесплатных дней посещения Эрмитажа в введенном году
# и вывести их. Даты должны быть расположены в порядке возрастания, каждая на отдельной
# строке, в формате DD.MM.YYYY.

from datetime import datetime
from calendar import*


def get_third_thursday(year):
    result = []

    for i in range(1, 13):
        counter = 0
        days_in_month = monthrange(int(year), i)[1]
        for j in range(1, days_in_month+1):
            check_date = datetime(year, i, j)
            y, m, d = list(map(int, check_date.strftime('%Y %m %d').split(' ')))
            if weekday(y, m, d) == THURSDAY:
                counter += 1
            if counter == 3:
                result.append(check_date)
                counter = 0

    return print(*list(map(lambda d: d.strftime('%d.%m.%Y'), result)), sep='\n')


get_third_thursday(int(input()))