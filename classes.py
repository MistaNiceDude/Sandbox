import pygame
import os
from pygame import *

red = (255, 0, 0)

WIN = WIDTH, HEIGHT = 800, 800
surface = pygame.display.set_mode(WIN)


class Player:

    def __init__(self, x, y):
        self.player = pygame.Surface((40,40))
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

    def draw(self, WINDOW: pygame.Surface):
        WINDOW.blit(self.player, (self.x, self.y))
        pygame.draw.rect(WINDOW, red, self.rect)

    def get_height(self):
        return self.player.get_height()

    def get_width(self):
        return self.player.get_width()

    def transform(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        self.rect.x = self.x
        self.rect.y = self.y


    def move(self, DISPLAY):
        player_vel = 4
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.x - player_vel > 0:
            self.transform(-player_vel, 0)

        if keys[pygame.K_w] and self.y - player_vel > 0:
            self.transform(0, -player_vel)

        if keys[pygame.K_s] and self.y + self.player.get_height() < HEIGHT:
            self.transform(0, player_vel)

        if keys[pygame.K_d] and self.x + self.player.get_width() < WIDTH:
            self.transform(player_vel, 0)


