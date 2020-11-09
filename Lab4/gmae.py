import pygame
from pygame.draw import *
from random import randint
pygame.init()

# Setting game parameters

FPS = 30
x_size = 1200
y_size = 700
screen = pygame.display.set_mode((x_size, y_size))

# Creating colors

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# Setting parameters of targets and number of them

global balls_coordinates
global number_of_balls
global balls_movement
global squares_movement
global number_of_squares
global squares_coordinates


def new_square(i):
    """Draws a new square.
       x - horizontal coordinate of the square
       y - vertical coordinate of the square
       r - radius of a circle inscribed in a square
       velocity - speed of the square
    """
    x = randint(100, x_size - 100)
    y = randint(100, y_size - 100)
    r = randint(10, 50)
    color = COLORS[randint(0, 5)]
    squares_coordinates[i] = [x, y, r, color]
    rect(screen, color, [x, y, r, r])


def new_ball(i, x, y, r, velocity):
    """Draws a new ball.
       x - horizontal coordinate of the ball
       y - vertical coordinate of the ball
       r - ball radius
       velocity - speed of the ball
     """
    color = COLORS[randint(0, 5)]
    balls_coordinates[i] = [x, y, r, color]
    balls_movement[i] = [randint(-5, 5), velocity]
    circle(screen, color, (x, y), r)


def score_count_balls(first_coordinate, second_coordinate):
    """Checks if you clicked on ball or not."""
    flag = -1
    for i in range(number_of_balls):
        x = balls_coordinates[i][0]
        y = balls_coordinates[i][1]
        r = balls_coordinates[i][2]
        if (first_coordinate - x) ** 2 + (second_coordinate - y) ** 2 <= r * r:
            flag = i
    return flag


def score_count_squares(first_coordinate, second_coordinate):
    """Checks if you clicked on square or not."""
    flag = -1
    for i in range(number_of_squares):
        x = squares_coordinates[i][0]
        y = squares_coordinates[i][1]
        r = squares_coordinates[i][2]
        if (first_coordinate - x) ** 2 + (second_coordinate - y) ** 2 <= r * r:
            flag = i
    return flag


def squares_coordinates_update():
    """Updates square coordinates according to moving type.

    If squares are not out of display we change their coordinates using formula x+=velocity, y+=k*velocity and
    x is changed based on current velocity which is set in squares_movement array (3rd element). Then checking
    if the square coordinates would be out of range in the next game moment.
    """
    for i in range(number_of_squares):
        x = squares_coordinates[i][0]
        y = squares_coordinates[i][1]
        r = squares_coordinates[i][2]
        vx = squares_movement[i][0]
        vy = squares_movement[i][1]
        vr = squares_movement[i][2]
        if x + vx + r > screen_x:
            squares_movement[i][0] = -vx
            squares_movement[i][1] = -vy
            squares_movement[i][2] = -vr
        elif y + vx ** 2 * vy + vr + r > screen_y:
            squares_movement[i][0] = -vx
            squares_movement[i][1] = -vy
            squares_movement[i][2] = -vr
        elif x + vx - r < 0:
            squares_movement[i][0] = -vx
            squares_movement[i][1] = -vy
            squares_movement[i][2] = -vr
        elif y + vx ** 2 * vy + vr - r < 0:
            squares_movement[i][0] = -vx
            squares_movement[i][1] = -vy
            squares_movement[i][2] = -vr
        squares_coordinates[i][0] = x + vx
        squares_coordinates[i][1] = y + vx ** 2 * vy + vr
        rect(screen, squares_coordinates[i][3], (x, y, r, r))


def balls_coordinates_update():
    """Updates coordinates of balls according to moving type.

    If balls are not out of display we change their coordinates using formula x+=velocity, y+=k*velocity and
    x is changed based on current velocity which is set in balls_movement array (3rd element). Then checking
    if the ball coordinates would be out of range in the next game moment.
    """
    for i in range(number_of_balls):
        x = balls_coordinates[i][0]
        y = balls_coordinates[i][1]
        r = balls_coordinates[i][2]
        vx = balls_movement[i][0]
        vy = balls_movement[i][1]
        if x + vy + r > screen_x:
            balls_movement[i][1] = - vy
        elif y + vx * vy + r > screen_y:
            balls_movement[i][1] = - vy
        elif y + vx * vy + r > screen_y:
            balls_movement[i][1] = - vy
        elif x + vy - r < 0:
            balls_movement[i][1] = - balls_movement[i][1]
        elif y + vx * vy - r < 0:
            balls_movement[i][1] = - vy

        balls_coordinates[i][0] += vy
        balls_coordinates[i][1] += vx * vy
        circle(screen, balls_coordinates[i][3], (x, y), r)


