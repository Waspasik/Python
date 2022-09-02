# Forbidden words 🌶️
# На вход программе подается строка текста с именем текстового файла. Напишите
# программу, выводящую на экран содержимое этого файла, но с заменой всех
# запрещенных слов звездочками * (количество звездочек равно количеству букв
# в слове).

# Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле
# forbidden_words.txt. Гарантируется, что все слова в этом файле записаны в
# нижнем регистре.

# Формат входных данных
# На вход программе подается строка текста с именем существующего текстового
# файла, в котором необходимо заменить запрещенные слова звездочками.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание 1. Ваша программа должна заменить запрещенные слова, где бы они
# ни встречались, даже если они встречаются в середине другого слова.

# Примечание 2. Программа должна заменять запрещенные слова независимо от их
# регистра. Например, если файл forbidden_words.txt содержит запрещенное слово
# exam, то слова exam, Exam, ExaM, EXAM и подобные должны быть заменены на ****.

# Примечание 3. Если бы файл forbidden_words.txt содержал слова:

# hello email python the exam wor is

# а файл в котором заменяются слова имел бы вид:

# Hello, world! Python IS the programming language of thE future. My EMAIL is....
# PYTHON is awesome!!!!

# то результатом будет:

# *****, ***ld! ****** ** *** programming language of *** future. My ***** **....
# ****** ** awesome!!!!

with open('data.txt', 'r', encoding='utf-8') as file, open('forbidden_words.txt', 'r', encoding='utf-8') as forbidden_words:
    text = file.read()
    text_lower = text.lower()
    forb_w = forbidden_words.read().split()
    
    for word in forb_w:
        text_lower = text_lower.replace(word, '*' * len(word))

    result = ''

    for i in range(len(text_lower)):
        if text_lower[i] == '*':
            result += '*'
        else:
            if text_lower[i] != '*' and text_lower[i] == text[i]:
                result += text_lower[i]
            else:
                result += text[i]

    print(result)



# Транслитерация 🌶️
# Транслитерация — передача знаков одной письменности знаками другой письменности,
# при которой каждый знак (или последовательность знаков) одной системы письма
# передаётся соответствующим знаком (или последовательностью знаков) другой системы
# письма.

# Вам доступен текстовый файл cyrillic.txt, содержащий текст. Напишите программу
# для транслитерации этого файла, то есть замены кириллических символов на латинские
# в соответствии с предложенной таблицей. Все остальные символы надо оставить без
# изменений. Результат транслитерации требуется записать в файл transliteration.txt.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна создать файл с именем transliteration.txt в соответствии с условием
# задачи.

# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной
# папке.

# Примечание 2. Обратите внимание, что заглавные буквы должны заменяться на
# соответствующие им заглавные же буквы, но если транслитерационная последовательность
# состоит из нескольких символов, то заглавным будет только первый из них: «С» на «S»,
# а «Я» на «Ya».

# Примечание 3. Если бы файл cyrillic.txt содержал текст:

# Президент США Дональд Трамп продолжил обмен выпадами с руководством КНДР.
# We all know why Joe Biden is rushing to falsely pose as the winner, and why his media
# allies are trying so hard to help him: they don’t want the truth to be exposed.
# то содержимое файла transliteration.txt будет:

# Prezident SShA Donal'd Tramp prodolzhil obmen vypadami s rukovodstvom KNDR.
# We all know why Joe Biden is rushing to falsely pose as the winner, and why his media
# allies are trying so hard to help him: they don’t want the truth to be exposed.

with open('cyrillic.txt', 'r', encoding='utf-8') as cyrillic, open('transliteration.txt', 'w') as transliteration:
    trans = '''
а     a     к     k     х     h
б     b     л     l     ц     c
в     v     м     m     ч     ch
г     g     н     n     ш     sh
д     d     о     o     щ     shh
е     e     п     p     ъ     *
ё     jo     р     r     ы     y
ж     zh     с     s     ь     '
з     z     т     t     э     je
и     i     у     u     ю     ju
й     j     ф     f     я     ya'''.split()

    abc_dict = dict(zip([trans[i] for i in range(0, len(trans), 2)],
                        [trans[i] for i in range(1, len(trans), 2)]))

    abc_dict.update(zip([trans[i].upper() for i in range(0, len(trans), 2)],
                        [trans[i].title() for i in range(1, len(trans), 2)]))
    
    cyr_text = cyrillic.read()
    
    for key, value in abc_dict.items():
        if key in cyr_text:
            cyr_text = cyr_text.replace(key, value)
    
    print(cyr_text, file=transliteration)



# Пропущенные комменты 🌶️
# При написании собственных функций рекомендуется в комментарии описывать назначение
# функции, ее параметры и возвращаемое значение. Часто программисты откладывают
# написание таких комментариев напоследок, а потом и вовсе забывают о них 😂.

# На вход программе подается строка текста с именем текстового файла, в котором
# написан код на языке Python. Напишите программу, выводящую на экран имена всех
# функций для которых отсутствует поясняющий комментарий. Будем считать, что любая
# строка, начинающаяся со слова def и пробела, является началом определения функции.
# Функция содержит комментарий, если первый символ предыдущей строки - #.

# Формат входных данных
# На вход программе подается строка текста, содержащая имя существующего текстового
# файла с кодом на языке Python.

# Формат выходных данных
# Программа должна вывести названия всех функций (не меняя порядка их следования в
# исходном файле), каждое на отдельной строке, для которых отсутствует поясняющий
# комментарий. Если все функции в файле имеют поясняющий комментарий, то следует
# вывести: Best Programming Team.

# Примечание 1. Если бы файл содержал код:

# def powers(a):
#     return a, a**2, a**3

# # функция вычисляет сумму всех переданных чисел
# def sum_all(*args):
#     return sum(args)

# def matrix():
#     pass

# # функция возвращает количество переданных аргументов
# def count_args(*args):
#     return len(args)

# def mean(*args):
#     total = 0.0
#     count = 0  
#     for i in args:
#         if type(i) in (int, float):
#             total += i
#             count += 1
#     if count == 0:
#         return 0.0
#     else:
#         return total / count
    
# def greet(name, *args):
#     args = (name,) + args
#     return f'Hello, {" and ".join(args)}!'

# # функция вычисляет факториал переданного числа
# def fact(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res

# то результатом будет:

# powers
# matrix
# mean
# greet

# Примечание 2. Гарантируется, что в файле есть хотя бы одна функция при этом
# вложенных функций в файле нет.

with open(input(), 'r', encoding='utf-8') as file:
    def_list = []
    comment = 'nothing'
    
    for line in file:
        line = line.strip()
        if 'def' in line and '#' not in comment:
            def_list.append(line[4::])
        comment = line
    
    if len(def_list) == 0:
        print('Best Programming Team')
       
    for d in def_list:
        print(d[0:d.find('(')])