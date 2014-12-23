import random

# data structure

data = [[None] * 100] * 100
NUM_COLOURS = 5


def randomize():
    for row in range(len(data)):
        for col in range(len(data[row])):
            data[row][col] = random.randint(0, NUM_COLOURS-1)
