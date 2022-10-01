# Дополните приведенный ниже код, чтобы он вывел содержимое словаря countries,
# расположив его элементы в лексикографическом порядке ключей, указав в качестве
# разделителя пар ключ-значение строку   -  (пробел дефис пробел), а в качестве
# отступов — три пробела.

# Примечание 1. Начальная часть ответа выглядит так:

# {
#    "Angola" - "Luanda",
#    "Australia" - "Canberra",
#    ...

import json

countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

print(json.dumps(countries, indent=3, separators=(',', ' - '), sort_keys=True))



# Дополните приведенный ниже код, чтобы он преобразовал словарь words в строку в
# формате JSON, пропуская пары, которые имеют недопустимые ключи, и присвоил
# полученный результат переменной data_json.

import json

words = {
         frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
         "travel": "trævl",
         ("hello", "world"): ("həˈləʊ", "wɜːld"),
         "moonlight": "muːn.laɪt",
         "sunshine": "ˈsʌn.ʃaɪn",
         ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
         "adventure": "ədˈventʃər",
         "beautiful": "ˈbjuːtɪfl",
         frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
         "bicycle": "baisikl",
         ("pilot", "fly"): ("pailət", "flai")
        }

data_json = json.dumps(words, skipkeys=True)



# Вам доступны словари club1, club2 и club3, содержащие данные о различных футбольных
# клубах. Дополните приведенный ниже код, чтобы он объединил данные словари в списов
# и записал полученную структуру данных в файл data.json, указав в качестве отступов
# три символа пробела.

# Примечание 1. Словари в списке должны располагаться в своем исходном порядке.

# Примечание 2. Начальная часть файла data.json выглядит так:

# [
#    {
#       "name": "FC Byern Munchen",
#       "country": "Germany",
#       ...
#    },
#   ...
# ]

import json

club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
         "trainer": "Julian Nagelsmann", "gaolkeeper": "M. Neuer", "league_position": 1}

club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
         "trainer": "Xavier Creus", "gaolkeeper": "M. Ter Stegen", "league_position": 7}

club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
         "trainer": "Michael Carrick", "gaolkeeper": "D. De Gea", "league_position": 8}

clubs_list = [club1, club2, club3]

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(clubs_list, file, indent=3)



# Ниже представлена программа, которая должна преобразовать словарь specs в строку
# в формате JSON и вывести ее с отступами в три пробела, не заменяя кириллические
# символы на их коды. В программе допущена ошибка, поэтому она выводит:

# {"\u041c\u043e\u0434\u0435\u043b\u044c": "AMD Ryzen 5 5600G",
#  "\u0413\u043e\u0434 \u0440\u0435\u043b\u0438\u0437\u0430": 2021,
# "\u0421\u043e\u043a\u0435\u0442": "AM4",
# "\u0422\u0435\u0445\u043f\u0440\u043e\u0446\u0435\u0441\u0441": "7 \u043d\u043c",
# "\u042f\u0434\u0440\u043e": "Cezanne",
# "\u041e\u0431\u044a\u0435\u043c \u043a\u044d\u0448\u0430 L2": "3 \u041c\u0411",
# "\u041e\u0431\u044a\u0435\u043c \u043a\u044d\u0448\u0430 L3": "16 \u041c\u0411",
# "\u0411\u0430\u0437\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430": "3900 \u041c\u0413\u0446"}

# Найдите и исправьте ее, чтобы программа преобразовала словарь specs в строку в
# формате JSON и вывела ее с отступами в три пробела, не заменяя кириллические символы
# на их коды.

# Примечание 1. Начальная часть ответа выглядит так:

# {
#    "Модель": "AMD Ryzen 5 5600G",
#    "Год релиза": 2021,
#    ...

import json

specs = {
         'Модель': 'AMD Ryzen 5 5600G',
         'Год релиза': 2021,
         'Сокет': 'AM4',
         'Техпроцесс': '7 нм',
         'Ядро': 'Cezanne',
         'Объем кэша L2': '3 МБ',
         'Объем кэша L3': '16 МБ',
         'Базовая частота': '3900 МГц'
        }

specs_json = json.dumps(specs, indent=3, ensure_ascii=False)

print(specs_json)



# Функция is_correct_json()
# Реализуйте функцию is_correct_json(), которая принимает один аргумент:

# string — произвольная строка

# Функция должна возвращать True, если строка string удовлетворяет формату JSON,
# или False в противном случае.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию is_correct_json(), но не код, вызывающий ее.

import json

def is_correct_json(string):
    try:
        data_string = json.loads(string)
        if type(data_string):
            return True
    except json.decoder.JSONDecodeError:
        return False



# Элементы JSON
# Напишите программу, которая принимает на вход описание одного объекта в формате
# JSON и выводит все пары ключ-значение этого объекта.

# Формат входных данных
# На вход программе подается корректное описание одного объекта в формате JSON.

# Формат выходных данных
# Программа должна вывести все пары ключ-значение введенного объекта, разделяя ключ
# и значение двоеточием, каждую на отдельной строке. Если значением ключа является
# список, то все его элементы должны быть выведены через запятую.

# Примечание 1. Пары ключ-значение при выводе должны располагаться в своем исходном
# порядке.

import json
import sys

data = json.load(sys.stdin)
for key, value in data.items():
    if type(value) == list:
        print(f'{key}: {", ".join(list(map(lambda elem: str(elem), value)))}')
    else:
        print(f'{key}: {value}')



# Объединение объектов
# Вам доступны два файла data1.json и data2.json, каждый из которых содержит по
# единственному JSON-объекту:

