from pygame import Color
from easydraw import window, circle, line, rectangle, ellipse, triangle, draw, wait_for_exit

# create a new window for drawing on the screen
window(400, 400)

circle(Color("red"), 100, 100, 50)                 # Circle
line(Color("green"), 50, 300, 350, 270, 5)         # Line
rectangle(Color("blue"), 150, 50, 100, 50)         # Rectangle
ellipse(Color("yellow"), 250, 150, 100, 50)        # Ellipse
triangle(Color("purple"), 50, 350, 200, 200, 350, 350)  # Triangle

draw()  # copy the drawing to the window
wait_for_exit() # wait for window exit button
