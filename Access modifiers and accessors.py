# Класс Circle
# Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать
# один аргумент:

# radius — радиус круга
# Экземпляр класса Circle должен иметь три атрибута:

# _radius — радиус круга
# _diameter — диаметр круга
# _area — площадь круга
# Класс Circle должен иметь три метода экземпляра:

# get_radius() — метод, возвращающий радиус круга
# get_diameter() — метод, возвращающий диаметр круга
# get_area() — метод, возвращающий площадь круга

from math import pi


class Circle():
    def __init__(self, radius):
        self._radius = radius
        self._diameter = self._radius*2
        self._area = pi * self._radius**2
        
    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter
    
    def get_area(self):
        return self._area



# Класс BankAccount
# Реализуйте класс BankAccount, описывающий банковский счет. При создании экземпляра класс должен
# принимать один аргумент:

# balance — баланс счета, по умолчанию имеет значение 0
# Экземпляр класса BankAccount должен иметь один атрибут:

# _balance — баланс счета
# Класс BankAccount должен иметь четыре метода экземпляра:

# get_balance() — метод, возвращающий актуальный баланс счета
# deposit() — метод, принимающий в качестве аргумента число amount и увеличивающий баланс счета
# на amount
# withdraw() — метод, принимающий в качестве аргумента число amount и уменьшающий баланс счета
# на amount. Если amount превышает количество средств на балансе счета, должно быть возбуждено
# исключение ValueError с сообщением:
# На счете недостаточно средств
# transfer() — метод, принимающий в качестве аргументов банковский счет account и число amount.
# Метод должен уменьшать баланс текущего счета на amount и увеличивать баланс счета account на
# amount. Если amount превышает количество средств на балансе текущего счета, должно быть возбуждено
# исключение ValueError с сообщением:
# На счете недостаточно средств

class BankAccount():
    def __init__(self, balance=0):
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError('На счете недостаточно средств')
        else:
            self._balance -= amount

    def transfer(self, account, amount):
        if amount > self._balance:
            raise ValueError('На счете недостаточно средств')
        else:
            self.withdraw(amount)
            account.deposit(amount)
