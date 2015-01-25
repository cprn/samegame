import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONUP
import model


def get_click_pos(event):
    return (
        event.pos[0] // (PIECE_WIDTH + PIECE_MARGIN),
        event.pos[1] // (PIECE_HEIGHT + PIECE_MARGIN)
    )

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

pygame.init()
model.init()

windowSurface = pygame.display.set_mode((
    model.get_width() * (PIECE_WIDTH + PIECE_MARGIN),
    model.get_height() * (PIECE_HEIGHT + PIECE_MARGIN)
))
pygame.display.set_caption('Same Game')

while True:
    windowSurface.fill(BLACK)
    for row in range(model.get_height()):
        for col in range(model.get_width()):
            colour = model.get_block_colour(row, col)
            if colour is not None:
                pieceColour = PIECE_COLOURS[colour]
                pygame.draw.rect(windowSurface, pieceColour, (
                    col * (PIECE_WIDTH + PIECE_MARGIN),
                    row * (PIECE_HEIGHT + PIECE_MARGIN),
                    PIECE_WIDTH,
                    PIECE_HEIGHT
                ))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            model.remove_block(*get_click_pos(event))
