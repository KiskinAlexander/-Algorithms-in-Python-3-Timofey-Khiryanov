# Задание по пути: http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html
# Нарисуйте пружину. Используйте функцию, рисующую дугу.:
# http://judge.mipt.ru/mipt_cs_on_python3/images/lab1/spring.gif
import turtle
t = turtle.Pen()
t.shape('turtle')
t.speed(10)
t.left(90)
x = 1
while x <= 6:
    t.circle(-50, 180, 100)
    t.circle(-10, 180, 100)
    x += 1
turtle.exitonclick()
