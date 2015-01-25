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
    if row >= 0 and row < len(data) and col >= 0 and col < len(data[row]):
        return data[row][col]
    return None


def get_height():
    return len(data)


def get_width():
    return len(data[0])


def remove_block(x, y):
    data[y][x] = None
