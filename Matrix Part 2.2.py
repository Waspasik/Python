# Симметричная матрица
# Напишите программу, которая проверяет симметричность квадратной матрицы относительно
# главной диагонали.

# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести YES, если матрица симметрична относительно главной диагонали,
# и слово NO в противном случае.

n = int(input())
matrix_main = [input().split() for _ in range(n)]
matrix_transp = []
temp = []
for i in range(n):
    for j in range(n):
        temp.append(matrix_main[j][i])
    matrix_transp.append(temp)
    temp = []
if matrix_transp == matrix_main:
    print('YES')
else:
    print('NO')



# Обмен диагоналей
# Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы,
# стоящие на главной и побочной диагонали, при этом каждый элемент должен остаться в том
# же столбце (то есть в каждом столбце нужно поменять местами элемент на главной диагонали
# и на побочной диагонали).

# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести матрицу с элементами главной и побочной диагонали, поменявшимися
# своими местами.

n = int(input())
matrix = [input().split() for _ in range(n)]
for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
[print(*matrix[j]) for j in range(n)]



# Зеркальное отображение
# Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы
# относительно горизонтальной оси симметрии.

# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести матрицу в которой зеркально отображены элементы относительно
# горизонтальной оси симметрии.

n = int(input())
matrix = [input().split() for _ in range(n)]
for i in range(n // 2):
    for j in range(n):
        matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
[print(*matrix[l]) for l in range(n)]



# Поворот матрицы
# Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.

# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел.

# Формат выходных данных
# Программа должна вывести результат на экран, числа должны быть разделены одним пробелом.

n = int(input())
matrix = [input().split() for _ in range(n)]
new_matrix = []
temp = []
for i in range(n):
    for j in range(n - 1, -1, -1):
        temp.append(matrix[j][i])
    new_matrix.append(temp)
    temp = []
[print(*new_matrix[l]) for l in range(n)]



# Ходы коня
# На шахматной доске 8 × 8 стоит конь. Напишите программу, которая отмечает положение коня на
# доске и все клетки, которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N,
# клетки, которые бьет конь, отметьте символами *, остальные клетки заполните точками.

# Формат входных данных
# На вход программе подаются координаты коня на шахматной доске в шахматной нотации (то есть в
# виде e4, где сначала записывается номер столбца (буква от a до h, слева направо), затем номеру
# строки (цифра от 1 до 8, снизу вверх)).

# Формат выходных данных
# Программа должна вывести на экран изображение доски, разделяя элементы пробелами.

position, eng_alphabet, numbers = input(), 'abcdefgh', '12345678'
matrix = [['.' for _ in range(8)] for _ in range(8)]
rows, cols = 8 - int(position[1]), eng_alphabet.index(position[0])
matrix[rows][cols] = 'N'
for l in range(8):
    for k in range(8):
        p = (rows - k) * (cols - l)
        if p == 2 or p == -2:
            matrix[k][l] = '*'
for r in range(8):
    for c in range(8):
        print(str(matrix[r][c]).ljust(2), end='')
    print()
