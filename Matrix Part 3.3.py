# Заполнение спиралью 😈😈
# На вход программе подаются два натуральных числа n и m. Напишите программу,
# которая создает матрицу размером n × m заполнив её "спиралью" в соответствии
# с образцом.

# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m —
# количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести матрицу в соответствии образцом.

# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3
# символа на каждый элемент. Для этого используйте строковый метод ljust().
# Можно обойтись и без ljust(), система примет и такое решение 😇

n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
r, c, step = 0, 0, 0
location = ((0, 1,), (1, 0,), (0, -1,), (-1, 0,))

for i in range(1, n * m + 1):
    matrix[r][c] = i
    for j in range(4):
        currently_step = (step + j) % 4
        step_r, step_c = location[currently_step]
        currently_r, currently_c = r + step_r, c + step_c
        if 0 <= currently_r < n and 0 <= currently_c < m and matrix[currently_r][currently_c] == 0:
            r, c, step = currently_r, currently_c, currently_step
            break

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()