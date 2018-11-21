import sys
import pygame
from game_settings import Settings
from main_car import Car
import game_function
from enemy_car import Enemy
from pygame.sprite import Group
import random
import pygame.font
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard

def run_game():
    settings=Settings()
    pygame.init() #To initialize the background setting
    pygame.display.set_caption("Traffic Racer")#To set the caption of the game
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_height)) #To set the game resolution
    car=Car(screen)
    background=pygame.image.load('image/background.png').convert_alpha()#To load the image of the background and the convert.alpha is to convert the image surface to the same pixel used by the screen to improve performance
    gamestatus=Gamestats(settings)
    play_button=Button(settings,screen,"PLAY")
    score=Scoreboard(settings,screen,gamestatus)
    x=0 #to set the background image x coordinate
    y=0 #for the relative y
    enemylistleft=[]#List that is used to spawn enemy on the left
    enemylistright=[]#List that is used to spawn enemy on the right
    count=0 #The count that is use to adjust enemy spawnrate(spawn interval)
    scorecount=0 #The count that is use to adjust the interval in which the score is updated/increase
    scorescale=0 #The count that is use to adjust the time when the difficulty will
    while True:
        game_function.update_screen(car,gamestatus,play_button,score)#Updates/draw the recently drawn screen and also the player car position and scoreboard/highscore/and level
        rel_y=y%background.get_rect().height            #for the relative y position of the background image
        screen.blit(background,(x,rel_y-background.get_rect().height))#To blit the moving background image to the screen
        game_function.check_events(car,play_button,gamestatus,enemylistleft,enemylistright,screen,settings,count,score)#To check for player input such as keyboard and mouse like if the playe have pressed the button or not
        if rel_y<settings.screen_height:          #Line 36 to 37 is to blit another background image to fill the blank gap in the first moving background image
                screen.blit(background,(x,rel_y))
        if gamestatus.game_active:#To check if the game status is active or not
            pygame.mixer.music.load('car_driving.wav')
            pygame.mixer.music.play(-1)
            y+=settings.enemy_speed
            count+=1
            scorecount+=1
            scorescale+=1
            if count==500:#Line 43,44 is to set the interval in which the enemy spawns
                count=0
            if scorecount==300:#Line 45-46 is to set the interval in which the score increases
                game_function.update_score(gamestatus,score)
                scorecount=0
            if scorescale==6100:#Line 48-52 is to increase the difficulty(speed of the player and the enemy) when the gamescore has reached the multiplication of 200(200,400,etc)
               settings.increase_difficulty()
               scorescale=0
               gamestatus.level+=1
               score.draw_level()
            game_function.enemy_spawner(enemylistleft,enemylistright,screen,settings,count)#To spawn the enemy and also blit and update their position
            car.update_car()#To update the car position according the the player key input
            game_function.collision(car,enemylistleft,enemylistright,gamestatus,score)#To check if the player hits the enemy or not
            game_function.remove_enemies(enemylistleft,enemylistright)#To remove the enemies that have gone off screen
        elif gamestatus.game_active==False:
            count=0         #To reset all the count's back to 0 whenever there is a new game
            scorescale=0
            scorecount=0










run_game()
