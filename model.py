import random

# data structure

data = [[None] * 100] * 100
NUM_COLOURS = 5


def randomize():
    for row in range(len(data)):
        for col in range(len(data[row])):
            data[row][col] = random.randint(0, NUM_COLOURS-1)


def get_block_colour(row, col):
    if row >= 0 and row < len(data) and col >= 0 and col < len(data[row]):
        return data[row][col]
    return None
