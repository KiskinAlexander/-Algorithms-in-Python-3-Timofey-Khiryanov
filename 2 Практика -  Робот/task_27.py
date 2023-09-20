#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    s = 0    # Нумерация клеток начиная с закрашенной и заканчивая закр.
    t = s   # Нумерация только закрашенных клеток
    while not wall_is_on_the_right():
        if s < t:
            s += 1
            move_right()
            print(s, t)
        else:
            s = 0
            t += 1
            move_right()
            if not wall_is_on_the_right():
                fill_cell()
                
        


   


if __name__ == '__main__':
    run_tasks()
