import pygame
import math
import numpy as np
from pygame.draw import *
def trian(x,y,size,color,screen):
    lin=int(size/2/np.cos(math.radians(30)))
    polygon(screen,color,[(x,y-int(lin)),(x+int(size/2),y+int(lin/2)),(x-int(size/2),y+int(lin/2))])
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255,255,255))
surf = pygame.Surface((400, 400))
#screen.blit(surf,(0,0))
#surf.set_alpha(255)
trian(200,200,250,(255,255,100),screen)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
