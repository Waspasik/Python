# Дополните приведенный ниже код, чтобы в переменной infinite_love содержался итератор,
# бесконечно генерирующий единственное значение — строку i love beegeek!.

# Примечание. В тестирующую систему сдайте программу, содержащую только необходимый
# итератор infinite_love.

infinite_love = iter(lambda x='i love beegeek!': x, '')



# Функция is_iterable()
# Реализуйте функцию is_iterable(), которая принимает один аргумент:

# obj — произвольный объект

# Функция должна возвращать True, если объект obj является итерируемым объектом, или
# False в противном случае.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию is_iterable(), но не код, вызывающий ее.

def is_iterable(obj):
    return hasattr(obj, '__iter__')



# Функция is_iterator()
# Реализуйте функцию is_iterator(), которая принимает один аргумент:

# obj — произвольный объект

# Функция должна возвращать True, если объект obj является итератором, или False в
# противном случае. 

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию is_iterator(), но не код, вызывающий ее.

def is_iterator(obj):
    return hasattr(obj, '__next__')



# Функция random_numbers()
# Реализуйте функцию random_numbers(), которая принимает два аргумента:

# left — целое число
# right — целое число

# Функция должна возвращать итератор, генерирующий бесконечную последовательность
# случайных целых чисел в диапазоне от left до right включительно.

# Примечание 1. Гарантируется, что left <= right.

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый
# итератор random_numbers(), но не код, вызывающий её.

from random import choice


def random_numbers(left, right):
    diapason = list(range(left, right+1))
    return iter(lambda: choice(diapason), '')