# Example file showing a basic pygame "game loop"
from random import random
import pygame

from cell import Cell
from food import Food

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
running = True
myfont = pygame.font.SysFont("monospace", 15)

cells = []
foods = []

for _ in range(10):
    cells.append(Cell(screen,screen.get_width()/2,screen.get_height()/2))
for _ in range(200):
    foods.append(Food(screen,screen.get_width()*random(),screen.get_height()*random()))

while running:
    secondsFromStart = (pygame.time.get_ticks()-start_ticks)/1000
    elapsedTime = clock.get_time()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT and event.dict["name"]=="food":
            foods.remove(event.dict["food"])
        if event.type == pygame.USEREVENT and event.dict["name"]=="cell":
            if event.dict["status"]=="dead":
                cell = event.dict["cell"]
                cells.remove(cell)
                newFood = Food(screen,cell.position[0],cell.position[1])
                newFood.quantity = cell.energy + cell.radius
                foods.append(newFood)
            if event.dict["status"]=="alive":
                cell = event.dict["cell"]
                cells.append(cell)
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cyan")

    #update
    for cell in cells:
        cell.update(screen,elapsedTime,foods)
    #render
    for food in foods:
        food.render(screen)
    for cell in cells:
        cell.render(screen)
    label = myfont.render(f'Cells: {len(cells)}', 1, (0,0,0))
    screen.blit(label, (0, 0))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()