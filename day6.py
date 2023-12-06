import numpy as np

with open('/home/space/phrpzz/aoc_inputs/input6.txt', 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    lines[i] = line.strip()
times = [int(s) for s in lines[0].split(' ') if s.isdigit()]
records = [int(s) for s in lines[1].split(' ') if s.isdigit()]

beat = []
for r, time in enumerate(times):
    options = 0
    for t in range(time):
        d = (time-t)*t
        if d>records[r]:
            options += 1
    beat.append(options)
res1 = np.prod(beat)
print('part1:', res1)

# part2: actyally just one race
times = int("".join([str(t) for t in times]))
records = int("".join([str(r) for r in records]))
option2 = 0
for t in range(times):
    d = (times-t)*t
    if d>records:
        option2 += 1
print('part2:', option2)
