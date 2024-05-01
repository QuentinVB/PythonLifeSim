import math
from random import random
import pygame


class Cell:

    def __init__(self,ctx,x,y,radius) -> None:
        self.position = (x,y)
        self.radius = radius
        self.lifeDuration = 0
        self.speed=0.1
        self.updateDirection(ctx)
        pass

    def updateDirection(self,ctx):
        if self.position[0] < 0 or self.position[0]>ctx.get_width() or  self.position[1] < 0 or self.position[1]>ctx.get_height():
            distance = (ctx.get_width()/2-self.position[0],ctx.get_height()/2-self.position[1])
            norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
            self.direction = (distance[0] / norm, distance[1] / norm)
            print(f'redirect direction to {self.direction[0]}:{self.direction[1]}')
            return
        if self.lifeDuration%100 == 0 :
            x = (random()*2)-1
            y = (random()*2)-1
            print(f'change direction to {x}:{y}')
            self.direction = (x,y)
            return
        pass

    def update(self,ctx,elapsedTime):
        self.lifeDuration+=elapsedTime
        self.updateDirection(ctx)
        self.position = (self.position[0]+self.direction[0]*elapsedTime*self.speed, self.position[1]+self.direction[1]*elapsedTime*self.speed)
        pass
    
    def render(self,ctx):
        pygame.draw.circle(ctx,0xff0000,(self.position[0],self.position[1]),self.radius)
        pass