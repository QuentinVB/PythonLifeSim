# Example file showing a basic pygame "game loop"
import pygame

from cell import Cell

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
running = True

cell = Cell(10,10,10)


while running:
    seconds = (pygame.time.get_ticks()-start_ticks)/1000

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cyan")

    # RENDER YOUR GAME HERE
    cell.render(screen,seconds)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()