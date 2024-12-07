# easydraw.py, by djb

import pygame
from pygame import Color
import sys

gamescreen = None

def window(width, height):
    global gamescreen
    gamescreen = pygame.display.set_mode((width, height))
    gamescreen.fill(Color("white"))

def draw():
    pygame.display.flip()

def wait_for_exit():
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

  
def circle(color, x, y, radius):
     pygame.draw.circle(gamescreen, color, (x, y), radius)  

def line(color, x1, y1, x2, y2, width=1):
    pygame.draw.line(gamescreen, color, (x1, y1), (x2, y2), width)

def rectangle(color, x, y, width, height):
    pygame.draw.rect(gamescreen, color, (x, y, width, height))

def ellipse(color, x, y, width, height):
    pygame.draw.ellipse(gamescreen, color, (x, y, width, height))

def triangle(color, x1, y1, x2, y2, x3, y3):
    pygame.draw.polygon(gamescreen, color, [(x1, y1), (x2, y2), (x3, y3)])


def test_draw():
    # tests the drawing code

    circle(Color("red"), 100, 100, 50)                 # Circle
    line(Color("green"), 50, 300, 350, 270, 5)         # Line
    rectangle(Color("blue"), 150, 50, 100, 50)         # Rectangle
    ellipse(Color("yellow"), 250, 150, 100, 50)        # Ellipse
    triangle(Color("purple"), 50, 350, 200, 200, 350, 350)  # Triangle

gamescreen = None
 
if __name__ == "__main__":

    window(400, 400)
    test_draw()
    draw()
    wait_for_exit()
