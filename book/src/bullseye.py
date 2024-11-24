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
   
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background
        gamescreen.fill(Color('white'))

        # Draw circles
        draw()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

def circle(color, x, y, radius):
     pygame.draw.circle(gamescreen, color, (x, y), radius)  

gamescreen = init()

def draw():
    # you can put all your drawing code here
    
    circle(Color('black'), 200, 200, 90)
    circle(Color('blue'), 200, 200, 70)
    circle(Color('red'), 200, 200, 50)
    circle(Color('yellow'), 200, 200, 30)

if __name__ == "__main__":
    game_loop()
