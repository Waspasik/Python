#На вход программе подается строка текста. Напишите программу, которая удаляет из нее все символы с индексами кратными 3, то есть символы с индексами 0, 3, 6, ....

#Формат входных данных 
#На вход программе подается строка текста.

#Формат выходных данных
#Программа должна вывести строку текста в соответствии с условием задачи.

s = input()
for i in range(len(s)):
    if i % 3 != 0:
        print(s[i], end='')



#На вход программе подается строка текста. Напишите программу, которая заменяет все вхождения цифры 1 на слово «one».

#Формат входных данных 
#На вход программе подается строка текста.

#Формат выходных данных
#Программа должна вывести текст в соответствии с условием задачи.

s = input()
print(s.replace('1', 'one'))



#На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения символа «@».

#Формат входных данных 
#На вход программе подается строка текста.

#Формат выходных данных
#Программа должна вывести текст в соответствии с условием задачи.

s = input()
print(s.replace('@', ''))



#На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f». Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.

#Формат входных данных 
#На вход программе подается строка текста.

#Формат выходных данных
#Программа должна вывести текст в соответствии с условием задачи.

s = input()
counter = 0
for i in range(len(s)):
    index = 0
    if "f" in s[i]:
        counter += 1
        index += i
        if counter == 2:
            break
if counter == 2:
    print(index)
elif counter == 1:
    print(-1)
elif counter == 0:
    print(-2)



#На вход программе подается строка текста в которой буква «h» встречается как минимум два раза. Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним вхождением буквы «h».

#Формат входных данных 
#На вход программе подается строка текста.

#Формат выходных данных
#Программа должна вывести текст в соответствии с условием задачи.

s = input()
slc = s[s.find('h') + 1:s.rfind('h')]
slc_new = slc[::-1]
print(s.replace(slc, slc_new))