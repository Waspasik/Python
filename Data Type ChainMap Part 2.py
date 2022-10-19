# Функция get_all_values()
# Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем
# порядке:

# chainmap — объект типа ChainMap, элементами которого являются словари
# key — произвольный объект

# Функция должна возвращать множество, элементами которого являются все значения
# по ключу key из всех словарей в chainmap. Если ключ key отсутствует в chainmap,
# функция должна вернуть пустое множество.

# Примечание 1. Гарантируется, что передаваемый в функцию объект типа ChainMap
# содержит словари с хешируемыми значениями.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию get_all_values(), но не код, вызывающий ее.

from collections import ChainMap

def get_all_values(chainmap, key):
    all_values = set()
    for dct in chainmap.maps:
        try:
            all_values.add(dct[key])
        except:
            KeyError
    return all_values



# Функция deep_update()
# Реализуйте функцию deep_update(), которая принимает три аргумента в следующем порядке:

# chainmap — объект типа ChainMap, элементами которого являются словари
# key — хешируемый объект
# value — произвольный объект

# Функция должна изменять все значения по ключу key во всех словарях в chainmap на value.
# Если ключ key отсутствует в chainmap, функция должна добавить пару key: value в первый
# словарь.

# Примечание 1. Функция должна изменять передаваемый объект типа ChainMap и возвращать
# значение None.

# Примечание 2. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит
# хотя бы один словарь.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию deep_update(), но не код, вызывающий ее.

from collections import ChainMap

def deep_update(chainmap, key, value):
    if key in chainmap:
        for dct in chainmap.maps:
            if key in dct:
                dct.update({key: value})
    else:
        chainmap[key] = chainmap.get(key, value)



# Функция get_value()
# Реализуйте функцию get_value(), которая принимает три аргумента в следующем порядке:

# chainmap — объект типа ChainMap, элементами которого являются словари
# key — произвольный объект
# from_left — булево значение, по умолчанию равное True

# Функция должна возвращать значение по ключу key из chainmap, причем:

# если from_left имеет значение True, поиск ключа в chainmap должен происходить от
# первого словаря к последнему
# если from_left имеет значение False, поиск ключа в chainmap должен происходить от
# последнего словаря к первому

# Если ключ key отсутствует в chainmap, функция должна вернуть значение None.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию get_value(), но не код, вызывающий ее.

from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    chainmap_copy = chainmap.copy()
    if key in chainmap_copy:
        if from_left:
            return chainmap_copy[key]
        else:
            chainmap_copy.maps.reverse()
            return chainmap_copy[key]