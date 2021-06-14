#Import Modules
import pygame
from paddlesClass import Paddle
from ball import Ball


#Initialize pygame instance
pygame.init()

#Create colors
Black = (0, 0, 0)
WHITE = (255, 255, 255)

#Create display window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#Create PaddleA and PaddleB objects
LeftPaddle = Paddle(WHITE, 10, 100)
LeftPaddle.rect.x = 20
LeftPaddle.rect.y = 200

RightPaddle = Paddle(WHITE, 10, 100)
RightPaddle.rect.x = 670
RightPaddle.rect.y = 200

#Create Ball object
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#List that contains all the sprites we will use in our game
all_sprites_list = pygame.sprite.Group()

#Adds sprites (objects) to list
all_sprites_list.add(LeftPaddle)
all_sprites_list.add(RightPaddle)
all_sprites_list.add(ball)

#Create clock
clock = pygame.time.Clock()

#Initialise player scores
scoreA = 0
scoreB = 0

#Initialize ball direction variables
ballDirection = 0

#Initialize Paddle Movement Speed
PaddleSpeed = 15

# Count Down event for timer
PlayerScored = pygame.USEREVENT+1
my_event = pygame.event.Event(PlayerScored)
count = 4
current_time = 0
player_scored_time = 0

#Initialize game font
font = pygame.font.Font(None, 74)

#Set game loop condition
carryOn = True

#Begin game loop
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False

    #Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        LeftPaddle.moveUp(PaddleSpeed)
    if keys[pygame.K_s]:
        LeftPaddle.moveDown(PaddleSpeed)
    if keys[pygame.K_UP]:
        RightPaddle.moveUp(PaddleSpeed)
    if keys[pygame.K_DOWN]:
        RightPaddle.moveDown(PaddleSpeed)


    # --- game logic goes here
    all_sprites_list.update()


    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 690:
        scoreA += 1
        ballDirection = 1
        ball.reset()
        ball.launchBall(ballDirection)
    if ball.rect.x <= 0:
        scoreB += 1
        ballDirection = -1
        ball.reset()
        ball.launchBall(ballDirection)
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, LeftPaddle):
        ballDirection = -1
        ball.bounce(ballDirection)
    if pygame.sprite.collide_mask(ball, RightPaddle):
        ballDirection = 1
        ball.bounce(ballDirection)

    # --- Drawing code goes here
    # #fills screen to black
    screen.fill(Black)

    #draws the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    #draw all the sprites
    all_sprites_list.draw(screen)

    #Display scores:
    text = font.render(str(scoreA), True, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), True, WHITE)
    screen.blit(text, (420, 10))

    #update screen
    pygame.display.flip()

    #limit frames to 60
    clock.tick(60)


pygame.quit()




