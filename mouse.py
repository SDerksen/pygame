# mouse input 
# By Sem Derksen

import pygame, sys
from pygame.locals import *

# set the constant variables

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30


UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF

    mousex = 0
    mousey = 0

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Mouse locator')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                print mousex, mousey
                pygame.display.update()
            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                print "Left mouse button down on %d, %d" % (mousex, mousey)
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                print "Left mouse button up on %d, %d" % (mousex, mousey)
            elif event.type == K_SPACE:
                print "Meow Meow"


if __name__ == '__main__':
    main()
