# Задание по пути: http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Нарисуйте «цветок» из окружностей. Используйте функцию, рисующую окружность:
# http://judge.mipt.ru/mipt_cs_on_python3/images/lab1/flower.gif
import turtle

turtle.shape('turtle')
print('Введите радиус')
r = int(input())
print('Введите количество окружностей')
n = int(input())
i = 1
for i in range(int(n / 2)):
    turtle.circle(r)
    turtle.circle(-r)
    turtle.left(360 / (n))
