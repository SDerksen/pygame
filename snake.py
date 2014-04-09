import pygame, sys, grid
from pygame.locals import * 

pygame.init()

FPS = 30
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
snakex = 000
snakey = 0
mov_speed = boxsize
direction = 'right'

grid.drawGrid(WINDOWWIDTH, WINDOWHEIGHT,screen,boxsize)

def detectCollision(snakex,snakey,WINDOWWIDTH,WINDOWHEIGHT, boxsize):
    if snakex > WINDOWWIDTH - boxsize:
        snakex = WINDOWWIDTH - boxsize
        return snakex, snakey

    if snakex < 0:
        snakex = 0
        return snakex, snakey

    if snakey < 0:
        snakey = 0
        return snakex, snakey

    if snakey > WINDOWHEIGHT - boxsize:
        snakey = WINDOWHEIGHT - boxsize
        return snakex, snakey

        
while True:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if key[K_RIGHT]:
            direction = 'right'
        if key[K_UP]:
            direction = 'up'
        if key[K_DOWN]:
            direction = 'down'
        if key[K_LEFT]:
            direction = 'left'

    if direction == 'right':
        snakex = snakex + mov_speed
    if direction == 'left':
        snakex = snakex - mov_speed
    if direction == 'up':
        snakey = snakey - mov_speed
    if direction == 'down':
        snakey = snakey + mov_speed
    playbox = pygame.draw.rect(screen, BLUE, (snakex, snakey, boxsize, boxsize))
    hit = detectCollision(snakex,snakey,WINDOWWIDTH,WINDOWHEIGHT,boxsize)
    if hit != None:
        snakex = hit[0]
        snakey = hit[1]
    pygame.display.update()
    FPSCLOCK.tick(FPS)
