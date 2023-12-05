import numpy as np

grid = []
coord_s = []
coord_n = []
with open('~/aoc_inputs/input3.txt', 'r') as file:
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
with_symb_filtered = []
for c, a in list(reversed(with_symb)):
    if [[c[0], c[1]-1], a] in with_symb:
        pass
    else:
        numbers.append(c)
        with_symb_filtered.append([c, a])
# extract all numbers from starting coordinate
result = []
def find_num(c0, c1):
    num = grid[c0][c1]
    if grid[c0][c1+1].isdigit():
        num = num+grid[c0][c1+1]
        if grid[c0][c1+2].isdigit():
            num = num+grid[c0][c1+2]
    if grid[c0][c1-1].isdigit():
        num = grid[c0][c1-1]+num
        if grid[c0][c1-2].isdigit():
            num = grid[c0][c1-2]+num
    return num

for c in numbers:
    num = find_num(c[0], c[1])
    result.append(int(num))
print('part1:', np.sum(result))

# part 2: find all stars adjacent to two numbers and multiply those two numbers
# go through all with_symb coordinates and find which ones are a star
stars = []
for c, a in with_symb_filtered:
    if grid[a[0]][a[1]] == '*':
        stars.append([c, a])
# find those which have more than 1 number
stars_filtered = []
for c, a in stars:
    count = 0
    for c2, a2 in stars:
        if a2==a:
            count +=1
    if count == 2:
        stars_filtered.append([c,a])
# multiply the two numbers associated with the same star
result2 = []
completed_stars = []
for c, a in stars_filtered:
    if a in completed_stars:
        pass
    else:
        # find first number
        num1 = find_num(c[0],c[1])
        # find second number
        c2 = []
        for x,y in stars_filtered:
            if y==a:
                if x != c:
                    a2 = y
                    c2 = x
        num2 = find_num(c2[0], c2[1])
        completed_stars.append(a)
        result2.append(int(num1)*int(num2))
print('part2:', np.sum(result2))
