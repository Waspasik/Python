#Дополните приведенный код, чтобы он:

#Вывел длину списка;
#Вывел последний элемент списка;
#Вывел список в обратном порядке (вспоминаем срезы);
#Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
#Вывел список с удаленным первым и последним элементами.
#Примечание. Каждый вывод осуществлять с новой строки.

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers), numbers[-1], numbers[::-1], sep='\n')
if 5 and 17 in numbers:
    print('YES')
else:
    print("NO")
del numbers[0]
del numbers[-1]
print(numbers)



#На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая создает из указанных строк список и выводит его.

#Формат входных данных
#На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.

#Формат выходных данных
#Программа должна вывести список состоящий из указанных строк.

n = int(input())
my_list = []
for i in range(n):
    language = input()
    my_list.append(language)
print(my_list)



#Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
#Формат выходных данных
#Программа должна вывести указанный список.

#Примечание. Последний элемент списка состоит из 26 символов z.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
my_list = []
for i in range(len(alphabet)):
    letter = alphabet[i]
    my_list.append(letter * (i + 1))
print(my_list)



#На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая создает из указанных чисел список их кубов.

#Формат входных данных
#На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

#Формат выходных данных
#Программа должна вывести список, состоящий из кубов указанных чисел.

n = int(input())
my_list = []
for i in range(n):
    number = int(input())
    my_list.append(number**3)
print(my_list)



#На вход программе подается натуральное число nn. Напишите программу, которая создает список состоящий из делителей введенного числа.

#Формат входных данных
#На вход программе подается натуральное число nn.

#Формат выходных данных
#Программа должна вывести список, состоящий из делителей введенного числа.

n = int(input())
my_list = []
for i in range(1, n+1):
    if n % i == 0:
        my_list.append(i)
print(my_list)



#На вход программе подается натуральное число n≥2, а затем nn целых чисел. Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (00 и 11, 11 и 22, 22 и 33 и т.д.).

#Формат входных данных
#На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

#Формат выходных данных
#Программа должна вывести список, состоящий из сумм соседних чисел.

n = int(input())
main_list = []
my_list = []
for i in range(n):
    number = int(input())
    main_list.append(number)
for i in range(len(main_list)-1):
    sum_numbers = main_list[i] + main_list[i+1]
    my_list.append(sum_numbers)
print(my_list)



#На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

#Формат входных данных
#На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

#Формат выходных данных
#Программа должна вывести список в соответствии с условием задачи.

#Примечание. Используйте оператор del.

n = int(input())
main_list = []
for i in range(n):
    number = int(input())
    main_list.append(number)
del main_list[1::2]
print(main_list)



#На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая создает список из символов всех строк, а затем выводит его.

#Формат входных данных
#На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.

#Формат выходных данных
#Программа должна вывести список состоящий из символов всех введенных строк.

#Примечание. В результирующем списке могут содержаться одинаковые символы.

n = int(input())
my_list = []
for i in range(n):
    letters = input()
    my_list.extend(letters)
print(my_list)