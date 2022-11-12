# Функция tabulate()
# Реализуйте функцию tabulate(), которая принимает один аргумент:

# func — произвольная функция

# Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность
# возвращаемых значений функции func сначала с аргументом 1, затем 2, затем 3, и так далее.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию
# tabulate(), но не код, вызывающий ее.

from itertools import count


def tabulate(func):
    yield from map(func, count(1))



# Функция factorials()
# Реализуйте функцию factorials() с использованием функции accumulate(), которая принимает
# один аргумент:

# n — натуральное число

# Функция должна возвращать итератор, генерирующий последовательность из n чисел, каждое из
# которых является факториалом очередного натурального числа.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию
# factorials(), но не код, вызывающий ее.

from itertools import accumulate
import operator


def factorials(n):
    yield from accumulate(range(1,n+1), operator.mul)



# Функция alnum_sequence()
# Реализуйте функцию alnum_sequence(), которая не принимает никаких аргументов.

# Функция должна возвращать итератор, циклично генерирующий бесконечную последовательность
# натуральных чисел и заглавных латинских букв:
# 1, A, 2, B, 3, C, .., X, 25, Y, 26, Z

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию
# alnum_sequence(), но не код, вызывающий ее.

from itertools import count, cycle
from string import ascii_uppercase


def alnum_sequence():
    for couple_items in zip(cycle(range(1, len(ascii_uppercase)+1)), cycle(ascii_uppercase)):
        for item in couple_items:
            yield item



# Функция roundrobin() 🌶️
# Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных
# аргументов, каждый из которых является итерируемым объектом.

# Функция должна возвращать итератор, генерирующий последовательность из элементов всех
# переданных итерируемых объектов: сначала первый элемент первого итерируемого объекта,
# затем первый элемент второго итерируемого объекта, и так далее; после второй элемент
# первого итерируемого объекта, затем второй элемент второго итерируемого объекта, и так
# далее.

# Примечание 1. Элементы итерируемых объектов в возвращаемом функцией итераторе должны
# располагаться в своем исходном порядке.

# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является
# множеством.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию
# roundrobin(), но не код, вызывающий ее.

from itertools import zip_longest


def roundrobin(*args):
    wrapper_args = [[item for item in elem] for elem in args]
    zip_args = zip_longest(*wrapper_args, fillvalue='')
    for elem in zip_args:
        for item in elem:
            if item == '':
                continue
            else:
                yield item



# Функция drop_while_negative()
# Реализуйте функцию drop_while_negative(), которая принимает один аргумент:

# iterable — итерируемый объект, элементами которого являются целые числа

# Функция должна возвращать итератор, генерирующий все числа итерируемого объекта
# iterable, начиная с первого неотрицательного числа.

# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны
# располагаться в своем исходном порядке.

# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не
# является множеством.

# римечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию drop_while_negative(), но не код, вызывающий ее.

from itertools import dropwhile


def drop_while_negative(iterable):
    return dropwhile(lambda x: x < 0, iterable)



# Функция drop_this()
# Реализуйте функцию drop_this(), которая принимает два аргумента в следующем порядке:

# iterable — итерируемый объект
# obj — произвольный объект

# Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого
# объекта iterable, начиная с элемента, не равного obj.

# Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны
# располагаться в своем исходном порядке.

# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является
# множеством.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию drop_this(), но не код, вызывающий ее.

from itertools import dropwhile


def drop_this(iterable, obj):
    return dropwhile(lambda x: x == obj, iterable)



# Функция first_true()
# Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:

# iterable — итерируемый объект
# predicate — функция-предикат; если имеет значение None, то работает аналогично функции
# bool()

# Функция first_true() должна возвращать первый по счету элемент итерируемого объекта
# iterable, для которого функция predicate вернула значение True. Если такого элемента нет,
# функция first_true() должна вернуть значение None.

# Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от
# переданного в качестве аргумента значения.

# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является
# множеством.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию first_true(), но не код, вызывающий ее.

from itertools import dropwhile

def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool
    return next(dropwhile(lambda elem: not predicate(elem), iterable), None)



# Функция take()
# Реализуйте функцию take(), которая принимает два аргумента в следующем порядке:

# iterable — итерируемый объект
# n — натуральное число

# Функция должна возвращать итератор, генерирующей последовательность из первых n элементов
# итерируемого объекта iterable.

# римечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны
# располагаться в своем исходном порядке.

# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является
# множеством.

# римечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию take(), но не код, вызывающий ее.

from itertools import islice


def take(iterable, n):
    return islice(iterable, n)



# Функция take_nth()
# Реализуйте функцию take_nth(), которая принимает два аргумента в следующем порядке:

# iterable — итерируемый объект
# n — натуральное число

# Функция должна возвращать n-ый по счету элемент итерируемого объекта iterable. Если
# итерируемый объект iterable содержит менее n элементов, функция должна вернуть значение
# None.

# Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является
# множеством.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию take_nth(), но не код, вызывающий ее.

from itertools import islice


def take_nth(iterable, n):
    return next(islice(iterable, n-1, n), None)



# Функция first_largest()
# Реализуйте функцию first_largest(), которая принимает два аргумента в следующем порядке:

# terable — итерируемый объект, элементами которого являются целые числа
# number — произвольное число

# Функция должна возвращать индекс первого элемента итерируемого объекта iterable, который
# больше number. Если таких элементов нет, функция должна вернуть число -1.

# Примечание 1. Рассмотрим список чисел 10, 2, 14, 7, 7, 18, 20 из первого теста. Первым
# числом, превосходящим 1, является число 14, которое имеет индекс 2.

# Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является
# множеством.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию first_largest(), но не код, вызывающий ее.

from itertools import dropwhile


def first_largest(iterable, number):
    return next(dropwhile(lambda x: x[1] < number, enumerate(iterable)), [-1])[0]