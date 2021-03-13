import pygame
from paddlesClass import Paddle
from ball import Ball
pygame.init()

Black = (0, 0, 0)
WHITE = (255, 255, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#list that contains all the sprites we will use in our game
all_sprites_list = pygame.sprite.Group()

#adds paddles to list
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

carryOn = True

clock = pygame.time.Clock()

#Initialise player scores
scoreA = 0
scoreB = 0

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)


    # --- game logic goes here
    all_sprites_list.update()

    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=690:
        scoreA +=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB +=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    # --- Drawing code goes here
    # #fills screen to black
    screen.fill(Black)

    #draws the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    #draw all the sprites
    all_sprites_list.draw(screen)

    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))

    #update screen
    pygame.display.flip()

    #limit frames to 60
    clock.tick(60)


pygame.quit()


