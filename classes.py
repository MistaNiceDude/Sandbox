import pygame
import os
from pygame import *

red = (255, 0, 0)
green = (0, 255,0)

WIN = WIDTH, HEIGHT = 800, 800
surface = pygame.display.set_mode(WIN)
LEFT_COLLIDE = 0
RIGHT_COLLIDE = 1
TOP_COLLIDE = 2
BOTTOM_COLLIDE = 3



class Collision():
    def __init__(self, x, y, width, height):
        self.collide_box = pygame.Rect(x, y, width, height)
        self.has_collide = False

    def set_pos(self, x, y):
        self.collide_box.x = x
        self.collide_box.y = y











class Player():
    def __init__(self, x, y):
        self.player = pygame.Surface((40,40))
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        self.mask = pygame.mask.from_surface(self.player)
        #self.collide = collide(Player, obj2)
        self.hitbox = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())



    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y 


    def draw(self, WINDOW: pygame.Surface):
        WINDOW.blit(self.player, (self.x, self.y))
        pygame.draw.rect(WINDOW, red, self.rect)
        self.hitbox = (self.x, self.y, self.get_width(), self.get_height())
        pygame.draw.rect(WINDOW, (0, 0, 255), self.hitbox, 2)


    def get_height(self):
        return self.player.get_height()

    def get_width(self):
        return self.player.get_width()

    def transform(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        self.rect.x = self.x
        self.rect.y = self.y



    def get_rect(self):
        return self.player.get_rect()

    #def collision(self, obj):
    #    return collide(obj, self)
    #
    #def collide_dir(self):
    #    rect = self.hitbox
    #    if rect.collidepoint(self.rect.midleft):
    #        return LEFT_COLLIDE
    #    elif rect.collidepoint(self.rect.midbottom):
    #        return BOTTOM_COLLIDE
    #    elif rect.collidepoint(self.rect.midtop):
    #        return TOP_COLLIDE
    #    elif rect.collidepoint(self.rect.midright):
    #        return RIGHT_COLLIDE
    #    else:
    #        return 4




    def move(self, DISPLAY):
        player_vel = 5
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.x - player_vel > 0:
            self.transform(-player_vel, 0)

        if keys[pygame.K_w] and self.y - player_vel > 0:
            self.transform(0, -player_vel)

        if keys[pygame.K_s] and self.y + self.player.get_height() < HEIGHT:
            self.transform(0, player_vel)

        if keys[pygame.K_d] and self.x + self.player.get_width() < WIDTH:
            self.transform(player_vel, 0)


class Block():
    def __init__(self, x, y):
        self.block = pygame.Surface((40,40))
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        self.mask = pygame.mask.from_surface(self.block)

    def draw(self, WINDOW: pygame.Surface):
        WINDOW.blit(self.block, (self.x, self.y))
        pygame.draw.rect(WINDOW, green, self.rect)
        self.hitbox = (self.x, self.y, self.get_width(), self.get_height())
        pygame.draw.rect(WINDOW, (255, 0, 0), self.hitbox, 2)

    def get_height(self):
        return self.block.get_height()

    def get_width(self):
        return self.block.get_width()

    def transform(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        self.rect.x = self.x
        self.rect.y = self.y
        vel = 5

    def get_rect(self):
        return self.block.get_rect()

    def collision(self, obj):
        return collide(obj, self)

   # def collide_dir(self, rect: pygame.Rect):
   #     if rect.collidepoint(self.rect.midleft):
   #         return LEFT_COLLIDE
   #     elif rect.collidepoint(self.rect.midbottom):
   #         return BOTTOM_COLLIDE
   #     elif rect.collidepoint(self.rect.midtop):
   #         return TOP_COLLIDE
   #     elif Player.rect.collidepoint(self.rect.midright):
   #         return RIGHT_COLLIDE
   #     else:
   #         return 4