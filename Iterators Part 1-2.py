# Вам доступен список numbers, содержащий целые числа. Дополните приведенный ниже
# код с использованием функций iter() и next(), чтобы он вывел последний элемент
# данного списка.

numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64,
           -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]

iter_numbers = iter(numbers)

for _ in range(len(numbers)-1):
    next(iter_numbers)

print(next(iter_numbers))



# Функция filterfalse()
# Реализуйте функцию filterfalse() с использованием функции filter(), которая принимает
# два аргумента:

# predicate — функция-предикат; если имеет значение None, то работает аналогично функции
# bool()
# iterable — итерируемый объект

# Функция должна работать противоположно функции filter(), то есть возвращать итератор,
# элементами которого являются элементы итерируемого объекта iterable, для которых функция
# predicate вернула значение False.

# Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости
# от переданного в качестве аргумента значения.

# Примечание 2. Элементы итерируемого объекта в возвращаемом функцией итераторе должны
# располагаться в своем исходном порядке.

# Примечание 3. Гарантируется, что итерируемый объект, передаваемый в функцию, не является
# множеством.

# Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию filterfalse(), но не код, вызывающий ее.

def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    return filter(lambda elem: not predicate(elem), iterable)



# Функция transpose()
# Реализуйте функцию transpose() с использованием функции zip(), которая принимает один
# аргумент:

# matrix — матрица произвольной размерности

# Функция должна возвращать транспонированную матрицу matrix.

# Примечание 1. Под матрицей подразумеваются исключительно вложенные списки.

# Примечание 2. Функция должна возвращать новую матрицу, а не изменять переданную.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию transpose(), но не код, вызывающий ее.

def transpose(matrix):
    return list(map(list, zip(*matrix)))



# Функция get_min_max() 😎
# Реализуйте функцию get_min_max() c использованием функции enumerate(), которая принимает
# один аргумент:

# data — список произвольных объектов, сравнимых между собой

# Функция должна возвращать кортеж, в котором первым элементом является индекс минимального
# элемента в списке data, вторым — индекс максимального элемента в списке data. Если список
# data пуст, функция должна вернуть значение None.

# Примечание 1. Если минимальных / максимальных элементов несколько, следует вернуть индексы
# первого по порядку элемента.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию get_min_max(), но не код, вызывающий ее.

def get_min_max(data):
    if data:
        enumerate_data_tuple = tuple(enumerate(data))
        min_elem = min(enumerate_data_tuple, key=lambda elem: elem[1])[0]
        max_elem = max(enumerate_data_tuple, key=lambda elem: elem[1])[0]
        return min_elem, max_elem



# Функция get_min_max() 😳
# Реализуйте функцию get_min_max(), которая принимает один аргумент:

# iterable — итерируемый объект, элементы которого сравнимы между собой

# Функция должна возвращать кортеж, в котором первым элементом является минимальный
# элемент итерируемого объекта iterable, вторым — максимальный элемент итерируемого
# объекта iterable. Если итерируемый объект iterable пуст, функция должна вернуть
# значение None.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию get_min_max(), но не код, вызывающий ее.

def get_min_max(iterable):
    if hasattr(iterable, '__next__'):
        try:
            min_value = max_value = next(iterable)
            for item in iterable:
                if item > max_value:
                    max_value = item
                if item < min_value:
                    min_value = item
            return min_value, max_value
        except StopIteration:
            return  
    else:    
        iterable_list = list(iterable)
        if iterable_list:
            return min(iterable_list), max(iterable_list)



# Функция starmap()
# Как известно, функция map() принимает функцию и итерируемый объект и возвращает итератор,
# элементами которого являются элементы итерируемого объекта, к которым была применена
# переданная функция. Нередко элементами итерируемого объекта являются коллекции (списки,
# кортежи, ..), тогда внутри переданной функции нам приходится обращаться к каждому элементу
# этих коллекций по индексу. Например:

# persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]

# full_names = map(lambda tup: tup[0] + ' ' + tup[1], persons)

# Было бы удобно иметь функцию, назовем ее starmap(), которая бы принимала функцию не с одним
# аргументом, а с несколькими — каждым элементом коллекции:

# persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]

# full_names = starmap(lambda name, surname: f'{name} {surname}', persons)

# Реализуйте функцию starmap() с использованием функции map(), которая принимает два аргумента:

# func — функция
# iterable — итерируемый объект, элементами которого являются коллекции

# Функция starmap() должна работать аналогично функции map(), то есть возвращать итератор,
# элементами которого являются элементы итерируемого объекта iterable, к которым была применена
# функция func, с единственным отличием: func должна принимать не один аргумент — коллекцию
# (элемент iterable), а каждый элемент этой коллекции в качестве самостоятельного аргумента.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию
# starmap(), но не код, вызывающий ее.

def starmap(func, iterable):
    return map(func, *zip(*iterable))