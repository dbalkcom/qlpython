# circles.py

from pygame import Color
from simplegraphics import init_graphics, circle, draw_and_wait_for_exit
 
init_graphics(400, 400)  # create a new game window of size 400 x 400

circle(Color('blue'), 125, 100, 50)
circle(Color('green'), 275, 100, 50)
 
# copy the drawing onto the window and wait for exit 
# button to be clicked:
draw_and_wait_for_exit()  