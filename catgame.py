import pygame, sys, grid
from pygame.locals import * 

pygame.init()

FPS = 60
FPSCLOCK = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600


screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('Poesje')

WHITE = (255,255,255)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)
BLACK = (  0,  0,  0)


catx = 000
caty = 300
catx2 = 780
caty2 = 300
mov_speed = 20

GRIDLINES = 10

teller = 0 
positionx = 0 
positiony = 0 

grid.drawGrid(WINDOWWIDTH, WINDOWHEIGHT,screen)

while True:
    for event in pygame.event.get():
        key =pygame.key.get_pressed()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif key[K_SPACE]:
            print "Space"
        elif key[K_RIGHT]:
            catx += mov_speed
            catx2 -= mov_speed
            if catx > WINDOWWIDTH - 20:
                catx = WINDOWWIDTH - 20
            if catx2 < 0:
                catx2 = 0
        elif key[K_UP]:
            caty -= mov_speed
            caty2 += mov_speed
            if caty < 0:
                caty = 0
            if caty2 > WINDOWHEIGHT - 20:
                caty2 = WINDOWHEIGHT - 20
        elif key[K_DOWN]:
            caty += mov_speed
            caty2 -= mov_speed
            if caty > WINDOWHEIGHT - 20:
                caty = WINDOWHEIGHT - 20
            if caty2 < 0:
                caty2 = 0
        elif key[K_LEFT]:
            catx -= mov_speed
            catx2 += mov_speed
            if catx < 0:
                catx = 0
            if catx2 > WINDOWWIDTH - 20:
                catx2 = WINDOWWIDTH - 20
    playbox = pygame.draw.rect(screen, RED, (catx, caty, 20, 20))
    playbox2 = pygame.draw.rect(screen, BLUE, (catx2, caty2, 20, 20))
    pygame.display.flip()
    FPSCLOCK.tick(FPS)

