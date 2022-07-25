# Заполнение диагоналями 🌶️
# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает
# матрицу размером n × m заполнив её "диагоналями" в соответствии с образцом.

#   1  2  4  7  10
#   3  5  8  11 13
#   6  9  12 14 15

# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m — количество строк и
# столбцов в матрице.

# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.

# Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 3 символа на каждый
# элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система
# примет и такое решение 😇

numbers = input().split()
n, m = int(numbers[0]), int(numbers[1])
matrix = [[0] * m for _ in range(n)]
counter = 1

for x in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == x:
                matrix[i][j] = counter
                counter += 1

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()