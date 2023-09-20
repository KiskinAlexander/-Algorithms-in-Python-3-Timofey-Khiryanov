import turtle


def draw(l, n, sign=1):
    x = l / (2 ** 0.5)
    if n == 0:
        turtle.forward(l)
        return
    else:
        turtle.right(45 * sign)
        draw(x, n - 1, 1)
        turtle.left(90 * sign)
        draw(x, n - 1, -1)
        turtle.right(45 * sign)


# turtle.speed('fastest')
draw(200, 10)
