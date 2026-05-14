from turtle import *
import random
answer = int(input('Wpisz liczbe kątów: '))
e = 360//answer
def square(a, b='black', c=5, d='#00e5ff'):
    pencolor(b)
    pensize(c)
    fillcolor(d)
    begin_fill()
    for _ in range (answer):
        forward (a)
        right (e)
    end_fill()
square(40, '#84ff00', 10)
teleport(-200,-200)
square(60, '#ff007b', 15)
teleport(300, 300)
square(60)

