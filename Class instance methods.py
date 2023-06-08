# Класс Gun
# Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен
# принимать никаких аргументов.

# Класс Gun должен иметь один метод экземпляра:

# shoot() — метод, при вызове которого выводится строка pif

class Gun():
    def shoot(self):
        print('pif')



# Класс User
# Вам доступен класс User, описывающий интернет-пользователя. При создании экземпляра
# класс принимает один аргумент:

# name — имя пользователя

# Экземпляр класса User имеет два атрибута:

# name — имя пользователя
# friends — количество друзей пользователя, начальным значением является 0

# Класс User имеет один метод экземпляра:

# add_friends() — метод, принимающий в качестве аргумента целое число n и увеличивающий
# количество друзей пользователя на n

# Найдите и исправьте ошибки, допущенные при реализации метода add_friends().

class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n



# Класс House
# Вам доступен класс House, описывающий дом. При создании экземпляра класс принимает два
# аргумента в следующем порядке:

# color — цвет дома
# rooms — количество комнат в доме

# Экземпляр данного класса имеет два атрибута:

# color — цвет дома
# rooms — количество комнат в доме

# Реализуйте для класса House два метода экземпляра:

# paint() — метод, принимающий в качестве аргумента значение new_color и изменяющий текущий
# цвет дома на new_color
# add_rooms() — метод, принимающий в качестве аргумента целое число n и увеличивающий
# количество комнат в доме на n

class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms
        
    def paint(self, new_color):
        self.color = new_color
    
    def add_rooms(self, n):
        self.rooms += n



# Класс Circle
# Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать
# один аргумент:

# radius — радиус круга

# Экземпляр класса Circle должен иметь три атрибута:

# radius — радиус круга
# diameter — диаметр круга
# area — площадь круга

from math import pi


class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius*2
        self.area = pi * self.radius**2



# Класс Bee
# Реализуйте класс Bee, описывающий пчелку, которая перемещается по координатной плоскости в
# четырех направлениях: вверх, вниз, влево и вправо. При создании экземпляра класс должен
# принимать два аргумента в следующем порядке:

# x — координата пчелки по оси x, по умолчанию имеет значение 0
# y — координата пчелки по оси y, по умолчанию имеет значение 0

# Экземпляр класса Bee должен иметь два атрибута:

# x — координата пчелки по оси x
# y — координата пчелки по оси y

# Класс Bee должен иметь четыре метода экземпляра:

# move_up() — метод, принимающий в качестве аргумента целое число n и увеличивающий координату пчелки по оси y на n
# move_down() — метод, принимающий в качестве аргумента целое число n и уменьшающий координату пчелки по оси y на n
# move_right() — метод, принимающий в качестве аргумента целое число n и увеличивающий координату пчелки по оси x на n
# move_left() — метод, принимающий в качестве аргумента целое число n и уменьшающий координату пчелки по оси x на n

class Bee():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n
    
    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n
    
    def move_left(self, n):
        self.x -= n



# Класс Gun
# Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать
# никаких аргументов.

# Класс Gun должен иметь один метод экземпляра:

# shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при
# третьем — pif, при четвертом — paf, и так далее

class Gun():
    def __init__(self):
        self.counter = 0
    
    def shoot(self):
        print('pif' if self.counter % 2 == 0 else 'paf')
        self.counter += 1



# Класс Gun
# Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать
# никаких аргументов.

# Класс Gun должен иметь три метода экземпляра:

# shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при
# третьем — pif, при четвертом — paf, и так далее
# shots_count() — метод, возвращающий актуальное количество вызовов метода shoot()
# shots_reset() — метод, сбрасывающий количество вызовов метода shoot() до нуля

class Gun():
    def __init__(self):
        self.counter = 0
    
    def shoot(self):
        print('pif' if self.counter % 2 == 0 else 'paf')
        self.counter += 1
    
    def shots_count(self):
        return self.counter

    def shots_reset(self):
        self.counter = 0



# Класс Scales
# Реализуйте класс Scales, описывающий весы с двумя чашами. При создании экземпляра класс не
# должен принимать никаких аргументов.

# Класс Scales должен иметь три метода экземпляра:

# add_right() — метод, принимающий в качестве аргумента массу груза в килограммах и добавляющий
# на правую чашу весов этот груз
# add_left() — метод, принимающий в качестве аргумента массу груза в килограммах и добавляющий
# на левую чашу весов этот груз
# get_result() — метод, возвращающий строку Весы в равновесии, если массы грузов на чашах
# совпадают, Правая чаша тяжелее — если правая чаша тяжелее, Левая чаша тяжелее — если левая
# чаша тяжелее

# Примечание 1. Пустые весы всегда находятся в равновесии.

class Scales():
    def __init__(self):
        self.right_pan = 0
        self.left_pan = 0
    
    def add_right(self, cargo):
        self.right_pan += cargo
        
    def add_left(self, cargo):
        self.left_pan += cargo

    def get_result(self):
        if self.right_pan > self.left_pan:
            return 'Правая чаша тяжелее'
        elif self.right_pan < self.left_pan:
            return 'Левая чаша тяжелее'
        return 'Весы в равновесии'

    
    
