#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()    
    for n in range(2,14):
        i=0
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
            i+=1
        move_left(i)
        move_down()
    pass


if __name__ == '__main__':
    run_tasks()
