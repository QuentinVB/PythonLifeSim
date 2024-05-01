import math
from random import randint, random
import pygame


class Cell:
    BASE_ENERGY = 100
    MUTATION_FACTOR=0.6

    def __init__(self,ctx,x,y,genome={}) -> None:
        self.ctx = ctx
        self.position = (x,y)
        self.lifeDuration = 0
        self.energy=Cell.BASE_ENERGY
        self.isAlive=True
    
        if len(genome):
            self.radius = genome["radius"]
            self.speed= genome["speed"]
            self.updateFrequency = genome["updateFrequency"] 
            self.foodEfficiency = genome["foodEfficiency"] 
            self.color = genome["color"] 
        else:
            self.radius = 10
            self.speed=  0.1
            self.updateFrequency = math.floor(1000*random())+1
            self.foodEfficiency =  0.1
            self.color =  pygame.Color(0xff,0x00,0xa0)

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
        genome = {
            "radius": self.radius*(random()*Cell.MUTATION_FACTOR+1),
            "speed" :self.speed*(random()*Cell.MUTATION_FACTOR+1),
            "updateFrequency":self.updateFrequency*(random()*Cell.MUTATION_FACTOR+1),
            "foodEfficiency":self.foodEfficiency*(random()*Cell.MUTATION_FACTOR+1),
            "color": pygame.Color(
                pygame.math.clamp(self.color.r+randint(-100,100),0,255),
                pygame.math.clamp(self.color.g+randint(-100,100),0,255),
                pygame.math.clamp(self.color.b+randint(-100,100),0,255),
                ),
        }
        newCell=Cell(self.ctx ,self.position[0],self.position[1],genome)
        self.energy-=Cell.BASE_ENERGY
        pygame.event.post(pygame.event.Event(pygame.USEREVENT,{"name":"cell","status":"alive","cell":newCell}))
        pass

    def update(self,ctx,elapsedTime,foods):
        self.lifeDuration+=elapsedTime
        self.energy -=self.speed*elapsedTime*self.foodEfficiency

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
        finalspeed= self.speed * (10/self.radius)
        self.updateDirection(ctx)
        self.position = (self.position[0]+self.direction[0]*elapsedTime*finalspeed, self.position[1]+self.direction[1]*elapsedTime*finalspeed)
        pass
    
    def render(self,ctx):
        pygame.draw.circle(ctx,self.color,(self.position[0],self.position[1]),self.radius,3)
        pass