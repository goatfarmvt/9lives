##Imports
import pygame, random, sys, colors, gameFunc, time
from pygame.locals import *

##Constants
windowWidth = 640
windowHeight = 480
fps = 60
fpsClock = pygame.time.Clock()
foods = []
foodNumber = 1
foodSize = 20
catSprite = pygame.image.load('cat.png')
catXCoord = windowWidth / 2
catYCoord = windowHeight / 2
catSpeed = 6
catLives = 9
seconds = 0
ticks = 0

##Death Screen
def die(screen):
    screen.fill((0, 0, 0))

    ##The words grow in size
    fontsize = 5
    while fontsize <= 70:

        font = pygame.font.SysFont(None, fontsize)

        # Set up the text
        text = font.render('You Died!', True, (colors.Red), (0, 0, 0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery
        screen.blit(text, textRect)
        
        ## Score
        font2 = pygame.font.SysFont(None, 30)
        text2 = font2.render("Survived for " + str(seconds) + " seconds.", True, (colors.Yellow), (0, 0, 0))
        displaySurf.blit(text2, (320, 300))



        pygame.display.update()

        time.sleep(0.2)

        fontsize += 5
        
    if fontsize >= 70:
        time.sleep (2)
        pygame.quit()

##Game starts
pygame.init()
displaySurf = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('9Lives v1.0')
gameFunc.intro(displaySurf)

##Block 1
block1XStart = random.randint(20, windowWidth)
block1YStart = random.randint(20, windowHeight)
block1Width = 30
block1Height = 30
rectangle1 = pygame.Rect(block1XStart, block1YStart, block1Width, block1Height)

##Block 2
block2XStart = random.randint(0, windowWidth)
block2YStart = random.randint(0, windowHeight)
block2Width = 30
block2Height = 30
rectangle2 = pygame.Rect(block2XStart, block2YStart, block2Width, block2Height)

##Block 3
block3XStart = random.randint(0, windowWidth)
block3YStart = random.randint(0, windowHeight)
block3Width = 15
block3Height = 15
rectangle3 = pygame.Rect(block3XStart, block3YStart, block3Width, block3Height)

##Block4
block4XStart = random.randint(0, windowWidth)
block4YStart = random.randint(0, windowHeight)
block4Width = 15
block4Height = 15
rectangle4 = pygame.Rect(block4XStart, block4YStart, block4Width, block4Height)

block1direction = "upright"
block2direction = "downleft"
block3direction = "upleft"
block4direction = "downright"

while True:
    displaySurf.fill(colors.Black)

    ##Make cat's collision box
    cat = pygame.Rect(catXCoord, catYCoord, 15, 15)
    pygame.draw.rect(displaySurf, (0,0,0), cat)
    
    ##Blit cat
    displaySurf.blit(catSprite, (catXCoord - 10, catYCoord - 15))

    ##Movements
    pressedKeys = pygame.key.get_pressed()
    if pressedKeys[ord('w')]:
        catYCoord -= catSpeed 
    if pressedKeys[ord('a')]:
        catXCoord -= catSpeed
    if pressedKeys[ord('s')]:
        catYCoord += catSpeed
    if pressedKeys[ord('d')]:
        catXCoord += catSpeed
        
    ##Boundaries
    if catXCoord > windowWidth:
        catXCoord = 0
    elif catXCoord < 0:
        catXCoord = windowWidth
    if catYCoord > windowHeight:
        catYCoord = 0
    elif catYCoord < 0:
        catYCoord = windowHeight

    ##Collide
    if pygame.Rect.colliderect(rectangle1, cat)== True:
        catLives -= 1
    if pygame.Rect.colliderect(rectangle2, cat)== True:
        catLives -= 1
    if pygame.Rect.colliderect(rectangle3, cat)== True:
        catLives -= 1
    if pygame.Rect.colliderect(rectangle4, cat)== True:
        catLives -= 1

    ##Blocks bounce
    pygame.draw.rect(displaySurf, colors.White, rectangle1)
    pygame.draw.rect(displaySurf, colors.White, rectangle2)
    pygame.draw.rect(displaySurf, colors.White, rectangle3)
    pygame.draw.rect(displaySurf, colors.White, rectangle4)
                               
    block1direction = gameFunc.move(rectangle1, block1direction)
    block2direction = gameFunc.move(rectangle2, block2direction)
    block3direction = gameFunc.move(rectangle3, block3direction)
    block4direction = gameFunc.move(rectangle4, block4direction)
    
    # Place the score on the screen
    font = pygame.font.SysFont(None, 24)
    scoretext = font.render("Lives: " + str(catLives), True, (255, 255, 255), (0, 0, 0))
    textRect = scoretext.get_rect()
    displaySurf.blit(scoretext, textRect)

    ##Seconds
    timerText = font.render("Seconds: " +str(seconds), True, (255, 255, 255), (0, 0, 0))
    displaySurf.blit(timerText, (70, 0))

    ##Timer
    ticks += 1
    if ticks % fps == 0:
        seconds += 1

    ##Death
    if catLives <= 0:
        die(displaySurf)
    
    ##Those things
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(fps)

