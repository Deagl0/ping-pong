from pygame import *
window = display.set_mode((700,500))
display.set_caption("ping pong")
background = transform.scale(image.load("back.jpg"), (700,500))

game = True
finish = False
speed_x = 3
speed_y = 3
p1score = 0
p2score = 0

win_height = 500
win_width = 700

font.init()
font = font.SysFont("Arial", 16)



win1 = font.render("Player 1 WINS!!!", True, (255, 215, 0))
win2 = font.render("Player 2 WINS!!!", True, (255, 215, 0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_width, player_height, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.x = player_y
        self.width = player_width
        self.height = player_height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        self.rect.y += self.speed
        global p1score
        global p2score
        if self.rect.x > 700:
            self.rect.x = 350
            self.rect.y = 250
            p1score += 1
        if self.rect.x < 0:
            self.rect.x = 350
            self.rect.y = 250
            p2score += 1
class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 435:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed
ball = GameSprite("ball.png", 5, 5, 350, 250, 1)
player_1 = Player1("p1.png", 10, 100, 250, 1, 5)
player_2 = Player2("p1.png", 10, 100, 250, 630, 5)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        text_score1 = font.render("P1 Score: "+ str(p1score), 1 ,(255, 255, 255))
        window.blit(text_score1, (10,10))
        text_score2 = font.render("P2 Score: "+ str(p2score), 1 ,(255, 255, 255))
        window.blit(text_score2, (625,10))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y< 0:
            speed_y *= -1
        if sprite.collide_rect(player_1,ball) or sprite.collide_rect(player_2,ball):
            speed_x*=-1
        
        player_1.reset()
        player_1.update()
        player_2.reset()
        player_2.update()
        ball.update()
        ball.reset()
        if p1score == 10:
            finish = True
            window.blit(win1, (350,200))
        if p2score == 10:
            finish = True
            window.blit(win2, (350,200))
    display.update()