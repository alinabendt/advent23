import parse
import numpy as np

with open('/home/alina/aoc_inputs/input8.txt', 'r') as file:
# with open('/home/space/phrpzz/aoc_inputs/input8.txt', 'r') as file:
    lines = file.readlines()

instruct = lines[0].strip()

def line_dict(lin, pattern):
    """
    When given a line and pattern returns a dictonary of keys and values

    example repeated line:
    "1 Card 1: 41 48 83 86 17 | 81 87  9 41 27  4 48 52\n"

    example corresponding pattern
    "Card {card:d}: {winners} | {hand}\n"

    example returned dict
    {'card': 1, 'winners': '41 48 83 86 17', 'hand': '81 87  9 41 27  4 48 52'}

    """
    pattern = parse.compile(pattern)
    match = pattern.search(lin)
    return match.named

# construct network from nodes
# dictionary? each node is a key with left and right options
nodes = {}
# find node AAA as start point and follow instruct to navigate
for line in lines[2:]:
    line = line.strip()
    line_d = line_dict(line, '{node} = ({left}, {right})')
    nodes[line_d['node']] = line_d
x = 0
steps = 0
current = nodes['AAA']
while current != nodes['ZZZ']:
    steps += 1
    if x>=len(instruct):
        x = 0
    if instruct[x]=='R':
        current = nodes[current['right']]
    else:
        current = nodes[current['left']]
    x += 1
print('part1:', steps)

# part 2
# follow every node that ends in A until every path simultaneaously is at a node that ends in Z
# replace all starting letters with numbers for nodes
all_a = {}
for node in nodes.keys():
    if node.endswith('A'):
        all_a[node] = nodes[node]
steps2 = []
# find common minimum number of steps from each branch
for i, a in enumerate(list(all_a.keys())):
    current = nodes[a]
    x = 0
    steps = 0
    while len(steps2)<i+1:
        steps += 1
        if x>=len(instruct):
            x = 0
        if instruct[x]=='R':
            current = nodes[current['right']]
        else:
            current = nodes[current['left']]
        if current['node'].endswith('Z'):
            steps2.append(steps)
        x += 1
# find step number at which all reach
# every node comes to an end node every multiple of the first hit
lcm = np.lcm.reduce(steps2)
print('part2:', lcm)
