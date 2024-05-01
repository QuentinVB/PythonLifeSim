import math
from random import random
import pygame


class Cell:
    BASE_ENERGY = 100

    def __init__(self,ctx,x,y,radius) -> None:
        self.ctx = ctx
        self.position = (x,y)
        self.radius = radius
        self.lifeDuration = 0
        self.speed=0.1
        self.energy=Cell.BASE_ENERGY
        self.isAlive=True
        self.updateFrequency = math.floor(1000*random())+1
        self.updateDirection(ctx)
        pass

    def updateDirection(self,ctx):
        if self.position[0] < 0 or self.position[0]>ctx.get_width() or  self.position[1] < 0 or self.position[1]>ctx.get_height():
            distance = (ctx.get_width()/2-self.position[0],ctx.get_height()/2-self.position[1])
            norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
            self.direction = (distance[0] / norm, distance[1] / norm)
            #print(f'redirect direction to {self.direction[0]}:{self.direction[1]}')
            return
        if self.lifeDuration%self.updateFrequency == 0 :
            x = (random()*2)-1
            y = (random()*2)-1
            #print(f'change direction to {x}:{y}')
            self.direction = (x,y)
            return
        pass

    def eat(self,food):
        #print(f'Eaten {food.quantity}, energy now at {self.energy}')
        self.energy+=food.quantity
        food.eaten()
        #print("emit event")
    
    def kill(self):
        print("i'm ded")
        self.isAlive=False
        pygame.event.post(pygame.event.Event(pygame.USEREVENT,{"name":"cell","status":"dead","cell":self}))
        pass
    def reproduce(self):
        print("give life")
        newCell=Cell(self.ctx ,self.position[0],self.position[1],self.radius)
        self.energy-=Cell.BASE_ENERGY
        pygame.event.post(pygame.event.Event(pygame.USEREVENT,{"name":"cell","status":"alive","cell":newCell}))

    def update(self,ctx,elapsedTime,foods):
        self.lifeDuration+=elapsedTime
        self.energy -=self.speed*elapsedTime*0.1

        if self.energy<=0 :
            self.kill()
            return
        if self.energy> Cell.BASE_ENERGY *2 :
            self.reproduce()
            return
        
        for food in foods:
            if food.isAlive:
                distance = (food.position[0]-self.position[0],food.position[1]-self.position[1])
                norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)

                if norm < self.radius+food.radius:
                    self.eat(food)

        self.updateDirection(ctx)
        self.position = (self.position[0]+self.direction[0]*elapsedTime*self.speed, self.position[1]+self.direction[1]*elapsedTime*self.speed)
        pass
    
    def render(self,ctx):
        pygame.draw.circle(ctx,0xff0000,(self.position[0],self.position[1]),self.radius)
        pass