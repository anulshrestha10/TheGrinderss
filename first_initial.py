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

playerX=380
playerY=460

def playercar():
    screen.blit(CarImg, (playerX, playerY))
# Game loop (infinite loop which makes sure game is always running)
running= True
while running:
    # RGB= Red, Green, Blue (goes from 0 to 255)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

    playercar()
    pygame.display.update()