#Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает
#расстояние в милях. Формула для преобразования: мили = километры * 0.6214.

def convert_to_miles(km):
    return km * 0.6214

num = int(input())

print(convert_to_miles(num))



#Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.

#Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.

#Примечание 2. Считайте, что год является невисокосным.

def get_days(month):
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months[month]

num = int(input())

print(get_days(num))



#Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.

def get_factors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result

n = int(input())

print(get_factors(n))



#Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.

#Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.

def number_of_factors(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result += 1
    return result

n = int(input())

print(number_of_factors(n))



#Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке. Проблема заключается в том, что данный метод не находит местоположение всех символов а.

#Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.

#Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.

def find_all(target, symbol):
    result = []
    for i in range(len(target)):
        if target[i] == symbol:
            result.append(i)
    return result

s = input()
char = input()

print(find_all(s, char))



#Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.

#Примечание 1. Списки list1 и list2 могут иметь разную длину.

#Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него 😎.

def merge(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))