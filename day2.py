import numpy as np

# 12 red, 13, green, 14 blue
# ; marks between rounds
# : marks game
games_list = []
with open('input2.txt', 'r') as file:
    for line in file:
        line = line.strip()
        # find first number: game number
        game = int("".join([s for s in line[4:8] if s.isdigit()]))
        # assume game is possible
        possible = True
        # extract all numbers, check if any are larger than 12
        numbers = [int(s) for s in line.split() if s.isdigit()]
        if any(n>12 for n in numbers):
            # check for colours
            for n in [ns for ns in numbers if ns>12]:
                index = line.find(str(n))
                if n > 14 and 'blue' in line[index:index+8]:
                    possible = False
                elif n > 13 and 'green' in line[index:index+8]:
                    possible = False
                elif n > 12 and 'red' in line[index:index+8]:
                    possible = False
        if possible is True:
            games_list.append(game)
print(games_list)
res1 = np.sum(games_list)
print('part 1:', res1)
