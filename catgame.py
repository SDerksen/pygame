import pygame, sys, grid
from pygame.locals import * 

pygame.init()

FPS = 100
FPSCLOCK = pygame.time.Clock()

WINDOWWIDTH = 1020
WINDOWHEIGHT = 800

screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('Poesje')

WHITE = (255,255,255)
RED   = (255,  0,  0)
BLUE  = (  0,  0,255)
BLACK = (  0,  0,  0)

boxsize = 20
catx = 000
caty = 0
catx2 = WINDOWWIDTH - boxsize
caty2 = WINDOWHEIGHT - boxsize
mov_speed = boxsize

grid.drawGrid(WINDOWWIDTH, WINDOWHEIGHT,screen,boxsize)

while True:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if key[K_SPACE]:
            print "Space"
        if key[K_RIGHT]:
            catx += mov_speed
            catx2 -= mov_speed
            if catx > WINDOWWIDTH - boxsize:
                catx = WINDOWWIDTH - boxsize
            if catx2 < 0:
                catx2 = 0
        if key[K_UP]:
            caty -= mov_speed
            caty2 += mov_speed
            if caty < 0:
                caty = 0
            if caty2 > WINDOWHEIGHT - boxsize:
                caty2 = WINDOWHEIGHT - boxsize
        if key[K_DOWN]:
            caty += mov_speed
            caty2 -= mov_speed
            if caty > WINDOWHEIGHT - boxsize:
                caty = WINDOWHEIGHT - boxsize
            if caty2 < 0:
                caty2 = 0
        if key[K_LEFT]:
            catx -= mov_speed
            catx2 += mov_speed
            if catx < 0:
                catx = 0
            if catx2 > WINDOWWIDTH - boxsize:
                catx2 = WINDOWWIDTH - boxsize
    playbox = pygame.draw.rect(screen, RED, (catx, caty, boxsize, boxsize))
    playbox2 = pygame.draw.rect(screen, BLUE, (catx2, caty2, boxsize, boxsize))
    pygame.display.update()
    FPSCLOCK.tick(FPS)
