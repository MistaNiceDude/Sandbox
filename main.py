import pygame
from classes import *

pygame.init()
pygame.display.init()

WIN = WIDTH, HEIGHT = 800, 800
DISPLAY = pygame.display.set_mode(WIN)
red = (255, 0, 0)
black = (0,0,0)



#player = pygame.draw.rect(surface, red, pygame.Rect(30, 30, 60,60))
#sdfgs gj uk df gas
run = True
player = Player(WIDTH/2, HEIGHT/2)
player.x = 400
player.y = 400


while run:
    DISPLAY.fill(black)
    player.draw(DISPLAY)
    player.move(DISPLAY)



    # pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #main()

    pygame.display.flip()