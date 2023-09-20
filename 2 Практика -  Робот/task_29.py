#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    t=0
    while not wall_is_on_the_right():
        if not cell_is_filled():
            t=0
        if cell_is_filled():
            t+=1
        if t==3:
            return
        move_right()
    


    pass


if __name__ == '__main__':
    run_tasks()
