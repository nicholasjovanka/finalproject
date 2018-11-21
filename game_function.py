import sys
import pygame
from enemy_car import Enemy
import random
import pygame.font

def check_events(car,playbutton,stats,enemylistleft,enemylistright,screen,settings,count,scoreboard):  #To check for player inputs
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                    sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                car.moving_left=True
            elif event.key==pygame.K_RIGHT:
                car.moving_right=True
            elif event.key==pygame.K_UP:
                car.moving_up=True
            elif event.key==pygame.K_DOWN:
                car.moving_down=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                car.moving_left=False
            elif event.key==pygame.K_RIGHT:
                car.moving_right=False
            elif event.key==pygame.K_UP:
                car.moving_up=False
            elif event.key==pygame.K_DOWN:
                car.moving_down=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(stats,playbutton,mouse_x,mouse_y,enemylistleft,enemylistright,car,screen,settings,count,scoreboard)


def check_play_button(stats,play_button,mouse_x,mouse_y,enemylistleft,enemylistright,car,screen,settings,count,scoreboard):#To check if the play button is clicked
        button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
        if button_clicked and not stats.game_active:                                    #Line 36 to 46 is to reset the game
            stats.level=1
            stats.score=0
            scoreboard.draw_level()
            pygame.mouse.set_visible(False)
            stats.game_active=True
            enemylistleft.clear()
            enemylistright.clear()
            enemy_spawner(enemylistleft,enemylistright,screen,settings,count)
            car.reset_position()
            settings.initial_speed()


def enemy_spawner(enemylistleft,enemylistright,screen,settings,count):                  #To spawn the enemies
    if count ==1:
        enemylistleft.append(Enemy(settings,screen,random.randint(138,400)))
        enemylistright.append(Enemy(settings,screen,random.randint(420,660)))
    for enemy in enemylistleft:
        enemy.update()
        enemy.blitme()
    for enemy in enemylistright:
        enemy.update()
        enemy.blitme()


def update_screen(car,stats,play_button,scoreboard):    #
    scoreboard.show_score()
    if not stats.game_active:
        play_button.draw_button()
    car.blitme()
    pygame.display.flip()

def update_score(stats,scoreboard):
    stats.score+=10
    scoreboard.draw_score()

def check_highscore(stats,scoreboard): #To check if there is a new highscore
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        scoreboard.draw_high_score()
        with open("highscore.txt","w") as f: #Line 77 and 78 is to save the highscore to the highscore.txt file
            f.write(str(stats.score))
def collision(car,enemylistleft,enemylistright,gamestatus,score):#To check if the player car collided with the enemy car
    for enemy in enemylistright,enemylistleft:
        if pygame.sprite.spritecollideany(car,enemy):
           gamestatus.game_active=False
           check_highscore(gamestatus,score)
           pygame.mouse.set_visible(True)
           pygame.mixer.music.load('car_crash.mp3')#Line 84 to 85 is to play a sound effect if the car crash the enemy car
           pygame.mixer.music.play(0)
def remove_enemies(enemylistleft,enemylistright):#To remove enemies that have gone offscreen
    for enemy in enemylistright:
        if enemy.rect.y>800:
            enemylistright.remove(enemy)
    for enemy in enemylistleft:
        if enemy.rect.y>800:
            enemylistleft.remove(enemy)

