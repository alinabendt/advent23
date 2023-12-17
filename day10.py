# find one giant loop:
# | straight, - straight, L north-east, J north-west, 7 south-west, F south-east
# F-7
# |.|
# L-J
# starting position is S
# find S and the giant loop conneecting it back to itself:
# go through all adjacent paths and try which one leads back to S
with open('/home/alina/aoc_inputs/input10.txt', 'r') as file:
    lines = file.readlines()
count = 0
for line in lines:
    if 'S' in line:
        i = line.find('S')
        s_coord = (count, i)
    count += 1
# from S coord find all adjacent pipes and follow each path

def adjacent(c1, c2):
    # only down, up, right or left options
    return [(c1+1, c2), (c1-1, c2), (c1, c2+1), (c1, c2-1)]

def next_possible(pipe, coord):
    if pipe == '|':  # can only go up or down:
        next_c = [(coord[0]-1, coord[1]), (coord[0]+1, coord[1])]
        # possible smybols to connect to: F, 7, | for up and J, L, | for down
        next_s = [['F', '7', '|'],['J', 'L', '|']]
    elif pipe == '-':  # can only go right or left:
        next_c = [(coord[0], coord[1]+1), (coord[0], coord[1]-1)]
        next_s = [['J', '-', '7'],['L', '-', 'F']]
    elif pipe == 'F':  # can only go right or down:
        next_c = [(coord[0]+1, coord[1]), (coord[0], coord[1]+1)]
        next_s = [['|', 'J', 'L'],['-', 'J', '7']]
    elif pipe == 'J':  # can only go left or up
        next_c = [(coord[0]-1, coord[1]), (coord[0], coord[1]-1)]
        next_s = [['|', '7', 'F'],['-', 'F', 'L']]
    elif pipe == '7':  # can only go left or down:
        next_c = [(coord[0]+1, coord[1]), (coord[0], coord[1]-1)]
        next_s = [['|', 'J', 'L'],['-', 'F', 'L']]
    elif pipe == 'L':  # can only go up or right:
        next_c = [(coord[0]-1, coord[1]), (coord[0], coord[1]+1)]
        next_s = [['|', '7', 'F'],['-', 'J', '7']]
    return next_c, next_s

def check(possible, symb):
    coords = []
    for p, sy in zip(possible, symb):  # adjacent coordinates which might be possible depending on symbol
        if any(s==lines[p[0]][p[1]] for s in sy):
            # if p corresponds to symbol which connects, then save to possible coordinates
            for s in sy:
                if s==lines[p[0]][p[1]]:
                    coords.append(p)
    return coords  # returns next possible coordinates from pipe

paths = adjacent(s_coord[0], s_coord[1])
# possible pipes from S:
# for up: F, |, 7
# fown: |, J, L
# right: J, -, 7
# left: L, F, -
s_symb = [['|', 'J', 'L'],['F', '|', '7'],['J','-','7'],['L','F','-']]
ends = {}
# go through each possible path from s_coord:
for p, s in zip(paths, s_symb):
    if any(y==lines[p[0]][p[1]] for y in s):
        # try and follow path for as long as possible and save end point
        cs = [0]
        p_1 = [s_coord]
        p_0 = p
        length = 1
        # since each pipe only has two connection points, no branches
        while cs != []:
            # check next possible coords and symbols:
            n_c, n_s = next_possible(lines[p[0]][p[1]], p)
            # check if any of the possible coords ligns up with p
            cs = check(n_c, n_s)
            # remove the previous coordinate from cs
            if p_1[-1] in cs:
                cs.remove(p_1[-1])
            if cs == []:
                # dead end
                # only save as end if p not in paths
                ends[p_0] = [p, length]
                break
            elif p in p_1:
                ends[p_0] = [p, length]
                break
            else:  # continue with new p
                p_1.append(p)
                p = cs[0]
                length +=1
path_length = []
for key in ends:
    path_length.append((ends[key][1]+1)/2)
print('part1:', max(path_length))
