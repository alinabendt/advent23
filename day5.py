import numpy as np

seeds = []
with open('/home/alina/aoc_inputs/input5_ex.txt', 'r') as file:
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
ranges_o = [(seeds[s], seeds[s]+seeds[s+1]) for s in np.arange(len(seeds), step=2)]
# create list of separate sets for seeds
def merge_ranges(ranges):
    new_rs = []
    for i, (s, e) in enumerate(ranges):
        if any(t[1] >= s for t in new_rs):
            for j, (s1, e1) in enumerate(new_rs):
                if s1<=s and e1>=e:  # fully included
                    break
                elif s1<=s and e1<=e:  # extend range to new e
                    new_rs[j] = (s1, e)
                elif s1>=s and e1>=e and s1<=e:  # extend range to new s
                    new_rs[j] = (s, e1)
        else:
            new_rs.append((s,e))
    return new_rs

ranges_o = sorted(ranges_o)
ranges = merge_ranges(ranges_o)
print(ranges_o)

new_ranges = []
for line in lines[1:]:
    line = line.strip()
    if 'map' in line or line=='':
        print(line)
        # integrate new ranges into original ones
        if new_ranges != []:
            print(new_ranges)
            ranges = merge_ranges(new_ranges)
            print(ranges)
        new_ranges = []
        pass
    else:
        # extract numbers
        dest, source, r_len = [int(s) for s in line.split() if s.isdigit()]
        dest = dest-source
        # if source range overlaps with an existing range:
        # three cases for each source:
        # 1. start and end of range are in source
        # 2. start is in source, end outside
        # 3. start is outside source, end is inside
        # for each range test if it overlaps with source:
        for (rs, re) in ranges:
            print('range',rs,re, source, source+r_len, dest)
            if rs in range(source, source+r_len) or re in range(source, source+r_len):  # if there is any overlap
                # save new ranges into array until next mapping
                if rs >= source and re <= source+r_len:
                    if (rs,re) in new_ranges:
                        ind = [i for i, item in enumerate(new_ranges) if item==(rs,re)]
                        new_ranges.remove((rs,re))
                    new_ranges.append((rs+dest, re+dest))
                elif rs >= source and re > source+r_len:
                    # split into subranges: rs-source-end and source-end-re
                    # adjust rs-source-end by destination
                    new_ranges.append((rs+dest, source+r_len+dest))
                    new_ranges.append((source+r_len, re))
                    # print(dest, rs, source+r_len, rs+dest, source+r_len+dest)
                elif rs < source and re >= source and re <= source+r_len:
                    # split into subranges: rs-source and source-re
                    # adjust source-re by destination
                    new_ranges.append((rs, source))
                    new_ranges.append((source+dest, re+dest))
                    # print(dest, source, re, source+dest, re+dest)
            else:  # no overlap, leave as it is
                if (rs, re) in new_ranges:
                    pass
                else:
                    new_ranges.append((rs, re))
print(ranges_o)
print(ranges)
