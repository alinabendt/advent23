import numpy as np

# 12 red, 13, green, 14 blue
# ; marks between rounds
# : marks game
games_list = []
with open('~/aoc_inputs/input2.txt', 'r') as file:
    for line in file:
        line = line.strip()
        # find first number: game number
        game = int("".join([s for s in line[0:line.find(':')] if s.isdigit()]))
        # assume game is possible
        possible = True
        rounds = line.split(';')
        # extract all numbers, check if any are larger than 12
        numbers = [int(s) for s in line.split() if s.isdigit()]
        # check for colours
        if any(n>14 for n in numbers):
            possible = False
        elif any(n>12 for n in numbers):
            # go through each round
            for r in rounds:
                ns = [int(s) for s in r.split() if s.isdigit()]
                for n in [m for m in ns if m>12]:
                    index = r.find(str(n))
                    if  n > 12 and 'red' in r[index:index+8]:
                        possible = False
                    elif n > 13 and 'green' in r[index:index+8]:
                        possible = False
        if possible is True:
            games_list.append(game)
res1 = np.sum(games_list)
print('part 1:', res1)

# part 2:
# fewest number of cubes in bag
powers = []
with open('input2.txt', 'r') as file:
    for line in file:
        line = line.strip()
        # find largest number of one colour pulled in each game:
        # split after each symbol
        print(line)
        line = re.split('[:,;]', line)
        colours = line[1:]
        game = [int(s) for s in line[0].split() if s.isdigit()]
        greens = "".join([g for g in line if 'green' in g])
        greens = [int(s) for s in greens.split() if s.isdigit()]
        min_g = np.max(greens)
        reds = "".join([r for r in line if 'red' in r])
        reds = [int(s) for s in reds.split() if s.isdigit()]
        min_r = np.max(reds)
        blues = "".join([b for b in line if 'blue' in b])
        blues = [int(s) for s in blues.split() if s.isdigit()]
        min_b = np.max(blues)
        print('blue', min_b, 'red', min_r, 'green', min_g)
        powers.append(min_b*min_g*min_r)
res2 = np.sum(powers)
print('part2:', res2)
