# Напишите программу, которая рисует прямоугольник.

from turtle import*

width, height = 200, 100

def rectangle(w, h):
  for _ in range(2):
    forward(w)
    left(90)
    forward(h)
    left(90)

rectangle(width, height)



# Напишите программу, которая рисует прямоугольник.

from turtle import*

side = 150

def triangle(s):
  for _ in range(3):
    forward(s)
    left(120)

triangle(side)



# Напишите программу, которая рисует изображенную фигуру, состоящую из трех квадратов.

from turtle import*

side = 100

def square(s):
  angle = 20
  for i in range(3):
    setheading(angle)
    for j in range(4):
      forward(s)
      left(90)
    angle += 25

square(side)



# Напишите программу, которая рисует изображенную фигуру из восьми квадратов.

from turtle import*

side = 100

def square(s):
  angle = 0
  for i in range(8):
    setheading(angle)
    for j in range(4):
      forward(s)
      left(90)
    angle += 45

square(side)



# Напишите программу, которая рисует правильный шестиугольник.

from turtle import*

side = 100

def hexagon(s):
  for _ in range(6):
    forward(s)
    left(60)

hexagon(side)



# Напишите программу, которая рисует соты.

from turtle import*

side = 40

def hexagon(s):
    for _ in range(6):
      forward(s)
      left(60)

def honeycombs(s):
  for _ in range(6):
    hexagon(s)
    left(120)
    forward(s)
    right(60)

honeycombs(side)



# Напишите программу, которая рисует ромб с углами 60 и 120 градусов.

from turtle import*

side = 200

def rhombus(s):
  for _ in range(2):
    forward(s)
    left(135)
    forward(s)
    left(45)

rhombus(side)



# Напишите программу, которая рисует снежинку из 10 ромбов.

from turtle import*

side = 80

def rhombus(s):
  for _ in range(2):
    forward(s)
    left(60)
    forward(s)
    left(120)

def honeycombs(s):
  for _ in range(10):
    rhombus(s)
    right(35)

honeycombs(side)


# Напишите программу, которая рисует лучи звезды, показанной на рисунке.

from turtle import*

side = 100

def star_rays(s):
  for _ in range(6):
    forward(s)
    backward(s*2)
    forward(s)
    right(30)

star_rays(side)



# Напишите программу, которая рисует правильную пятиконечную звезду.

from turtle import*

side = 150

def five_pointed_star(s):
  for _ in range(5):
    forward(s)
    right(144)

five_pointed_star(side)



# Напишите программу, которая рисует квадраты, чтобы создать узор, показанный на рисунке.

from turtle import*

side = 200

def square(s):
  for _ in range(4):
    left(90)
    forward(s)

def square_in_square(s):
  for _ in range(31):
    square(s)
    s -= 5

square_in_square(side)



# Напишите программу, которая рисует узор, показанный на рисунке.

from turtle import*

for i in range(5, 210, 5):
  left(90)
  forward(i)