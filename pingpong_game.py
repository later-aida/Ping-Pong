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
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x += self.speed



# player = Player("rocket.png",80,420,5,40,80)




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

    display.update()#обновление содержимого окна на каждом шаге цикла\
    clock.tick(FPS)
