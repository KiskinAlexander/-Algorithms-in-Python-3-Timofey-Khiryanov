import turtle

turtle.shape('turtle')
n=50
for i in range(1,10):
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    n+=50
