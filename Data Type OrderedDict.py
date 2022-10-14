# Вам доступен словарь data. Дополните приведенный ниже код, чтобы он вывел
# данный словарь, расположив его элементы в обратном порядке.

# Примечание. Например, если бы словарь data имел вид:

# data = OrderedDict(key1='value1', key2='value2', key3='value3')

# то программа должна была бы вывести:

# OrderedDict([('key3', 'value3'), ('key2', 'value2'), ('key1', 'value1')])

from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
                    'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

data_copy = data.copy()

for key in reversed(data_copy):
    data.move_to_end(key)

print(data)



# Вам доступен словарь data с четным количеством элементов. Дополните приведенный
# ниже код, чтобы он вывел данный словарь, расположив его элементы по следующему
# правилу: первый, последний, второй, предпоследний, третий, и так далее.

# Примечание. Например, если бы словарь data имел вид:

# data = OrderedDict(key1='value1', key2='value2', key3='value3')

# то программа должна была бы вывести:

# OrderedDict([('key3', 'value3'), ('key2', 'value2'), ('key1', 'value1')])

from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника',
                    'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

data_copy = data.copy()

for i in range(len(data)):
    if i % 2 == 0:
        print()
        data.move_to_end(list(data_copy)[i])
    else:
        data.move_to_end(list(data_copy)[-i])
    
print(data)



# Вам доступна переменная data, содержащая OrderedDict словарь. Дополните
# приведенный ниже код, чтобы он добавил этому словарю два атрибута:

# sorted_keys() — функция, которая возвращает отсортированный по возрастанию
# список ключей словаря data
# sorted_values() — функция, которая возвращает отсортированный по возрастанию
# список значений словаря data

# Обе функции должны принимать один необязательный аргумент reverse, по умолчанию
# равный False, который определяет порядок сортировки:

# False — по возрастанию
# True — по убыванию

# Примечание 1. Гарантируется, что ключи и значения словаря data можно отсортировать,
# то есть он не содержит ключи, имеющие разные типы, а также значения, имеющие разные
# типы.

# Примечание 2. Функции data.sorted_keys() и data.sorted_values() должны учитывать
# содержимое словаря. Например, если в словарь data будет добавлена новая пара
# ключ-значение, то и в возвращаемых функциями списках данные ключ и значение должны
# присутствовать.

# Примечание 3. Программа ничего не должна выводить.

from collections import OrderedDict

data = OrderedDict({'Law & Order': 1990, 'The Practice': 1997, 'Six Feet Under': 2001,
                    'Joan of Arcadia': 2003, 'The West Wing': 1999, 'Deadwood': 2004,
                    'The Sopranos': 1999, 'Boston Legal': 2004, 'ER': 1994,
                    'Friday Night Lights': 2006, '24': 2001, 'Heroes': 2006,
                    'Lost': 2004, 'Dexter': 2006, 'Damages': 2007,
                    'Big Love': 2006, 'House': 2004, 'Downton Abbey': 2010,
                    "Grey's Anatomy": 2005, 'Homeland': 2011, 'Breaking Bad': 2008,
                    'Game of Thrones': 2011, 'CSI: Crime Scene Investigations': 2000, 'Boardwalk Empire': 2010,
                    'True Blood': 2008, 'House of Cards': 2013, 'True Detective': 2014})

data.sorted_keys = lambda reverse=False: sorted(data.keys(), reverse=reverse)
data.sorted_values = lambda reverse=False: sorted(data.values(), reverse=reverse)



# Функция custom_sort() 🌶️
# Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем
# порядке:

# ordered_dict — словарь OrderedDict
# by_values — булево значение, по умолчанию имеет значение False

# Функция должна сортировать словарь ordered_dict:

# по ключам, если by_values имеет значение False
# по значениям, если by_values имеет значение True

# Примечание 1. Функция должна изменять переданный словарь, а не возвращать новый.
# Возвращаемым значением функции должно быть None.

# Примечание 2. Гарантируется, что переданный в функцию словарь можно отсортировать,
# то есть он не содержит ключи, имеющие разные типы, а также значения, имеющие разные
# типы.

# Примечание 3. Если два элемента имеют равные значения, то следует сохранить их
# исходный порядок следования.

# Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию custom_sort(), но не код, вызывающий ее.

from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    for key in sorted(ordered_dict, key=ordered_dict.get):
        ordered_dict.move_to_end(key)
    else:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)
    return None

data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=False)

print(*data.items())