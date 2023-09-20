#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    move_right()
    s=0
    while not wall_is_on_the_right():
        i=0
        while not wall_is_above():
            move_up()
            fill_cell()
            i+=1
        if i != 0:
            move_down(i)
        s+=1
        move_right()
    if wall_is_above():
            move_left(s+1)
            return
    i=0        
    while not wall_is_above():
        move_up()
        fill_cell()
        i+=1
    move_down(i)
    move_left(s+1)
      
    


if __name__ == '__main__':
    run_tasks()
