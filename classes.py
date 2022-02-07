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

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
VEL = 5
collision_objs = []


class Collision:
    def __init__(self, x, y, width, height):
        self.collide_box = pygame.Rect(x, y, width, height)
        self.has_collide = False
        self.collide_with = None
        self.collide_side = None
        self.can_move = [True, True, True, True]
        self.move_dir = None
        collision_objs.append(self)

    def set_pos(self, x, y):
        self.collide_box.x = x
        self.collide_box.y = y

    def update(self):
        pass



collision_objs: list[Collision]
def obj_update():
    for obj in collision_objs:
        obj.update()

def collide(obj1: Collision, obj2: Collision):
   if obj2.collide_box.collidepoint(obj1.collide_box.midleft):
       obj1.has_collide = True
       obj1.collide_with = obj2
       obj1.collide_side = LEFT_COLLIDE
       obj2.has_collide = True
       obj2.collide_with = obj2
       obj2.collide_side = RIGHT_COLLIDE
   elif obj2.collide_box.collidepoint(obj1.collide_box.midright):
       obj1.has_collide = True
       obj1.collide_with = obj2
       obj1.collide_side = RIGHT_COLLIDE
       obj2.has_collide = True
       obj2.collide_with = obj2
       obj2.collide_side = LEFT_COLLIDE
   elif obj2.collide_box.collidepoint(obj1.collide_box.midtop):
       obj1.has_collide = True
       obj1.collide_with = obj2
       obj1.collide_side = TOP_COLLIDE
       obj2.has_collide = True
       obj2.collide_with = obj2
       obj2.collide_side = BOTTOM_COLLIDE
   elif obj2.collide_box.collidepoint(obj1.collide_box.midbottom):
       obj1.has_collide = True
       obj1.collide_with = obj2
       obj1.collide_side = BOTTOM_COLLIDE
       obj2.has_collide = True
       obj2.collide_with = obj2
       obj2.collide_side = TOP_COLLIDE


class Player(Collision):
    def __init__(self, x, y):
        self.player = pygame.Surface((40,40))
        super().__init__(x, y, self.player.get_width(), self.player.get_height())
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        self.mask = pygame.mask.from_surface(self.player)
        #self.collide = collide(Player, obj2)
        self.hitbox = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        super().set_pos(self.x,self.y)
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
        self.collide_box.x = self.x
        self.collide_box.y = self.y

    def get_rect(self):
        return self.player.get_rect()

    def update(self):
        collidee = None
        if self.has_collide:
            collidee = self.collide_with
            if self.collide_side == TOP_COLLIDE and collidee.can_move[UP]:
                collidee.move_dir = UP
            if self.collide_side == BOTTOM_COLLIDE and collidee.can_move[DOWN]:
                collidee.move_dir = DOWN
            if self.collide_side == LEFT_COLLIDE and collidee.can_move[LEFT]:
                collidee.move_dir = LEFT
            if self.collide_side == RIGHT_COLLIDE and collidee.can_move[RIGHT]:
                collidee.move_dir = RIGHT

                
        self.has_collide = False
        self.collide_with = None
        self.collide_side = None


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
            self.move_dir = LEFT

        if keys[pygame.K_w] and self.y - player_vel > 0:
            self.transform(0, -player_vel)
            self.move_dir = UP

        if keys[pygame.K_s] and self.y + self.player.get_height() < HEIGHT:
            self.transform(0, player_vel)
            self.move_dir = DOWN

        if keys[pygame.K_d] and self.x + self.player.get_width() < WIDTH:
            self.transform(player_vel, 0)
            self.move_dir = RIGHT


class Block(Collision):
    def __init__(self, x, y):
        self.block = pygame.Surface((40,40))
        super().__init__(x, y, self.block.get_width(), self.get_height())
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
        self.collide_box.x = self.x
        self.collide_box.y = self.y

    def get_rect(self):
        return self.block.get_rect()

    def collision(self, obj):
        return collide(obj, self)

    def update(self):
        collidee = self.collide_with
        if self.move_dir == UP and self.can_move[UP] == True and collidee.move_dir == UP:   #TODO implement how to set can_move
            self.transform(0, -VEL)
        elif self.move_dir == DOWN and self.can_move[DOWN] == True and collidee.move_dir == DOWN:
            self.transform(0, VEL)
        elif self.move_dir == LEFT and self.can_move[LEFT] == True and collidee.move_dir == LEFT:
            self.transform(-VEL, 0)
        elif self.move_dir == RIGHT and self.can_move[RIGHT] == True and collidee.move_dir ==RIGHT:
            self.transform(VEL, 0)
        self.move_dir = None
  
  
  
  
  
  
  
  