# Вам доступен список кортежей data с данными о доходах некоторого образовательного
# ресурса. Первым элементом кортежа является название продукта, вторым — прибыль в
# долларах.

# Дополните приведенный ниже код, чтобы он определил, какой общий доход принес каждый
# продукт и вывел названия всех продуктов, указав для каждого соответствующую общую
# прибыль. Продукты должны быть расположены в лексикографическом порядке, каждый на
# отдельной строке, в следующем формате:

# <продукт>: $<общая прибыль>

# Примечание. Начальная часть ответа выглядит так:

# Books: $7969
# Courses: $2991
# ...

from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145),
        ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642),
        ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003),
        ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]

result = defaultdict()

for book in sorted(data, key=lambda book: book[0]):
    result[book[0]] = result.get(book[0], 0) + book[1]

for key, value in result.items():
    print(f'{key}: ${value}')



# Вам доступен список кортежей staff с данными о сотрудниках некоторой компании.
# Первым элементом кортежа является название отдела, вторым — имя и фамилия
# сотрудника, работающего в этом отделе.

# Дополните приведенный ниже код, чтобы он определил, какое число сотрудников
# работает в каждом отделе и вывел названия всех отделов, указав для каждого
# соответствующее количество сотрудников. Отделы должны быть расположены в
# лексикографическом порядке, каждый на отдельной строке, в следующем формате:

# <отдел>: <количество сотрудников>

# Примечание. Начальная часть ответа выглядит так:

# Accounting: 17
# Developing: 7
# ...

from collections import defaultdict

staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'),
         ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'),
         ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'),
         ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'),
         ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'),
         ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'),
         ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'),
         ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'),
         ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'),
         ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'),
         ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'), 
         ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'),
         ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'),
         ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'),
         ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'),
         ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'),
         ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]

result = defaultdict()

for department, employee in staff:
    result[department] = result.get(department, 0) + 1

for key, value in sorted(result.items()):
    print(f'{key}: {value}')



# Вам доступен список список кортежей staff_broken с данными о сотрудниках некоторой
# компании. Первым элементом кортежа является название отдела, вторым — имя и фамилия
# сотрудника, работающего в этом отделе. Некоторые сотрудники могут встречаться в
# списке несколько раз.

# Дополните приведенный ниже код, чтобы он сгруппировал сотрудников по соответствующим
# отделам и вывел названия всех отделов, указав для каждого имена и фамилии его
# сотрудников. Отделы, а также имена и фамилии сотрудников в этих отделах, должны быть
# расположены в лексикографическом порядке, каждый на отдельной строке, в следующем
# формате:

# <отдел>: <имя> <фамилия>, <имя> <фамилия>, ...

# Примечание. Начальная часть ответа выглядит так:

# Accounting: Aaron Ferguson, Ann Bell, Brenda Davis, Casey Jenkins, Craig Wood, Dale Houston, Edna Cunningham, Gloria Higgins, James Wilkins, Jane Jackson, John Watts, Kay Scott, Kimberly Reynolds, Linda Hudson, Michelle Wright, Rosemary Garcia, Steven Diaz
# Developing: Arlene Gibson, Deborah George, Joyce Rivera, Miguel Norris, Nicole Watts, Thomas Porter, Wilma Woods
# ...

from collections import defaultdict

staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'),
                ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'),
                ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
                ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'),
                ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
                ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'),
                ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
                ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'),
                ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
                ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'),
                ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
                ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'),
                ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'),
                ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
                ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'),
                ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
                ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'),
                ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
                ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'),
                ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
                ('Accounting', 'Dale Houston')]

result = defaultdict(set)

for department, employee in staff_broken:
    result[department].add(employee)

for key, value in sorted(result.items()):
    print(f'{key}: {", ".join(sorted(value))}')



# Функция wins()
# В онлайн-школе BEEGEEK каждое лето проходят соревнования по шахматам, во время
# которых ведется статистика побед и поражений. Каждая партия описывается кортежем
# из двух элементов, где первый элемент — имя победившего ученика, второй элемент
# — имя проигравшего ученика.

# Реализуйте функцию wins(), которая принимает один аргумент:

# pairs — итерируемый объект, элементами которого являются кортежи, каждый из
# которых представляет собой пару имён победитель-проигравший

# Функция должна возвращать словарь, в котором ключом служит имя ученика, а значением
# — множество имен учеников, которых он победил.

# Примечание 1. Гарантируется, что каждая партия заканчивается победой одного из
# учеников, то есть ничьей быть не может.

# Примечание 2. Элементы в возвращаемом функцией могут располагаться в произвольном
# порядке.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию wins(), но не код, вызывающий ее.

from collections import defaultdict

def wins(pairs):
    pairs_dict = defaultdict(set)
    for winner, loser in pairs:
        pairs_dict[winner].add(loser)
    return pairs_dict



# Функция flip_dict()
# Рассмотрим следующий словарь:

# {'a': [1, 2], 'b': [3, 1], 'c': [2]}
# «Перевернем» его, представив ключи в виде значений, а значения — в виде ключей:

# {1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']}

# Реализуйте функцию flip_dict(), которая принимает один аргумент:

# dict_of_lists — словарь, в котором ключом является число или строка, а значением
# — список чисел или строк

# Функция должна возвращать новый словарь (тип defaultdict с типом list в качестве
# значения по умолчанию), который представляет собой «перевернутый» словарь dict_of_lists.

# Примечание 1. Ключи в возвращаемом функцией словаре, а также элементы в списках
# должны располагаться в своем исходном порядке.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию flip_dict(), но не код, вызывающий ее.

from collections import defaultdict

def flip_dict(dict_of_lists):
    result = defaultdict(list)
    for key, value in dict_of_lists.items():
        for item in value:
            result[item].append(key)
    return result



# Функция best_sender()
# Рассмотрим два списка:

# messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']

# senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

# Первый список представляет набор отправленных сообщений в некотором мессенджере,
# второй список — набор отправителей этих сообщений. Причем сообщение messages[i]
# отправлено пользователем senders[i]. Каждое сообщение представляет собой
# последовательность слов, разделенных пробелом (знаки препинания считаются частями
# слов). Количество слов — это общее число слов, отправленное пользователем.
# Обратите внимание, что каждый пользователь может отправлять более одного сообщения.
# Например, пользователь Sam Fisher отправил 2 слова в первом сообщении и 4 слова во
# втором, следовательно, его количество слов равно 2 + 4 = 6. 

# Реализуйте функцию best_sender(), которая принимает два аргумента в следующем порядке:

# messages — список сообщений
# senders — список имен отправителей

# Функция должна определять отправителя, имеющего наибольшее количество слов, и
# возвращать его имя. Если таких отправителей несколько, следует вернуть имя того,
# чье имя больше в лексикографическом сравнении.

# Примечание 1. Гарантируется, что длины передаваемых в функцию списков совпадают.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию best_sender(), но не код, вызывающий ее.

from collections import defaultdict

def best_sender(messages, senders):
    senders_and_messanges = defaultdict(int)
    for i in range(len(messages)):
        senders_and_messanges[senders[i]] += len(messages[i].split())
    return max(senders_and_messanges.items(), key=lambda x: (x[1], x[0]))[0]
