import pygame as pg
import sys,random,math
#setup
pg.init()
clock = pg.time.Clock()

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <=0 or ball.bottom >= screen_y:
        ball_speed_y *= -1
    if ball.left <=0 or ball.right >= screen_x:
        ball_restart()
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *=-1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_y:
        player.bottom = screen_y

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_y:
        opponent.bottom = screen_y

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_x/2,screen_y/2)
    theta = random.randint(round(math.pi*1000000/12),round(math.pi*1000000/3))/1000000
    ball_speed_x = math.cos(theta)*random.choice((10,-10))
    ball_speed_y = math.sin(theta)*random.choice((10,-10))

#main menu
screen_x = 1280
screen_y = 960
screen = pg.display.set_mode((screen_x,screen_y))
pg.display.set_caption('PONG')


#rectangles
ball = pg.Rect(screen_x/2 -15,screen_y/2 -15,30,30)
player = pg.Rect(screen_x-20,screen_y/2 -70,10,140)
opponent = pg.Rect(10,screen_y/2 -70,10,140)
player_speed = 0
opponent_speed = 10

bg_color = pg.Color('grey12')
light_grey = (200,200,200)

ball_restart()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                player_speed += 10
            if event.key == pg.K_UP:
                player_speed -= 10
        if event.type == pg.KEYUP:
            if event.key == pg.K_DOWN:
                player_speed -= 10
            if event.key == pg.K_UP:
                player_speed += 10

    ball_animation()
    player_animation()
    opponent_animation()

    screen.fill(bg_color)
    pg.draw.rect(screen,light_grey,player)
    pg.draw.rect(screen,light_grey,opponent)
    pg.draw.ellipse(screen,light_grey,ball)
    pg.draw.aaline(screen, light_grey, (screen_x/2,0), (screen_x/2,screen_y))


    pg.display.flip()
    clock.tick(60)