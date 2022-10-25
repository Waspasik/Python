# Функция is_good_password() 👀
# Назовем пароль хорошим, если

# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра

# Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:

# string — произвольная строка

# Функция должна возвращать True, если строка string представляет собой хороший пароль,
# или False в противном случае.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию is_good_password(), но не код, вызывающий ее. 

def is_good_password(string):
    return all((len(string) >= 9,
               any(char.isdigit() for char in string),
               any(char.islower() for char in string),
               any(char.isupper() for char in string)))



# Функция is_good_password() 🐍
# Назовем пароль хорошим, если

# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра

# Реализуйте функцию is_good_password() в стиле EAFP, которая принимает один аргумент:

# string — произвольная строка

# Функция должна возвращать True, если строка string представляет собой хороший пароль,
# или возбуждать исключение:

# LengthError, если его длина меньше 99 символов
# LetterError, если в нем отсутствуют буквы или все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры

# Примечание 1. Исключения LengthError, LetterError и DigitError уже определены и доступны.

# Примечание 2. Приоритет возбуждения исключений в случае невыполнения нескольких условий:
# LengthError, затем LetterError, а уже после DigitError.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию is_good_password(), но не код, вызывающий ее. 

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    if not len(string) >= 9:
        raise LengthError
    if not any(char.isalpha() for char in string) or string.islower() or string.isupper():
        raise LetterError
    if not any(char.isdigit() for char in string):
        raise DigitError
    else:
        return True