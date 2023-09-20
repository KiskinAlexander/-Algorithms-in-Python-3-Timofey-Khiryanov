import turtle


def draw(l, n, x=0, y=0):
    dist = l / 3
    if n == 0:
        # turtle.forward(dist)
        return
    else:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(l)
        draw(dist, n - 1, x, y - 20)
        draw(dist, n - 1, x + dist * 2, y - 20)


# turtle.speed('fastest')
draw(400, 4)
