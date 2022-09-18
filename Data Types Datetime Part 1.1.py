# Дополните приведенный ниже код, чтобы в переменной dt содержался объект типа
# datetime с датой и временем, которые указаны в строке text.

# Примечание. Дата, указанная в строке text, записана в формате DD.MM.YYYY, а
# время — в формате HH:MM.

from datetime import datetime

text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'

dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')

print(dt)



# Дополните приведенный ниже код, чтобы он преобразовал секунды seconds (прошедшие от
# начала эпохи) в объект datetime и, наоборот, объект datetime в секунды (прошедшие от
# начала эпохи).

from datetime import datetime

seconds = 2483228800
dt = datetime(2011, 11, 4)

print(datetime.fromtimestamp(seconds))
print(dt.timestamp())



# Вам доступен список times_of_purchases, содержащий даты (тип datetime), в которые
# были совершены покупки в некотором интернет-магазине. Дополните приведенный ниже
# код, чтобы он вывел текст До полудня, если большее число покупок было совершено
# до полудня, или текст После полудня в противном случае.

# Примечание 1. Гарантируется, что ни одна покупка не была совершена ровно в 12:00:00.

# Примечание 2. Гарантируется, что до полудня и после полудня совершено различное
# количество покупок.

from datetime import datetime, time

times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26), 
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59), 
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53), 
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3), 
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5), 
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54), 
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45), 
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57), 
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42), 
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12), 
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27), 
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41), 
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44), 
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

if len(list(filter(lambda date: date.time() > time(12, 0, 0), times_of_purchases))) > len(times_of_purchases) / 2:
    print('После полудня')
else:
    print('До полудня')



# Вам доступны список dates, содержащий даты, и список times, содержащий времена.
# Количество элементов в этих списках одинаковое. Дополните приведенный ниже код,
# чтобы он вывел datetime объекты, полученные путем объединения элементов списков
# dates и times, находящихся на одинаковых позициях. Полученные объекты должны
# быть расположены в порядке возрастания секунд, каждый на отдельной строке.

# Примечание 1. Например, если бы списки dates и times имели вид:

# dates = [date(2020, 11, 12), date(2021, 7, 2), date(2020, 9, 25)]
# times = [time(12, 50, 22), time(12, 19, 1), time(7, 30, 1)]

# то программа должна была бы вывести:

# 2021-07-02 12:19:01
# 2020-09-25 07:30:01
# 2020-11-12 12:50:22

# Примечание 2. Если объекты имеют равное количество секунд, то следует сохранит
#  их исходный порядок.

from datetime import date, time, datetime

dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24), 
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59), 
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2), 
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]

combine = zip(dates, times)

sorted_combine = sorted(combine, key=lambda x: x[1].second)

for comb in sorted_combine:
    print(comb[0], comb[1])



# Ученики онлайн-школы BEEGEEK решили выяснить, кто из них быстрее всех решит
# домашнее задание по математике. Для этого каждый ученик зафиксировал время
# начала и окончания решения своей домашней работы.

# Вам доступен словарь data, содержащий результаты учеников. Ключом в словаре
# является имя ученика, а значением — кортеж, первый элемент которого — время
# начала решения, второй элемент — время окончания решения. Дополните приведенный
# ниже код, чтобы он вывел имя ученика, который затратил на решение домашнего
# задания меньше всего времени.

# Примечание 1. Гарантируется, что искомый ученик единственный.

# Примечание 2. Дата-времена в кортежах представлены в виде строк в формате
# DD.MM.YYYY HH:MM:SS.

from datetime import datetime

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'), 
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'), 
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'), 
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'), 
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'), 
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'), 
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'), 
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'), 
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

min_decision_time = 10000000000
best_student = ''

for name, value in data.items():
    time_start = datetime.strptime(value[0], '%d.%m.%Y %H:%M:%S')
    time_end = datetime.strptime(value[1], '%d.%m.%Y %H:%M:%S')
    if time_end.timestamp() - time_start.timestamp() < min_decision_time:
        min_decision_time = time_end.timestamp() - time_start.timestamp()
        best_student = name

print(best_student)