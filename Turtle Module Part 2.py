# Напишите программу, которая рисует пунктирную линию

from turtle import*

shape('circle')

for _ in range(11):
  stamp()
  penup()
  forward(30)
  pendown()



# Напишите программу, которая рисует пунктирную линию

from turtle import*

width, height = 200, 100
shape('circle')

def rectangle(w, h):
  for _ in range(2):
    stamp()
    forward(w)
    left(90)
    stamp()
    forward(h)
    left(90)

rectangle(width, height)



# Напишите программу для рисования паутины в соответствии с примером. Программа должна
# считывать количество лучей паутины, число nn.

# Примечание. Угол заданный каждой парой лучей составляеn 360 / n градусов.

from turtle import*

count_rays = 8
side = 100

def spiderweb(n, s):
  shape('circle')
  stamp()
  for _ in range(n):
    shape('arrow')
    forward(s)
    stamp()
    backward(s)
    right(360/n)

spiderweb(count_rays, side)



# Напишите программу, которая рисует черепашек в соответствии с образцом.

from turtle import*

shape('turtle')
stamp()
for _ in range(10):
  penup()
  forward(100)
  stamp()
  backward(100)
  right(360/10)



# Напишите программу, которая рисует циферблат часов в соответствии с образцом.

from turtle import*

Screen().bgcolor('light blue')
shape('turtle')
stamp()

for _ in range(12):
  pensize(5)
  penup()
  forward(100)
  pendown()
  forward(15)
  penup()
  forward(15)
  stamp()
  backward(130)
  right(360/12)



# Напишите программу, которая рисует черепашью спираль в соответствии с образцом.

from turtle import*

Screen().bgcolor('light green')
shape('turtle')

for i in range(1, 68, 2):
  stamp()
  right(360/15)
  penup()
  forward(i)
  pendown()



# Напишите программу, которая рисует узор в соответствии с образцом.

from turtle import*

colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
size = 1
long = 1

for i in range(7):
  for color in colors:
    pensize(size)
    pencolor(color)
    forward(long)
    left(45)
    long += 3
  size += 2



# Напишите программу, которая рисует звезду Давида, показанную на рисунке. Такую звезду можно
# создать из двух треугольников. Однако их невозможно нарисовать непрерывной линией,
# поэтому перо нужно будет поднять для перехода ко второму треугольнику.

from turtle import*

def triangle():
  for _ in range(3):
    forward(200)
    left(120)

speed(8)
penup()
goto(0, -120)
pendown()
left(60)

triangle()

penup()
goto(0, 120)
pendown()
right(180)

triangle()



# Напишите программу, которая рисует изображение в соответствии с образцом.

from turtle import*

penup()
goto(0, 50)
pencolor('medium aquamarine')
pendown()

for i in range(-150, 151, 33):
  goto(i, -100)
  dot(5, 'blue')
  goto(0, 50)
  
dot(5, 'red')



# Напишите программу, которая рисует изображение символа олимпиады в соответствии с образцом.

from turtle import*

colors = ['lawn green', 'red',  'black', 'deep sky blue', 'yellow']
step_up = 0
step_down = 0

for i in range(5):
  if i == 0 or i == 4:
    penup()
    goto(60 - step_down, -50)
    color(colors[i])
    pensize(3)
    pendown()
    circle(40)
    step_down += 83
  if 0 < i < 4:
    penup()
    goto(100 - step_up, 0)
    color(colors[i])
    pensize(3)
    pendown()
    circle(40)
    step_up += 83



# Напишите программу, которая рисует изображение мишки в соответствии с образцом.

from turtle import*

Screen().setup(500, 500)
Screen().bgcolor('light yellow')
color('brown')
speed(0)

# head
penup()
goto(0, -150)
pendown()
fillcolor('BurlyWood')
begin_fill()
circle(120)
end_fill()

# muzzle
fillcolor('wheat')
begin_fill()
circle(65)
end_fill()
penup()
goto(0, -50)
pendown()
fillcolor('brown')
begin_fill()
circle(12)
end_fill()
goto(0, -120)

# eyes
penup()
goto(-50, -20)
pensize(10)
color('black')
dot()
goto(50, -20)
dot()

# ears
penup()
goto(-85, 65)
pendown()
pensize(1)
fillcolor('indian red')
begin_fill()
circle(30)
end_fill()
penup()
goto(85, 65)
pendown()
fillcolor('indian red')
begin_fill()
circle(30)
end_fill()



# Напишите программу, которая случайным образом рисует снежинки разного цвета и размера
# в соответствии с образцом.

from turtle import*
from random import*

Screen().setup(400, 400)
Screen().bgcolor('light cyan')
snowflake_color = ['blue', 'plum', 'medium purple', 'cyan']
seed(10)
speed(0)

def snowflake(size):
  penup()
  x, y = randint(-200, 200), randint(-200, 200)
  goto(x, y)
  pendown()
  color(choice(snowflake_color))
  for _ in range(8):
    for _ in range(4):
      forward(size)
      left(45)
      forward(size)
      backward(size)
      right(90)
      forward(size)
      backward(size)
      left(45)
    goto(x, y)
    left(45)

for i in range(5, 14, 2):
  snowflake(i)