# Класс Vector
# Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс
# должен принимать два аргумента в следующем порядке:

# x — координата вектора по оси x, по умолчанию имеет значение 0
# y — координата вектора по оси y, по умолчанию имеет значение 0
# Экземпляр класса Vector должен иметь два атрибута:

# x — координата вектора по оси x
# y — координата вектора по оси y
# Класс Vector должен иметь один метод экземпляра:

# abs() — метод, возвращающий модуль вектора

from math import sqrt


class Vector():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def abs(self):
        return sqrt(self.x**2 + self.y**2)



# Класс Numbers
# Реализуйте класс Numbers, описывающий изначально пустой расширяемый набор целых чисел.
# При создании экземпляра класс не должен принимать никаких аргументов.

# Класс Numbers должен иметь три метода экземпляра:

# add_number() — метод, принимающий в качестве аргумента целое число и добавляющий его в набор
# get_even() — метод, возвращающий список всех четных чисел из набора
# get_odd() — метод, возвращающий список всех нечетных чисел из набора
# Примечание 1. Числа в списках, возвращаемых методами get_even() и get_odd(), должны
# располагаться в том порядке, в котором они были добавлены в набор.

class Numbers():
    def __init__(self):
        self.nums = list()
    
    def add_number(self, num):
        self.nums.append(num)
    
    def get_even(self):
        return list(filter(lambda x: x % 2 == 0, self.nums))
    
    def get_odd(self):
        return list(filter(lambda x: x % 2 != 0, self.nums))



# Класс TextHandler
# Будем называть словом любую последовательность из одной или более букв. Текстом будем считать
# набор слов, разделенных пробелами.

# Реализуйте класс TextHandler, описывающий изначально пустой расширяемый набор слов. При создании
# экземпляра класс не должен принимать никаких аргументов.

# Экземпляр класса TextHandler должен иметь три метода:

# add_words() — метод, принимающий в качестве аргумента текст и добавляющий слова из данного текста
# в набор
# get_shortest_words() — метод, возвращающий актуальный список самых коротких слов в наборе
# get_longest_words() — метод, возвращающий актуальный список самых длинных слов в наборе
# Примечание 1. Слова в списках, возвращаемых методами get_shortest_words() и get_longest_words(),
# должны располагаться в том порядке, в котором они были добавлены в набор.

class TextHandler():
    def __init__(self):
        self.words = list()
        
    def add_words(self, text):
        self.words += text.split()

    def get_shortest_words(self):
        return list(filter(lambda x: len(x) == len(min(self.words, key=len)), self.words))
    
    def get_longest_words(self):
        return list(filter(lambda x: len(x) == len(max(self.words, key=len)), self.words))



# Класс Todo
# Реализуйте класс Todo, описывающий список дел. При создании экземпляра класс не должен принимать
# никаких аргументов.

# Экземпляр класса Todo должен иметь один атрибут:

# things — изначально пустой список дел, которые нужно выполнить
# Класс Todo должен иметь четыре метода экземпляра:

# add() — метод, принимающий название дела и его приоритет (целое число) и добавляющий данное дело
# в список дел в виде кортежа:
# (<название дела>, <приоритет>)
# get_by_priority() — метод, принимающий в качестве аргумента целое число n и возвращающий список
# названий дел, имеющих приоритет n
# get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет 
# get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет 
# Примечание 1. Названия дел в списках, возвращаемых методами get_by_priority(), get_low_priority()
# и get_high_priority(), должны располагаться в том порядке, в котором они были добавлены в список.

class Todo():
    def __init__(self):
        self.things = list()
        self.low_priority = 0
        self.high_priority = 0
        
    def add(self, name, priority):
        self.things += [(name, priority)]
        self.low_priority = min(self.things, key=lambda x: x[1])
        self.high_priority = max(self.things, key=lambda x: x[1])

    def get_by_priority(self, n):
        return list(map(lambda x: x[0], filter(lambda x: x[1]==n, self.things)))
    
    def get_low_priority(self):
        return list(map(lambda x: x[0], filter(lambda x: x[1]==self.low_priority[1], self.things)))
    
    def get_high_priority(self):
        return list(map(lambda x: x[0], filter(lambda x: x[1]==self.high_priority[1], self.things)))



# Класс Postman
# Реализуйте класс Postman, описывающий почтальона. При создании экземпляра класс не должен
# принимать никаких аргументов.

# Экземпляр класса Postman должен иметь один атрибут:

# delivery_data — изначально пустой список адресов, по которым следует доставить письма
# Экземпляр класса Postman должен иметь три метода экземпляра:

