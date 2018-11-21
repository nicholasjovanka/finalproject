import pygame
from game_settings import  Settings

settings=Settings()

class Car:
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('image/car.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect=self.rect.inflate(-68,-50)#To reduce the player hitbox because it was previously too big
        self.screen_rect=screen.get_rect()
        self.moving_right=False #Line 13 to 16 is to allow smooth movement
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        #Set the car image location when it spawns
        self.rect.y=500
        self.rect.centerx=self.screen_rect.centerx


    #To update the car location based on the movement in game function
    def update_car(self):#To update the car base on the player input and limiting the player movement so the player doesnt go off the playing area that is setted
        if self.moving_left and self.rect.left>138:
            self.rect.centerx-=settings.car_speed
        if self.moving_right and self.rect.right<670:
            self.rect.centerx+=settings.car_speed
        if self.moving_up and self.rect.top>0:
            self.rect.centery-=settings.car_speed
        if self.moving_down and self.rect.bottom<600:
            self.rect.centery+=settings.car_speed

    def blitme(self):
        self.screen.blit(self.image,self.rect) #To blit the player car to the screen

    def reset_position(self):#To reset the player position
        self.rect.y=500
        self.rect.centerx=self.screen_rect.centerx
