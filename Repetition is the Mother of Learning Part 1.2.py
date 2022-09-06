# Функция index_of_nearest()
# Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем
# порядке:

# numbers — список целых чисел
# number — целое число

# Функция должна находить в списке numbers ближайшее по значению число к числу number
# и возвращать его индекс. Если список numbers пуст, функция должна вернуть число -1.

# Примечание 1. Если в функцию передается список, содержащий несколько чисел,
# одновременно являющихся ближайшими к искомому числу, функция должна возвращать
# наименьший из индексов ближайших чисел.

# Примечание 2. Рассмотрим третий тест. Ближайшими числами к числу 4 являются 5 и 3,
# имеющие индексы 1 и 2 соответственно. Наименьший из индексов равен 1.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию index_of_nearest(), но не код, вызывающий ее.

from math import*

def index_of_nearest(numbers, number):
    if bool(numbers):
        num_difference = abs(numbers[0] - number)
        result_index = 0
        for i in range(len(numbers)):
            if abs(numbers[i] - number) < num_difference:
                num_difference = abs(numbers[i] - number)
                result_index = i
        return result_index
    else:
        return -1



# Функция spell()
# Реализуйте функцию spell(), которая принимает произвольное количество позиционных
# аргументов-слов и возвращает словарь, ключи которого — первые буквы слов, а значения
# — максимальные длины слов на эту букву.

# Примечание 1. Если в функцию не передается ни одного аргумента, функция должна
# возвращать пустой словарь.

# Примечание 2. Функция должна игнорировать регистр слов, при этом в результирующий
# словарь должны попасть именно буквы в нижнем регистре.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию, но не код, вызывающий ее.

def spell(*args):
    lowercase_words = list(map(lambda word: word.lower(), args))
    return {word[0]: max(map(len, filter(lambda w: w.startswith(word[0]), lowercase_words))) for word in lowercase_words}



# Функция choose_plural() 🌶️🌶️
# Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем
# порядке:

# amount — натуральное число, количество
# declensions — кортеж из трех вариантов склонения существительного

# Функция должна возвращать строку, полученную путем объединения подходящего
# существительного из кортежа declensions и количества amount, в следующем формате:

# <количество> <существительное>

# Примечание 1. Передаваемый в функцию кортеж легко составить по мнемоническому
# правилу: один, два, пять. Например:

# для слова «арбуз»: арбуз, арбуза, арбузов
# для слова «рубль»: рубль, рубля, рублей

# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую
# функцию choose_plural(), но не код, вызывающий ее.

def choose_plural(amount, declensions):
    suffixes = {
        1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2,
        11: 2, 12: 2, 13: 2, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 2, 20: 2, 0: 2,
    }
    
    for key, value in suffixes.items():
        if len(str(amount)) >= 2 and str(amount)[-2:] in ['11', '12', '13', '14']:
            return f'{amount} {declensions[suffixes[11]]}'
        elif len(str(amount)) >= 2 and str(amount)[-2:] == str(key):
            return f'{amount} {declensions[value]}'
        elif len(str(amount)) >= 2 and str(amount)[-1] == str(key):
            return f'{amount} {declensions[value]}' 
        elif len(str(amount)) == 1 and str(amount)[-1] == str(key):
            return f'{amount} {declensions[value]}'