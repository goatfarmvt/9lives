import pygame, sys, time, colors

##Movement of blocks
moveSpeed = 6
windowWidth = 640
windowHeight = 480
def move(rectangle, direction):
    
    if direction == "downleft":
        rectangle.left -= moveSpeed
        rectangle.top += moveSpeed
    elif direction == "downright":
        rectangle.left += moveSpeed
        rectangle.top += moveSpeed
    elif direction == "upleft":
        rectangle.left -= moveSpeed
        rectangle.top -= moveSpeed
    elif direction == "upright":
        rectangle.left += moveSpeed
        rectangle.top -= moveSpeed

    # Check to see if the rectangle has moved out of the screen
    if rectangle.top < 0:
        # We've hit the top
        if direction == "upleft":
            direction = "downleft"
        elif direction == "upright":
            direction = "downright"
    elif rectangle.bottom > windowHeight:
        # We've hit the bottom
        if direction == "downleft":
            direction = "upleft"
        elif direction == "downright":
            direction = "upright"
    elif rectangle.left < 0:
        # We've high the left side
        if direction == "downleft":
            direction = "downright"
        elif direction == "upleft":
            direction = "upright"
    elif rectangle.right > windowWidth:
        if direction == "downright":
            direction = "downleft"
        elif direction == "upright":
            direction = "upleft"
    return direction

##Intro Screen
def intro(screen):
    screen.fill((0, 0, 0))

    # Have the words grow in size, and stop at size 60
    fontsize = 5
    while fontsize <= 60:

        # Set up the fonts
        font = pygame.font.SysFont(None, fontsize)

        # Set up the text
        text = font.render('Nine Lives', True, (colors.Aqua), (0, 0, 0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery

        # Put the text in the rectangle, and blit it onto the screen
        screen.blit(text, textRect)

        # Make the screen display the new stuff
        pygame.display.update()

        time.sleep(0.1)

        fontsize += 5

    font = pygame.font.SysFont(None, 35, True, False)
    
    presentstext1 = font.render('Use w a s d to move.', True, (255, 255, 0), (0, 0, 0))
    presentstext2 = font.render('Avoid the blocks.', True, (255, 255, 0), (0, 0, 0))
    
    screen.blit(presentstext1, (screen.get_rect().centerx + 35, screen.get_rect().centery + 70))
    screen.blit(presentstext2, (screen.get_rect().centerx + 35, screen.get_rect().centery + 100))
    
    pygame.display.update()

    time.sleep(2.6)



