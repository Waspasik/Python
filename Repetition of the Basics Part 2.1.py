# Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество
# точек, лежащих в каждой координатной четверти.

# Формат входных данных
# В первой строке записано количество точек. Каждая следующая строка состоит из двух целых
# чисел — координат точки (сначала абсцисса – xx, затем ордината – yy), разделенных символом
# пробела.

# Формат выходных данных
# Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в
# примерах.

# Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой-либо
# координатной четверти.

first_quarter = 0
second_quarter = 0
third_quarter = 0
fourth_quarter = 0

for i in range(int(input())):
    i = input().split()
    x, y = i[0], i[1]
    if int(x) > 0 and int(y) > 0:
        first_quarter += 1
    elif int(x) < 0 and int(y) > 0:
        second_quarter += 1
    elif int(x) < 0 and int(y) < 0:
        third_quarter += 1
    elif int(x) > 0 and int(y) < 0:
        fourth_quarter += 1
    elif int(x) or int(y) == 0:
        continue

print('Первая четверть: ', first_quarter)
print('Вторая четверть: ', second_quarter)
print('Третья четверть: ', third_quarter)
print('Четвертая четверть: ', fourth_quarter)



# На вход программе подается строка текста из натуральных чисел. Из неё формируется список
# чисел. Напишите программу подсчета количества чисел, которые больше предшествующего им в
# этом списке числа, то есть, стоят вслед за меньшим числом. 

# Формат входных данных
# На вход программе подается строка текста из разделенных пробелами натуральных чисел.

# Формат выходных данных
# Программа должна вывести одно число – количество элементов списка, больших предыдущего.

numbers = input().split()
counter = 0
for i in range(1, len(numbers)):
    if int(numbers[i]) > int(numbers[i-1]):
        counter += 1
print(counter)



#На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется
# список чисел. Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1],
# a[2] c a[3] и т.д.). Если в списке нечетное количество элементов, то последний остается на своем
# месте.

# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

# Формат выходных данных
# Программа должна вывести измененный список, разделяя его элементы одним пробелом.

numbers = input().split()
num_list = []
if len(numbers) % 2 != 0:
    for i in range(1, len(numbers), 2):
        num_list.append(numbers[i])
        num_list.append(numbers[i-1])
    num_list.append(numbers[-1])
elif len(numbers) % 2 == 0:
    for i in range(1, len(numbers), 2):
        num_list.append(numbers[i])
        num_list.append(numbers[i-1])
print(' '.join(num_list))



# На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется
# список чисел. Напишите программу циклического сдвига элементов списка направо, когда последний
# элемент становится первым, а остальные сдвигаются на одну позицию вперед, в сторону увеличения
# индексов.

# Формат входных данных
# На вход программе подается строка текста из разделенных пробелами натуральных чисел.

# Формат выходных данных
# Программа должна вывести элементы измененного списка с циклическим сдвигом, разделяя его элементы
# одним пробелом.

numbers = input().split()
numbers.insert(0, numbers[-1])
numbers.pop(-1)
print(' '.join(numbers))



# На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию.
# Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в
# списке.

# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела,
# расположенные по неубыванию.

# Формат выходных данных
# Программа должна вывести одно число – количество различных элементов списка.

# Примечание. Задачу можно решить без множеств.

numbers = input().split()
count_element = 1
for i in range(1, len(numbers)):
    if int(numbers[i]) == int(numbers[i-1]):
        continue
    count_element += 1
print(count_element)



