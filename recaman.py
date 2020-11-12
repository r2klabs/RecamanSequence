# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:20:15 2020

@author: rkelley

FROM: https://simpleprogrammer.com/python-generative-art-math/

"""

import turtle

window = turtle.Screen()
window.setup(width=800, height=600, startx=10, starty=0.5)

euler = turtle.Turtle()  # A good mathy name for our turtle
euler.shape("circle")
euler.shapesize(0.5, 0.5, 0.5)
euler.color("green", "green")
euler.pencolor("purple")

scale = 3  # This isn't a turtle module setting.  This is just for us.

# Move the little buddy over to the left side to give him more room to work
euler.penup()
euler.setpos(-390, 0)
euler.pendown()

current = 0   # Here's how we know where we are
seen = set()  # Here's where we'll keep track of where we've been

# Step increases by 1 each time
for step_size in range(1, 100):
    if step_size % 5 == 0:
        euler.color("purple", "purple")
        #euler.stamp()
        euler.color("green", "green")
    backwards = current - step_size

    # Step backwards if its positive and we've never been there before
    if backwards > 0 and backwards not in seen:
        euler.pencolor("purple")
        euler.setheading(90)  # 90 degrees is pointing straight up
        # 180 degrees means "draw a semicircle"
        euler.circle(scale * step_size/2, 180)
        current = backwards
        seen.add(current)

    # Otherwise, go forwards
    else:
        euler.pencolor("blue")
        euler.setheading(270)  # 270 degrees is straight down
        euler.circle(scale * step_size/2, 180)
        current += step_size
        seen.add(current)

turtle.done()
