# Вам доступен именованный кортеж Person, который содержит данные о человеке. Первым
# элементом именованного кортежа является имя человека, вторым — возраст, третьим —
# рост. Также доступен список persons, содержащий эти кортежи.

# Дополните приведенный ниже код, чтобы он сгруппировал людей из данного списка по их
# росту и вывел полученные группы. Для каждой группы сначала должен быть указан рост,
# а затем через запятую перечислены имена людей, имеющих соответствующий рост. Группы
# должны быть расположены в порядке увеличения роста, каждая на отдельной строке, имена
# в группах — в алфавитном порядке, в следующем формате:

# <рост>: <имя>, <имя>, ...

# Примечание. Начальная часть ответа выглядит так:

# 158: Ariana, Eva
# 172: Mark
# ...

from collections import namedtuple
from itertools import groupby


Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

key_func = lambda p: p[-1]
sorted_persons_name = sorted(persons, key=lambda p: p[0])
sorted_persons_age = sorted(sorted_persons_name, key=key_func)
sorted_persons_height = groupby(sorted_persons_age, key=key_func)

for key, group in sorted_persons_height:
    print(f'{key}: {", ".join([person[0] for person in list(group)])}')



# Вам доступен именованный кортеж Student, который содержит данные об ученике. Первым
# элементом именованного кортежа является фамилия ученика, вторым — имя, третьим — класс.
# Также доступен список students, содержащий эти кортежи.

# Дополните приведенный ниже код, чтобы он вывел наиболее часто встречаемое имя среди
# учеников из данного списка.

# Примечание. Гарантируется, что искомое имя единственное.

from collections import namedtuple
from itertools import groupby


Student = namedtuple('Student', ['surname', 'name', 'grade'])

students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
            Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
            Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
            Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
            Student('Елькина', 'Мария', 11),Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
            Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
            Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
            Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
            Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]

key_func = lambda p: p[1]
sorted_students_name = sorted(students, key=key_func)
sorted_students_groups = groupby(sorted_students_name, key=key_func)
list_groups = [(key, list(group)) for key, group in sorted_students_groups]
common_name = max(list_groups, key=lambda s: len(list(s)[1]))

print(common_name[0])



# Группы слов
# Напишите программу, которая группирует слова по их длине.

# Формат входных данных
# На вход программе подается последовательность слов, разделенных пробелом. Каждое слово
# записано строчными латинскими буквами.

# ормат выходных данных
# Программа должна сгруппировать введенные слова по их длине и вывести полученные группы.
# Для каждой группы должна быть указана длина, а затем через запятую перечислены слова,
# имеющие соответствующую длину. Группы должны быть расположены в порядке увеличения длины,
# каждая на отдельной строке, слова в группах — в алфавитном порядке, в следующем формате:

# <длина> -> <слово>, <слово>, ...

from itertools import groupby


words = sorted(input().split())
key_func = lambda w: len(w)
sorted_words = groupby(sorted(words, key=key_func), key=key_func)
for key, group in sorted_words:
    print(f'{key} -> {", ".join(list(group))}')



# Нет дел
# Каждый день Тимур записывает в блокнот дела, которые ему нужно выполнить. Каждое дело
# он разбивает на несколько действий.

# Вам доступен список tasks, в котором записаны все дела Тимура. Каждый элемент списка
# представляет собой кортеж из трех элементов: первый — название дела, второй — действие,
# третий — очередность.

# Дополните приведенный ниже код, чтобы он вывел все дела Тимура в алфавитном порядке,
# указав для каждого набор соответствующих действий в правильной очередности, в следующем
# формате:

# <дело>:
#     1. <действие>
#     2. <действие>
#     ...

# Между двумя делами должна быть расположена пустая строка.

# Примечание 1. Начальная часть ответа выглядит так (в качестве отступов используйте четыре
# пробела):

# ЕГЭ Математика:
#     1. доделать курс по параметрам

# Курс по ооп:
#     1. обсудить темы
#     2. обсудить задачи

# ...

from itertools import groupby


tasks = [('Отдых', 'поспать днем', 3),
        ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
        ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
        ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
        ('Отдых', 'погулять вечером', 4),
        ('Курс по ооп', 'обсудить темы', 1),
        ('Урок по groupby', 'добавить задачи на программирование', 3),
        ('Урок по groupby', 'написать конспект', 1),
        ('Отдых', 'погулять днем', 2),
        ('Урок по groupby', 'добавить тестовые задачи', 2),
        ('Уборка', 'убраться в ванной', 2),
        ('Уборка', 'убраться в комнате', 1),
        ('Уборка', 'убраться на кухне', 3),
        ('Отдых', 'погулять утром', 1),
        ('Курс по ооп', 'обсудить задачи', 2)]

key_func = lambda t: t[0]
sorted_tasks = sorted(tasks, key=key_func)
sorted_groups_task = groupby(sorted_tasks, key=key_func)

for key, group in sorted_groups_task:
    print(f'{key}:')
    for deal in sorted(list(group), key=lambda t: t[-1]):
        print(f'    {deal[-1]}. {deal[1]}')
    print()



# Функция group_anagrams()
# Анаграммы — это слова, которые состоят из одинаковых букв. Например:

# адаптер — петарда
# адресочек — середочка
# азбука — базука
# аистенок — осетинка

# Реализуйте функцию group_anagrams(), которая принимает один аргумент:

# words — список слов

# Функция должна группировать в кортежи слова из списка words, являющиеся анаграммами, и
# возвращать список полученных кортежей.

# Примечание 1. Порядок кортежей в возвращаемом функцией списке, а также порядок элементов в
# этих кортежах, не важен.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию
# group_anagrams(), но не код, вызывающий ее.

from itertools import groupby


def group_anagrams(words):
    key_func = lambda word: ''.join(sorted(word))
    anagrams_groups = groupby(sorted(words, key=key_func), key=key_func)
    return (tuple(group) for _, group in anagrams_groups)