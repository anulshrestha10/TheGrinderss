import pygame

# initialize the pygame
pygame.init()
# create screen
screen= pygame.display.set_mode((800,600))


# Title and icon
pygame.display.set_caption("Car Race Arcade")
icon = pygame.image.load('CarIcon.png')
pygame.display.set_icon(icon)

# Player
CarImg= pygame.image.load('car1.jpg')

grassimg = pygame.image.load("grass.png")
yellowstripe = pygame.image.load("yellowstripe.png")
whitestripe = pygame.image.load("whitestripe.png")
traffic_cone = pygame.image.load("cone.png")
backgroundimg = pygame.image.load('grass.png')

playerX=380
playerY=460

def playercar():
    screen.blit(CarImg, (playerX, playerY))
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


def game_loop():
    running = True
    while running:
        # RGB= Red, Green, Blue (goes from 0 to 255)
        screen.fill((119, 119, 119))
        background()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        playercar()
        pygame.display.update()

game_loop()