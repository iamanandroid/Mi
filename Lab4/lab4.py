import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
x_size=1200
y_size=900
screen = pygame.display.set_mode((x_size, y_size))
global scrx,scry
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
#Setting parametres of targets and number of them
global balls_coordinates
global number_of_balls
global balls_movement
global squares_movement
global number_of_squares
global squares_coordinates
def new_square(i):
    '''рисует новый square '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 50)
    color = COLORS[randint(0, 5)]
    squares_coordinates[i]=[x,y,r,color]
    rect(screen, color, [x, y,r,r])
def new_ball(i):
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 50)
    color = COLORS[randint(0, 5)]
    balls_coordinates[i]=[x,y,r,color]
    circle(screen, color, (x, y), r)
def score_count_balls(first_coordinate,second_coordinate):
    ''' Checks if you clicked on ball or not'''
    flag=-1
    for i in range(number_of_balls):
        #print(balls_coordinates)
        x=balls_coordinates[i][0]
        y=balls_coordinates[i][1]
        r=balls_coordinates[i][2]
        if (first_coordinate-x)**2+(second_coordinate-y)**2<=r*r:
            flag=i
    return flag
def score_count_squares(first_coordinate,second_coordinate):
    ''' Checks if you clicked on ball or not'''
    flag=-1
    for i in range(number_of_squares):
        #print(balls_coordinates)
        x=squares_coordinates[i][0]
        y=squares_coordinates[i][1]
        r=squares_coordinates[i][2]
        if (first_coordinate-x)**2+(second_coordinate-y)**2<=r*r:
            flag=i
    return flag
def squares_coordinates_update():
    for i in range(number_of_squares):
        r=squares_coordinates[i][2]
        if squares_coordinates[i][0] + squares_movement[i][0] + r > scrx or squares_coordinates[i][1] + squares_movement[i][0]**2*squares_movement[i][1]+squares_movement[i][2] + r > scry or \
                squares_coordinates[i][0] + squares_movement[i][0] - r < 0 or squares_coordinates[i][1] + squares_movement[i][0]**2*squares_movement[i][1]+squares_movement[i][2] - r < 0:
            squares_movement[i][0] = -squares_movement[i][0]
            squares_movement[i][1] = - squares_movement[i][1]
            squares_movement[i][2]=-squares_movement[i][2]
        squares_coordinates[i][0] += squares_movement[i][0]
        squares_coordinates[i][1] += squares_movement[i][0]**2*squares_movement[i][1]+squares_movement[i][2]
        rect(screen, squares_coordinates[i][3], (squares_coordinates[i][0], squares_coordinates[i][1],squares_coordinates[i][2],squares_coordinates[i][2]))
    pygame.display.update()
    screen.fill(BLACK)
def balls_coordinates_update():
    '''Updates coordinates of balls according to moving type'''
    for i in range(number_of_balls):
        #print(balls_coordinates)
        #print(i)
        r=balls_coordinates[i][2]
        if balls_coordinates[i][0]+balls_movement[i][0]+r>scrx or balls_coordinates[i][1]+balls_movement[i][1]+r>scry or \
                balls_coordinates[i][0]+balls_movement[i][0]-r<0 or  balls_coordinates[i][1]+balls_movement[i][1]-r<0:
            balls_movement[i][0]=- balls_movement[i][0]
            balls_movement[i][1]=- balls_movement[i][1]
        balls_coordinates[i][0]+=balls_movement[i][0]
        balls_coordinates[i][1]+=balls_movement[i][1]
        circle(screen,balls_coordinates[i][3],(balls_coordinates[i][0],balls_coordinates[i][1]),balls_coordinates[i][2])
    #screen.fill(BLACK)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
score=0
#Setting paramtrrs of the game
scrx=x_size
scry=y_size
number_of_balls=7
number_of_squares=3
squares_movement=[[]]*number_of_squares
squares_coordinates=[[]]*number_of_squares
balls_movement=[[]]*number_of_balls
balls_coordinates=[[]]*number_of_balls
#creating targets
for i in range(number_of_balls): balls_movement[i]=[randint(-5,5),randint(-10,10)]
for i in range (number_of_balls): new_ball(i)
print (balls_coordinates)
for i in range(number_of_squares):squares_movement[i]=[randint(-5,5),randint(-2,2),randint(-5,5)]
for i in range(number_of_squares): new_square(i)
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            hit_ball=score_count_balls(event.pos[0],event.pos[1])
            hit_square=score_count_squares(event.pos[0],event.pos[1])
            if hit_ball>-1:
                score+=1
                print(score)
                new_ball(hit_ball)
            if hit_square>-1:
                score+=5
                print(score)
                new_square(hit_square)

    balls_coordinates_update()
    squares_coordinates_update()
pygame.quit()