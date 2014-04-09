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

class Snake(object):
    def __init__(self):
        self.boxsize = 20
        self.snakex = 000
        self.snakey = 0
        self.mov_speed = self.boxsize
        self.direction = 'right'

    def drawSelf(self,screen, color):
        pygame.draw.rect(screen, BLUE, (self.snakex, self.snakey, self.boxsize, self.boxsize))

        
    def detectWall(self, windowx, windowy):
        if self.snakex > windowx - self.boxsize:
            self.snakex = windowx - self.boxsize
            return self.snakex, self.snakey
        if self.snakex < 0:
            self.snakex = 0
            return self.snakex, self.snakey
        if self.snakey < 0:
            self.snakey = 0
            return self.snakex, self.snakey
        if self.snakey > windowy - self.boxsize:
            self.snakey = windowy - self.boxsize
            return self.snakex, self.snakey

snake = Snake()
grid.drawGrid(WINDOWWIDTH, WINDOWHEIGHT,screen,snake.boxsize)


while True:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if key[K_RIGHT]:
            snake.direction = 'right'
        if key[K_UP]:
            snake.direction = 'up'
        if key[K_DOWN]:
            snake.direction = 'down'
        if key[K_LEFT]:
            snake.direction = 'left'

    if snake.direction == 'right':
        snake.snakex = snake.snakex + snake.mov_speed
    if snake.direction == 'left':
        snake.snakex = snake.snakex - snake.mov_speed
    if snake.direction == 'up':
        snake.snakey = snake.snakey - snake.mov_speed
    if snake.direction == 'down':
        snake.snakey = snake.snakey + snake.mov_speed
    snake.drawSelf(screen, BLUE)
    snake.detectWall(WINDOWWIDTH,WINDOWHEIGHT)
    #hit = detectCollision(snakex,snakey,WINDOWWIDTH,WINDOWHEIGHT,snake.boxsize)
    #if hit != None:
    #    snakex = hit[0]
    #    snakey = hit[1]
    pygame.display.update()
    FPSCLOCK.tick(FPS)
