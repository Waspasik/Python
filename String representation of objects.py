# Класс Book
# Требовалось реализовать класс Book, описывающий книгу. При создании экземпляра класс должен
# был принимать три аргумента в следующем порядке:

# title — название книги
# author — автор книги
# year — год выпуска книги

# Предполагалось, что экземпляры класса Book будут иметь следующее формальное строковое
# представление:

# Book('<название книги>', '<автор книги>', <год выпуска книги>)

# И следующее неформальное строковое представление:

# <название книги> (<автор книги>, <год выпуска книги>)

# Программист торопился и решил задачу неправильно. Исправьте приведенный ниже код и реализуйте
# класс Book правильно.


# before
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book('{title}', '{author}', {year})"

    def __repr__():
        return f'{title} ({author}, {year})'

# after
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} ({self.author}, {self.year})'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"



# Класс Rectangle
# Вам доступен класс Rectangle, описывающий прямоугольник. При создании экземпляра класс принимает
# два аргумента в следующем порядке:

# length — длина прямоугольника
# width — ширина прямоугольника

# Реализуйте для экземпляров класса Rectangle следующее формальное и неформальное строковое
# представление:

# Rectangle(<длина прямоугольника>, <ширина прямоугольника>)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"



# Класс Vector
# Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен
# принимать два аргумента в следующем порядке:

# x — координата вектора по оси x
# y — координата вектора по оси y

# Экземпляр класса Vector должен иметь следующее формальное строковое представление:

# Vector(<координата x>, <координата y>)

# И следующее неформальное строковое представление:

# Вектор на плоскости с координатами (<координата x>, <координата y>)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Вектор на плоскости с координатами ({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"



# Класс IPAddress
# IP-адрес — это уникальный адрес, идентифицирующий устройство в интернете или локальной сети.
# IP-адреса представляют собой набор из четырех целых чисел, разделенных точками. Например,
# 192.158.1.38. Каждое число в наборе принадлежит интервалу от 0 до 255. Таким образом, полный
# диапазон IP-адресации — это адреса от 0.0.0.0 до 255.255.255.255.

# Реализуйте класс IPAddress, описывающий IP-адрес. При создании экземпляра класс должен принимать
# один аргумент:

# ipaddress — IP-адрес, представленный в одном из следующих вариантов:

# строка из четырех целых чисел, разделенных точками
# список или кортеж из четырех целых чисел

# Экземпляр класса IPAddress должен иметь следующее формальное строковое представление:

# IPAddress('<IP-адрес в виде четырех целых чисел, разделенных точками>')

# И следующее неформальное строковое представление:

# <IP-адрес в виде четырех целых чисел, разделенных точками>

from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        raise TypeError('Аргумент переданного типа не поддерживается')
        
    @__init__.register(str)
    def _from_str(self, ipaddress):
        self.ipaddress = ipaddress
    
    @__init__.register(list)
    @__init__.register(tuple)
    def _from_list_tuple(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))
    
    def __str__(self):
        return self.ipaddress
    
    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"



# Класс PhoneNumber
# Реализуйте класс PhoneNumber, описывающий телефонный номер. При создании экземпляра класс
# должен принимать один аргумент:

# phone_number — телефонный номер, представляющий строку из десяти цифр в одном из следующих
# форматов:

# dddddddddd
# ddd ddd dddd

# Экземпляр класса PhoneNumber должен иметь следующее формальное строковое представление:

# PhoneNumber('<телефонный номер в формате dddddddddd>')

# И следующее неформальное строковое представление:

# <телефонный номер в формате (ddd) ddd-dddd>

class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = phone_number.replace(' ', '')
    
    def __str__(self) -> str:
        return f"({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6::]}"
    
    def __repr__(self) -> str:
        return f"PhoneNumber('{self.phone_number}')"
