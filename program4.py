from turtle import *
import random
speed('fastest')
def square_black(b='black', c=1, d='black'):
    pencolor(b)
    pensize(c)
    fillcolor(d)
    begin_fill()
    for _ in range (4):
        forward (20)
        right (90)
    end_fill()
def square_white(b='black', c=1, d='white'):
    pencolor(b)
    pensize(c)
    fillcolor(d)
    begin_fill()
    for _ in range (4):
        forward (20)
        right (90)
    end_fill()
def col_a():
    for _ in range (4):
        square_black()
        penup()
        forward(20)
        pendown()
        square_white()
        penup()
        forward(20)
        pendown()
def col_b():
    for _ in range (4):
        square_white()
        penup()
        forward(20)
        pendown()
        square_black()
        penup()
        forward(20)
        pendown()
for _ in range (8):
    if _ % 2 == 0:
        col_a()    
    else:
        col_b()
    backward(160)
    left(90)
    forward(20)
    right(90)
right(90)
pencolor('white')
forward(20)