# Main body of the function

pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
flag = -2
hits_in_row = 0

# Setting parameters of the game

screen_x = x_size
screen_y = y_size
misses = 10
number_of_balls = 7
number_of_squares = 3
squares_movement = [[]] * number_of_squares
squares_coordinates = [[]] * number_of_squares
balls_movement = [[]] * number_of_balls
balls_coordinates = [[]] * number_of_balls
while not finished:
    clock.tick(FPS)

    # Making starting screen

    if flag == -2:
        font = pygame.font.Font(None, 62)
        text = font.render("Добро пожаловать в мою игру ", 1, (255, 255, 255))
        text1 = font.render("Нажмите кнопку мыши для продолжения ", 1, (255, 255, 255))
        place = text.get_rect(center=(int(x_size / 2), int(y_size / 8)))
        place1 = text.get_rect(center=(int(x_size / 2), int(y_size / 8) + 70))
        screen.blit(text, place)
        screen.blit(text1, place1)
        pygame.display.update()

    # Creating targets for the game

    elif flag == -1:
        for i in range(number_of_balls):
            new_ball(i, randint(100, screen_x - 100), randint(100, screen_y - 100),
                     randint(10, 50), 1)
        print(balls_coordinates)
        for i in range(number_of_squares):
            squares_movement[i] = [randint(-5, 5), randint(-2, 2), randint(-5, 5)]
        for i in range(number_of_squares):
            new_square(i)
        flag = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if flag == 1:
                pass
            elif flag == -2:
                flag = -1
            elif flag == 0:
                hit_ball = score_count_balls(event.pos[0], event.pos[1])
                hit_square = score_count_squares(event.pos[0], event.pos[1])
                if hit_ball > -1:
                    hits_in_row += 1
                    score += max(1,
                                 int(abs(balls_movement[hit_ball][1]) ** 2 / 10 / balls_coordinates[hit_ball][2] * 40))
                    print(score)
                    x_of_newball = randint(100, x_size - 100)
                    y_of_newball = randint(100, y_size - 100)
                    radius_of_newball = randint(10, 50)
                    new_ball(hit_ball, x_of_newball, y_of_newball, radius_of_newball, abs(balls_movement[i][1]) + 1)
                elif hit_square > -1:
                    hits_in_row += 1
                    score += 5
                    print(score)
                    new_square(hit_square)

                else:
                    misses -= 1
                    hits_in_row = 0
                if misses == 0:
                    screen.fill(BLACK)
                    font = pygame.font.Font(None, 92)
                    text = font.render("GAME OVER", 1, (255, 255, 255))
                    font = pygame.font.Font(None, 62)
                    text1 = font.render("Ваш результат: " + str(score), 1, (255, 255, 255))
                    place = text.get_rect(center=(int(x_size / 2), int(y_size / 2)))
                    place1 = text.get_rect(center=(int(x_size / 2) + 7, int(y_size / 2) + 70))
                    screen.blit(text, place)
                    screen.blit(text1, place1)
                    pygame.display.update()
                    flag = 1

                    # Updating Records table

                    with open("Records_Table.txt", 'r') as Records_Table:
                        Previous_Results = list(Records_Table.read().split('\n'))
                        Previous_Results.pop()
                        Previous_Results = list(map(int, Previous_Results))
                        Previous_Results.sort()
                        for i in range(len(Previous_Results)):
                            if Previous_Results[i] > score:
                                break
                        text2 = font.render("Вы лучше " + str(i) + " игроков", 1, (255, 255, 255))
                        place2 = text.get_rect(center=(int(x_size / 2) - 10, int(y_size / 2) + 120))
                        screen.blit(text2, place2)
                        pygame.display.update()
                    with open("Records_Table.txt", 'a+') as Records_Table:
                        Records_Table.write(str(score) + '\n')
    #  Main stage of the game

    if flag == 0:
        if hits_in_row >= 5:
            misses += 1
            hits_in_row = 0
        balls_coordinates_update()
        squares_coordinates_update()
        pygame.display.update()
        screen.fill(BLACK)

        # Writing the score

        font = pygame.font.Font(None, 62)
        text = font.render(str(score), 1, (255, 255, 255))
        place = text.get_rect(center=(int(x_size / 2), int(y_size / 8)))
        text1 = font.render(str(misses), 1, (255, 255, 255))
        place1 = text.get_rect(center=(int(x_size / 2), int(y_size / 1.1)))
        screen.blit(text, place)
        screen.blit(text1, place1)
pygame.quit()
