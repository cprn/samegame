import random

data = []
NUM_COLOURS = 5
GRID_SIZE = 20


def init():
    for row in range(GRID_SIZE):
        r = []
        for col in range(GRID_SIZE):
            r.append(random.randint(0, NUM_COLOURS - 1))
        data.append(r)


def get_block_colour(row, col):
    if row >= 0 and row < get_height() and col >= 0 and col < get_width():
        return data[row][col]
    return None


def get_syblings(x, y, syblings=None):
    colour = get_block_colour(x, y)
    if colour is None:
        return
    if syblings is None:
        syblings = [(x, y)]
    for neighbour in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
        if neighbour in syblings:
            continue
        if get_block_colour(*neighbour) == colour:
            syblings.append(neighbour)
            syblings = get_syblings(*neighbour, syblings=syblings)
    return syblings


def get_height():
    return len(data)


def get_width():
    return len(data[0])


def remove_block(x, y):
    data[y][x] = None
