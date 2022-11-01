# Декоратор sandwich
# Реализуйте декоратор sandwich, который выводит тексты:

# ---- Верхний ломтик хлеба ----
# ---- Нижний ломтик хлеба ----

# до и после вызова декорируемый функции соответственно.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый
# декоратор sandwich, но не код, вызывающий его.

def sandwich(func):
    print('---- Верхний ломтик хлеба ----')
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return result
    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))

add_ingredients(['томат', 'салат', 'сыр', 'бекон'])



# Новый print
# Напишите программу с использованием декоратора, которая переопределяет функцию print()
# так, чтобы она печатала весь текст в верхнем регистре.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна задекорировать функцию print() так, чтобы она печатала весь текст в
# верхнем регистре.

# Примечание 1. Значения sep и end также должны переводиться в верхний регистр.

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        args = tuple(map(lambda elem: elem.upper() if isinstance(elem, str) else elem, args))
        kwargs = {key: value.upper() for key, value in kwargs.items()}
        func(*args, **kwargs)
    return wrapper


print = uppercase_decorator(print)
print(111, 222, 333, sep='xxx')



# Декоратор do_twice
# Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.

def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@do_twice
def beegeek():
    print('beegeek')
    
beegeek()



# Декоратор reverse_args
# Реализуйте декоратор reverse_args, который передает все позиционные аргументы в
# декорируемую функцию func в обратном порядке.

def reverse_args(func):
    def wrapper(*args, **kwargs):
        args = args[::-1]
        return func(*args, **kwargs)
    return wrapper


@reverse_args
def power(a, n):
    return a ** n
    
print(power(2, 3))



# Декоратор exception_decorator
# Реализуйте декоратор exception_decorator, который возвращает

# кортеж (value, 'Функция выполнилась без ошибок'), если декорируемая функция завершила
# свою работу без ошибок, где value — возвращаемое значение декорируемой функции
# кортеж (None, 'При вызове функции произошла ошибка'), если при выполнении декорируемой
# функции возникла ошибка

def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), 'Функция выполнилась без ошибок'
        except Exception:
            return None, 'При вызове функции произошла ошибка'
    return wrapper


@exception_decorator
def f(x):
    return x**2 + 2*x + 1
    
print(f(7))



# Декоратор takes_positive
# Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые
# в декорируемую функцию, являются положительными целыми числами.

# Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать
# исключение:

# TypeError, если аргумент не является целым числом
# ValueError, если аргумент является целым числом, но отрицательным или равным нулю

# Примечание 1. Приоритет возбуждения исключений при несоответствии аргумента обоим условиям
# или при наличии разных аргументов, несоответствующих разным условиям: TypeError, затем
# ValueError

def takes_positive(func):
    def wrapper(*args, **kwargs):
        if any(not isinstance(num, int) for num in (*args, *kwargs.values())):
            raise TypeError
        if any(isinstance(num, int) and num <= 0 for num in (*args, *kwargs.values())):
            raise ValueError
        else:
            return func(*args, **kwargs)
    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)
    
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))