#Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

#fill – символ заполнитель;
#base – величина основания равнобедренного треугольника;
#а затем выводит его.

#Примечание. Гарантируется, что основание треугольника – нечетное число.

def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i)
    for j in range(base // 2):
        print(fill * (base // 2 - j))

fill = input()
base = int(input())

draw_triangle(fill, base)



#Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:

#name – имя человека;
#surname – фамилия человека;
#patronymic – отчество человека;
#а затем выводит на печать ФИО человека.

#Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.

def print_fio(name, surname, patronymic):
    print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')       

name, surname, patronymic = input(), input(), input()

print_fio(name, surname, patronymic)



#Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

def print_digit_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    print(total)

n = int(input())

print_digit_sum(n)