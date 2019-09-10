
import pygame
import random
from random import randint
from random import seed
from time import time

#self.color
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

screen_size=[1500,800]

color_list=[black, red, green, blue]

unit_length=40
seed(int(time()))

def get_random(i):
    random=randint(0,i-1)
    return random

class Black():
    
    def __init__(self, x, y):
        self.x = 0
        self.y = 0

    def draw_mino(self, x, y, color, screen):
        pygame.draw.rect(screen, color, [x,y, unit_length, unit_length] )

class Omino(Black):

    def __init__(self):
        self.hash_map = [[0,0,0,0],
                         [0,1,1,0],
                         [0,1,1,0],
                         [0,0,0,0]]
        self.xpos=40
        self.ypos=0
        self.width = unit_length * 2
        self.color=red
        self.rotation = 0

    
    def set_xpos(self, new_xpos):
        self.xpos = new_xpos

    def mov_xpos(self, mov_xpos):
        self.xpos = self.xpos + mov_xpos
        
    def set_ypos(self, new_ypos):
        self.ypos = new_ypos
        
    def mov_ypos(self, mov_ypos):
        self.ypos = self.ypos + mov_ypos

    def get_xpos(self):
        return self.xpos

    def get_ypos(self):
        return self.ypos

    
    def get_width(self):

        return self.width
    

    def set_color(self, color):
        self.color = color
            
    def set_rotation(self, mov_rotation):
        self.rotation = mov_rotation

    def draw(self,screen):
        #draw Tmino
        for g in range(0,len(self.hash_map[self.rotation])):
            for j in range(0, len(self.hash_map[self.rotation][g])):
                if self.hash_map[self.rotation][g][j] == 1:
                    self.draw_mino(j*unit_length, g*unit_length, self.color,screen)
                

    def get_length(self):        
        return 2


