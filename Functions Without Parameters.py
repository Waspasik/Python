#Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10 в соответствии с образцом:

# **********
# *        *
# *        *
# *        *
# *         *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********
#Примечание. Для вывода прямоугольника используйте цикл for.

def draw_box():
    print('*' * 10)
    for i in range(12):
        print('*', (' ' * 6), '*')
    print('*' * 10)

draw_box()



#Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 1010 в соответствии с образцом:

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
#Примечание. Для вывода треугольника используйте цикл for.

def draw_triangle():
    for i in range(1, 11):
        print('*' * i)

draw_triangle()