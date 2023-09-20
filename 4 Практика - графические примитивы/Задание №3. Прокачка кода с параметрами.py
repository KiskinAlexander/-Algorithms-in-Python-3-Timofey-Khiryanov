import graphics as gr

window = gr.GraphWin("Jenkslex and Ganzz project", 400, 400)


def draw_sky():
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(400, 200))
    sky.setFill('blue')

    sky.draw(window)


def draw_earth():
    earth = gr.Rectangle(gr.Point(0, 200), gr.Point(400, 400))
    earth.setFill('light grey')

    earth.draw(window)


def dray_clouds(x, y, size):
    cloud = gr.Circle(gr.Point(x, y), size)
    cloud.setFill('white')
    cloud.draw(window)


def draw_sun():
    sun = gr.Circle(gr.Point(300, 90), 35)
    sun.setFill('yellow')

    sun.draw(window)


def draw_spruce():
    spruce_trunk = gr.Rectangle(gr.Point(300, 330), gr.Point(310, 370))
    spruce_triangl1 = gr.Polygon(gr.Point(250, 330), gr.Point(360, 330), gr.Point(305, 280))
    spruce_triangl2 = gr.Polygon(gr.Point(250, 290), gr.Point(360, 290), gr.Point(305, 240))
    spruce_triangl3 = gr.Polygon(gr.Point(250, 250), gr.Point(360, 250), gr.Point(305, 200))
    spruce_trunk.setOutline('black')
    spruce_trunk.setWidth(5)
    spruce_trunk.setFill('brown')
    spruce_triangl1.setOutline('black')
    spruce_triangl1.setWidth(3)
    spruce_triangl1.setFill('green')
    spruce_triangl2.setOutline('black')
    spruce_triangl2.setWidth(3)
    spruce_triangl2.setFill('green')
    spruce_triangl3.setOutline('black')
    spruce_triangl3.setWidth(3)
    spruce_triangl3.setFill('green')

    spruce_trunk.draw(window)
    spruce_triangl1.draw(window)
    spruce_triangl2.draw(window)
    spruce_triangl3.draw(window)


def draw_house():
    house_wall = gr.Rectangle(gr.Point(100, 170), gr.Point(225, 295))
    house_roof = gr.Polygon(gr.Point(100, 170), gr.Point(225, 170), gr.Point(162.5, 100))
    house_window1 = gr.Rectangle(gr.Point(141.67, 211.67), gr.Point(162.51, 232.51))
    house_window2 = gr.Rectangle(gr.Point(162.51, 211.67), gr.Point(183.35, 232.51))
    house_window3 = gr.Rectangle(gr.Point(141.67, 232.51), gr.Point(162.51, 253.35))
    house_window4 = gr.Rectangle(gr.Point(162.51, 232.51), gr.Point(183.35, 253.35))
    house_wall.setOutline('black')
    house_wall.setWidth(3)
    house_wall.setFill('grey')
    house_roof.setOutline('black')
    house_roof.setWidth(3)
    house_roof.setFill('brown')
    house_window1.setOutline('black')
    house_window1.setWidth(3)
    house_window1.setFill('yellow')
    house_window2.setOutline('black')
    house_window2.setWidth(3)
    house_window2.setFill('yellow')
    house_window3.setOutline('black')
    house_window3.setWidth(3)
    house_window3.setFill('yellow')
    house_window4.setOutline('black')
    house_window4.setWidth(3)
    house_window4.setFill('yellow')

    house_wall.draw(window)
    house_roof.draw(window)
    house_window1.draw(window)
    house_window2.draw(window)
    house_window3.draw(window)
    house_window4.draw(window)


draw_sky()
draw_earth()
draw_sun()
dray_clouds(80, 80, 20)
dray_clouds(100, 80, 20)
dray_clouds(110, 90, 20)
dray_clouds(90, 90, 20)
dray_clouds(70, 90, 20)
dray_clouds(280, 80, 20)
dray_clouds(300, 80, 20)
dray_clouds(310, 90, 20)
dray_clouds(290, 90, 20)
dray_clouds(270, 90, 20)
dray_clouds(180, 40, 20)
dray_clouds(200, 40, 20)
dray_clouds(210, 50, 20)
dray_clouds(190, 50, 20)
dray_clouds(170, 50, 20)

draw_spruce()
draw_house()

window.getMouse()

window.close()
