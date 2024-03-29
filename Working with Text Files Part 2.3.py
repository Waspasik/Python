# CSV-файл
# Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию
# read_csv для чтения данных из этого файла. Она должна возвращать список словарей,
# интерпретируя первую строку как имена ключей, а каждую последующую строку как значения
# этих ключей.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна содержать реализованную функцию read_csv.

# Примечание 1. Вызывать функцию read_csv не нужно.

# Примечание 2. Функция read_csv не должна принимать аргументов. 

# Примечание 3. Считайте, что все ключи и значения по этим ключам в результирующем словаре 
# имеют строковый тип (str).

# Примечание 4. Если бы файл data.csv содержал информацию

# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21

# то вызов функции read_csv() вернул бы список:

# [{'name': 'George', 'address': '4312 Abbey Road', 'age': '22'},
#  {'name': 'John', 'address': '54 Love Ave', 'age': '21'}]

def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as file:
        keys_list = file.readline().strip().split(',')
        return list(map(lambda value: dict(zip(keys_list, value)), [value.strip().split(',') for value in file]))