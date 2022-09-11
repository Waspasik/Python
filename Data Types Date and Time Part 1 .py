# Вам доступен список dates, содержащий даты. Дополните приведенный ниже код, чтобы
# он вывел год и номер квартала каждой даты из данного списка. Компоненты дат должны
# быть расположены в исходном порядке, каждые на отдельной строке, в следующем формате:

# <год>-Q<номер квартала>

from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27),
         date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14),
         date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

quarter = {'Q1': [1, 2, 3], 'Q2': [4, 5, 6], 'Q3': [7, 8, 9], 'Q4': [10, 11, 12]}

for d in dates:
    for key, value in quarter.items():
        if d.month in value:
            print(f'{d.year}-{key}')



# Функция get_min_max()
# Реализуйте функцию get_min_max(), которая принимает один аргумент:

# dates — список дат (тип date)

# Функция должна возвращать кортеж, первым элементом которого является минимальная
# дата из списка dates, вторым — максимальная дата из списка dates. Если список
# dates пуст, функция должна вернуть пустой кортеж.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию get_min_max(), но не код, вызывающий ее.

def get_min_max(dates):
    if bool(dates):
        return (min(dates), max(dates))
    else:
        return tuple()



# Функция get_date_range()
# Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем
# порядке:

# start — начальная дата, тип date
# end — конечная дата, тип date

# Функция get_date_range() должна возвращать список, состоящий из дат (тип date)
# от start до end включительно. Если start > end, функция должна вернуть пустой
# список.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию get_date_range(), но не код, вызывающий ее.

def get_date_range(start, end):
    return [date.fromordinal(ordinal) for ordinal in range(start.toordinal(), end.toordinal() + 1)]



# Функция saturdays_between_two_dates()
# Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента
# в следующем порядке:

# start — начальная дата, тип date
# end — конечная дата, тип date

# Функция должна возвращать количество суббот между датами start и end включительно.

# Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется,
# что первая дата меньше второй.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию saturdays_between_two_dates(), но не код, вызывающий ее.

def saturdays_between_two_dates(start, end):
    if start.toordinal() > end.toordinal():
        start, end = end, start
    dates_list = [date.fromordinal(ordinal) for ordinal in range(start.toordinal(), end.toordinal() + 1)]
    return len(list(filter(lambda d: d.weekday() == 5, dates_list)))