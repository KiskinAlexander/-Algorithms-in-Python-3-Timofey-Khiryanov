#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    i = 0
    while True:
        move_right()
        if cell_is_filled():
            i+=1
        if i==5:
            return

    pass


if __name__ == '__main__':
    run_tasks()
