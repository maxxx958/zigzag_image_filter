import turtle
import math
import numpy as np
from PIL import Image

def square(bounces, side):
    tmp = turtle.pos()[0]
    global up
    bounces *= 2
    if int(bounces) == 0:
        turtle.forward(side)
        return
    one_part = side / bounces
    c = math.sqrt(one_part ** 2 / 4.0 + side ** 2 / 4.0)
    angle = np.arcsin(side / 2.0 / c)
    if up == True:
        turtle.left(angle)
    else:
        turtle.right(angle)
    for i in range(bounces):
        turtle.forward(c)
        if up == True:
            turtle.right(2 * angle)
        else:
            turtle.left(2 * angle)
        turtle.forward(c)
        up = ~up
    if up == True:
        turtle.right(angle)
    else:
        turtle.left(angle)

def get_color(i, j, size):
    global img
    tmp = 0
    cnt = 0
    for x in range(i * size, (i + 1) * size):
        for y in range(j * size, (j + 1) * size):
            if y < img.width and x < img.height:
                tmp += img.getpixel((y, x))
                cnt += 1
    return tmp / cnt if cnt > 0 else 0

def to_bounces(color):
    minbounces = 0
    maxbounces = 4
    widthbounces = maxbounces - minbounces
    color /= 256
    color *= widthbounces
    color = maxbounces - color
    return round(color)

def move_to_next_line(size, img, ratio):
    turtle.penup()
    turtle.backward(img.width // size * size * ratio)
    turtle.degrees()
    turtle.right(90)
    turtle.forward(size * ratio)
    turtle.left(90)
    turtle.radians()
    turtle.pendown()

wn = turtle.Screen()
#wn.tracer(0)
turtle.speed('fastest')

up = True
turtle.radians()
turtle.hideturtle()
# read image
img = Image.open('image9.jpg').convert('L')
img.show()

turtle.penup()
turtle.goto(-800, 300)
turtle.pendown()

size = 10
ratio = 900 / max(img.height, img.width)
for i in range(img.height // size):
    up = True
    for j in range(img.width // size):
        square(to_bounces(get_color(i, j, size)), size*ratio)
    move_to_next_line(size, img, ratio)

#wn.update()
wn.mainloop()
