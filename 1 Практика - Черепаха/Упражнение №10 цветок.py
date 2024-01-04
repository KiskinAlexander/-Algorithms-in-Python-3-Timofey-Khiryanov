import turtle

turtle.shape('turtle')
print('Введите радиус')
r=int(input())
print('Введите количество окружностей')
n=int(input())
i=1
for i in range(int(n/2)):
    turtle.circle(r)
    turtle.circle(-r)
    turtle.left(360/(n))
