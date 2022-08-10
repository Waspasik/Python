# Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры,
# задаваемой с помощью системы неравенств:
  
# −2 ≤ x ≤ 2
# −2 ≤ y ≤ 2
# x^3 + y^4 + 2 ≥ 0
# 3x + y^2 ≤ 2

from random import*

n = 10**6       # количество испытаний

def area_formula():
    k = 0
    s0 = 16
    
    for _ in range(n):
        x, y = uniform(-2, 2), uniform(-2, 2)
        if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
            k += 1
    
    return print((k/n) * s0)

area_formula()



# Напишите программу, которая при помощи метода Монте-Карло определяет приближённое
# значение числа pi.

from random import*

n = 10**6       # количество испытаний

def area_formula():
    x0 = 0
    y0 = 0
    r = 1
    k = 0
    s = 4
    
    for _ in range(n):
        x, y = uniform(-1, 1), uniform(-1, 1)
        if (x - x0)**2 + (y - y0)**2 <= r**2:
            k += 1

    return print((k/n) * s)

area_formula()