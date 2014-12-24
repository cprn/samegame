import pygame
import sys
from pygame.locals import *
import model


pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

PIECE_COLOURS = (WHITE, RED, GREEN, BLUE, YELLOW)

PIECE_WIDTH = 30
PIECE_HEIGHT = 30
PIECE_MARGIN = 2


windowSurface = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Same Game')

while True:
    windowSurface.fill(BLACK)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
