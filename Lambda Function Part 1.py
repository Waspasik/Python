# Требовалось написать программу, которая:

# преобразует список floats в список чисел, возведенных в квадрат и округленных с
# точностью до одного десятичного знака;
# фильтрует список words  и оставляет только палиндромы длиной более 4 символов;
# находит произведение чисел из списка numbers.
# Программист торопился и написал программу неправильно. Доработайте его программу.

from functools import reduce 

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
map_result = list(map(lambda num: round(num**2, 1), floats))
filter_result = list(filter(lambda name: name == name[::-1] and len(name) > 4, words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)



# Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и
# reduce() выводит в алфавитном порядке список primary городов с населением более
# 10 000 000 человек, в формате:

# Cities: Beijing, Buenos Aires, ...
# Примечание 1. Тестирующая система никак не "покарает" вас за неиспользование встроенных
# функций filter(), map(), sorted() и reduce(), однако лучше сделать это задание честно 😃.

# Примечание 2. Ставить запятую в конце вывода не нужно.

from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

filter_primary = list(filter(lambda city_info: 'primary' in city_info and city_info[1] > 10000000, data))
map_cities = sorted(list(map(lambda city_info: city_info[0], filter_primary)))
reduce_result = reduce(lambda result, city_info: result + ', ' + city_info, map_cities)

print('Cities:' , reduce_result)