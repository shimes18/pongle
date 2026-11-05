import pygame
import random
import asyncio

pygame.init()
pygame.mixer.init()

screen= pygame.display.set_mode((800,600))
player1=pygame.Rect(0,350,5,80)
player2=pygame.Rect(795,350,5,80)
ball= pygame.Rect(395,295,20,20)
ballradius=10

icounter2=1
icounter1=1
font = pygame.font.Font(None,32)

ballvisible=True
score1=0
score2=0

lcounter1=1
lcounter2=1

item_sound = pygame.mixer.Sound("sounds/acquired.ogg")
item_sound.set_volume(0.8)

hit_sound = pygame.mixer.Sound("sounds/hit.ogg")
hit_sound.set_volume(0.7)

pygame.mixer.music.load("sounds/bg.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

logo=pygame.image.load("images/user.png").convert_alpha()
logo= pygame.transform.scale(logo,(40,40))

ballimg=pygame.image.load("images/image.png").convert_alpha()
ballimg= pygame.transform.scale(ballimg,(20,20))

newvar=0
speedcounter=0

fps=30

clock=pygame.time.Clock()

speedx=1
speedy=1
running=True
game_over=False
game_finish=False
game_home=True
rule_space=False
direction_x=random.choice([-1,1])
direction_y=random.choice([-1,1])


l1,l2=0,0

e1,e2,timere1,timere2,ecounter1,ecounter2=0,0,0,0,1,1

s1,s2,timers1,timers2,scounter1,scounter2=0,0,0,0,1,1

r1,r2,timerr1,timerr2,rcounter1,rcounter2=0,0,0,0,1,1

fr1,fr2,timerfr1,timerfr2,frcounter1,frcounter2=0,0,0,0,1,1

async def main():
    global running, game_over, game_finish, game_home, rule_space
    global score1, score2, ballvisible, newvar, speedcounter
    global ball, player1, player2
    global l1, l2, lcounter1, lcounter2
    global icounter1, icounter2
    global e1, e2, timere1, timere2, ecounter1, ecounter2
    global s1, s2, timers1, timers2, scounter1, scounter2
    global r1, r2, timerr1, timerr2, rcounter1, rcounter2
    global fr1, fr2, timerfr1, timerfr2, frcounter1, frcounter2
    global direction_x, direction_y, speedx, speedy   

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type== pygame.KEYDOWN and game_over and event.key == pygame.K_r:
                ball= pygame.Rect(395,295,10,10) 
                direction_x=random.choice([-1,1])
                direction_y=random.choice([-1,1])
                ballvisible=True
                game_over=False
            if game_finish and event.type==pygame.KEYDOWN and event.key == pygame.K_s:
                game_home = True
                game_over = False
                game_finish = False
                direction_x=random.choice([-1,1])
                direction_y=random.choice([-1,1])

                speedcounter=0

                speedx=1
                speedy=1

                newvar=0

                l1,l2=0,0
                lcounter1=1
                lcounter2=1

                icounter2=1
                icounter1=1

                e1,e2,timere1,timere2,ecounter1,ecounter2=0,0,0,0,1,1

                s1,s2,timers1,timers2,scounter1,scounter2=0,0,0,0,1,1

                r1,r2,timerr1,timerr2,rcounter1,rcounter2=0,0,0,0,1,1

                fr1,fr2,timerfr1,timerfr2,frcounter1,frcounter2=0,0,0,0,1,1

                player1=pygame.Rect(0,350,5,80)
                player2=pygame.Rect(795,350,5,80)
                ball= pygame.Rect(395,295,10,10)


            if game_home and event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                score1=0
                score2=0
                game_over=False
                game_finish=False
                game_home=False
                rule_space=False
            if game_home and event.type==pygame.KEYDOWN and not game_finish and event.key == pygame.K_r and not game_over:
                game_home=False
                rule_space=True
            if rule_space and event.type==pygame.KEYDOWN and event.key == pygame.K_h and not game_over:
                game_home = True
                rule_space = False



        if not game_over and not game_finish and not game_home and not rule_space:
            ball.x+=int(direction_x*5*speedx)+newvar*direction_x*speedx
            ball.y+=int(direction_y*5*speedy)+newvar*direction_y*speedy
            press=pygame.key.get_pressed()
            if press[pygame.K_w]:
                player1.y-=10
            if press[pygame.K_s]:
                    player1.y+=10
            if press[pygame.K_UP]:
                    player2.y-=10
            if press[pygame.K_DOWN]:
                    player2.y+=10

            if r2==1:
                timerr2+=1
                if timerr2<10*fps:
                    press1=pygame.key.get_pressed()
                    if press1[pygame.K_w]:
                        player1.y+=20
                    if press1[pygame.K_s]:
                        player1.y-=20
                else:
                    r2=0

            if r1==1:
                timerr1+=1
                if timerr1<10*fps:
                    press2=pygame.key.get_pressed()
                    if press2[pygame.K_UP]:
                        player2.y+=20
                    if press2[pygame.K_DOWN]:
                        player2.y-=20
                else:
                    r1=0

            if player1.y>=600-player1.h:
                player1.y=600-player1.h
            if player2.y>=600-player2.h:
                player2.y=600-player2.h
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
    
            if ball.x<-10:
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
                hit_sound.play()
            if player2.colliderect(ball):
                speedx=-speedx
                hit_sound.play()



            if ball.y<0+newvar:
                ball.y=2*newvar
                speedy=-speedy

            if ball.y>580-newvar:
                ball.y=580-2*newvar
                speedy=-speedy

            if score1==5:
                if lcounter1==1:
                    lcounter1=0
                    l1=1
                    item_sound.play()
            if score2==5:
                if lcounter2==1:
                    lcounter2=0
                    l2=1
                    item_sound.play()


            if score1==8:
                if ecounter1==1:
                    ecounter1=0
                    e1=1
                    timere1=0
                    item_sound.play()


            if score2==8:
                if ecounter2==1:
                    ecounter2=0
                    e2=1
                    timere2=0
                    item_sound.play()



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

            if score1==12:
                if scounter1==1:
                    scounter1=0
                    s1=1
                    timers1=0
                    item_sound.play()


            if score2==12:
                if scounter2==1:
                    scounter2=0
                    s2=1
                    timers2=0
                    item_sound.play()




            if s2==1:
                timers2+=1
                if timers2<10*fps:
                    player1.h = 30
                else:
                    player1.h = 80
                    s2=0

            if s1==1:
                timers1+=1
                if timers1<10*fps:
                    player2.h = 30
                else:
                    player2.h = 80
                    s1=0

            if score1==16:
                if rcounter1==1:
                    rcounter1=0
                    r1=1
                    timerr1=0
                    item_sound.play()


            if score2==16:
                if rcounter2==1:
                    rcounter2=0
                    r2=1
                    timerr2=0
                    item_sound.play()

            if score2==20 :
                if icounter2==1:
                    temp1=score1
                    temp2=score2
                    icounter2=0
                if (temp1+temp2==score1+score2):
                    ballvisible=False


            if score1==20 :
                if icounter1==1:
                    temp1=score1
                    temp2=score2
                    icounter1=0
                if (temp1+temp2==score1+score2):
                    ballvisible=False

            if (score1==25):
                game_finish=True
            if (score2==25):
                game_finish=True




            if (score1==5 or score2==5) and speedcounter==0:
                newvar+=1
                speedcounter=1
                print(speedx)
            if (score1==10 or score2==10) and speedcounter==1:
                newvar+=1

                speedcounter=2
            if (score1==15 or score2==15) and speedcounter==2:
                newvar+=1

                speedcounter=3
            if (score1==20 or score2==20) and speedcounter==3:
                newvar+=1
                speedcounter=4

        screen.fill((20,20,20))
            
        if not game_home and not rule_space and not game_finish:
            player1= pygame.draw.rect(screen, (255,255,255),player1)
            player2= pygame.draw.rect(screen, (255,255,255),player2)
            if ballvisible:
                screen.blit(ballimg,ball)
            scoret= font.render(str(score1) + " - " + str(score2),True,(255,255,255))
            screen.blit(scoret,(400,0))


        if game_over and not game_finish:
            start = font.render("Press R to continue ", True, (255,255,255))
            screen.blit(start,(300,250))

            life=font.render("+1 life",True,(255,255,255))
            extend=font.render("Long",True,(255,255,255))
            shrink= font.render("Shrink",True,(255,255,255))
            reverse= font.render("Reversed", True, (255,255,255))

        if (l1==1):
            screen.blit(life,(0,0))
        if (l2==1):
            screen.blit(life,(700,0))

        if (e1==1):
            screen.blit(extend,(0,40))
        if (e2==1):
            screen.blit(extend,(700,40))
        if (s1==1):
            screen.blit(shrink,(700,80))
        if (s2==1):
            screen.blit(shrink,(0,80))
        if (r1==1):
            screen.blit(reverse,(700,120))
        if (r2==1):
            screen.blit(reverse,(0,120))

        if game_finish:
            if (score1>score2):
                winner="Player1"
                score1,score2=0,0
            if(score2>score1):
                winner="Player2"
                score1,score2=0,0
            winnert = font.render("WINNER IS "+ winner, True , (255,255,255))
            instruction = font.render("Press S to return to main menu", True , (255,255,255))
            screen.blit(winnert,(300,200))
            screen.blit(instruction,(200,250))

        if game_home and not rule_space:
            textt = font.render("Press Spacebar to start",True,(255,255,255))
            rulet = font.render("Press R for rules", True,(255,255,255))
            screen.blit(logo,(350,160))
            screen.blit(textt,(250,200))
            screen.blit(rulet,(300,250))


        if rule_space and not game_home:
            ruleh= font.render("RULES",True,(255,255,255))
            rule1= font.render("1. Opponent gains one point if you miss the ball",True,(255,255,255))
            rule2= font.render("2. Ball returns back if you hit it with the pad",True,(255,255,255))
            rule3= font.render("3. There are special power ups at certain score point",True,(255,255,255))
            rule4= font.render("4. There are debuffs for opponent at certain score point",True,(255,255,255))
            rule5= font.render("5. Ball  gets faster every 5 points",True,(255,255,255))
            rule6= font.render("6. First to 25 points wins",True,(255,255,255))
            back = font.render("Press H to go back",True,(255,255,255))
            screen.blit(ruleh, (380,10))
            screen.blit(rule1, (100,50))
            screen.blit(rule2, (100,100))
            screen.blit(rule3, (100,150))
            screen.blit(rule4, (100,200))
            screen.blit(rule5, (100,250))
            screen.blit(rule6, (100,300))
            screen.blit(back,(300,350))
        
        if not ballvisible:
            inv = font.render("INVISIBLE BALL",True,(255,255,255))
            screen.blit(inv,(350,50))
        pygame.display.flip()
        clock.tick(fps)
        await asyncio.sleep(0)


asyncio.run(main())