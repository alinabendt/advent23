import numpy as np

points = 0
with open('input4.txt', 'r') as file:
    for line in file:
        line = line.strip()
        winning, yours = line.split('|')
        winning = [int(s) for s in winning.split() if s.isdigit()]
        yours = [int(s) for s in yours.split() if s.isdigit()]
        matches = np.isin(winning, yours)
        # count up matches: first =1, every other doubles
        first = np.where(matches==True)
        point = 0
        if np.size(first[0])!=0:
            m = np.size(np.where(matches[first[0][0]+1:]==True)[0])
            point = 2**m
        points = points+point
print('part1:', points)
