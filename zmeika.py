from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Zмейка')
background = transform.scale(image.load("фон.png"), (700,500))
score = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.player_speed = player_speed
        self.speed_x = player_speed
        self.speed_y = 0
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Player(GameSprite):
    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
food_spawn = randint(0,700)
head = Player('голова.png',50,350,250,50,50)
food = GameSprite('еда.png',0,randint(0,14)*50,randint(0,10)*50,50,50)
wait = 0 
clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    if wait == 0:
        if finish != True:
            window.blit(background, (0,0))
            food.update()
            food.reset()
            head.update()
            head.reset()
            if head.colliderect(food):
                score += 1
                food.rect.x = randint(0,14)*50-50
                food.rect.y = randint(0,10)*50-50
            wait = 30
    keys_pressed = key.get_pressed()
    if keys_pressed[K_w] and head.rect.y > 0:
        head.speed_y = -head.player_speed
        head.speed_x = 0
    if keys_pressed[K_s] and head.rect.y < 550:
        head.speed_y = head.player_speed
        head.speed_x = 0
    if keys_pressed[K_a] and head.rect.x > 0:
        head.speed_x = -head.player_speed
        head.speed_y = 0
    if keys_pressed[K_d] and head.rect.x < 650:
        head.speed_x = head.player_speed
        head.speed_y = 0
    wait -= 1
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)

