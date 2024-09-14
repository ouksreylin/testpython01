#14-09-24
import turtle
from turtle import *
t=Turtle()
t.shape('turtle')
t.color('blue')

size=int(input("Size of square :"))
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)

turtle.mainloop()
turtle.bye()