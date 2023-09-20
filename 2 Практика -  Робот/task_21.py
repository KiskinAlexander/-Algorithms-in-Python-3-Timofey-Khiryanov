#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_down()
    move_right()
    s=1
    for n in range(2,15):
        
        for i in range(s):
            fill_cell()
            move_right()
        s+=1
        
        move_left(s-1)
        move_down()
        
    pass


if __name__ == '__main__':
    run_tasks()
