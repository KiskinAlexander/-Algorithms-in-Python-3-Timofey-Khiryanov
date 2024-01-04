import turtle

turtle.shape('turtle')
n = 50
for i in range(1, 11):
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.penup()
    turtle.forward(50/2)
    turtle.right(90)
    turtle.forward(50/2)
    turtle.right(180)
    turtle.pendown()
    n+=50