# {
#    "Holly-Anne": [
#       33,
#       "failed"
#    ],
#    "Caty": [
#       36,
#       "failed"
#    ],
#    ...
# }
# Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект,
# причем если пары из первого и второго объектов имеют совпадающие ключи, то значение
# следует взять из второго объекта. Полученный JSON-объект программа должна записать
# в файл data_merge.json.

import json

with open('data1.json', encoding='utf-8') as file1, open('data2.json', encoding='utf-8') as file2:
    data1_dict = json.load(file1)
    data2_dict = json.load(file2)
    data_merge = data1_dict | data2_dict
    
    with open('data_merge.json', 'w', encoding='utf-8') as file:
        json.dump(data_merge, file)

        
        
# Разные типы
# Вам доступен файл data.json, содержащий список различных объектов:

# [
#    "nwkWXma",
#    null,
#    {
#       "ISgHT": "dIUbf"
#    },
#    "Pzt",
#    "BXcbGVTE",
#    ...
# ]

# Напишите программу, которая создает список, элементами которого являются
# объекты из списка, содержащегося в файле data.json, измененные по следующим
# правилам:

# если объект является строкой, в его конец добавляется восклицательный знак
# если объект является числом, он увеличивается на единицу
# если объект является логическое значением, он инвертируется
# если объект является списком, он удваивается
# если объект является JSON-объектом (словарем), в него добавляется новая пара
# "newkey": null
# если объект является пустым значением (null), он не добавляется

# Полученный список программа должна записать в файл updated_data.json.

# Примечание 1. Например, если бы файл data.json имел вид:

# ["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]

# то программа должна была бы создать файл updated_data.json со следующим
# содержанием:

# ["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]

import json

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)
    result_data = []

    for elem in data:
        if elem is None:
            continue
        elif type(elem) is bool:
                result_data.append(not elem)
        elif type(elem) is str:
            result_data.append(elem + '!')
        elif type(elem) is int or type(elem) is float:
            result_data.append(elem + 1)
        elif type(elem) is list:
            result_data.append(elem * 2)
        elif type(elem) is dict:
            result_data.append(elem | {"newkey": None})
    
    with open('updated_data.json', 'w', encoding='utf-8') as new_file:
        json.dump(result_data, new_file, indent=3)



# Восстановление недостающих ключей
# Вам доступен файл people.json, содержащий список JSON-объектов. Причем у
# различных объектов может быть различное количество ключей:

# [
#    {
#       "age": 33,
#       "country": "Lesotho",
#       "phone": "(927) 316-2249",
#       "family_status": "married",
#       "email": "neonatus@outlook.com"
#    },
#    {
#       "age": 25,
#       "country": "Guinea",
#       "name": "Dorey",
#       "children": "yes",
#       "email": "ismail@gmail.com",
#       "university": "Khalifa University",
#       "family_status": "married"
#    },
#    ...
# ]

# Напишите программу, которая добавляет в каждый JSON-объект из данного списка
# все недостающие ключи, присваивая этим ключам значение null. Ключ считается
# недостающим, если он присутствует в каком-либо другом объекте, но отсутствует
# в данном. Программа должна создать список с обновленными JSON-объектами и
# записать его в файл updated_people.json.

# Примечание 1. JSON-объекты в создаваемом программой списке должны располагаться
# в своем исходном порядке. Порядок ключей в JSON-объектах не важен.

# Примечание 2. Например, если бы файл people.json имел вид:

# [
#    {
#       "age": 33,
#       "country": "Lesotho"
#    },
#    {
#       "age": 25,
#       "country": "Guinea",
#       "name": "Dorey"
#    }
# ]

# то программа должна была создать файла updated_people.json со следующим содержанием:

# [
#    {   
#       "age": 33,
#       "country": "Lesotho"
#       "name": null
#    },
#    {
#       "age": 25,
#       "country": "Guinea",
#       "name": "Dorey"
#    }
# ]

import json

with open('people.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    result_data = []
    all_keys_dict = {}

    for elem in data:
        for key in elem:
            all_keys_dict[key] = all_keys_dict.get(key, None)
    
    for elem in data:
        for key in all_keys_dict:
            elem[key] = elem.get(key, None)
        result_data.append(elem)
    
    with open('updated_people.json', 'w', encoding='utf-8') as new_file:
        json.dump(result_data, new_file, indent=3)



# Я исповедую Python, а ты?
# Вам доступен файл countries.json, содержащий список JSON-объектов c информацией
# о странах и исповедуемых в них религиях:

# [
#    {
#       "country": "Afghanistan",
#       "religion": "Islam"
#    },
#    {
#       "country": "Albania",
#       "religion": "Islam"
#    },
#    ...
# ]

# Каждый объект из этого списка содержит два атрибута:

# country — страна
# religion — исповедуемая религия

# Напишите программу, которая создает единственный JSON-объект, имеющий в качестве
# ключа название религии, а в качестве значения — список стран, в которых исповедуется
# данная религия. Полученный JSON-объект программа должна записать в файл religion.json.

# Примечание 1. Страны в списках должны располагаться в своем исходном порядке.

# Примечание 2. Начальная часть файла religion.json выглядит так:

# {
#    "Islam":[
#       "Afghanistan",
#       "Albania",
#       "Algeria",
#       ...
#    ],
#    ...
# }

import json

with open('D:/Python/Stepik/countries.json', encoding='utf-8') as file:
    data = json.load(file)
    religion_dict = {}

    for elem in data:
        religion_dict[elem['religion']] = religion_dict.get(elem['religion'], []) + [elem['country']]
    
    with open('religion.json', 'w', encoding='utf-8') as new_file:
        json.dump(religion_dict, new_file, indent=3)
