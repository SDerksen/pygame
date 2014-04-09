# Draws a grid on the screen
import pygame, sys
from pygame.locals import *

def drawGrid( WINDOWWIDTH, WINDOWHEIGHT,screen,boxsize):
    WHITE = (255,255,255)
    RED   = (255,  0,  0)  
    BLUE  = (  0,  0,255)
    BLACK = (  0,  0,  0)
    GREEN = (  0,255,  0)

    
    linespacex = boxsize
    linespacey = boxsize
    GRIDLINES = WINDOWWIDTH / linespacex
    teller = 0
    positionx = 0
    positiony = 0
    while teller < GRIDLINES:
        GRIDSPACEX = WINDOWWIDTH
        positionx = positionx + linespacex
        pygame.draw.line(screen, GREEN, (positionx, 0), (positionx, WINDOWHEIGHT))

        GRIDSPACEY = WINDOWHEIGHT
        positiony = positiony + linespacey
        pygame.draw.line(screen, GREEN, (0, positiony), (WINDOWWIDTH, positiony))
    
        teller = teller + 1

        print "Done %d" % teller
        pygame.display.update()
