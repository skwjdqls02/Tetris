
import pygame
import random
from random import randint
from random import seed
from time import time
from block import unit_length, Imino, Lmino, Omino, Zmino, Tmino

#color
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
color_list=[black, red, green, blue]

seed(int(time()))

screen_size=[1500,800]

title="TETRIS"

def mino_collision(mino):

    falling_mino = mino[-1]
    for i in range(0, len(mino)-1):
        low = -1
        for g in range(0, mino[i].get_width()/unit_length):
            if falling_mino.get_xpos() == g:
                pass



def get_random(i):
    random=randint(0,i-1)
    return random

#def check_down(mino):
#        return False

#check touch the wall
def wall_collision(mino):
    if mino.get_xpos() <= 0:
        mino.set_xpos(0)
    
    elif mino.get_xpos() + mino.get_width() > screen_size[0]:
        mino.set_xpos(screen_size[0] - mino.get_width())
    
    elif mino.get_ypos() + (mino.get_length() * unit_length) >= screen_size[1]:
        mino.set_ypos(screen_size[1] - (mino.get_length() * unit_length))
    
    return mino

#check touch the ground 
def ground_collision(mino):
    falling = True
    length=mino.get_length()
    if mino.get_ypos() + unit_length * length >= screen_size[1]:
        falling = False
    return falling

def main():
    pygame.init()

    FPS_CLOCK=pygame.time.Clock()

    screen=pygame.display.set_mode(screen_size)
    pygame.display.set_caption(title)

    done=False
    class_list=[Imino, Lmino, Omino, Tmino, Zmino]
    #random=get_random(len(class_list))
    old_mino=[]
    falling=False

    while not done:
        
        buttons_list=[]

        # event check.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed=pygame.key.get_pressed()
                buttons = [pygame.key.name(k) for k,v in enumerate(pressed) if v]
                for i in buttons:
                    buttons_list.append(i)
            elif event.type == pygame.QUIT:
                done= True
        
        # background color.
        screen.fill(white)
        rot = int(input("Number: "))
        if rot == 4:
            break
        # draw mino.
        a = Omino()
        a.set_rotation(rot)
        a.draw(screen)
            #b = Zmino()
        #b.draw(screen)
        #c = Imino()
        #c.draw(screen)
        #d = Tmino()
        #d.set_rotation(rot)
        #d.draw(screen)
        #e = Lmino()
        #e.draw(screen)
        #if not falling:
        #    random_color=color_list[get_random(len(color_list))]
        #    random_mino=class_list[get_random(len(class_list))]()
        #    random_mino.set_color(random_color)
        #    old_mino.append(random_mino)
        #    
        #    for i in old_mino:
        #        i.draw(screen)
        #    falling= True
#
        #else:
        #    #down_bool = True
#
        #    # mino drop
        #    old_mino[-1].mov_ypos(5)
#
        #    # move mino
        #    if buttons_list == ['right']:
        #        old_mino[-1].mov_xpos(unit_length)
        #        old_mino[-1] = wall_collision(old_mino[-1])
#
        #    elif buttons_list == ["left"]:
        #        old_mino[-1].mov_xpos(-unit_length)
        #        old_mino[-1] = wall_collision(old_mino[-1])
#
        #    elif buttons_list == ["down"]:
        #        old_mino[-1].mov_ypos(10)
        #        old_mino[-1] = wall_collision(old_mino[-1])
        #    
        #    for i in old_mino:
        #        i.draw(screen)
#
        ##check touch the ground 
        #falling = ground_collision(old_mino[-1])
#
        FPS_CLOCK.tick(25)
        pygame.display.flip()
    pygame.quit()


if __name__ =="__main__":
    main()