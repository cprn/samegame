#!/usr/bin/env python
import model


def verify(condition, error):
    if not condition:
        print(error)

model.init()

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
verify(model.get_block_colour(2, 0) is None, "Colour 2,0 not None")

model.data = [[1, 2, 5, 8], [6, 3, 4, 7]]
verify(model.get_height() == 2, "Height not 2")
verify(model.get_width() == 4, "Width not 4")

rm = (1, 1)
verify(model.get_block_colour(*rm) is not None, "Block 2,0 None before test")
model.remove_block(*rm)
verify(model.get_block_colour(*rm)is None, "Block 2,0 not None")

print('END')
