import random

data = []
NUM_COLOURS = 5
GRID_SIZE = 20


def init():
    for y in range(GRID_SIZE):
        r = []
        for x in range(GRID_SIZE):
            r.append(random.randint(0, NUM_COLOURS - 1))
        data.append(r)


def get_block_colour(x, y):
    if x >= 0 and x < get_width() and y >= 0 and y < get_height():
        return data[x][y]
    return None


def get_syblings(x, y, syblings=None):
    colour = get_block_colour(x, y)
    if colour is None:
        return []
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
    for block in get_syblings(x, y):
        data[block[0]][block[1]] = None


def run_gravity():
    for y in reversed(range(get_height())):
        for x in range(get_width()):
            if get_block_colour(x, y) is None and y != 0:
                data[x][y] = data[x][y-1]
                data[x][y-1] = None