class Zmino(Black):
    
    def __init__(self):
        self.hash_map = [[[1,1,0,0],
                          [0,1,1,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                         [[0,0,1,0],
                          [0,1,1,0],
                          [0,1,0,0],
                          [0,0,0,0]]]
        self.xpos=40
        self.color=red
        self.ypos=0
        self.width = unit_length * 3
        self.rotation = 0

    def set_xpos(self, new_xpos):
        self.xpos = new_xpos

    def mov_xpos(self, mov_xpos):
        self.xpos = self.xpos + mov_xpos
        
    def set_ypos(self, new_ypos):
        self.ypos = new_ypos
        
    def mov_ypos(self, mov_ypos):
        self.ypos = self.ypos + mov_ypos
        
    def get_xpos(self):
        return self.xpos
        
    def get_ypos(self):
        return self.ypos
        
    def get_width(self):

        return self.width
    

    def set_color(self, color):
        self.color = color
            
        
    def set_rotation(self, mov_rotation):
        self.rotation = mov_rotation

    def draw(self,screen):
        #draw Tmino
        for g in range(0,len(self.hash_map[self.rotation])):
            for j in range(0, len(self.hash_map[self.rotation][g])):
                if self.hash_map[self.rotation][g][j] == 1:
                    self.draw_mino(j*unit_length, g*unit_length, self.color,screen)
        
    def get_length(self):    
        return 2

class Lmino(Black):
    def __init__(self):
        self.hash_map = [[[1,0,0,0],
                          [1,0,0,0],
                          [1,1,0,0],
                          [0,0,0,0]],
                        [[1,1,1,0],
                         [1,0,0,0],
                         [0,0,0,0],
                         [0,0,0,0]],
                        [[0,1,1,0],
                         [0,0,1,0],
                         [0,0,1,0],
                         [0,0,0,0]],
                        [[0,0,0,0],
                         [0,0,1,0],
                         [1,1,1,0],
                         [0,0,0,0]]]
        self.xpos=40
        self.ypos=0
        self.color=red
        self.width = unit_length * 2
        self.rotation = 0

    
    def set_xpos(self, new_xpos):
        self.xpos = new_xpos

    def mov_xpos(self, mov_xpos):
        self.xpos = self.xpos + mov_xpos
        
    def set_ypos(self, new_ypos):
        self.ypos = new_ypos
        
    def mov_ypos(self, mov_ypos):
        self.ypos = self.ypos + mov_ypos
        
    def get_xpos(self):
        return self.xpos
        
    def get_ypos(self):
        return self.ypos

    def get_width(self):

        return self.width
    

    def set_color(self, color):
        self.color = color
            
    
    def set_rotation(self, mov_rotation):
        self.rotation = mov_rotation

    def draw(self,screen):
        #draw Tmino
        for g in range(0,len(self.hash_map[self.rotation])):
            for j in range(0, len(self.hash_map[self.rotation][g])):
                if self.hash_map[self.rotation][g][j] == 1:
                    self.draw_mino(j*unit_length, g*unit_length, self.color,screen)
        
    def get_length(self):    
        return 3

class Imino(Black):

    def __init__(self):
        self.hash_map = [[[0,1,0,0],
                          [0,1,0,0],
                          [0,1,0,0],
                          [0,1,0,0]],
                         [[0,0,0,0],
                          [1,1,1,1],
                          [0,0,0,0],
                          [0,0,0,0]]]
        self.xpos=40
        self.ypos=0
        self.color=red
        self.width = unit_length
        self.rotation = 0

    def set_color(self, color):
        self.color = color

    def set_xpos(self, new_xpos):
        self.xpos = new_xpos

    def mov_xpos(self, mov_xpos):
        self.xpos = self.xpos + mov_xpos
        
    def set_ypos(self, new_ypos):
        self.ypos = new_ypos
        
    def mov_ypos(self, mov_ypos):
        self.ypos = self.ypos + mov_ypos
        
    def get_width(self):
    
        return self.width
    
    def get_xpos(self):
        return self.xpos
        
    def get_ypos(self):
        return self.ypos

    def set_rotation(self, mov_rotation):
        self.rotation = mov_rotation

    def draw(self,screen):
        #draw Tmino
        for g in range(0,len(self.hash_map[self.rotation])):
            for j in range(0, len(self.hash_map[self.rotation][g])):
                if self.hash_map[self.rotation][g][j] == 1:
                    self.draw_mino(j*unit_length, g*unit_length, self.color,screen)
        
    def get_length(self):
        return 4

class Tmino(Black):

    def __init__(self):
        self.hash_map = [[[1,1,1,0],
                          [0,1,0,0],
                          [0,0,0,0],
                          [0,0,0,0]],
                         [[0,0,1,0],
                          [0,1,1,0],
                          [0,0,1,0],
                          [0,0,0,0]],
                         [[0,0,0,0],
                          [0,1,0,0],
                          [1,1,1,0],
                          [0,0,0,0]],
                         [[1,0,0,0],
                          [1,1,0,0],
                          [1,0,0,0],
                          [0,0,0,0]]]
        self.xpos=40
        self.ypos=0
        self.color=red
        self.width = unit_length * 3
        self.length_list=[]
        self.rotation=0

    def get_width(self):

        return self.width
    
    def set_xpos(self, new_xpos):
        self.xpos = new_xpos

    def mov_xpos(self, mov_xpos):
        self.xpos = self.xpos + mov_xpos
        
    def set_ypos(self, new_ypos):
        self.ypos = new_ypos
        
    def mov_ypos(self, mov_ypos):
        self.ypos = self.ypos + mov_ypos
        
    def get_xpos(self):
        return self.xpos
        
    def get_ypos(self):
        return self.ypos

    def set_color(self, color):
        self.color = color

    def set_rotation(self, mov_rotation):
        self.rotation = mov_rotation

    def draw(self,screen):
        #draw Tmino
        for g in range(0,len(self.hash_map[self.rotation])):
            for j in range(0, len(self.hash_map[self.rotation][g])):
                if self.hash_map[self.rotation][g][j] == 1:
                    self.draw_mino(j*unit_length, g*unit_length, self.color,screen)
        
    
    def get_length(self):
        return 3