# Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа, и возвращает
# значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.

def is_valid_triangle(side1, side2, side3):
    if (a < b + c) and (b < a + c) and (c < a + b):
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))



# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True если число
# является простым и False в противном случае.

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())

print(is_prime(n))



# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое
# число большее числа num.

def get_next_prime(num):
    next_prime_number = 0
    for i in range(num + 1, num * 10):
        divisor = 0
        for j in range(1, i + 1):
            if i % j == 0:
                divisor += 1
        if divisor == 2:
            next_prime_number = i
            break
        else:
            continue
    return next_prime_number

n = int(input())

print(get_next_prime(n))



# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает
# значение True если пароль является надежным и False в противном случае.

def is_password_good(password):
    requirement_fail = 0
    if password.islower() == True:
        requirement_fail += 1
    if password.isupper() == True:
        requirement_fail += 1
    if password.isalnum() == False:
        requirement_fail += 1
    if password.isalpha() == True:
        requirement_fail += 1
    if password.isdigit() == True:
        requirement_fail += 1
    if len(password) < 8:
        requirement_fail += 1
    if requirement_fail > 0:
        return False
    else:
        return True

txt = input()

print(is_password_good(txt))



# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и возвращает значение
# True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.

def is_one_away(word1, word2):
    right_letter = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            right_letter += 1
    if len(word1) == len(word2) and right_letter + 1 == len(word1):
        return True
    else:
        return False

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))



# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True если указанный
# текст является палиндромом и False в противном случае.

# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы, а также символы , . ! ? -.

def is_palindrome(text):
    res_text = ''
    for i in range(len(text)):
        if text[i] not in ',.!?- ':
            res_text += text[i]
    res_text = res_text.lower()
    if res_text[:] == res_text[::-1]:
        return True
    else:
        return False

txt = input()

print(is_palindrome(txt))



# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от
# математики, то он решил:

# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает
# значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.

def is_valid_password(password):
    password = password.split(':')
    valid = 0
    
    if len(password) == 3:
        valid += 1
    if password[0] == password[0][::-1]:
        valid += 1
    divider = 0
    for i in range(1, int(password[1]) + 1):
        if int(password[1]) % i == 0:
            divider += 1
    if divider == 2:
        valid += 1
    if int(password[2]) % 2 == 0:
        valid += 1
    if password.count(':') != 2:
        valid += 1
    
    if valid == 5:
        return True
    else:
        return False

psw = input()

print(is_valid_password(psw))



# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из символов
# ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной последовательностью и False в
# противном случае.

# Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ), где каждой
# открывающей скобке найдется парная закрывающая скобка.

def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    if len(text) == 0:
        return True
    else:
        return False

txt = input()

print(is_correct_bracket(txt))



# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и
# преобразует его в «змеиный регистр».

def convert_to_python_case(text):
    
    python_case_string = []
    python_case_string.extend(text[0].lower())
    for i in range(1, len(text)):
        if text[i].islower() or text[i].isdigit():
            python_case_string.extend(text[i].lower())
        elif text[i].isupper():
            python_case_string.extend('_')
            python_case_string.extend(text[i].lower())
    
    return ''.join(python_case_string)

txt = input()

print(convert_to_python_case(txt))