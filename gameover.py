import pygame
import random
import math
import time
import sys

# initialize the pygame
pygame.init()
# create screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Car Race Arcade")
icon = pygame.image.load('CarIcon.png')
pygame.display.set_icon(icon)

# Player
CarImg = pygame.image.load('car1.jpg')
grassimg = pygame.image.load("grass.png")
yellowstripe = pygame.image.load("yellowstripe.png")
whitestripe = pygame.image.load("whitestripe.png")
traffic_cone = pygame.image.load("cone.png")
backgroundimg = pygame.image.load('grass.png')

#images used for backgrounds
entryimg = pygame.image.load('background_entry.jpg')
instruction_part = pygame.image.load('background2.png')


playerX = 380
playerY = 460
playerX_change = 0

over_font = pygame.font.Font('freesansbold.ttf', 74)
over_text = over_font.render("Crashed! Game Over", 2, (245, 66, 66))

# function for texts
def text_object(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

font = pygame.font.Font('freesansbold.ttf', 20)


def show_score(x, y):
    score1 = font.render("Score : " + str(score), True, (1, 1, 1))
    screen.blit(score1, (10, 10))
    passed = font.render("Car Passed : " + str(car_passed), True, (1, 1, 1))
    screen.blit(passed, (10, 40))

def entrypage_loop():
    entry = True

    while entry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(entryimg, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', 70)
        font1 = pygame.font.Font('freesansbold.ttf', 35)
        show_font = font.render('Car Race Arcade', True, (235, 52, 52))

        screen.blit(show_font, (120, 100))
        pygame.draw.rect(screen, (0, 200, 0), (320, 260, 150, 50))
        pygame.draw.rect(screen, (0, 0, 200), (300, 360, 190, 50))
        pygame.draw.rect(screen, (0, 120, 0), (320, 460, 150, 50))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > 321 and mouse[0] < 470 and mouse[1] > 260 and mouse[1] < 310:
            pygame.draw.rect(screen, (0, 250, 0), (320, 260, 150, 50))
            if click == (True, 0, 0):
                game_loop()

        if mouse[0] > 300 and mouse[0] < 490 and mouse[1] > 360 and mouse[1] < 410:
            pygame.draw.rect(screen, (0, 0, 255), (300, 360, 190, 50))
            if click == (True, 0, 0):
                instructions()


        if mouse[0] > 321 and mouse[0] < 470 and mouse[1] > 460 and mouse[1] < 510:
            pygame.draw.rect(screen, (0, 180, 0), (320, 460, 150, 50))
            if click == (True, 0, 0):
                pygame.quit()
                quit()

        smallText = pygame.font.Font('freesansbold.ttf', 25)
        textSurface, textRect = text_object("START", smallText)
        textRect.center = ((320 + 73)), (260 + 27)
        screen.blit(textSurface, textRect)

        textSurface, textRect = text_object("How to Play?", smallText)
        textRect.center = ((320 + 73)), (360 + 27)
        screen.blit(textSurface, textRect)

        textSurface, textRect = text_object("EXIT", smallText)
        textRect.center = ((320 + 73)), (460 + 27)
        screen.blit(textSurface, textRect)

        pygame.display.update()


def instructions():
    instruction = True
    while instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(instruction_part, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = text_object("This is a car race game in which you need to dodge the incoming vehicle",
                                         smalltext)
        textRect.center = ((430), (230))

        TextSurf, TextRect = text_object("INSTRUCTIONS", largetext)
        TextRect.center = ((400), (100))
        screen.blit(TextSurf, TextRect)
        screen.blit(textSurf, textRect)
        stextSurf, stextRect = text_object("ARROW LEFT : MOVE LEFT ", smalltext)
        stextRect.center = ((400), (400))
        hTextSurf, hTextRect = text_object("ARROW RIGHT : MOVE  RIGHT ", smalltext)
        hTextRect.center = ((400), (450))

        ptextSurf, ptextRect = text_object("P : PAUSE  ", smalltext)
        ptextRect.center = ((400), (350))
        sTextSurf, sTextRect = text_object("CONTROLS", mediumtext)
        sTextRect.center = ((400), (300))
        screen.blit(sTextSurf, sTextRect)
        screen.blit(stextSurf, stextRect)
        screen.blit(hTextSurf, hTextRect)
        screen.blit(ptextSurf, ptextRect)

        pygame.draw.rect(screen, (0, 200, 0), (550, 500, 150, 50))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > 550 and mouse[0] < 700 and mouse[1] > 500 and mouse[1] < 550:
            pygame.draw.rect(screen, (0, 250, 0), (550, 500, 150, 50))
            if click == (True, 0, 0):
                entrypage_loop()

        smallText = pygame.font.Font('freesansbold.ttf', 25)
        textSurface, textRect = text_object("Back", smallText)
        textRect.center = ((550 + 73)), (500 + 27)
        screen.blit(textSurface, textRect)

        pygame.display.update()


def gameover_page():
    crash = True
    while crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.blit(entryimg, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', 70)
        font1 = pygame.font.Font('freesansbold.ttf', 35)
        show_font = font.render('Game Over', True, (255, 255, 255))
        showscore_font = font.render('Score: ' + str(score), True, (255, 255, 255))
        screen.blit(show_font, (120, 100))
        screen.blit(showscore_font, (120, 200))
        pygame.draw.rect(screen, (0, 200, 0), (320, 360, 150, 50))
        pygame.draw.rect(screen, (0, 120, 0), (320, 460, 150, 50))
        mouse = pygame.mouse.get_pos()
        if mouse[0] > 321 and mouse[0] < 470 and mouse[1] > 360 and mouse[1] < 410:
            pygame.draw.rect(screen, (0, 250, 0), (320, 360, 150, 50))
            if click == (True, 0, 0):
                game_loop()

        if mouse[0] > 321 and mouse[0] < 470 and mouse[1] > 460 and mouse[1] < 510:
            pygame.draw.rect(screen, (0, 180, 0), (320, 460, 150, 50))
            if click == (True, 0, 0):
                pygame.quit()
                quit()

        smallText = pygame.font.Font('freesansbold.ttf', 25)
        textSurface, textRect = text_object("Restart", smallText)
        textRect.center = ((320 + 73)), (360 + 27)
        screen.blit(textSurface, textRect)

        textSurface, textRect = text_object("EXIT", smallText)
        textRect.center = ((320 + 73)), (460 + 27)
        screen.blit(textSurface, textRect)

        pygame.display.update()


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
# function for player
def playercar(x, y):
    screen.blit(CarImg, (x, y))

# function for collision of player and enemy
def isCollision(totalenemy_car_x, totalenemy_car_y, playerX, playerY):
    distance = math.sqrt(math.pow(totalenemy_car_x - playerX, 2) + (math.pow(totalenemy_car_y - playerY, 2)))
    if distance < 70:
        return True
    else:
        return False


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

global game_loop
# Game loop (infinite loop which makes sure game is always running)
def game_loop():
    global car_passed
    global score
    playerX_change = 0
    playerX = 365
    playerY = 470
    running = True
    enemycar_speed = 2
    totalenemy_car=0
    totalenemy_car_x=random.randrange(150, 640)
    totalenemy_car_y = -750

    car_passed = 0
    score=0
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

        totalenemy_car_y -= (enemycar_speed / 6)
        enemycar(totalenemy_car_x, totalenemy_car_y, totalenemy_car)
        totalenemy_car_y += enemycar_speed
        playercar(playerX, playerY)

        collision = isCollision(totalenemy_car_x, totalenemy_car_y, playerX, playerY)
        if collision:
            time.sleep(4)
            screen.blit(over_text, (25, 250))
            gameover_page()
            score = score - score
            car_passed = car_passed - car_passed
            pygame.display.update()
            game_loop()
            break

        if playerX <= 95 or playerX >= 645:
            crash = True
            break
        if totalenemy_car_y >= 800:
            totalenemy_car_y = 0 - 56
            totalenemy_car_x = random.randint(150, 600)
            totalenemy_car = random.randint(0, 6)

        #score
        if totalenemy_car_y >= 800:
            totalenemy_car_y = 0 - 56
            totalenemy_car_x = random.randint(150, 600)
            totalenemy_car = random.randint(0, 6)
            car_passed += 1
            score = car_passed * 10

        playercar(playerX,playerY)
        show_score(score, car_passed)
        pygame.display.update()

entrypage_loop()
gameover_page()
game_loop()
