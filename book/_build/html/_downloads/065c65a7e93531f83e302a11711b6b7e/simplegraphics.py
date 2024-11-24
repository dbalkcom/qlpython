import pygame
from pygame import Color

def init():
      
    # Initialize Pygame
    pygame.init()

    # Set dimensions and create a screen
    width, height = 400, 400
    screen = pygame.display.set_mode((width, height))

    return screen


def game_loop():
   
    # Set the background color
    background_color = (255, 255, 255)  # white
    
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background
        gamescreen.fill(background_color)

        # Draw circles
        draw()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

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


gamescreen = init()

def draw():
    # you can put all your drawing code here

    circle(pygame.Color("red"), 100, 100, 50)                 # Circle
    line(pygame.Color("green"), 50, 300, 350, 270, 5)         # Line
    rectangle(pygame.Color("blue"), 150, 50, 100, 50)         # Rectangle
    ellipse(pygame.Color("yellow"), 250, 150, 100, 50)        # Ellipse
    triangle(pygame.Color("purple"), 50, 350, 200, 200, 350, 350)  # Triangle

 
if __name__ == "__main__":
    game_loop()
