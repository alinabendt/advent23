import numpy as np

seeds = []
with open('~/aoc_inputs/input5.txt', 'r') as file:
    lines = file.readlines()

seeds = [int(s) for s in lines[0].split() if s.isdigit()]
seed_map = seeds.copy()
for line in lines[1:]:
    line = line.strip()
    if 'map' in line:
        changed = []
    elif line == '':
        pass
    else:
        dest, source, r_len = [int(s) for s in line.split() if s.isdigit()]
        dest = dest-source
        for i, s in enumerate(seed_map):
            if s in range(source, source+r_len):
                if i in changed:
                    pass
                else:
                    seed_map[i] = s+dest
                    changed.append(i)
low_loc = min(seed_map)
print('part1:', low_loc)

# part 2: each pair of numbers gives range of seeds
seeds = [int(s) for s in lines[0].split() if s.isdigit()]
starts = [seeds[s] for s in np.arange(len(seeds), step=2)]
ends = [seeds[s] for s in np.arange(1, len(seeds), step=2)]
seed_map = seeds.copy()

