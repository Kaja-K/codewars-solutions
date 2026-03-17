"""
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. 
A tower block is represented with "*" character.

    Tower with 3 floors looks like this:

    [
    "  *  ",
    " *** ", 
    "*****"
    ]


"""


def tower_builder(n_floors):
    tower = []
    stars = "*"
    width = (n_floors * 2) - 1
    for x in range(1, 2 * n_floors, 2):
        stars = x * "*"
        line = stars.center(width)
        tower.append(line)
    return tower
