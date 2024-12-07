from pygame import Color
from easydraw import window, circle, draw, wait_for_exit
 
window(400, 400)  # create a new game window of size 400 x 400

circle(Color('black'), 200, 200, 90)
circle(Color('blue'), 200, 200, 70)
circle(Color('red'), 200, 200, 50)
circle(Color('yellow'), 200, 200, 30)

draw() # copy the drawing onto the window
wait_for_exit()  # and wait for exit button to be clicked
