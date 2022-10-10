# Я и сам своего рода переводчик
# Дана строка соответствия латинскому алфавиту: первый символ строки соответствует
# букве a, второй — b, третий — c, и так далее. Каждый символ соответствует как
# заглавной, так и строчной буквам. Количество символов в строке совпадает с количеством
# букв в латинском алфавите.

# Напишите программу, которая с помощью данной строки переводит заданный текст.

# Формат входных данных
# На вход программе в первой строке подается строка соответствия латинскому алфавиту,
# в следующей — текст, требующий перевода.

# Формат выходных данных
# Программа должна с помощью данной строки соответствия латинскому алфавиту перевести
# введенный текст и вывести полученный результат.

# Примечание 1. Программа должна игнорировать все символы, не являющиеся латинскими
# буквами.

# Примечание 2. Составить словарь соответствия можно с помощью строкового метода
# maketrans()

# first solution

import string

eng_alphabet = list(string.ascii_lowercase)
symbols_dict = {}
result = ''
counter = 0

for char in input():
    symbols_dict[counter] = symbols_dict.get(counter, char)
    counter += 1

for char in input().lower():
    if char.isalpha():
        result += symbols_dict[eng_alphabet.index(char)]
    else:
        result += char
        
print(result)

# second solution 😎

import string

symbols_string = input()
text = input()
result = str.maketrans(string.ascii_letters, symbols_string * 2)
print(text.translate(result))