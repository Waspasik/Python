# Функция cubes_of_odds()
# Вам доступна генераторная функция cubes_of_odds(), принимающая в качестве аргумента
# итерируемый объект, элементами которого являются целые числа, и возвращающая генератор,
# порождающий последовательность нечетных чисел переданного итерируемого объекта,
# возведенных в третью степень.

# Перепишите данную функцию с использованием генераторного выражения, чтобы она выполняла
# ту же задачу.

# Примечание 1. Если генераторное выражение становится достаточно большим, его можно
# записать в виде нескольких строк.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию cubes_of_odds(), но не код, вызывающий ее.

def cubes_of_odds(iterable):
    return (num**3 for num in iterable if num % 2 != 0)



# Функция is_prime()
# Реализуйте генераторную функцию is_prime() с использованием генераторных выражений,
# которая принимает один аргумент:

# number — натуральное число

# Функция должна возвращать True, если число number является простым, или False в противном
# случае.

# Примечание 1. Простое число — натуральное число, имеющее ровно два различных натуральных
# делителя — единицу и самого себя.

# Примечание 2. В задаче удобно воспользоваться функциями all() или any(). 

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию is_prime(), но не код, вызывающий ее.

def is_prime(number):
    if number == 1 or any(number % divider == 0 for divider in range(2, number // 2)):
        return False
    else:
        return True



# Функция count_iterable()
# Реализуйте функцию count_iterable() с использованием генераторных выражений,
# которая принимает один аргумент:

# iterable — итерируемый объект

# Функция должна возвращать единственное число — количество элементов итерируемого
# объекта iterable.

# Примечание 1. Гарантируется, что передаваемый в функцию итерируемый объект является
# конечным.

# римечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию count_iterable(), но не код, вызывающий ее.

def count_iterable(iterable):
    return sum(1 for _ in iterable)



# Функция all_together()
# Реализуйте генераторную функцию all_together() с использованием генераторных выражений,
# которая принимает произвольное количество позиционных аргументов, каждый из которых
# является итерируемым объектом.

# Функция должна возвращать генератор, порождающий каждый элемент всех переданных
# итерируемых объектов: сначала все элементы первого итерируемого объекта, затем
# второго, и так далее.

# Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не
# является множеством.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию all_together(), но не код, вызывающий ее.

def all_together(*args):
    return (item for arg in args for item in arg)



# Функция interleave()
# Реализуйте генераторную функцию interleave() с использованием генераторных выражений,
# которая принимает произвольное количество позиционных аргументов, каждый из которых
# является последовательностью.

# Функция должна возвращать генератор, порождающий каждый элемент всех переданных
# последовательностей: сначала первый элемент первой последовательности, затем первый
# элемент второй последовательности, и так далее; после второй элемент первой
# последовательности, затем второй элемент второй последовательности, и так далее.

# римечание 1. Последовательностью является коллекция, поддерживающая индексацию и
# имеющая длину. Например, объекты типа list, str, tuple являются последовательностями.

# Примечание 2. Гарантируется, что все последовательности, передаваемые в функцию, имеют
# равные длины.

# Примечание 3. Гарантируется, что в функцию всегда подается хотя бы одна последовательность.

# Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию interleave(), но не код, вызывающий ее.

def interleave(*args):
    return (item for arg in zip(*args) for item in arg)