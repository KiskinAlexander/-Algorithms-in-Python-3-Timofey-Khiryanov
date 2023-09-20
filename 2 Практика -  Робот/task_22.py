#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    if wall_is_beneath() and wall_is_on_the_right():
        fill_cell()
        return
    t=1
    while not wall_is_beneath():
        move_down()
        t+=1
    move_up(t-1)
    for i in range(1,t):
        s=0
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
            s+=1
        fill_cell()

        move_left(s)
        move_down()
    for n in range(1,s+1):
        fill_cell()
        move_right()
    fill_cell()
    move_left(s)
    pass


if __name__ == '__main__':
    run_tasks()
