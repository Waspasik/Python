# Функция calculate_it()
# Реализуйте функцию calculate_it(), которая принимает один или более аргументов
# в следующем порядке:

# func — произвольная функция
# *args — переменное количество позиционных аргументов, каждый из которых является
# произвольным объектом

# Функция должна возвращать кортеж, первым элементом которого является возвращаемое
# значение функции func при вызове с аргументами *args, а вторым — примерное время
# (в секундах), затраченное на вычисление этого значения.

# Примечание 1. Например, если функция add() определена так:

# def add(a, b, c):
#     time.sleep(3)
#     return a + b + c

# то вызов

# calculate_it(add, 1, 2, 3)

# должен вернуть кортеж (6, 3.000720262527466), где 6 — результат вызова add(1, 2, 3),
# а 3.000720262527466 — примерное время работы функции add() в секундах.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию calculate_it(), но не код, вызывающий ее.

from time import*


def calculate_it(func, *args):
    start_time = monotonic()
    result = func(*args)
    end_time = monotonic()
    elapsed_time = end_time - start_time

    return result, elapsed_time



# Функция get_the_fastest_func()
# Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в
# следующем порядке:

# funcs — список произвольных функций
# arg — произвольный объект

# Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая
# затратила на вычисление значения при вызове с аргументом arg наименьшее количество
# времени.

# Примечание. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию get_the_fastest_func(), но не код, вызывающий ее.

from time import*


def get_the_fastest_func(funcs, arg):
    min_time = 100
    fastest_func = ''

    for func in funcs:
        start_time = monotonic()
        func(arg)
        end_time = monotonic()
        elapsed_time = end_time - start_time
        if elapsed_time < min_time:
            min_time = elapsed_time
            fastest_func = func

    return fastest_func



# Вам доступны три реализации функции, которая вычисляет факториал числа n:

# встроенная из модуля math
# рекурсивная
# итеративная

# Выясните, какая функция быстрее вычислит факториал числа 900.

from time import*
from math import factorial    


def factorial_modul_math(n):                 # функция из модуля math 
    return factorial(n)


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)    


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def get_the_fastest_func(funcs, arg):
    min_time = 100
    fastest_func = ''

    for func in funcs:
        start_time = monotonic()
        func(arg)
        end_time = monotonic()
        elapsed_time = end_time - start_time
        if elapsed_time < min_time:
            min_time = elapsed_time
            fastest_func = func

    return fastest_func


funcs = [factorial_modul_math, factorial_recurrent, factorial_classic]
print(get_the_fastest_func(funcs, 900))



# Вам доступны две реализации функции, которая создает и возвращает список из
# чисел от 1 до 10 000 000 включительно:

# с использованием цикла for и метода append()
# с использованием списочного выражения

# Определите, какая функция быстрее создаст и вернет требуемый список.

from time import*    


def for_and_append():                            # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result
        

def list_comprehension():                        # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)] 


def get_the_fastest_func(funcs):
    min_time = 100
    fastest_func = ''

    for func in funcs:
        start_time = monotonic()
        func()
        end_time = monotonic()
        elapsed_time = end_time - start_time

        if elapsed_time < min_time:
            min_time = elapsed_time
            fastest_func = func
            
    return fastest_func


funcs = [for_and_append, list_comprehension]
print(get_the_fastest_func(funcs))