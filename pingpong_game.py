#Создай собственный Шутер!

from pygame import *
from random import *
from time import time as timer


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed




player1 = Player("rac1.png",0,420,5,60,80)
player2 = Player("rac2.png",640,420,5,60,80)





window = display.set_mode((700, 500))
display.set_caption("Ping Pong")
background = transform.scale(image.load("photo.jpg"), (700,500))
game = True
finish = False



clock = time.Clock()
FPS = 60
font.init()
font1 = font.SysFont("Arial", 30)
font2 = font.SysFont("Arial", 80)

lose_ = font2.render("YOU LOSE!", True,(255,0,0))
win_ = font2.render("YOU WIN!", True,(0,225,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
    
        player1.update_left()
        player1.reset()
        player2.update_right()
        player2.reset()

    display.update()#обновление содержимого окна на каждом шаге цикла\
    clock.tick(FPS)
