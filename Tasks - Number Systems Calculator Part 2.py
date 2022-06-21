# В саду 88n фруктовых деревьев, из них 32n яблони, 22n груши, 16n слив и 17n вишен. В какой системе счисления посчитаны деревья?
# Примечание. Переведите числа из n-ой системы счисления в десятичную и составьте уравнение.

def fruits_trees():
    apple = 32
    pear = 22
    plum = 16
    cherry = 17
    fruits_trees = 88
    for i in range(1, 17):
        if ((apple // 10) * i**1 + (apple % 10)) + ((pear // 10) * i**1 + (pear % 10)) + ((plum // 10) * i**1 + (plum % 10)) + ((cherry // 10) * i**1 + (cherry % 10)) == ((fruits_trees // 10) * i**1 + (fruits_trees % 10)):
            return print(i)
        else:
            continue

fruits_trees()


# Переведите десятичное число 1000 в шестнадцатеричную систему счисления.

def hexadecimal_conversion():
    decimal_number = 1000
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    while decimal_number > 0:
        modulo = decimal_number % 16
        if modulo >= 10:
            letter = upper_eng_alphabet[(modulo % 10)]
            result.append(letter)
        elif modulo < 10:
            result.append(str(modulo))
        decimal_number //= 16
    result = ''.join(result)
    return print(result[::-1])

hexadecimal_conversion()


# Переведите десятичное число 513 в двоичную систему счисления.

def binary_conversion():
    decimal_number = 513
    result = []
    while decimal_number > 0:
        modulo = decimal_number % 2
        result.append(str(int(modulo)))
        if modulo == 1:
            decimal_number = (decimal_number - modulo) / 2
        elif modulo == 0:
            decimal_number = (decimal_number - modulo) / 2
    result = ''.join(result)
    return print(result[::-1])

binary_conversion()