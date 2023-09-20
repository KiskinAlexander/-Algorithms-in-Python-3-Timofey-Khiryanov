#!/usr/bin/python3

from pyrob.api import *


@task
   
def task_2_2():
    draw_figure(1, 2)
    for i in range(1,5):
        draw_figure(5, 1)    
def draw_figure(delta_x, delta_y):
    for i in range(1,delta_x+1):
        move_right()
    for n in range(1, delta_y+1):
        move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    move_right()
    move_down()
    fill_cell()
    move_up(2)
    fill_cell()
    move_left()
    


if __name__ == '__main__':
    run_tasks()
