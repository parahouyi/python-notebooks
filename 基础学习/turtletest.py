# from turtle import *
# import random
#
# setup(1000,800)
# penup()
# goto(-500,0)
# speed(10)
# for i in range(3, 10):
#     pendown()
#     begin_fill()
#     a = 180 - ((i - 2) * 180 / i)
#     pcolor = (random.random(), random.random(), random.random())
#     bcolor = (random.random(), random.random(), random.random())
#     color(pcolor, bcolor)
#     for j in range(i):
#         fd(30 - 2*i)
#         left(a)
#     end_fill()
#     penup()
#     fd(80)
from turtle import *
goto(-200,0)
color('red', 'red')
bgcolor('green')
fillcolor('gold')
speed(20)
for i in range(3, 20, 2):
    pendown()
    begin_fill()
    for j in range(i):
        fd(30)
        rt(144 * 5 / i)
    end_fill()
    penup()
    fd(50)

input()

