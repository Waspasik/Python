# Вам доступен именованный кортеж Person, который содержит данные о человеке. Первым
# элементом именованного кортежа является имя и фамилия человека, вторым — национальность,
# третьим — пол, четвертым — год рождения, пятым — год смерти. Если человек жив, год
# смерти считается равным 00. Также доступен список persons, содержащий эти кортежи.

# Дополните приведенный ниже код с использованием конвейеров генераторов, чтобы он
# вывел имя и фамилию самого молодого живого мужчины из Швеции (Swedish).

# Примечание 1. Пример вывода:

# Goran Aslin

# Примечание 2. Гарантируется, что искомый человек единственный.

from collections import namedtuple

Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
           Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
           Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
           Person('Genevieve Asse', 'French', 'female', 1949, 0),
           Person('Irene Adler', 'Swedish', 'female', 2005, 0),
           Person('Sergio Asti', 'Italian', 'male', 1926, 0),
           Person('Olof Backman', 'Swedish', 'male', 1999, 0),
           Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
           Person('Dana Atchley', 'American', 'female', 1941, 2000),
           Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
           Person('Shura_Stone', 'Russian', 'male', 2000, 0),
           Person('Jon Bale', 'Swedish', 'male', 1950, 0)]

alive_swedish_male_persons = (
    person
    for person in persons
    if person[1] == 'Swedish' and person[-1] == 0 and person[2] == 'male'
    )
    
print(max(alive_swedish_male_persons, key=lambda p: p[-2])[0])



# Функция parse_ranges()
# Назовем диапазоном запись двух натуральных чисел через дефис a-b, где a — левая
# граница диапазона, b — правая граница диапазона, причем a <= b. Диапазон содержит
# в себе все числа от a до b включительно. Например, диапазон 1-4 содержит числа 1,
# 2, 3 и 4.

# Реализуйте генераторную функцию parse_ranges(), которая принимает один аргумент:

# ranges — строка, в которой через запятую указаны диапазоны чисел

# Функция должна возвращать генератор, порождающий последовательность чисел,
# содержащихся в диапазонах ranges.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию parse_ranges(), но не код, вызывающий ее.

def parse_ranges(ranges):
    iter_ranges = (list(map(int, rng.split('-'))) for rng in ranges.split(','))
    all_numbers = (num for rng in iter_ranges for num in range(rng[0], rng[1]+1))
    return all_numbers



# Функция filter_names()
# Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в
# следующем порядке:

# names — список имен
# ignore_char — одиночный символ
# max_names — натуральное число

# Функция должна возвращать генератор, порождающий max_names имён из списка names,
# игнорируя имена, которые

# начинаются на ignore_char (в любом регистре)
# содержат хотя бы одну цифру

# Если max_names больше количества имен в списке names, то генератор должен породить
# все возможные имена из данного списка. 

# Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем
# исходном порядке.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию filter_names(), но не код, вызывающий ее.

with open('D:/Python/Stepik/data.csv', encoding='utf-8') as file:
    file_lines = (line.rstrip().split(',') for line in file if line != '')
    file_headers = next(file_lines)
    line_dicts = (dict(zip(file_headers, data)) for data in file_lines)
    only_a_round_lines = filter(lambda line: line['round'] == 'a', line_dicts)
    sum_total = sum(int(line['raisedAmt']) for line in only_a_round_lines)
    print(sum_total)



# Функция years_days()
# Реализуйте генераторную функцию years_days(), которая принимает один аргумент:

# year — натуральное число

# Функция должна возвращать генератор, порождающий последовательность всех дат (тип date)
# в году year.

# римечание 1. Возьмем в качестве примера 20222022 год. В январе этого года 31 день, в
# феврале — 28, в марте — 31, и так далее. Тогда генератор, полученный при вызове
# years_days(2022), должен порождать сначала все даты с 1 по 31 января, затем с 1 по 28
# февраля, и так далее до 31 декабря.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию years_days(), но не код, вызывающий ее.

