import turtle

import colorgram
from turtle import Turtle,Screen
import random

colours_list = [(2, 2, 1), (13, 25, 31), (35, 104, 131), (194, 237, 248), (96, 181, 211), (243, 230, 210)]
yaxis = 0
xaxis = 0

crosshair = Turtle()
turtle.colormode(255)
crosshair
for i in range(10):
    xaxis += 0
    yaxis += 30
    crosshair.goto(xaxis, yaxis)

    for j in range(10):
        crosshair.penup()
        crosshair.speed("fastest")

        crosshair.dot(15, random.choice(colours_list) )
        crosshair.penup()
        crosshair.forward(40)









screen = Screen()
screen.exitonclick()
