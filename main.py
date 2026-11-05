import pygame


screen= pygame.display.set_mode((800,600))
player1=(0,100,5,80)
player2=(795,100,5,80)
pygame.init()
running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    press=pygame.key.get_pressed()
    if press[pygame.K_w]:
        player1.y-=10
    if press[pygame.K_s]:
            player1.y+=10
    if press[pygame.K_UP]:
            player2.y-=10
    if press[pygame.K_DOWN]:
            player2.y+=10


    screen.fill((20,20,20))
    player1= pygame.draw.rect(screen, (255,255,255),player1)
    player2= pygame.draw.rect(screen, (255,255,255),player2)

    pygame.display.flip()
    pygame.time.Clock().tick(20)

pygame.quit()