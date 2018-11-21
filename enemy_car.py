import pygame
import random
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self,settings,screen,location):
        super(Enemy, self).__init__()
        self.screen=screen
        self.settings=settings
        self.speed=self.settings.enemy_speed
        self.screen_rect=screen.get_rect()
        enemy = pygame.image.load('image/enemy.png').convert_alpha()
        enemy1 = pygame.image.load('image/enemy1.png').convert_alpha()
        enemy2 = pygame.image.load('image/enemy2.png').convert_alpha()
        enemy3 = pygame.image.load('image/enemy3.png').convert_alpha()
        enemylist=[enemy,enemy1,enemy2,enemy3]#List that is used to store the enemy images
        self.image=random.choice(enemylist)#To randomly chose the enemy image
        self.rect=self.image.get_rect()
        self.rect=self.rect.inflate(-70,-25)#To set the enemy hitbox because it was previously too big
        self.rect.x=location
        self.rect.y=int(-30)


    def blitme(self):
        self.screen.blit(self.image,self.rect)#To blit the enemy image to the screen

    def update(self):
        self.rect.y+=self.speed# #To move the enemy car/update the position of the enemy car





