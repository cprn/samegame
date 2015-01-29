#!/usr/bin/env python
import model


def verify(condition, error):
    if not condition:
        print(error)

model.init()

num_colours = 0
colours = []

for y in model.data:
    for x in y:
        if x not in colours:
            num_colours += 1
            colours.append(x)

verify(num_colours == model.NUM_COLOURS, 'Wrong amount of colours')

model.data = [[1, 2], [3, 4]]
verify(model.get_block_colour(0, 0) == 1, "Colour 0,0 not 1")
verify(model.get_block_colour(0, 1) == 2, "Colour 0,1 not 2")
verify(model.get_block_colour(1, 0) == 3, "Colour 1,0 not 3")
verify(model.get_block_colour(1, 1) == 4, "Colour 1,1 not 4")
verify(model.get_block_colour(2, 0) is None, "Colour 2,0 not None")

model.data = [[1, 2, 5, 8], [6, 3, 4, 7]]
verify(model.get_width() == 2, "Height not 2")
verify(model.get_height() == 4, "Width not 4")

model.data = [[0, 0], [1, 1]]
rm = (1, 1)
verify(model.get_block_colour(*rm) is not None, "Block 2,0 None before test")
model.remove_block(*rm)
verify(model.get_block_colour(*rm) is None, "Block 2,0 not None")

model.data = [
    [1, 1, 2],
    [3, 2, 2],
    [1, 1, 1]
]
syblings = [(0, 2), (1, 2), (1, 1)]
verify(model.get_syblings(*syblings[0]) == syblings, "No syblings")
x = (0, 2)
model.remove_block(*x)
for s in syblings:
    verify(model.get_block_colour(*s) is None, repr(s) + " not removed")

'''
[1, 1, 0]
[3, 0, 0]
[1, 1, 1]
after 1st gravity pass:
[0, 1, 1]
[0, 3, 0]
[1, 1, 1]
'''
before = model.data
model.run_gravity()
verify(model.get_block_colour(0, 2) == 1, "0, 2 didn't get new colour")
verify(model.get_block_colour(0, 0) is None, "0, 0 colour didn't drop")
verify(model.get_block_colour(1, 0) is None, "1, 0 colour didn't drop")
verify(model.get_block_colour(1, 1) == 3, "1, 1 didn't get new colour")
verify(model.get_block_colour(1, 2) is None, "1, 2 got new colour")
verify(before[2] == model.data[2], "Gravity moved row 2")

'''
[0, 1, 1]
[0, 3, 0]
[1, 1, 1]
after rm block:
[0, 1, 1]
[0, 0, 0]
[1, 1, 1]
after 2nd gravity pass:
[0, 1, 1]
[1, 1, 1]
'''
model.remove_block(1, 1)
model.run_gravity()
verify(model.data == [[None, 1, 1], [1, 1, 1]], "2nd gravity pass failed")

print('FINISHED')
