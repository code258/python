import random
import pygame
import sys

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
TRANSPARENT = (0, 0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
screen.fill(WHITE)

background = pygame.image.load("sprites/zbackground.png")
down = pygame.image.load("sprites/adown.png")
up = pygame.image.load("sprites/aup.png")
ax = SCREEN_WIDTH + 70
pos_x = 0
location = []
interval = SCREEN_WIDTH / 3 + 100
random1, random2 = 0, 0
score = 0


class FlappyBird(object):
    def __init__(self):
        self.image = pygame.image.load('sprites/flappy_bird.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))

    def draw(self, x, y):
        screen.blit(self.image, (x, y))


def moveB(pos_x, background):
    pos_x -= 3
    if pos_x < -700:
        pos_x = 0
    screen.blit(background, [pos_x, 0])
    screen.blit(background, [pos_x + 700, 0])
    return pos_x


def crashed():
    font = pygame.font.SysFont("arial", 40)
    text = font.render("You were crashed by the obstacle.", True, BLACK)
    screen.blit(text, (75, 200))
    pygame.quit()
    sys.exit()


random_y = random.randrange(-400, -100)
for i in range(3):
    location.append([ax, random_y])
    ax = -75


flappy_bird = FlappyBird()
flappy_birds = []


def game_loop():
    x, y = 300, 200
    speed = 1
    check = 0
    global pos_x
    global interval
    global score
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flappy_bird.draw(x, y)
                    speed = -3
        if y < -200 or y > 500:
            crashed()
        y += speed
        speed += 0.1
        pos_x = moveB(pos_x, background)
        for i in range(3):
            if location[i][0] < -70:
                random_y = random.randrange(-400, -100)
                location[i] = [location[(i + 2) % 3][0] + interval, random_y]
            location[i][0] -= 3
            screen.blit(down, [location[i][0], location[i][1]])
            screen.blit(up, [location[i][0], location[i][1] + 570])
            if location[i][0] - 10 < x < location[i][0] + 10:
                if y > location[i][1] + 495 or y < location[i][1] + 400:
                    crashed()
        flappy_bird.draw(x, y)
        pygame.time.delay(10)
        check += 1
        if check == 120:
            check = 0
            score += 1
        font = pygame.font.SysFont("arial", 25)
        text = font.render("Score: {}".format(score), True, BLACK)
        screen.blit(text, (3, 5))
        pygame.display.update()
        screen.fill(WHITE)
        clock.tick(59)


game_loop()
        