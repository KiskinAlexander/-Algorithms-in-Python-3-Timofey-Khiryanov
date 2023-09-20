#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_on_the_left() and wall_is_above():
        while True:
          move_right()
          move_down()
          if wall_is_on_the_right():
              break
    elif wall_is_on_the_right() and wall_is_above():
        while True:
          move_left()
          move_down()
          if wall_is_on_the_left():
              break
    elif wall_is_on_the_left() and wall_is_beneath():
        while True:
          move_right()
          move_up()
          if wall_is_on_the_right():
              break
    elif wall_is_on_the_right() and wall_is_beneath():
        while True:
          move_left()
          move_up()
          if wall_is_on_the_left():
              break

    
    pass


if __name__ == '__main__':
    run_tasks()
