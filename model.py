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
    if x in range(get_width()) and y in range(get_height()):
        return data[x][y]
    return None


def get_siblings(x, y, siblings=None):
    colour = get_block_colour(x, y)
    if colour is None:
        return []
    if siblings is None:
        siblings = [(x, y)]
    for neighbour in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
        if neighbour in siblings:
            continue
        if get_block_colour(*neighbour) == colour:
            siblings.append(neighbour)
            siblings = get_siblings(*neighbour, siblings=siblings)
    return siblings


def get_height():
    if len(data):
        return len(data[0])
    return 0


def get_width():
    return len(data)


def remove_block(x, y):
    for block in get_siblings(x, y):
        data[block[0]][block[1]] = None


def run_gravity():
    for x in reversed(range(get_width())):
        if data[x] == [None] * get_height():
            data.pop(x)
            continue
        for y in reversed(range(get_height())):
            if get_block_colour(x, y) is None and y != 0:
                data[x][y] = data[x][y-1]
                data[x][y-1] = None
