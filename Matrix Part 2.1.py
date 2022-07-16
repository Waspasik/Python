# Таблица умножения
# На вход программе подаются два натуральных числа nn и m — количество строк и столбцов в
# матрице. Создайте матрицу mult размером n × m и заполните её таблицей умножения
# по формуле mult[i][j] = i * j.

# Формат входных данных
# На вход программе на разных строках подаются два числа n и m — количество строк и
# столбцов в матрице.

# Формат выходных данных
# Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 3 символа
# (для этого используйте строковый метод ljust()).

n, m = int(input()), int(input())
[print(*[l * k for k in range(m)]) for l in range(n)]



# Максимум в таблице
# На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в
# матрице, затем nn строк по mm целых чисел в каждой, отделенных символом пробела.

# Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального
# элемента.

# Формат входных данных
# На вход программе на разных строках подаются два числа nn и mm — количество строк и столбцов
# в матрице, затем сами элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести два числа: номер строки и номер столбца, в которых стоит наибольший
# элемент таблицы. Если таких элементов несколько, то выводится тот, у которого меньше номер
# строки, а если номера строк равны то тот, у которого меньше номер столбца.

# Примечание. Считайте, что нумерация строк и столбцов начинается с нуля.

n, m = int(input()), int(input())
maximum = -100
index_n, index_m = 0, 0
matrix = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(m):
        if int(matrix[i][j]) > maximum:
            maximum = int(matrix[i][j])
            index_n, index_m = i, j
print(index_n, index_m)



# Обмен столбцов
#Напишите программу, которая меняет местами столбцы в матрице.

# Формат входных данных
# На вход программе на разных строках подаются два натуральных числа n и m — количество строк
# и столбцов в матрице, затем элементы матрицы построчно через пробел, затем числа i и j —
# номера столбцов, подлежащих обмену.

# Формат выходных данных
# Программа должна вывести указанную таблицу с замененными столбцами.

n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]
index = input().split()
for i in range(n):
    matrix[i][int(index[0])], matrix[i][int(index[1])] = matrix[i][int(index[1])], matrix[i][int(index[0])]
[print(*matrix[j]) for j in range(n)]



