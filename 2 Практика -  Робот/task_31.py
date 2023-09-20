#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while not wall_is_on_the_left():
        while not wall_is_beneath():
            move_down()
        while not wall_is_on_the_right():
            move_right()
        while wall_is_beneath():
            move_left()
            if wall_is_on_the_left():
                return


if __name__ == '__main__':
    run_tasks()
