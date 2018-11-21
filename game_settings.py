import pygame
class Settings:
    def __init__(self):
        self.screen_height=600 #Line 4 to 5 is for the screen resolution height and witdh
        self.screen_width=800
        self.difficulty_scale=1.3 #The difficulty scale
        self.car_speed=1
        self.enemy_speed=1
        self.textbox_color=(255,255,255)
        self.initial_speed()
    def initial_speed(self):#To reset the speed of the player car and enemy car
        self.car_speed=1
        self.enemy_speed=1.5
    def increase_difficulty(self): #To increase the difficulty
        self.car_speed *= self.difficulty_scale
        self.enemy_speed *=self.difficulty_scale
