# Продуктивность
# Артуру нужно подготовить 1010 задач для нового курса "ООП на Python". Чтобы
# занятие не оказалось утомительным, он придумал правило:

# если сегодня он подготовил первую задачу, то вторую он должен подготовить 
# через один день
# если сегодня он подготовил вторую задачу, то третью он должен подготовить
# через два дня
# если сегодня он подготовил третью задачу, то четвертую он должен подготовить
# через три дня
# и так далее

# Напишите программу, которая определяет даты, в которые Артуру нужно подготовить
# задачи.

# Формат входных данных
# На вход программе подается дата подготовки первой задачи в формате DD.MM.YYYY.

# Формат выходных данных
# Программа должна вывести 10 дат, удовлетворяющих условию задачи, каждую на
# отдельной строке, в формате DD.MM.YYYY.

from datetime import datetime, timedelta

date_input = datetime.strptime(input(), '%d.%m.%Y')
result = [date_input]

for i in range(2, 11):
    date_input += timedelta(days=i)
    result.append(date_input)

print(*map(lambda x: x.strftime('%d.%m.%Y'), result), sep='\n')



# Соседние даты
# Дана последовательность дат. Напишите программу, которая создает и выводит список,
# элементами которого являются неотрицательные целые числа — количество дней между
# двумя соседними датами последовательности.

# Формат входных данных
# На вход программе подается последовательность дат, разделенных пробелом, в формате
# DD.MM.YYYY.

# Формат выходных данных
# Программа должна вывести список, содержащий неотрицательные целые числа, каждое из
# которых — количество дней между двумя соседними датами последовательности.

# Примечание 1. Даты в последовательности могут располагаться в произвольном порядке,
# то есть не гарантируется, что следующая дата больше предыдущей.

# Примечание 2. Если последовательность состоит из одной даты, то программа должна
# вывести пустой список.

# Примечание 3. Рассмотрим второй тест, в котором подается последовательность из пяти
# дат. Определим элементы результирующего списка:

# первый элемент — 1, количество дней между датами 06.10.2021 и 05.10.2021
# второй элемент — 3, количество дней между датами 05.10.2021 и 08.10.2021
# третий элемент — 1, количество дней между датами 08.10.2021 и 09.10.2021
# четвертый элемент — 2, количество дней между датами 09.10.2021 и 07.10.2021

from datetime import datetime, timedelta

dates_list = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), input().split(' ')))
result = []

for i in range(1, len(dates_list)):
    amount_days1 = dates_list[i] - dates_list[i-1]
    amount_days2 = dates_list[i-1] - dates_list[i]
    if amount_days1.days < 0:
        result.append(amount_days2.days)
    else:
        result.append(amount_days1.days)

print(result)



# Функция fill_up_missing_dates()
# Реализуйте функцию fill_up_missing_dates(), которая принимает на вход один аргумент:

# dates — список строковых дат в формате DD.MM.YYYY

# Функция должна возвращать список, в котором содержатся все даты из списка dates,
# расположенные в порядке возрастания, а также все недостающие промежуточные даты.

# Примечание 1. Рассмотрим первый тест. Список dates содержит период с 01.11.2021 по 07.11.2021:

# dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

# в котором отсутствуют даты 02.11.2021, 05.11.2021, 06.11.2021. Тогда вызов функции:

# fill_up_missing_dates(dates)

# должен вернуть список: 

# ['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021']

# Примечание 2. Функция должна создавать и возвращать новый список, а не изменять
# переданный.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию fill_up_missing_dates(), но не код, вызывающий ее.

from datetime import datetime, timedelta

def fill_up_missing_dates(dates):
    dates_list = list(map(lambda d: datetime.strptime(d, '%d.%m.%Y'), dates))
    min_date, max_date = min(dates_list), max(dates_list)
    result = [min_date]
    
    while min_date != max_date:
        min_date += timedelta(days=1)
        result.append(min_date)
        
    return list(map(lambda d: d.strftime('%d.%m.%Y'), result))



# Реп по матеше
# Репетитор по математике проводит занятия по 4545 минут с перерывами по 10 минут.
# Репетитор обозначает время начала рабочего дня и время окончания рабочего дня.
# Напишите программу, которая генерирует и выводит расписание занятий.

# Формат входных данных
# На вход программе в первой строке подается время начала рабочего дня в формате
# HH:MM. В следующей строке вводится время окончания рабочего дня в том же формате.

# Формат выходных данных
# Программа должна сгенерировать и вывести расписание занятий. На первой строке
# выводится время начала и окончания первого занятия в формате HH:MM - HH:MM, на
# второй строке — время начала и окончания второго занятия в том же формате, и так
# далее.

# Примечание 1. Если занятие обрывается временем окончания работы, то добавлять
# его в расписание не нужно.

# Примечание 2. Если разница между временем начала и окончания рабочего дня меньше
# 45 минут, программа ничего не должна выводить.

from datetime import datetime, timedelta

start_lessons, end_lessons = datetime.strptime(input(), '%H:%M'), datetime.strptime(input(), '%H:%M')

time_lesson = timedelta(minutes=45)
break_time = timedelta(minutes=10)
start_lesson = start_lessons

while start_lesson < end_lessons:
    end_lesson = start_lesson + time_lesson
    if end_lesson <= end_lessons:
        print(start_lesson.strftime('%H:%M'), '-', end_lesson.strftime('%H:%M'))
    start_lesson = end_lesson + break_time