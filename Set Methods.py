# Уникальные символы 1
# Напишите программу для вывода количества уникальных символов каждого считанного слова без
# учета регистра.

# Формат входных данных
# На вход программе в первой строке подается число n – общее количество слов. Далее идут n
# строк с словами.

# Формат выходных данных
# Программа должна вывести на отдельной строке количество уникальных символов для каждого
# слова.

n = int(input())

for i in range(n):
    my_set = set(input().upper())
    print(len(my_set))



# Уникальные символы 2
# Напишите программу для вывода общего количества уникальных символов во всех считанных словах
# без учета регистра.

# Формат входных данных
# На вход программе в первой строке подается число n – общее количество слов. Далее идут n
# строк со словами.

# Формат выходных данных
# Программа должна вывести одно число – общее количество уникальных символов во всех словах
# без учета регистра.

n = int(input())
myset = set()

for i in range(n):
    word = input().upper()
    for j in range(len(word)):
        myset.add(word[j])

print(len(myset))



# Количество слов в тексте
# Напишите программу для определения общего количества различных слов в строке текста.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести одно число – общее количество различных слов в строке без учета
# регистра.

# Примечание 1. Словом считается последовательность непробельных символов, идущих подряд,
# слова разделены одним или большим числом пробелов.

# Примечание 2. Знаками препинания .,;:-?! пренебрегаем.

string = input().lower().split()
myset = set()
symbols = '.,;:-?!'

for i in range(len(string)):
    if string[i][-1] in symbols:
        myset.add(string[i][:-1])
    elif string[i][0] in symbols:
        myset.add(string[i][1:])
    else:
        myset.add(string[i])

print(len(myset))



# Встречалось ли число раньше?
# На вход программе подается строка текста, содержащая числа. Для каждого числа выведите
# слово YES (в отдельной строке), если это число ранее встречалось в последовательности или
# NO, если не встречалось.

# Формат входных данных
# На вход программе подается строка текста, содержащая числа, разделенные символом пробела.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Ведущие нули в числах должны игнорироваться.

numbers = input().split()
myset = set()

for i in range(len(numbers)):
    if int(numbers[i]) not in myset:
        print('NO')
    else:
        print('YES')
    myset.add(int(numbers[i]))