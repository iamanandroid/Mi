import pygame
import numpy as np
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen,(255,255,0),(200,200),150)
circle(screen,(255,0,0),(130,150),40)
circle(screen,(255,0,0),(280,150),40)
circle(screen,(0,0,0),(130,150),20)
circle(screen,(0,0,0),(280,150),20)
line(screen, (0,0,0), (130+int(2*40*np.sqrt(1/2)),150), (130-20,150-int(2*40*np.sqrt(1/2))-20), 20)
line(screen, (0,0,0), (280-int(2*40*np.sqrt(1/2)),150), (280+20,150-int(2*40*np.sqrt(1/2))-20), 20)
rect(screen,(0,0,0),(130,290,140,15))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
