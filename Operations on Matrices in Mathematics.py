# Сложение матриц
# Напишите программу для вычисления суммы двух матриц.

# Формат входных данных
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в
# матрицах, затем элементы первой матрицы, затем пустая строка, далее следуют элементы
# второй матрицы.

# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

numbers = input().split()
n, m = int(numbers[0]), int(numbers[1])

matrix_A = [[int(i) for i in input().split()] for _ in range(n)]
input()
matrix_B = [[int(i) for i in input().split()] for _ in range(n)]
matrix_C = [[matrix_A[i][j] + matrix_B[i][j] for j in range(m)] for i in range(n)]

for row in matrix_C:
    print(*row)



# Умножение матриц 🌶️
# Напишите программу, которая перемножает две матрицы.

# Формат входных данных
# На вход программе подаются два натуральных числа n и m — количество строк и столбцов в
# первой матрице, затем элементы первой матрицы, затем пустая строка. Далее следуют числа
# m и k — количество строк и столбцов второй матрицы затем элементы второй матрицы.

# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

numbers_A = input().split()
n, m = int(numbers_A[0]), int(numbers_A[1])
matrix_A = [[int(i) for i in input().split()] for _ in range(n)]
input()
numbers_B = input().split()
m, k = int(numbers_B[0]), int(numbers_B[1])
matrix_B = [[int(i) for i in input().split()] for _ in range(m)]

matrix_C = []
temp = []
row = []

for i in range(n):
    for j in range(k):
        for l in range(m):
            temp.append(matrix_A[i][l] * matrix_B[l][j])
        row.append(sum(temp))
        temp = []
    matrix_C.append(row)
    row = []

for row in matrix_C:
    print(*row)



# Возведение матрицы в степень 🌶️
# Напишите программу, которая возводит квадратную матрицу в m-ую степень.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы, затем натуральное число m.

# Формат выходных данных
# Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.

from copy import*

n = int(input())
matrix_A = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())

matrix_X = deepcopy(matrix_A)
counter = 0

while counter != m - 1:
    matrix_B = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for l in range(n):
                matrix_B[i][j] += matrix_X[i][l] * matrix_A[l][j]
    matrix_A = matrix_B
    counter += 1

for row in matrix_A:
    print(*row)