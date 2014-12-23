import model


def verify(condition, error):
    if not condition:
        print error

model.randomize()

num_colours = 0
colours = []

for row in model.data:
    for col in row:
        if col not in colours:
            num_colours += 1
            colours.append(col)

verify(num_colours == 5, 'Wrong amount of colours')

print 'END'
