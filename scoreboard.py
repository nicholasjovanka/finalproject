import pygame.font
class Scoreboard:
    def __init__(self,settings,screen,stats):
        self.screen=screen
        self.settings=settings
        self.stats=stats
        self.screen_rect=self.screen.get_rect()
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None, 48)
        self.draw_score()
        self.draw_high_score()
        self.draw_level()

    def draw_score(self):#To set the score box
        score_str=str(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.settings.textbox_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.left=self.screen_rect.left+20
        self.score_rect.top=35

        self.font_score=pygame.font.SysFont(None,30)
        self.font_image=self.font_score.render("Score",True,(255,255,255))
        self.font_image_rect=self.font_image.get_rect()
        self.font_image_rect.bottom=self.score_rect.top-5



    def show_score(self):#To draw the score,highscore,and level to the screen
        self.screen.blit(self.font_image,self.font_image_rect)
        self.screen.blit(self.font_highscore_image,self.font_highscore_rect)
        self.screen.blit(self.font_level_image,self.font_level_image_rect)
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)

    def draw_high_score(self):#To set the high score box
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image =self.font.render(high_score_str,True,self.text_color,self.settings.textbox_color)
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.right=self.screen_rect.right-20
        self.high_score_rect.top=self.score_rect.top

        self.font_highscore=pygame.font.SysFont(None,30)
        self.font_highscore_image=self.font_highscore.render("High Score",True,(255,255,255))
        self.font_highscore_rect=self.font_highscore_image.get_rect()
        self.font_highscore_rect.right=self.high_score_rect.right
        self.font_highscore_rect.bottom=self.high_score_rect.top-5
    def draw_level(self):#To set the level box
        self.level_str=str(self.stats.level)
        self.level_image =self.font.render(self.level_str, True,self.text_color,self.settings.textbox_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.high_score_rect.right
        self.level_rect.top=self.high_score_rect.bottom+35

        self.font_level=pygame.font.SysFont(None,30)
        self.font_level_image=self.font_level.render("Level",True,(255,255,255))
        self.font_level_image_rect=self.font_level_image.get_rect()
        self.font_level_image_rect.bottom=self.level_rect.top-5
        self.font_level_image_rect.right=self.high_score_rect.right

