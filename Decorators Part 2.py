# Декоратор square
# Реализуйте декоратор square, который возводит возвращаемое значение декорируемой
# функции во вторую степень. 

# акже декоратор должен сохранять имя и строку документации декорируемой функции.

# Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции
# является объект типа int или float.

import functools


def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result**2
    return wrapper


@square
def add(a, b):
    '''прекрасная функция'''
    return a + b

print(add(1, 1))
print(add.__name__)
print(add.__doc__)



# Декоратор returns_string
# Реализуйте декоратор returns_string, который проверяет, что возвращаемое значение
# декорируемой функции принадлежит типу str. Если возвращаемое значение принадлежит
# какому-либо другому типу, декоратор должен возбуждать исключение TypeError.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

import functools


def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        test_string = func(*args, **kwargs)
        if not isinstance(test_string, str):
            raise TypeError
        else:
            return test_string
    return wrapper


@returns_string
def beegeek():
    return 'beegeek'
    
print(beegeek())



# Декоратор trace
# Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой
# функции во время ее выполнения, а именно: имя функции, переданные аргументы и
# возвращаемое значение в следующем формате:

# TRACE: вызов <имя функции> с аргументами: <кортеж позиционных аргументов>, <словарь
# именованных аргументов>
# TRACE: возвращаемое значение <имя функции>: <возвращаемое значение>

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        print(f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}")
        print(f"TRACE: возвращаемое значение {func.__name__}(): {repr(func_result)}")
        return func_result
    return wrapper


@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c
    
print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)



# Декоратор prefix
# Реализуйте декоратор prefix, который принимает два аргумента в следующем порядке:

# string — произвольная строка
# to_the_end — булево значение, по умолчанию равное False

# Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции.
# Если to_the_end имеет значение True, строка string добавляется в конец, если False — в
# начало.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является
# объект типа str.

import functools


def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            input_string = func(*args, **kwargs)
            return input_string + string if to_the_end else string + input_string
        return wrapper
    return decorator


@prefix('€')
def get_bonus():
    return '2000'
    
print(get_bonus())



# екоратор make_html
# Тег — элемент языка разметки, используемый для форматирования текста. Например, текст,
# заключённый между начальным тегом <small> и конечным тегом </small>, отображается с
# меньшим размером, чем основной текст, а текст между тегами <big> и </big> отображается
# с большим размером.

# Реализуйте декоратор make_html(), который принимает один аргумент:

# tag — HTML-тег, например, del

# Декоратор должен обрамлять возвращаемое значение декорируемой функции в HTML-тег tag.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является
# объект типа str.

import functools


def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            input_text = func(*args, **kwargs)
            return f'<{tag}>{input_text}</{tag}>'
        return wrapper
    return decorator


@make_html('i')
@make_html('del')
def get_text(text):
    return text
    
print(get_text(text='decorators are so cool!'))



# Декоратор repeat
# Реализуйте декоратор repeat, который принимает один аргумент:

# times — натуральное число

# Декоратор должен вызывать декорируемую функцию times раз.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator


@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')
    
say_beegeek()



# Декоратор strip_range
# Реализуйте декоратор strip_range, который принимает три аргумента в следующем порядке:

# start — неотрицательное целое число
# end — неотрицательное целое число
# char — одиночный символ, по умолчанию равный точке .

# Декоратор должен изменять возвращаемое значение декорируемой функции, заменяя все
# символы в диапазоне индексов от start (включительно) до end (не включительно) на символ
# char.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является
# объект типа str.

# Примечание 2. Гарантируется, что start < end.

import functools


def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = [ch for ch in func(*args, **kwargs)]
            try:
                for i in range(start, end):
                    value[i] = char
            except IndexError:
                return ''.join(value)
            return ''.join(value)
        return wrapper
    return decorator


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'
    
print(beegeek())



# Декоратор returns
# Реализуйте декоратор returns, который принимает один аргумент:

# datatype — тип данных

# Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит
# типу datatype. Если возвращаемое значение принадлежит какому-либо другому типу, декоратор
# должен возбуждать исключение TypeError.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

import functools


def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if isinstance(value, datatype):
                return value
            else:
                raise TypeError
        return wrapper
    return decorator


@returns(list)
def beegeek():
    '''beegeek docs'''
    return 'beegeek'

print(beegeek.__name__)
print(beegeek.__doc__)

try:
    print(beegeek())
except TypeError as e:
    print(type(e))



# Декоратор takes
# Реализуйте декоратор takes, который принимает произвольное количество позиционных
# аргументов, каждый из которых является типом данных.

# Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию,
# принадлежат одному из этих типов. Если хотя бы один аргумент не принадлежит одному
# из данных типов, декоратор должен возбуждать исключение TypeError.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

import functools


def takes(*bools_args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if any(type(arg) not in bools_args for arg in (*args, *kwargs.values())):
                raise TypeError
            else:
                return value
        return wrapper
    return decorator


@takes(list, int, tuple, str)
def add(a, b):
    '''add docs'''
    return a + b

print(add.__name__)
print(add.__doc__)

try:
    print(add(1, b=2))
except TypeError as e:
    print(type(e))



# Декоратор add_attrs
# Реализуйте декоратор add_attrs, который принимает произвольное количество именованных
# аргументов и устанавливает их в качестве атрибутов декорируемой функции. Названием
# атрибута должно являться имя аргумента, значением атрибута — значение аргумента.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

import functools


def add_attrs(**attrs_kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return value
        for key, value in attrs_kwargs.items():
            wrapper.__dict__[key] = value
        return wrapper
    return decorator


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'
    
print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)



# Декоратор ignore_exception
# Реализуйте декоратор ignore_exception, который принимает произвольное количество
# позиционных аргументов — типов исключений, и выводит текст:

# Исключение <тип исключения> обработано
# если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее
# одному из переданных типов.

# Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно
# быть возбуждено снова.

# Также декоратор должен сохранять имя и строку документации декорируемой функции.

# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое
# значение декорируемой функции, а также должен уметь декорировать функции с произвольным
# количеством позиционных и именованных аргументов.

import functools


def ignore_exception(*exceptions_args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                if type(err) in exceptions_args:
                    print(f'Исключение {type(err).__name__} обработано')
                else:
                    raise
        return wrapper
    return decorator


@ignore_exception(ValueError, TypeError, NameError)
def func():
    '''func docs'''
    raise ValueError
 
print(func.__name__)
print(func.__doc__)
