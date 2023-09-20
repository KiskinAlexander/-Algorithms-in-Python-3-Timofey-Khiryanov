import turtle


def draw(l, n):
    x = l / (2 ** 0.5)
    if n == 0:
        turtle.forward(l)
        return
    else:
        turtle.left(45)
        draw(x, n - 1)
        turtle.right(45)
        turtle.right(45)
        draw(x, n - 1)
        turtle.left(45)


turtle.speed('fastest')
draw(200, 10)
