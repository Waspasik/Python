# Напишите программу, которая рисует изображение домика по образцу.

from turtle import*

penup()
goto(-70, 0)
pendown()
fillcolor('sienna')
begin_fill()
for _ in range(3):
  forward(140)
  left(120)
end_fill()

penup()
goto(-60, 0)
pendown()
fillcolor('cornflower blue')
begin_fill()
for _ in range(4):
  forward(120)
  right(90)
end_fill()



# Напишите программу, которая рисует изображение светофора по образцу.

from turtle import*

colors = ['red', 'yellow', 'lawn green']
step_down = 25
speed(0)

penup()
goto(-50, 100)
pendown()
begin_fill()
for _ in range(2):
  forward(100)
  right(90)
  forward(240)
  right(90)
end_fill()

for i in range(3):
  goto(0, step_down)
  fillcolor(colors[i])
  begin_fill()
  circle(30)
  end_fill()
  step_down -= 75



# Напишите программу, которая рисует оптическую иллюзию по образцу.

from turtle import*

speed(0)
penup()
goto(-100, -60)
pendown()
for _ in range(3):
    forward(200)
    left(120)

penup()
goto(-100, 60)
pendown()
color('white')
fillcolor('white')
begin_fill()
for _ in range(3):
    forward(200)
    color('black')
    dot(70)
    color('white')
    right(120)

end_fill()



# Напишите программу, которая рисует изображение радуги по образцу.

from turtle import*

colors = ['red', 'orange', 'yellow', 'lawn green', 'medium spring green',
         'cyan', 'dodger blue', 'blue', 'purple', 'deep pink']
radius = 200
pos_y = -200
Screen().setup(500, 500)
speed(0)
for col in colors:
  penup()
  goto(0, pos_y)
  pendown()
  begin_fill()
  fillcolor(col)
  circle(radius)
  end_fill()
  radius -= 20
  pos_y += 20



# Напишите программу, которая рисует изображение полумесяца по образцу.

from turtle import*

Screen().setup(400, 400)
Screen().bgcolor('dark blue')

colors = ['gold', 'dark blue']
pos_x = 0
speed(0)
for col in colors:
  penup()
  goto(pos_x, -150)
  pendown()
  color(col)
  fillcolor(col)
  begin_fill()
  circle(150)
  end_fill()
  pos_x += 50