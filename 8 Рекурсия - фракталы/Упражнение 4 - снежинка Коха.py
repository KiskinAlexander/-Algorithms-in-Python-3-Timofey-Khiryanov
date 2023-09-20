import turtle


def draw(l, n):
    x = l / 3
    if n == 0:
        turtle.forward(l)
        return
    else:
        draw(x, n - 1)
        turtle.left(60)
        draw(x, n - 1)
        turtle.right(120)
        draw(x, n - 1)
        turtle.left(60)
        draw(x, n - 1)


draw(400, 3)
turtle.right(120)
draw(400, 3)
turtle.right(120)
draw(400, 3)
turtle.right(120)