from datetime import date


def years_days(year):
    return (date.fromordinal(dt) for dt in range(date(year, 1, 1).toordinal(), date(year, 12, 31).toordinal()+1))



# Функция nonempty_lines()
# Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:

# file — название текстового файла, например, data.txt

# Функция должна возвращать генератор, порождающий последовательность всех непустых строк
# файла file с убранным символом переноса строки \n. Если строка содержит более 25 символов,
# она заменяется троеточием ....

# Примечание 1. При открытии файла используйте явное указание кодировки UTF-8.

# римечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию nonempty_lines(), но не код, вызывающий ее.

def nonempty_lines():
    with open(file, 'r', encoding='utf-8') as f:
        file_lines = (line.strip() for line in f)
        nonempty_lines = (line for line in file_lines if line != '')
        changed_lines = (line if len(line) <= 25 else '...' for line in nonempty_lines)
        yield from changed_lines



# Функция txt_to_dict()
# Вам доступен файл planets.txt, содержащий информацию о различных планетах. В первых
# четырех строках указаны характеристики первой планеты, после чего следует пустая строка,
# затем характеристики второй планеты, и так далее:

# Name = Mercury
# Diameter = 4879.4
# Mass = 3.302×10^23
# OrbitalPeriod = 0.241

# Name = Venus
# Diameter = 12103.6
# Mass = 4.869×10^24
# OrbitalPeriod = 0.615
# ...

# Реализуйте генераторную функцию txt_to_dict(), которая не принимает никаких аргументов.

# Функция должна возвращать генератор, порождающий последовательность словарей, каждый из
# которых содержит информацию об очередной планете из файла planets.txt, а именно ее название,
# диаметр, массу и орбитальный период. Например:

# {'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию txt_to_dict(), но не код, вызывающий ее.

def txt_to_dict():
    with open('planets.txt', 'r', encoding='utf-8') as file:
        file_lines = (line.split('\n') for line in file.read().split('\n\n'))
        planets_info = (dict(info.split(' = ') for info in planet) for planet in file_lines)
        return planets_info



# Функция unique()
# Реализуйте генераторную функцию, которая принимает один аргумент:

# iterable — итерируемый объект

# Функция должна возвращать генератор, порождающий последовательность элементов итерируемого
# объекта iterable без дубликатов.

# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны
# располагаться в своем исходном порядке.

# римечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является
# множеством.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию unique(), но не код, вызывающий ее.

def unique(iterable):
    yield from {item: 1 for item in iterable}



# Функция stop_on()
# Реализуйте генераторную функцию, которая принимает два аргумента в следующем порядке:

# iterable — итерируемый объект
# obj — произвольный объект

# Функция должна возвращать генератор, порождающий последовательность элементов итерируемого
# объекта iterable до тех пор, пока не будет достигнут элемент, равный obj. Если итерируемый
# объект iterable не содержит ни одного элемента, равного obj, генератор должен породить все
# элементы iterable.

# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны
# располагаться в своем исходном порядке.

# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является
# множеством.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию stop_on(), но не код, вызывающий ее.

def stop_on(iterable, obj):
    iterator = (item for item in iterable)
    for item in iterator:
        if item != obj:
            yield item
        else:
            break



# Функция with_previous()
# Реализуйте генераторную функцию, которая принимает один аргумент:

# iterable — итерируемый объект

# Функция должна возвращать генератор, порождающий последовательность кортежей, каждый
# из которых содержит очередной элемент итерируемого объекта iterable, а также
# предшествующий ему элемент:

# (<очередной элемент>, <предыдущий элемент>)

# Для первого элемента предыдущим считается значение None.

# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны
# располагаться в своем исходном порядке.

# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является
# множеством.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию with_previous(), но не код, вызывающий ее.

def with_previous(iterable):
    prev_item = None
    for item in iterable:
        if prev_item is None:
            yield item, prev_item
            prev_item = item
        else:
            yield item, prev_item
            prev_item = item