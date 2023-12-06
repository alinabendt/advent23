import numpy as np

seeds = []
# with open('/home/alina/aoc_inputs/input5_ex.txt', 'r') as file:
with open('/home/space/phrpzz/aoc_inputs/input5.txt', 'r') as file:
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
        if len(new_rs)>1 and new_rs[i-1][1] >= s:  # if previous range extends into new range
            s1, e1 = new_rs[i-1]
            if s1<=s and e1>=e:  # fully included
                break
            if s1<=s and e1<=e:  # extend range to new e
                new_rs[i-1] = (s1, e)
            elif e1>=e>=s1>=s:  # extend range to new s
                new_rs[i-1] = (s, e1)
        else:
            new_rs.append((s,e))
    return new_rs

ranges_o = sorted(ranges_o)
ranges = merge_ranges(ranges_o)

new_ranges = ranges
for line in lines[1:]:
    line = line.strip()
    if 'map' in line or line=='':
        # print(line)
        # print(new_ranges)
        # use new ranges for next mapping
        adjusted = []
        to_delete = []
    else:
        # extract numbers
        # print(to_delete)
        for i in to_delete:
            new_ranges.remove(i)
        to_delete = []
        dest, source, r_len = [int(s) for s in line.split() if s.isdigit()]
        dest = dest-source
        # if source range overlaps with an existing range:
        # three cases for each source:
        # 1. start and end of range are in source
        # 2. start is in source, end outside
        # 3. start is outside source, end is inside
        # for each range test if it overlaps with source:
        # print(new_ranges)
        for (rs, re) in new_ranges:
            # print(adjusted)
            # print(new_ranges)
            # print('range',rs,re, source, source+r_len, dest)
            if (rs,re) in adjusted:
                pass
            elif rs in range(source, source+r_len) or re in range(source, source+r_len):  # if there is any overlap
                # save new ranges into array until next mapping
                if rs >= source and re <= source+r_len:  # range is fully in source
                    if (rs,re) in new_ranges:
                        ind = [i for i, item in enumerate(new_ranges) if item==(rs,re)]
                        new_ranges.remove((rs,re))
                        new_ranges.insert(ind[0], (rs+dest, re+dest))
                    else:
                        new_ranges.append((rs+dest, re+dest))
                    adjusted.append((rs+dest, re+dest))
                elif source+r_len >= rs >= source and re > source+r_len:  # range start lies in source
                    # split into subranges: rs-source-end and source-end-re
                    # adjust rs-source-end by destination
                    if (rs,re) in new_ranges:
                        to_delete.append((rs,re))
                    new_ranges.append((rs+dest, source+r_len+dest))
                    adjusted.append((rs+dest, source+r_len+dest))
                    new_ranges.append((source+r_len, re))
                    # print(dest, rs, source+r_len, rs+dest, source+r_len+dest)
                elif rs < source and re > source and re <= source+r_len:  # range end lies in source
                    # split into subranges: rs-source and source-re
                    # adjust source-re by destination
                    if (rs,re) in new_ranges:
                        to_delete.append((rs,re))
                    new_ranges.append((rs, source))
                    new_ranges.append((source+dest, re+dest))
                    adjusted.append((source+dest, re+dest))
                    # print(dest, source, re, source+dest, re+dest)
                else:  # no overlap, leave as it is
                    if (rs,re) in new_ranges:
                        pass
                    else:
                        new_ranges.append((rs, re))
ranges = sorted(ranges)
low_loc2 = min(ranges)[0]
print('part2:', low_loc2)
