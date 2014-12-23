#!/usr/bin/env python3
import model


def verify(condition, error):
    if not condition:
        print(error)

model.randomize()

num_colours = 0
colours = []

for row in model.data:
    for col in row:
        if col not in colours:
            num_colours += 1
            colours.append(col)

verify(num_colours == 5, 'Wrong amount of colours')

model.data = [[1, 2], [3, 4]]
verify(model.get_block_colour(0, 0) == 1, "Colour 0,0 not 1")
verify(model.get_block_colour(0, 1) == 2, "Colour 0,1 not 2")
verify(model.get_block_colour(1, 0) == 3, "Colour 1,0 not 3")
verify(model.get_block_colour(1, 1) == 4, "Colour 1,1 not 4")

print('END')
