import pygame
import os
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init()
font_size = 40
my_font = pygame.font.SysFont('arial', font_size)

FPS = 30
time_to_play = 20
time = 0
x_size = 1200
y_size = 900
screen = pygame.display.set_mode((x_size, y_size))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


# Add more balls targets
"""
in following functions:
    dx: movement in pixels by X axes per tick
    dy: movement in pixels by Y axes per tick
"""


def new_balls(balls_number):

    '''
    :param balls_number: number of balls
    :return: nothing
    '''

    for i in range(balls_number):
        x_coordinate = randint(100, 1100)
        y_coordinate = randint(100, 800)
        radius = randint(30, 50)
        dx = randint(-8, 8)
        dy = randint(-8, 8)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x_coordinate, y_coordinate), radius)
        balls.append((x_coordinate, y_coordinate, radius, dx, dy, color))


# Add more face targets
def new_face(faces_number):

    '''
    :param faces_number: number of faces
    :return: nothing
    '''
    for i in range(faces_number):
        x_coordinate = randint(100, 700)
        y_coordinate = randint(100, 500)
        radius = randint(60, 100)
        dx = randint(-16, 16)
        dy = randint(-16, 16)
        g = 2

        img = pygame.transform.scale(image, (radius, radius))
        screen.blit(img, (x_coordinate, y_coordinate))

        faces.append((x_coordinate, y_coordinate, radius, dx, dy, g))


# Moving of targets with every frame
def new_frame():
    # Moving of balls
    for i in range(number_of_balls):
        x_coordinate, y_coordinate, r, dx, dy, color = balls[i]
        (x_coordinate, y_coordinate) = (x_coordinate + dx, y_coordinate + dy)
        if x_coordinate - r < 0 or x_coordinate + r > 1200:
            dx = -dx
        if y_coordinate - r < 0 or y_coordinate + r > 900:
            dy = -dy
        balls[i] = (x_coordinate, y_coordinate, r, dx, dy, color)
    for i in range(number_of_balls):
        circle(screen, balls[i][5], (balls[i][0], balls[i][1]), balls[i][2])

    # Moving of faces
    for i in range(number_of_faces):
        x_coordinate, y_coordinate, r, dx, dy, g = faces[i]
        (x_coordinate, y_coordinate) = (x_coordinate + dx, y_coordinate + dy + g/2)
        dy += g
        if x_coordinate < 0 or x_coordinate + r > x_size:
            dx = -dx
        if y_coordinate < 0 or y_coordinate + r > y_size:
            dy = -dy
        faces[i] = (x_coordinate, y_coordinate, r, dx, dy, g)
    for i in range(number_of_faces):
        img = pygame.transform.scale(image, (faces[i][2], faces[i][2]))
        screen.blit(img, (faces[i][0], faces[i][1]))


# Check if player hit any targets
def click(cur_event):
    # Check if player hit any ball
    for i in range(number_of_balls):
        if (cur_event.pos[0]-balls[i][0])**2 + (cur_event.pos[1]-balls[i][1])**2 < balls[i][2]**2:
            global hits
            hits += 1
            rect(screen, WHITE, (0, 0, x_size, y_size))
            balls.pop(i)
            new_balls(1)
            break

    # Check if player hit any face
    for i in range(number_of_faces):
        if 0 < cur_event.pos[0] - faces[i][0] < faces[i][2] and 0 < cur_event.pos[1] - faces[i][1] < faces[i][2]:
            hits += 5
            rect(screen, WHITE, (0, 0, x_size, y_size))
            faces.pop(i)
            new_face(1)
            break


# Make a results table
def results_table():
    # Read existing table
    output = open("output.txt", 'r+')
    file = output.readlines()
    # Add new result
    file.append(str(hits) + " " + input() + '\n')
    for line in file:
        line = line.split(' ')
    file.sort(reverse=True)

    # Rewrite results
    output.seek(0)
    for line in file:
        output.write(line)
    output.close()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

hits = 0
balls = []
number_of_balls = 20
new_balls(number_of_balls)

faces = []
number_of_faces = 10

# image of "face" targets
image = pygame.image.load(os.path.join('face.png'))
new_face(number_of_faces)

while not finished:
    clock.tick(FPS)
    time += 1
    if time >= FPS * time_to_play:
        screen.fill(BLACK)

        text = 'You lost. Enter your name'
        text_surface = my_font.render(text, False, WHITE)
        screen.blit(text_surface, (x_size / 2-len(text) * 8, y_size / 2))
        pygame.display.update()
        if time == FPS * time_to_play:
            results_table()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    else:
        # Displaying your current score and time left to play
        text_surface = my_font.render(str(hits), False, WHITE)
        screen.blit(text_surface, (x_size / 2, y_size / 1.1))

        text_surface = my_font.render(str(20 - time // 30), False, WHITE)
        screen.blit(text_surface, (x_size / 2, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click(event)

        new_frame()
        pygame.display.update()
        screen.fill(BLACK)

pygame.quit()
