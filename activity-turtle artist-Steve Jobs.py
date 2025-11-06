# Turtle Artist
# Author:
# 28 October

import turtle

# A one-of-a-kind drawing

wn = turtle.Screen()
t = turtle.Turtle()

def draw_house(x: int, y: int):
    """Draws a house at the location x and y.

    x, y - bottom left corner of the house"""

    t.goto(-100, -300)   # this is an offset for the house

# drawing a pizza
t.circle(100, 160)
t.forward(200)     # slicing up the pizza

wn.exitonclick()
