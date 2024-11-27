from pygame import Color
from simplegraphics import init_graphics, circle, draw_and_wait_for_exit
 
init_graphics(400, 400)  # create a new game window of size 400 x 400

circle(Color('black'), 200, 200, 90)
circle(Color('blue'), 200, 200, 70)
circle(Color('red'), 200, 200, 50)
circle(Color('yellow'), 200, 200, 30)

# copy the drawing onto the window and wait for exit button to be clicked:
draw_and_wait_for_exit()  
