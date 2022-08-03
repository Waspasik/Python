# Словарь программиста
# Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют
# весьма специфический язык. Чтобы систематизировать ваш пополняющийся профессиональный
# лексикон, мы придумали эту задачу. Напишите программу создания небольшого словаря
# сленговых программерских выражений, чтобы она потом по запросу возвращала значения из
# этого словаря.

# Формат входных данных
# В первой строке задано одно целое число n — количество слов в словаре. В следующих n
# строках записаны слова и их определения, разделенные двоеточием и символом пробела. В
# следующей строке записано целое число m — количество поисковых слов, чье определение
# нужно вывести. В следующих m строках записаны сами слова, по одному на строке.

# Формат выходных данных
# Для каждого слова, независимо от регистра символов, если оно присутствует в словаре,
# необходимо вывести его определение. Если слова в словаре нет, программа должна вывести
# "Не найдено", без кавычек.

# Примечание 1. Мини-словарь для начинающих разработчиков можно посмотреть тут.

# Примечание 2. Гарантируется, что в определяемом слове или фразе отсутствует двоеточие
# (:), следом за которым идёт пробел.

result = {}

lst = [tuple(input().split()) for _ in range(int(input()))]

for string in lst:
    result[string[0].lower().strip(':')] = result.get(string[0], string[1:])

for _ in range(int(input())):
    print(*result.get(input().lower(), ['Не', 'найдено']))



# Анаграммы 1
# Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих
# другое слово (или словосочетание). Например, английские слова evil и live – это анаграммы.

# На вход программе подаются два слова. Напишите программу, которая определяет, являются ли
# они анаграммами.

# Формат входных данных
# На вход программе подаются два слова, каждое на отдельной строке.

# Формат выходных данных
# рограмма должна вывести YES если слова являются анаграммами и NO в противном случае.

dict1 = {}
dict2 = {}

for i in input():
    dict1[i] = dict1.get(i, 0) + 1

for i in input():
    dict2[i] = dict2.get(i, 0) + 1

if dict1 == dict2:
    print('YES')
else:
    print('NO')



# Анаграммы 2
# На вход программе подаются два предложения. Напишите программу, которая определяет, являются
# они анаграммами или нет. Ваша программа должна игнорировать регистр символов, знаки препинания
# и пробелы.

# Формат входных данных
# На вход программе подаются два предложения, каждое на отдельной строке.

# Формат выходных данных
# рограмма должна вывести YES , если предложения – анаграммы и NO в противном случае.

# римечание. Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;-. Других
# символов в тексте нет.

dict1, dict2 = {}, {}

for word in input().split():
    for char in word.lower().strip('.,!?:;-'):
        dict1[char] = dict1.get(char, 0) + 1

for word in input().split():
    for char in word.lower().strip('.,!?:;-'):
        dict2[char] = dict2.get(char, 0) + 1

if dict1 == dict2:
    print('YES')
else:
    print('NO')



# Словарь синонимов
# Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите
# программу, которая для одного данного слова определяет его синоним.

# Формат входных данных
# На вход программе подается количество пар синонимов nn. Далее следует nn строк, каждая строка
# содержит два слова-синонима. После этого следует одно слово, синоним которого надо найти.

# Формат выходных данных
# Программа должна вывести одно слово, синоним введенного.

# Примечание 1. Гарантируется, что синоним введенного слова существует в словаре.

# Примечание 2. Все слова в словаре начинаются с заглавной буквы.

dict1, dict2 = {}, {}

for _ in range(int(input())):
    string = input().split()
    dict1[string[-1]] = dict1.get(string[-1], []) + [string[0]]
    dict2[string[0]] = dict2.get(string[0], []) + [string[-1]]

synonym = input()

if synonym in dict1:
    print(*dict1[synonym])
else:
    print(*dict2[synonym])