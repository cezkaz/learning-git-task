from turtle import *

for angle in range(0, 360, 15):
    setheading(angle)
    forward(100)
    write(str(angle) + '*')
    backward(100)

# =====================
import turtle

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
monty = turtle.Pen()
turtle.bgcolor("black")
for i in range(200):
    monty.pencolor(colors[i % 7])
    monty.width(i / 100 + 1)
    monty.forward(i)
    monty.left(51)