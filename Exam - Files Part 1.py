# Количество строк в файле
# На вход программе подается строка текста с именем текстового файла. Напишите
# программу для вывода на экран количества строк данного файла.

# Формат входных данных
# На вход программе подается строка текста, содержащая имя существующего
# текстового файла.

# Формат выходных данных
# Программа должна вывести количество строк файла.

# Примечание. Считайте, что исполняемая программа и указанный файл находятся
# в одной папке.

with open(input(), 'r', encoding='utf-8') as file:
    print(len(file.readlines()))



# Суммарная стоимость
# Вам доступен текстовый файл ledger.txt с данными о продажах фирмы за месяц.
# На каждой строке файла указано, сколько клиент заплатил за товар, в долларах
# (целое число):

# $47
# $100
# $60
# $12
# $8
# ...

# Напишите программу для подсчета суммарной месячной выручки фирмы. 

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести выручку фирмы (сумму всех чисел из файла) в соответствии
# с примером ниже.

# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в
# одной папке.

# Примечание 2. Если бы файл ledger.txt содержал строки:

# $37
# $44
# $19

# то результатом будет:

# $100

with open('ledger.txt', 'r', encoding='utf-8') as file:
    print(f'${sum(list(map(lambda x: int(x[1:]), [line.strip() for line in file.readlines()])))}')



# Goooood students
# Вам доступен текстовый файл grades.txt, содержащий оценки студента за три теста
# в каждом из триместров. Строки файла имеют вид: фамилия оценка_1 оценка_2 оценка_3.

# Напишите программу для подсчета количества студентов, сдавших все три теста.
# Тест считается сданным, если количество баллов по нему не меньше 65.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести количество студентов, сдавших все три теста.

# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в
# одной папке.

# Примечание 2. Если бы файл grades.txt содержал строки:

# Washington 83 77 54
# Adams 86 69 90
# Jacobson 50 49 71
# MacDonald 100 99 100
# Berrington 66 67 64

# то результатом будет:

# 2

with open('grades.txt', 'r', encoding='utf-8') as file:
    student_grades = [line.strip().split() for line in file.readlines()]
    student_grades = [line[1:] for line in student_grades]
    result = 0
    
    for grades in student_grades:
        grades_list = list(filter(lambda g: int(g) >= 65, grades))
        if len(grades_list) == 3:
            result += 1
    
    print(result)



# Самое длинное слово в файле
# Вам доступен текстовый файл words.txt со словами, разделенными пробелом. Напишите
# программу, которая находит и выводит самые длинные слова этого файла, не меняя 
# порядка их следования.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести самые длинные слова файла words.txt, каждое с новой строки,
# не меняя их порядка следования.

# Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной
# папке.

# Примечание 2. Словом считайте любую группу символов без пробелов, даже если она
# включает цифры или знаки препинания.

# Примечание 3. Если бы файл words.txt содержал строки:

# there are many different holidays on the first of january we celebrate new year on
# the seventh of january and the twenty-fifth of december we have christmas the
# twenty-third of february is the day of the defenders of the motherland or the
# army day then comes easter and radonitsa the first of may is the labour day the
# ninth of may is victory day the third of july is independence day then comes the
# seventh of november the day of the october revolution and so on

# то результатом будет:

# twenty-fifth
# twenty-third
# independence

with open('words.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()
    max_len = max(words, key=len)
    for word in words:
        if len(word) == len(max_len):
            print(word)



# Tail of a File
# На вход программе подается строка текста с именем текстового файла. Напишите
# программу, выводящую на экран последние 10 строк данного файла.

# Формат входных данных
# На вход программе подается строка текста с именем существующего текстового
# файла.

# Формат выходных данных
# Программа должна вывести последние 10 строк этого файла.

# Примечание 1. Считайте, что исполняемая программа и файл находятся в одной
# папке.

# Примечание 2. Если количество строк в файле меньше 10, необходимо вывести
# содержимое файла полностью.

# Примечание 3. Если бы файл содержал строки:

# there are many different holidays
# on the first of january we
# celebrate new year on the
# seventh of january and the
# twenty-fifth of december we
# have christmas the twenty-third
# of february is the day of the
# defenders of the motherland
# or the army day then comes
# easter and radonitsa the
# first of may is the labour
# day the ninth of may is
# victory day the third of july
# is independence day then comes
# the seventh of november the day
# of the october revolution and so on

# то результатом будет:

# of february is the day of the
# defenders of the motherland
# or the army day then comes
# easter and radonitsa the
# first of may is the labour
# day the ninth of may is
# victory day the third of july
# is independence day then comes
# the seventh of november the day
# of the october revolution and so on

# Примечание 4. Подумайте над ситуацией, когда файл очень большой и нерационально
# считывать все его содержимое в память компьютера.

with open(input(), 'r', encoding='utf-8') as file:
    print(*[line.strip() for line in file.readlines()][-10:], sep='\n')