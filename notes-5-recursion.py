# Recursion
# Author: Ubial
# 20 October

# We're drawing trees (recursively)

import turtle

# Create a turtle that draws
wn = turtle.Screen()
t = turtle.Turtle()

def draw_tree(level: int, branch_length: float):
    """A recursive function to draw trees
    level - the levels of branches
    branch_length - length of branch to draw
    """
    # Base case is when level is 0
    if level == 0:
        # Create a leaf
        t.color("darkgreen")
        t.stamp()
        t.color("brown")
    # For all other levels
    else:
        # 1. Go forward branch_length pixels
        t.forward(branch_length)
        # 2. Turn to the left and draw a -1 level tree
        t.left(37)
        draw_tree(level - 1, branch_length * 0.8)
        # 3. Turn to the right and draw a -1 level tree
        t.right(74)
        draw_tree(level - 1, branch_length * 0.8)
        # 4. Go back to where we started
        t.left(37)    # point north
        t.backward(branch_length)

# Set up the turtle
t.left(90)
t.color("brown")
t.pensize(5)
t.shape("turtle")
t.penup()
t.goto(0, -180)
t.pendown()

draw_tree(8, 128)


wn.exitonclick()
