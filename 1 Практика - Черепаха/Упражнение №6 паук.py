import turtle

n = int(input())
turtle.shape('turtle')
for i in range(0,n):
    turtle.forward(100)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(100)
    turtle.right(180 - 360/n)
    
