import pygame
import time
from classes import *

pygame.font.init()
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
block = Block(100, 100)
clock = pygame.time.Clock()
FPS = 60
clock_font = pygame.font.SysFont("comicsans", 20)
player.x_font = pygame.font.SysFont("comicsans", 20)
player.y_font = pygame.font.SysFont("comicsans", 20)

def redraw():
    player.x_m = (f"Player.x: {player.x}")
    player.y_m = (f"Player.y: {player.y}")
    DISPLAY.fill(black)
    DISPLAY.fill(black)
    player.draw(DISPLAY)
    player.move(DISPLAY)
    block.draw(DISPLAY)
    clock_label = clock_font.render(f"FPS: {clock}", 1, (255, 255, 255))
    player.x_label = player.x_font.render(f" {player.x_m}", 1, (255, 255, 255))
    player.y_label = player.y_font.render(f" {player.y_m}", 1, (255, 255, 255))
    DISPLAY.blit(clock_label, (20, HEIGHT - clock_label.get_height() - 20))
    DISPLAY.blit(player.x_label, (WIDTH - player.x_label.get_width() - 20, HEIGHT - player.x_label.get_height() - 40))
    DISPLAY.blit(player.y_label, (WIDTH - player.y_label.get_width() - 20, HEIGHT - player.y_label.get_height() - 20))


while run:
    clock.tick(FPS)
    redraw()
    print(Player.collide_dir(player.hitbox))



    #collision = collide(player, block)
    #if collision == True:
    #    if player.x > block.x + block.get_width()/2 and block.x > 0:
    #        block.move(0, -Player.player_vel)
    #        print("collision")
    #
    if collide(player, block) == True:
        if player.y > block.y + block.get_height()/2 - 10 and block.y > 0:
            block.move(0, -Player.player_vel)
        elif player.y < block.y - block.get_height()/2 + 10 and block.y + block.get_height() < HEIGHT:
            block.move(0, Player.player_vel)
        elif player.x > block.x + block.get_width()/2 + 10 and block.x > 0:
            block.move(-Player.player_vel, 0)
        elif player.x < block.x - block.get_width()/2 - 10 and block.x + block.get_width() < WIDTH:
            block.move(Player.player_vel, 0)














    # pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #main()

    pygame.display.flip()