# Функция get_digits()
# Реализуйте функцию get_digits() c использованием аннотаций типов, которая принимает
# один аргумент:

# number — положительное целое или вещественное число

# Функция должна возвращать список, состоящий из цифр числа number.

# Примечание 1. Порядок следования цифр в списке должен совпадать с порядком следования
#их в исходном числе.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию get_digits(), но не код, вызывающий ее.

def get_digits(number: int | float) -> list[int]:
    return [int(num) for num in filter(lambda x: x.isdigit(), str(number))]


print(get_digits(13.909934))



# Функция top_grade()
# Реализуйте функцию top_grade() c использованием аннотаций типов, которая принимает
# один аргумент:

# grades — словарь, содержащий данные об ученике, а именно имя по ключу name и список
# оценок по ключу grades

# Функция должна возвращать словарь, содержащий имя ученика по ключу name и его самую
# высокую оценку по ключу top_grade.

# Примечание 1. В возвращаемом функцией словаре сначала должно следовать имя, а затем
# — самая высокая оценка.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию top_grade(), но не код, вызывающий ее.

def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {'name': grades['name'], 'top_grade': max(grades['grades'])}


print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))



# Функция cyclic_shift()
# Реализуйте функцию cyclic_shift() с использованием аннотаций типов, которая
# принимает два аргумента в следующем порядке:

# numbers — список целых или вещественных чисел
# step — целое число

# Функция должна изменять переданный список, циклически сдвигая элементы списка на
# step шагов, и возвращать значение None. Если step является положительным числом,
# сдвиг происходит вправо, если отрицательным — влево.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию cyclic_shift(), но не код, вызывающий ее.

def cyclic_shift(numbers: list[int | float], step: int) -> None:
    if step < 0:
        for i in range(abs(step)):
            numbers.append(numbers.pop(0))
    else:
        for i in range(step):
            numbers.insert(0, numbers.pop())


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers)



# Функция matrix_to_dict()
# Реализуйте функцию matrix_to_dict() с использованием аннотаций типов, которая
# принимает один аргумент:

# matrix — матрица произвольной размерности, элементами которой являются целые
# или вещественные числа

# Функция должна возвращать словарь, ключом в котором является номер строки матрицы,
# а значением — список элементов этой строки.

# Примечание 1. Нумерация строк матрицы в возвращаемом функцией словаре должна начинаться
# с единицы.

# Примечание 2. Элементы матрицы в списке должны располагаться в своем исходном порядке.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию matrix_to_dict(), но не код, вызывающий ее.

def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    for index, row in enumerate(matrix, 0):
        print(row, index)


matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict(matrix))