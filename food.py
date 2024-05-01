import math
from random import random
import pygame

class Food:
    def __init__(self,ctx,x,y) -> None:
        self.position = (x,y)
        self.radius = 5
        quantityRatio = (random()*0.5+0.5)
        self.quantity = math.floor(quantityRatio*100)
        self.color = pygame.Color(0, math.floor(quantityRatio*255), 0)
        self.isAlive= True
        pass

    def eaten(self):
        self.isAlive = False
        pygame.event.post(pygame.event.Event(pygame.USEREVENT,{"name":"food","status":"eaten","food":self}))
        pass
    
    def update(self,ctx,elapsedTime):
        pass

    def render(self,ctx):
        if self.isAlive:
            pygame.draw.circle(ctx,self.color,(self.position[0],self.position[1]),self.radius)
       
        pass