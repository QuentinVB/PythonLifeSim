from random import random
import pygame


class Cell:


    def __init__(self,x,y,radius) -> None:
        self.position = (x,y)
        self.radius = radius
        self.lifeDuration = 0
        self.speed=0.1
        self.updateDirection()
        pass

    def updateDirection(self):
        if self.lifeDuration%100 == 0 :
            x = (random()*2)-1
            y = (random()*2)-1
            print(f'change direction to {x}:{y}')
            self.direction = (x,y)
        pass

    def update(self,elapsedTime):
        self.lifeDuration+=elapsedTime
        self.updateDirection()
        self.position = (self.position[0]+self.direction[0]*elapsedTime*self.speed, self.position[1]+self.direction[1]*elapsedTime*self.speed)
        pass
    
    def render(self,ctx):
        pygame.draw.circle(ctx,0xff0000,(self.position[0],self.position[1]),self.radius)
        pass