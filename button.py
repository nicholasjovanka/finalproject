import pygame.font

class Button:
    def __init__(self,settings,screen,text):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.width=200
        self.height=50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        self.msg(text)


    def msg(self,msg):#To set the text in the button
        self.msg_image= self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):#To draw the button and the text to the screen
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)



