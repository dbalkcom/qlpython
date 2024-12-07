# circles.py

from pygame import Color
from easydraw import window, circle, draw, wait_for_exit
 
window(400, 400)  # create a new game window of size 400 x 400

circle(Color('blue'), 125, 100, 50)
circle(Color('green'), 275, 100, 50)
 
# copy the drawing onto the window 
draw()

# wait for the exit button to be clicked
wait_for_exit()  