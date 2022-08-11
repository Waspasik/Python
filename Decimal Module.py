# Decimal числа, разделенные символом пробела, хранятся в строковой переменной s.
# Дополните приведенный код, чтобы он вывел сумму наибольшего и наименьшего Decimal
# числа.

from decimal import Decimal as D

s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'

lst = [D(i) for i in s.split()]

print(max(lst) + min(lst))



# Decimal числа, разделенные символом пробела, хранятся в строковой переменной s.
# Дополните приведенный код, чтобы он вывел на первой строке сумму всех чисел, а на
# второй строке 5 самых больших чисел в порядке убывания, разделенных символом пробела.

from decimal import Decimal as D

s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'

numbers = [D(i) for i in s.split()]
max_numbers = []

print(sum(numbers))

for _ in range(5):
    max_numbers.append(max(numbers))
    numbers.remove(max(numbers))

print(*max_numbers)



# Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal
# числа.

from decimal import Decimal as D

num = D(input())
numbers = num.as_tuple().digits

if -1 < num < 1:
    print(max(numbers))
else:
    print(min(numbers) + max(numbers))



# Математическое выражение
# На вход программе подается Decimal число d. Напишите программу, которая вычисляет значение
# выражения:
# e^(d) + ln(d) + lg(d) + sqrt(d)

# Формат входных данных
# На вход программе подается положительное десятичное число d.

# Формат выходных данных
# Программа должна вывести искомое значение выражения.

from decimal import*

d = Decimal(input())

print(d.exp() + d.ln() + d.log10() + d.sqrt())