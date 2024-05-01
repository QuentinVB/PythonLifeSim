import pygame


class Cell:

    def __init__(self,x,y,radius) -> None:
        self.position = (x,y)
        self.radius = radius
        pass


    def render(self,ctx,seconds):
        pygame.draw.circle(ctx,0xff0000,(self.position[0]*seconds,self.position[1]),self.radius)
        pass