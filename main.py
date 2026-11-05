import pygame
import random

pygame.init()

screen= pygame.display.set_mode((800,600))
player1=pygame.Rect(0,350,5,80)
player2=pygame.Rect(795,350,5,80)
ball= pygame.Rect(395,295,10,10)
ballradius=5

font = pygame.font.SysFont(None,32)

score1=0
score2=0

lcounter1=1
lcounter2=1


speedcounter=0

fps=30

clock=pygame.time.Clock()

speedx=1
speedy=1
running=True
game_over=False
direction_x=random.choice([-1,1])
direction_y=random.choice([-1,1])


l1,l2=0,0
e1,e2,timere1,timere2,ecounter1,ecounter2=0,0,0,0,1,1
s1,s2=0,0
f1,f2=0,0
store1,store2=0,0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type== pygame.KEYDOWN and game_over and event.key == pygame.K_r:
             ball= pygame.Rect(395,295,10,10) 
             direction_x=random.choice([-1,1])
             direction_y=random.choice([-1,1])
             game_over=False


    ball.x+=int((direction_x)*5*speedx)
    ball.y+=int((direction_y)*5*speedy)

    if not game_over:
        press=pygame.key.get_pressed()
        if press[pygame.K_w]:
            player1.y-=10
        if press[pygame.K_s]:
                player1.y+=10
        if press[pygame.K_UP]:
                player2.y-=10
        if press[pygame.K_DOWN]:
                player2.y+=10

        if player1.y>=520:
            player1.y=520
        if player2.y>=520:
            player2.y=520
        if player1.y<0:
            player1.y=0
        if player2.y<0:
            player2.y=0

        if ball.x>800:
            if l2==0:
                score1+=1
                game_over=True
            else:
                l2=0
                ball.x-=40
                speedx=-speedx
            ball.x+=20
  
        if ball.x<0:
            if l1==0:
                score2+=1
                game_over=True

            else:
                l1=0
                ball.x+=40
                speedx=-speedx
            ball.x-=20

        if player1.colliderect(ball):
             speedx=-speedx
        if player2.colliderect(ball):
             speedx=-speedx


        if ball.y<0:
             speedy=-speedy

        if ball.y>580:
             speedy=-speedy

        if score1==5:
            if lcounter1==1:
                lcounter1=0
                l1=1
        if score2==5:
            if lcounter2==1:
                lcounter2=0
                l2=1

        if score1==8:
            if ecounter1==1:
                ecounter1=0
                e1=1
                timere1=0

        if score2==8:
            if ecounter2==1:
                ecounter2=0
                e2=1
                timere2=0



        if e2==1:
            timere2+=1
            if timere2<10*fps:
                player2.h = 160
            else:
                player2.h=80
                e2=0

        if e1==1:
            timere1+=1
            if timere1<10*fps:
                player1.h = 160
            else:
                player1.h=80
                e1=0



        if (score1+score2==5 and speedcounter==0):
            speedx = speedx*1.5
            speedy = speedy*1.5
            speedcounter=1
            print(speedx)
        if (score1+score2==10 and speedcounter==1):
            speedx = speedx*1.5
            speedy = speedy*1.5
            speedcounter=2
        if (score1+score2==15 and speedcounter==2):
            speedx = speedx*1.5
            speedy = speedy*1.5
            speedcounter=3

    screen.fill((20,20,20))
    player1= pygame.draw.rect(screen, (255,255,255),player1)
    player2= pygame.draw.rect(screen, (255,255,255),player2)
    ball=pygame.draw.circle(screen,(255,255,255),(ball.x + ball.w//2, ball.y+ ball.h//2),ballradius,0)

    scoret= font.render(str(score1) + " - " + str(score2),True,(255,255,255))

    if game_over:
     start = font.render("Press R to continue ", True, (255,255,255))
     screen.blit(start,(300,250))

    life=font.render("+1 life",True,(255,255,255))
    extend=font.render("Long",True,(255,255,255))

    if (l1==1):
        screen.blit(life,(0,0))
    if (l2==1):
        screen.blit(life,(700,0))

    if (e1==1):
        screen.blit(extend,(0,40))
    if (e2==1):
        screen.blit(extend,(700,40))
    screen.blit(scoret,(400,0))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()