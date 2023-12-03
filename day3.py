import numpy as np
import re

grid = []
coord_s = []
coord_n = []
with open('input3.txt', 'r') as file:
    count = 0
    for line in file:
        line = line.strip()
        grid.append(line)
        # find all coordinates of symbols, ie not a dot or number
        for s in line:
            if s.isdigit():
                co = line.find(s)
                while [count, co] in coord_n:
                    co = line[co+1:].find(s)+co+1
                coord_n.append([count, co])
            elif s!='.':
                co = line.find(s)
                while [count, co] in coord_s:
                    co = line[co+1:].find(s)+co+1
                coord_s.append([count, co])
        count +=1
# check if number is adjacent to symbol
numbers = []
with_symb = []  # first coord is number, second is symbol
for c in coord_n:  # go through all digits
    adj = []
    for i in [[c[0]+1, c[1]], [c[0]-1, c[1]], [c[0], c[1]+1], [c[0], c[1]-1], [c[0]+1, c[1]+1], [c[0]+1, c[1]-1], [c[0]-1, c[1]+1], [c[0]-1, c[1]-1]]:
        if -1 in i:
            pass
        elif 140 in i:
            pass
        else:
            adj.append(i)
    for a in adj:
        if any(a == s for s in coord_s):
            # a digit is adjacent to a symbol
            with_symb.append([c, a])
# if previous coordinate is also number and adjacent to symbol, then pass, since it belongs to same number
for c, a in list(reversed(with_symb)):
    if [[c[0], c[1]-1], a] in with_symb:
        pass
    else:
        numbers.append(c)
# extract all numbers from starting coordinate
result = []
for c in numbers:
    num = grid[c[0]][c[1]]
    if grid[c[0]][c[1]+1].isdigit():
        num = num+grid[c[0]][c[1]+1]
        if grid[c[0]][c[1]+2].isdigit():
            num = num+grid[c[0]][c[1]+2]
    if grid[c[0]][c[1]-1].isdigit():
        num = grid[c[0]][c[1]-1]+num
        if grid[c[0]][c[1]-2].isdigit():
            num = grid[c[0]][c[1]-2]+num
    result.append(int(num))
print('part1:', np.sum(result))
