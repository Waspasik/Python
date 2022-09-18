# Дневник космонавта 🌶️
# Вам доступен текстовый файл diary.txt, в который космонавт записывал небольшие
# отчёты за день. Каждый новый отчёт он мог записать либо в начало файла, либо в
# середину, либо в конец. Все отчеты разделены между собой пустой строкой. Каждый
# новый отчёт начинается со строки с датой и временем в формате DD.MM.YYYY; HH:MM,
# после которой следуют события, произошедшие за указанный день:

# Напишите программу, которая расставляет все записи космонавта в хронологическом
# порядке и выводит полученный результат.

# Примечание 1. Например, если бы файл diary.txt имел вид:

# 13.02.1994; 18:49
# Уже несколько дней наблюдаем на теневой части орбиты в районе Канады мощнейшее полярное сияние.
# Прежде всего, поражают масштабы происходящего. Под нами огромная зелено-розовая «змея».

# 03.02.1994; 20:18
# Сегодня наблюдали и сняли на видео след Шаттла после выведения, дымит он прилично.
# Готовимся к радиолюбительской связи с экипажем Шаттла и, конечно, с Сергеем.
# При подготовке к сеансу связи с Шаттлом познакомился с Ритой, радиолюбителем из Австралии.
# Она немного говорит по-русски и очень приятно слышать родную речь.

 #12.02.1994; 17:17
# Сегодня возникли проблемы со сбросом через спутник ретранслятор видеоинформации по снятому нами следу Шаттла.
# Как сообщил нам ЦУП, в Щелкове холодно, все замерзло, антенна не работает...
# Все это наводит на грустные размышления о нашей безолаберности и разрухе.

# то программа должна была бы вывести:

# 03.02.1994; 20:18
# Сегодня наблюдали и сняли на видео след Шаттла после выведения, дымит он прилично.
# Готовимся к радиолюбительской связи с экипажем Шаттла и, конечно, с Сергеем.
# При подготовке к сеансу связи с Шаттлом познакомился с Ритой, радиолюбителем из Австралии.
# Она немного говорит по-русски и очень приятно слышать родную речь.

# 12.02.1994; 17:17
# Сегодня возникли проблемы со сбросом через спутник ретранслятор видеоинформации по снятому нами следу Шаттла.
# Как сообщил нам ЦУП, в Щелкове холодно, все замерзло, антенна не работает...
# Все это наводит на грустные размышления о нашей безолаберности и разрухе.

# 13.02.1994; 18:49
# Уже несколько дней наблюдаем на теневой части орбиты в районе Канады мощнейшее полярное сияние.
# Прежде всего, поражают масштабы происходящего. Под нами огромная зелено-розовая «змея».

from datetime import datetime

with open('D:/Python/Stepik/diary.txt', 'r', encoding='utf-8') as diary:
    diary_list = list(map(str.strip, diary.readlines()))
    diary_matrix = []
    record_diary = []

    for line in diary_list:
        if bool(line):
            record_diary.append(line)
            if line == diary_list[-1]:
                diary_matrix.append(record_diary)
        else:
            diary_matrix.append(record_diary)
            record_diary = []

    for part in diary_matrix:
        part[0] = datetime.strptime(' '.join(part[0].split('; ')), '%d.%m.%Y %H:%M')
    
    sorted_diary = sorted(diary_matrix, key=lambda x: x[0])

    for record in sorted_diary:
        record[0] = record[0].strftime('%d.%m.%Y; %H:%M')
        record[-1] = f'{record[-1]}\n'
        print(*record, sep='\n')



# Функция is_available_date() 🌶️
# Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна
# ли та или иная дата для бронирования номера.

# Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем
# порядке:

# booked_dates — список строковых дат, недоступных для бронирования. Элементом списка
# является либо одиночная дата, либо период (две даты через дефис). Например:

# ['04.11.2021', '05.11.2021-09.11.2021']

# date_for_booking — одиночная строковая дата или период (две даты через дефис), на
# которую гость желает забронировать номер. Например:

# '01.11.2021' или '01.11.2021-04.11.2021'

# Функция is_available_date() должна возвращать True, если дата или период date_for_booking
# полностью доступна для бронирования. В противном случае функция должна возвращать False.

# Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию is_available_date(), но не код, вызывающий ее.

from datetime import datetime, timedelta

def is_available_date(booked_dates, date_for_booking):
    
    def creating_dates_set(processed_dates):
        dates_set = set()
        for date in processed_dates:
            if '-' not in date:
                dates_set.add(datetime.strptime(date, '%d.%m.%Y'))
            else:
                date_interval = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), date.split('-')))
                start_date, end_date = date_interval[0], date_interval[1]
                delta = end_date - start_date
                for i in range(delta.days + 1):
                    date = start_date + timedelta(i)
                    dates_set.add(date)
        return dates_set
    
    booked_dates_set = creating_dates_set(booked_dates)
    available_dates_set = creating_dates_set(date_for_booking.split(', '))
    
    if booked_dates_set.intersection(available_dates_set):
        return False
    else:
        return True