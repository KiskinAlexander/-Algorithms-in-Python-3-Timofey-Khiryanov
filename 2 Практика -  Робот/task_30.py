#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    i = 1
    x = 1
    y = 1
    while not wall_is_on_the_right():
        move_right()
        i += 1
    move_left(i-1)

    while (x != i) or (y != i):
        if (x == y and not wall_is_on_the_right()) or ((x + y) == i + 1 and not wall_is_on_the_right()) :
            move_right()
            x += 1
        elif ((x + y) == i + 1 and wall_is_on_the_right()):
            move_left(i-1)
            move_down()
            y += 1
            x = 1
        elif wall_is_on_the_right():
            fill_cell()
            move_left(i-1)
            move_down()
            y += 1
            x = 1
        else:
            fill_cell()
            move_right()
            x += 1
    move_left(i-1)    
   
   


if __name__ == '__main__':
    run_tasks()
