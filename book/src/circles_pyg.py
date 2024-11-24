import pygame
from pygame import Color

def init():
      
    # Initialize Pygame
    pygame.init()

    # Set dimensions and create a screen
    width, height = 400, 200
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

gamescreen = init()

def draw():
    # you can put all your drawing code here
    
    circle(Color('blue'), 125, 100, 50)
    circle(Color('green'), 275, 100, 50)
 
if __name__ == "__main__":
    game_loop()
