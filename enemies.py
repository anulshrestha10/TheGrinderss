import pygame
import random

# initialize the pygame
pygame.init()
# create screen
screen= pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Car Race Arcade")
icon = pygame.image.load('CarIcon.png')
pygame.display.set_icon(icon)

# Player
CarImg = pygame.image.load('car1.jpg')
grassimg = pygame.image.load("grass.jpg")
yellowstripe = pygame.image.load("yellowstripe.jpg")
whitestripe = pygame.image.load("whitestripe.jpg")
traffic_cone = pygame.image.load("cone.png")
backgroundimg = pygame.image.load('grass.jpg')

playerX = 380
playerY = 460
playerX_change = 0
# Game loop (infinite loop which makes sure game is always running)
def background():
    screen.blit(grassimg, (0, 0))
    screen.blit(grassimg, (700, 0))
    screen.blit(yellowstripe, (383, 0))
    screen.blit(yellowstripe, (383, 100))
    screen.blit(yellowstripe, (383, 200))
    screen.blit(yellowstripe, (383, 300))
    screen.blit(yellowstripe, (383, 400))
    screen.blit(yellowstripe, (383, 500))
    screen.blit(yellowstripe, (383, 600))
    screen.blit(whitestripe, (115, 0))
    screen.blit(whitestripe, (683, 0))
    screen.blit(traffic_cone, (90, 500))
    screen.blit(traffic_cone, (90, 400))
    screen.blit(traffic_cone, (90, 300))
    screen.blit(traffic_cone, (90, 200))
    screen.blit(traffic_cone, (90, 100))
    screen.blit(traffic_cone, (90, 20))
    screen.blit(traffic_cone, (90, 580))
    screen.blit(traffic_cone, (685, 500))
    screen.blit(traffic_cone, (685, 400))
    screen.blit(traffic_cone, (685, 300))
    screen.blit(traffic_cone, (685, 200))
    screen.blit(traffic_cone, (685, 100))
    screen.blit(traffic_cone, (685, 20))
    screen.blit(traffic_cone, (685, 580))


def playercar(x, y):
    screen.blit(CarImg, (x, y))

def enemycar(totalenemy_car_x, totalenemy_car_y, totalenemy_car):
    global enemycarimg
    if totalenemy_car == 0:
        enemycarimg = pygame.image.load("car2.png")
    elif totalenemy_car == 1:
        enemycarimg = pygame.image.load("car3.jpg")
    elif totalenemy_car == 2:
        enemycarimg = pygame.image.load("car4.png")
    elif totalenemy_car == 3:
        enemycarimg = pygame.image.load("car5.png")
    elif totalenemy_car == 4:
        enemycarimg = pygame.image.load("car6.png")
    elif totalenemy_car == 5:
        enemycarimg = pygame.image.load("car7.png")

    screen.blit(enemycarimg, (totalenemy_car_x, totalenemy_car_y))


# Game loop (infinite loop which makes sure game is always running)
def game_loop():
    playerX_change = 0
    playerX = 365
    playerY = 470
    running = True
    enemycar_speed = 6
    totalenemy_car=0
    totalenemy_car_x=random.randrange(150, 640)
    totalenemy_car_y = -750
    y2 = True
    crash= False
    while running:
        # RGB= Red, Green, Blue (goes from 0 to 255)
        screen.fill((119, 119, 119))
        background()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if keystroke is pressed check it is right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -1
                if event.key == pygame.K_RIGHT:
                    playerX_change = +1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
        # changing values (increase or decrease)
        playerX += playerX_change
        screen.fill((119, 119, 119))

        rel_y = y2 % backgroundimg.get_rect().width
        screen.blit(backgroundimg, (0, rel_y - backgroundimg.get_rect().width))
        screen.blit(backgroundimg, (700, rel_y - backgroundimg.get_rect().width))
        if rel_y < 800:
            screen.blit(backgroundimg, (0, rel_y))
            screen.blit(backgroundimg, (700, rel_y))
            screen.blit(yellowstripe, (383, rel_y))
            screen.blit(yellowstripe, (383, rel_y + 100))
            screen.blit(yellowstripe, (383, rel_y + 200))
            screen.blit(yellowstripe, (383, rel_y + 300))
            screen.blit(yellowstripe, (383, rel_y + 400))
            screen.blit(yellowstripe, (383, rel_y + 500))
            screen.blit(yellowstripe, (383, rel_y - 100))
            screen.blit(whitestripe, (115, rel_y - 200))
            screen.blit(whitestripe, (115, rel_y + 20))
            screen.blit(whitestripe, (115, rel_y + 30))
            screen.blit(whitestripe, (683, rel_y - 100))
            screen.blit(whitestripe, (683, rel_y + 20))
            screen.blit(whitestripe, (683, rel_y + 30))
            screen.blit(traffic_cone, (90, rel_y + 100))
            screen.blit(traffic_cone, (90, rel_y + 200))
            screen.blit(traffic_cone, (90, rel_y + 300))
            screen.blit(traffic_cone, (90, rel_y + 400))
            screen.blit(traffic_cone, (90, rel_y + 500))
            screen.blit(traffic_cone, (90, rel_y - 40))

            screen.blit(traffic_cone, (685, rel_y + 100))
            screen.blit(traffic_cone, (685, rel_y + 200))
            screen.blit(traffic_cone, (685, rel_y + 300))
            screen.blit(traffic_cone, (685, rel_y + 400))
            screen.blit(traffic_cone, (685, rel_y + 500))
            screen.blit(traffic_cone, (685, rel_y - 40))

        y2 += enemycar_speed

        totalenemy_car_y -= (enemycar_speed / 4)
        enemycar(totalenemy_car_x, totalenemy_car_y, totalenemy_car)
        totalenemy_car_y += enemycar_speed
        playercar(playerX, playerY)

        if playerX <= 95 or playerX >= 645:
            crash = True
            break
        if totalenemy_car_y >= 800:
            totalenemy_car_y = 0 - 56
            totalenemy_car_x = random.randint(150, 600)
            totalenemy_car = random.randint(0, 6)

        pygame.display.update()


game_loop()




