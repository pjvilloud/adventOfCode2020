import copy

input = """.#.#.#..
..#....#
#####..#
#####..#
#####..#
###..#.#
#..##.##
#.#.####"""
#
# input = """.#.
# ..#
# ###"""


def initialize_grid_layer(col, row, char):
    return [[char for i in range(col)] for j in range(row)]


def apply_rules(g, zz, yy, xx):
    cube = g[zz][yy][xx]
    max_size_x_y = len(g[0][0])
    max_size_z = len(g)
    nb_of_active_cubes = 0
    nb_of_inactive_cubes = 0
    # Counting the number of active and inactive cubes around
    for z1 in [zz - 1, zz, zz + 1]:
        for y1 in [yy - 1, yy, yy + 1]:
            for x1 in [xx - 1, xx, xx + 1]:
                if xx == x1 and yy == y1 and zz == z1:
                    continue
                if x1 < 0 or y1 < 0 or z1 < 0 or x1 >= max_size_x_y or y1 >= max_size_x_y or z1 >= max_size_z:
                    nb_of_inactive_cubes += 1
                elif g[z1][y1][x1] == '#':
                    nb_of_active_cubes += 1
                else:
                    nb_of_inactive_cubes += 1
    # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
    # Otherwise, the cube becomes inactive.
    if cube == '#' and (nb_of_active_cubes < 2 or nb_of_active_cubes > 3):
        return '.'
    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
    # Otherwise, the cube remains inactive.
    elif cube == '.' and nb_of_active_cubes == 3:
        return '#'
    return cube


def expand_grid(g):
    for cols in g:
        for rows in cols:
            rows.insert(0, '.')
            rows.append('.')
        cols.insert(0, ['.' for i in range(len(cols[0]))])
        cols.append(['.' for i in range(len(cols[0]))])
    return g


nb_of_cycles = 6
active_cycle = 1

# Initialize the grid with input : grid is a 3 dimensional array
grid = [list(map(lambda l: list(l), input.splitlines()))]
while active_cycle <= nb_of_cycles:
    # Add inactive cubes all around each layer
    expand_grid(grid)
    size = len(grid[0])
    # Add a layer of inactive cube at the beginning and at the end of the grid
    grid.insert(0, initialize_grid_layer(size, size, '.'))
    grid.append(initialize_grid_layer(size, size, '.'))
    grid_to_copy = copy.deepcopy(grid)
    for z in range(len(grid_to_copy)):
        for y in range(len(grid_to_copy[z])):
            for x in range(len(grid_to_copy[z][y])):
                grid_to_copy[z][y][x] = apply_rules(grid, z, y, x)
    active_cycle += 1
    grid = grid_to_copy

print "There are", str(grid).count("#"), "cubes active"
