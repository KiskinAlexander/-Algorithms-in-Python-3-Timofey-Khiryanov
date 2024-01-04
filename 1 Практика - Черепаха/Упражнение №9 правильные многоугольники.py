import turtle
import math

def polygon(n,a):   #n-число сторон, a - длина стороны
    turtle.penup()
    turtle.forward(a/(2*math.sin(math.pi/n)))
    turtle.pendown()
    i=1
    turtle.left(90+360/(2*n))
    for i in range(n):
        turtle.forward(a)
        turtle.left(360/n)
    turtle.penup()
    turtle.goto(0,0)
    turtle.right(90+360/(2*n))
turtle.shape('turtle')

a=40
j=3
while j<10:
    polygon(j,a)
    j+=1
    a+=10
