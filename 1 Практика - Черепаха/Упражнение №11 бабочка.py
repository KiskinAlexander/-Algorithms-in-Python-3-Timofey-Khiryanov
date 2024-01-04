import turtle

turtle.shape('turtle')
turtle.left(90)
print("Введите радиус начальный")
r=int(input())
print("Введите приращение")
d=int(input())

def butterfly(a):
    turtle.circle(a)
    turtle.circle(-a)

x=1
while x<=20:
    butterfly(r)
    r+=5
    x+=1
