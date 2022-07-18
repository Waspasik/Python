# Магический квадрат 🌶️
# Магическим квадратом порядка nn называется квадратная таблица размера n × n, составленная
# из всех чисел 1, 2, 3, ... n^2 так, что суммы по каждому столбцу, каждой строке и каждой
# из двух диагоналей равны между собой. Напишите программу, которая проверяет, является ли
# заданная квадратная матрица магическим квадратом.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы: n строк, по nn чисел в каждой, разделённые пробелами.

# Формат выходных данных
# Программа должна вывести слово YES, если матрица является магическим квадратом, и слово
# NO в противном случае.

n = int(input())
matrix = [input().split() for _ in range(n)]
int_matrix = [[int(num) for num in lst] for lst in matrix]
total = sum(int_matrix[1])
flag = True

def check_all_numbers(matrix):
    flag = True
    numbers = [int(l) for l in range(1, n**2 + 1)]
    matrix = [(int(int_matrix[l][k])) for k in range(n) for l in range(n)]
    for i in range(n**2):
        if numbers[i] in matrix:
            continue
        else:
            flag = False
            return False
    if flag:
        return True

def func_rows(matrix):
    for numbers in matrix:
        if sum(numbers) == total:
            return True
        else:
            return False

def func_cols(matrix):
    flag = True
    for i in range(n):
        cols_sum = 0
        for j in range(n):
            cols_sum += matrix[j][i]
        if cols_sum == total:
            continue
        else:
            flag = False
            break
    if flag:
        return True
    else:
        return False

def func_diagonals(matrix):
    diag_sum1 = 0
    diag_sum2 = 0
    for i in range(n):
        diag_sum1 += matrix[i][i]
        diag_sum2 += matrix[i][n-i-1]
    if diag_sum1 and diag_sum2 == total:
        return True
    else:
        return False

if check_all_numbers(int_matrix) and func_rows(int_matrix) and func_cols(int_matrix) and func_diagonals(int_matrix):
    print('YES')
else:
    print('NO')