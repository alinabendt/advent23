import numpy as np

match_dict = {}
points = 0
with open('~/aoc_inputs/input4.txt', 'r') as file:
    for line in file:
        line = line.strip()
        card = "".join([s for s in line.split(':')[0] if s.isdigit()])
        winning, yours = line.split('|')
        winning = [int(s) for s in winning.split() if s.isdigit()]
        yours = [int(s) for s in yours.split() if s.isdigit()]
        matches = np.isin(winning, yours)
        # count up matches: first =1, every other doubles
        first = np.where(matches==True)
        # save number of matches and card number into dict for part 2
        match_dict[int(card)] = np.size(first[0])
        point = 0
        if np.size(first[0])!=0:
            m = np.size(np.where(matches[first[0][0]+1:]==True)[0])
            point = 2**m
        points = points+point
print('part1:', points)

# part 2: for each match win a consecutive card, get total number of cards
# go through each card in dict and get copies
copies = {}
for k in match_dict.keys():
    cps = np.arange(k+1, k+match_dict[k]+1)
    for c in cps:
        if c in copies.keys():
            copies[c] += 1
        elif c > max(match_dict.keys()):
            pass
        else:
            copies[c] = 1
# go through all copies and add cards up:
total_count = {}
for k in match_dict.keys():  # go through all cards
    total_count[k] = 1  # one for the original card
    if k in copies.keys():  # if card has copies then add copies to original number of cards
        total_count[k] = total_count[k]+copies[k]
        # add number of copies obtained from copies to following copy cards:
        for i in range(1, match_dict[k]+1):  # for number of matches add to copies
            copies[k+i] += copies[k]
# sum over all keys:
cards = sum(total_count.values())
print('part2:', cards)
