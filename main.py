# Example file showing a basic pygame "game loop"
import pygame

from cell import Cell

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
running = True

cell = Cell(screen.get_width()/2,screen.get_height()/2,10)


while running:
    secondsFromStart = (pygame.time.get_ticks()-start_ticks)/1000
    elapsedTime = clock.get_time()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cyan")

    # RENDER YOUR GAME HERE
    cell.update(elapsedTime)
    cell.render(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()