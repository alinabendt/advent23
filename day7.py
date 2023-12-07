from operator import itemgetter
from collections import Counter
import numpy as np

with open('/home/space/phrpzz/aoc_inputs/input7.txt', 'r') as file:
    lines = file.readlines()

hand_dict = {'five': [], 'four': [], 'full': [], 'three': [], 'two_p': [], 'one_p': [], 'high': []}
bids = {}
def determine_type(h, h_dict):
    count = Counter(h)
    count = dict(count)
    # different types:
    # five of a kind
    if any(item==5 for k, item in count.items()):
        h_dict['five'].append(list(h))
    # four of a kind
    elif any(item==4 for k, item in count.items()):
        h_dict['four'].append(list(h))
    elif any(item==3 for k, item in count.items()):
        # test whether full house or three of a kind:
        if any(item==2 for k, item in count.items()):
            # full house
            h_dict['full'].append(list(h))
        else:
            # three of a kind
            h_dict['three'].append(list(h))
    elif any(item==2 for k, item in count.items()):
        # test for two pair or just one pair
        pairs = 0
        for key, item in count.items():
            if item == 2:
                pairs += 1
        if pairs == 2:
            # two pair
            h_dict['two_p'].append(list(h))
        else:
            # one pair
            h_dict['one_p'].append(list(h))
    elif all(item==1 for k, item in count.items()):
        # high card, all cards are different
        h_dict['high'].append(list(h))
    return h_dict

# order lines by strength
for line in lines:
    line.strip()
    hand, bid = line.split(' ')
    bids[hand] = int(bid)
    hand_dict = determine_type(hand, hand_dict)
# sort each hand_dict key
l_to_n = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
n_to_l = {v: k for k, v in l_to_n.items()}
def sort(hand_d, ln, nl):
    for key in hand_d:
        # assign numbers to letters:
        to_sort = []
        for e in hand_d[key]:
            el = []
            for s in e:
                if s.isdigit():
                    el.append(int(s))
                else:
                    el.append(ln[s])
            to_sort.append(el)
        # sort list of numbers
        to_sort = sorted(to_sort, key=itemgetter(0,1,2,3,4))  # strongest comes last
        # convert back into letters and string:
        ha = []
        for e in to_sort:
            el = []
            for s in e:
                if s>=10 or s<2:  # smaller 2 for joker in part 2
                    el.append(nl[s])
                else:
                    el.append(str(s))
            ha.append("".join(el))
        hand_d[key] = ha
    return hand_d
hand_dict = sort(hand_dict, l_to_n, n_to_l)
# assign rank to each hand
ranks = []
for k, item in reversed(hand_dict.items()):
    ranks.append(item)
ranks = [item for typ in ranks for item in typ]
# winning: multiply each hands bid with rank and sum over all hands
wins = []
for r, h in enumerate(ranks):
    wins.append((r+1)*bids[h])
total_win = np.sum(wins)
print('part1:', total_win)

# part2: Js become Jokers
def determine_type_joker(h, h_dict):
    # if jokers present they increase strength
    if 'J' in h:
        js = Counter(h)['J']
        # exclude J from hand
        ha = h.replace('J', '')
        if ha == '':
            # only jokers, make fiver
            h_dict['five'].append(h)
        else:
            count = Counter(ha)
            count = dict(count)
            if any(item==4 for k, item in count.items()):
                h_dict['five'].append(list(h))
            elif any(item==3 for k, item in count.items()):
                if 3+js == 5:  # max 2 jokers
                    h_dict['five'].append(list(h))
                else:  # no full house since 3 card the same and at least one joker
                    h_dict['four'].append(list(h))
            elif any(item==2 for k, item in count.items()):
                # test whether full house or three of a kind:
                if js==3:
                    # five, since better than full house
                    h_dict['five'].append(list(h))
                elif js==2:
                    # fours, since better than two pairs
                    h_dict['four'].append(list(h))
                else:
                    # count pairs: if two then full house
                    pairs = 0
                    for key, item in count.items():
                        if item == 2:
                            pairs += 1
                    if pairs == 2:
                        # two pair + one joker
                        h_dict['full'].append(list(h))
                    else:
                        # one pair + one joker
                        h_dict['three'].append(list(h))
            else:
                # all different + joker: one pair
                h_dict['one_p'].append(list(h))
    else:
        # normal different types:
        h_dict = determine_type(h, h_dict)
    return h_dict

hand_dict2 = {'five': [], 'four': [], 'full': [], 'three': [], 'two_p': [], 'one_p': [], 'high': []}
# order lines by strength
for line in lines:
    line.strip()
    hand, bid = line.split(' ')
    bids[hand] = int(bid)
    hand_dict2 = determine_type_joker(hand, hand_dict2)
# sort each hand_dict key
l_to_n = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}
n_to_l = {v: k for k, v in l_to_n.items()}
hand_dict2 = sort(hand_dict2, l_to_n, n_to_l)
# assign rank to each hand
ranks2 = []
for k, item in reversed(hand_dict2.items()):
    ranks2.append(item)
ranks2 = [item for typ in ranks2 for item in typ]
# winning: multiply each hands bid with rank and sum over all hands
wins2 = []
for r, h in enumerate(ranks2):
    wins2.append((r+1)*bids[h])
total_win2 = np.sum(wins2)
print('part2:', total_win2)
