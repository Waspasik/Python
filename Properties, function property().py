# Класс Rectangle
# Реализуйте класс Rectangle, описывающий прямоугольник. При создании экземпляра класс должен
# принимать два аргумента в следующем порядке:

# length — длина прямоугольника
# width — ширина прямоугольника

# Экземпляр класса Rectangle должен иметь два атрибута:

# length — длина прямоугольника
# width — ширина прямоугольника

# Класс Rectangle должен иметь два свойства:

# perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
# area — свойство, доступное только для чтения, возвращающее площадь прямоугольника

# Примечание 1. При изменении сторон прямоугольника должны изменяться его периметр и площадь.

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return (self.length + self.width) * 2
    
    def get_area(self):
        return self.length * self.width

    perimeter = property(get_perimeter)
    area = property(get_area)



# Класс HourClock
# Реализуйте класс HourClock, описывающий часы с одной лишь часовой стрелкой. При создании
# экземпляра класс должен принимать один аргумент:

# hours — количество часов. Если hours не является целым числом, принадлежащим диапазону
# [1; 12], должно быть возбуждено исключение ValueError с текстом:
# Некорректное время

# Класс HourClock должен иметь одно свойство:

# hours — свойство, доступное для чтения и записи, возвращающее текущее количество часов. При
# изменении свойство должно проверять, что новое значение является целым числом, принадлежащим
# диапазону [1; 12], в противном случае должно быть возбуждено исключение ValueError с текстом:
# Некорректное время

# Примечание 1. Никаких ограничений касательно реализации класса HourClock нет, она может быть
# произвольной.

class HourClock():
    def __init__(self, hours):
        self.hours = hours
    
    def get_hours(self):
        return self._hours
    
    def set_hours(self, hours):
        if hours in (i for i in range(1, 13)):
            self._hours = hours
        else:
            raise ValueError('Некорректное время')
    
    hours = property(get_hours, set_hours)



# Класс Person
# Реализуйте класс Person, описывающий человека. При создании экземпляра класс должен принимать
# два аргумента в следующем порядке:

# name — имя человека
# surname — фамилия человека

# Экземпляр класса Person должен иметь два атрибута:

# name — имя человека
# surname — фамилия человека

# Класс Person должен иметь одно свойство:

# fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде
# строки:
# <имя> <фамилия>

# Примечание 1. При изменении имени и/или фамилии человека должно изменяться и его полное имя.
# Аналогично при изменении полного имени должны изменяться имя и фамилия.

class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def get_fullname(self):
        return f'{self.name} {self.surname}'
    
    def set_fullname(self, fullname):
        self.name, self.surname = fullname.split() 
    
    fullname = property(get_fullname, set_fullname)