# add_delivery() — метод, принимающий в качестве аргументов улицу, дом и квартиру, и добавляющий
# в список адресов эти данные в виде кортежа:
# (<улица>, <дом>, <квартира>)
# get_houses_for_street() — метод, принимающий в качестве аргумента улицу и возвращающий список
# всех домов на этой улице, в которые требуется доставить письма
# get_flats_for_house() — метод, принимающий в качестве аргументов улицу и дом и возвращающий
# список всех квартир в этом доме, в которые требуется доставить письма
# Примечание 1. Дома и квартиры в списках, возвращаемых методами get_houses_for_street() и
# get_flats_for_house(), должны располагаться в том порядке, в котором они были добавлены.

class Postman():
    def __init__(self):
        self.delivery_data = list()
    
    def add_delivery(self, street, build, apartment):
        self.delivery_data.append((street, build, apartment))
    
    def get_houses_for_street(self, street):
        builds = list(filter(lambda x: x[0]==street, self.delivery_data))
        dct = {build[1]: build[0] for build in builds}
        return list(dct.keys())
    
    def get_flats_for_house(self, street, build):
        builds = list(filter(lambda x: x[0]==street and x[1]==build, self.delivery_data))
        dct = {build[2]: build[1] for build in builds}
        return list(dct.keys())



# Класс Wordplay
# Будем называть словом любую последовательность из одной или более латинских букв.

# Реализуйте класс Wordplay, описывающий расширяемый набор слов. При создании экземпляра
# класс должен принимать один аргумент:

# words — список, определяющий начальный набор слов. Если не передан, начальный набор слов
# считается пустым
# Экземпляр класса Wordplay должен иметь один атрибут:

# words — список, содержащий набор слов
# Класс Wordplay должен иметь четыре метода экземпляра:

# add_word() — метод, принимающий в качестве аргумента слово и добавляющий его в набор.
# Если слово уже есть в наборе, метод ничего не должен делать
# words_with_length() — метод, принимающий в качестве аргумента натуральное число n и возвращающий
# список слов из набора, длина которых равна n
# only() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова
# из набора, которые состоят только из переданных букв
# avoid() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова
# из списка words, которые не содержат ни одну из этих букв
# Примечание 1. Слова в списках, возвращаемых методами words_with_length(), only() и avoid(), должны
# располагаться в том порядке, в котором они были добавлены.

# Примечание 2. Экземпляр класса Wordplay не должен зависеть от списка, на основе которого он был
# создан. Другими словами, если исходный список изменится, то экземпляр класса Wordplay измениться
# не должен.

from string import ascii_letters


class Wordplay():
    def __init__(self, words=[]):
        self.words = words.copy()
    
    def add_word(self, word):
        if set(word).issubset(ascii_letters) and word not in self.words:
            self.words.append(word)
    
    def words_with_length(self, n):
        return list(filter(lambda x: len(x)==n, self.words))
    
    def only(self, *letter):
        return list(filter(lambda x: set(x).issubset(set(letter)), self.words))
    
    def avoid(self, *letter):
        return list(filter(lambda x: set(letter).isdisjoint(x), self.words))



# Класс Knight ♞
# Реализуйте класс Knight, описывающий шахматного коня. При создании экземпляра класс должен
# принимать три аргумента в следующем порядке:

# horizontal — координата коня по горизонтали, представленная латинской буквой от a до h
# vertical — координата коня по вертикали, представленная целым числом от 1 до 8 включительно
# color — цвет коня (black или white)
# Экземпляр класса Knight должен иметь три атрибута:

# horizontal — координата коня на шахматной доске по горизонтали
# vertical — координата коня на шахматной доске по вертикали
# color — цвет коня
# Класс Knight должен иметь четыре метода экземпляра:

# get_char() — метод, возвращающий символ N
# can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтали и по
# вертикали, и возвращающий True, если конь может переместиться на клетку с данными координатами,
# или False в противном случае
# move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтали и по
# вертикали и заменяющий текущие координаты коня на переданные. Если конь из текущей клетки не
# может переместиться на клетку с указанными координатами, его координаты должны остаться неизменными
# draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на
# которые может переместиться конь. Пустые клетки должны быть отображены символом ., конь —
# символом N, клетки, на которые может переместиться конь, — символом *

class Knight():
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.eng_letters = 'abcdefgh'
    
    def get_char(self):
        return 'N'
    
    def can_move(self, horizontal, vertical):
        cur_row, cur_col = 8 - self.vertical, self.eng_letters.index(self.horizontal)
        next_row, next_col = 8 - vertical, self.eng_letters.index(horizontal)
        p = (cur_row - next_row) * (cur_col - next_col)
        if p == 2 or p == -2:
            return True
        return False
    
    def move_to(self, horizontal, vertical):
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical
    
    def draw_board(self):
        matrix = [['.' for _ in range(8)] for _ in range(8)]
        cur_row, cur_col = 8 - self.vertical, self.eng_letters.index(self.horizontal)
        matrix[cur_row][cur_col] = 'N'
        for r in range(8):
            for c in range(8):
                p = (cur_row - r) * (cur_col - c)
                if p == 2 or p == -2:
                    matrix[r][c] = '*' 
        for r in range(8):
            for c in range(8):
                print(str(matrix[r][c]), end='')
            print()
