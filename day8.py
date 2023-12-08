import parse

with open('/home/space/phrpzz/aoc_inputs/input8.txt', 'r') as file:
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
# find node AAA as start point and follow instruct to navigate
for line in lines[2:]:
    line_d = line_dict(line, "{node:w} = ({right} , {left})\n")
    print(line_d)
