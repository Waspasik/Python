# Дополните приведенный ниже код, чтобы он прибавил к объекту datetime(2021, 11, 4, 13, 6)
# одну неделю и 12 часов и вывел результат в формате DD.MM.YYYY HH:MM:SS.

from datetime import datetime, timedelta

dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))



# Дополните приведенный ниже код, чтобы он вывел количество дней (целое число) между
# датами today и birthday.

from datetime import date, timedelta

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = birthday - today

print(days.days)



# Предыдущая и следующая даты
# Напишите программу, которая принимает на вход дату и выводит предыдущую и следующую
# даты.

# Формат входных данных
# На вход программе подается дата в формате DD.MM.YYYY.

# Формат выходных данных
# Программа должна вывести предыдущую и следующую даты относительно введенной даты,
# каждую на отдельной строке, в формате DD.MM.YYYY.

# Примечание 1. Гарантируется, что у подаваемой даты есть предыдущая и следующая даты.

from datetime import date, datetime, timedelta

date_input = datetime.strptime(input(), '%d.%m.%Y')
yesterday = date_input - timedelta(hours=24)
tomorrow = date_input + timedelta(hours=24)

print(yesterday.strftime('%d.%m.%Y'), tomorrow.strftime('%d.%m.%Y'), sep='\n')



# Количество секунд
# Напишите программу, которая принимает на вход время и выводит целое количество
# секунд, прошедшее с начала суток.

# Формат входных данных
# На вход программе подается время в формате HH:MM:SS.

# Формат выходных данных
# Программа должна вывести целое количество секунд, прошедшее с начала суток.

# Примечание 1. Началом суток считается момент времени, соответствующий 00:00:00.

from datetime import datetime, timedelta

time_input = datetime.strptime(input(), '%H:%M:%S')
time_delta = timedelta(hours=time_input.hour, minutes=time_input.minute, seconds=time_input.second)
print(int(time_delta.total_seconds()))



# Таймер
# Часы показывают время в формате HH:MM:SS. На этих часах запустили таймер, который
# прозвенит через nn секунд. Напишите программу, которое определит, какое время будет
# на часах, когда прозвенит таймер.

# Формат входных данных
# На вход программе в первой строке подается текущее время на часах в формате HH:MM:SS.
# В следующей строке вводится целое неотрицательное число nn — количество секунд, через
# которое должен прозвенеть таймер.

# Формат выходных данных
# рограмма должна вывести время в формате HH:MM:SS, которое будет на часах, когда прозвенит
# таймер.

from datetime import datetime, timedelta

time_input = datetime.strptime(input(), '%H:%M:%S')
time_delta = timedelta(hours=time_input.hour, minutes=time_input.minute, seconds=time_input.second)

print(time_delta + timedelta(seconds=int(input())))



# Функция num_of_sundays()
# Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:

# year — натуральное число, год

# Функция должна возвращать количество воскресений в году year.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию num_of_sundays(), но не код, вызывающий ее.

from datetime import datetime, timedelta

def num_of_sundays(year):
    year_input = datetime(year=year, month=1, day=1)
    next_year = year_input + timedelta(days=365)
    single_day = timedelta(days=1)
    sundays = 0

    while year_input.year == next_year.year:
        if year_input.isoweekday() == 7:
            sundays += 1
        print(year_input)
        year_input += single_day

    return sundays