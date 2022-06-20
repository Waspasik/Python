# Переведите двоичное число 111111 в десятичную систему счисления.

def binary_number():
    binary_number = 111111
    degree = 0
    result = 0
    while binary_number > 0:
        result += binary_number % 10 * 2**degree
        degree += 1
        binary_number //= 10
    print(result)


# Переведите шестнадцатеричное число 1AF2 в десятичную систему счисления.

def hexadecimal_number():
    hexadecimal_num = '1AF2'
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    degree = len(hexadecimal_num) - 1
    result = 0
    for i in range(len(hexadecimal_num)):
        if hexadecimal_num[i].isdigit():
            result += int(hexadecimal_num[i]) * 16**degree
            degree -= 1
        elif hexadecimal_num[i].isalpha():
            index = upper_eng_alphabet.index(hexadecimal_num[i])
            result += (index + 10) * 16**degree
            degree -= 1
    return print(result)

hexadecimal_number()