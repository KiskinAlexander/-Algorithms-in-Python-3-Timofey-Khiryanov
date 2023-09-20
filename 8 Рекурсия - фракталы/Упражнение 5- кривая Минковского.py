import turtle


def draw(l, n):
    x = l / 4
    if n == 0:
        turtle.forward(l)
        return
    else:
        draw(x, n - 1)
        turtle.left(90)
        draw(x, n - 1)
        turtle.right(90)
        draw(x, n - 1)
        turtle.right(90)
        draw(x, n - 1)
        draw(x, n - 1)
        turtle.left(90)
        draw(x, n - 1)
        turtle.left(90)
        draw(x, n - 1)
        turtle.right(90)
        draw(x, n - 1)


draw(1000, 3)
