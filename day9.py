import numpy as np

with open('/home/alina/aoc_inputs/input9.txt', 'r') as file:
    lines = file.readlines()

def extract_number(line):
    ns = []
    for s in line.split():
        try:
            ns.append(float(s))
        except ValueError:
            pass
    return ns

predict = []
for l in lines:
    l = l.strip()
    l_hist = extract_number(l)
    # get differences until all diffs are 0
    l_pred = {0: l_hist}
    j = 1
    while set(l_pred[j-1]) != {0}:  # zeros become False
        l_pred[j] = np.diff(l_pred[j-1])
        if len(l_pred[j]) == 0:
            break
        j += 1
    if set(l_pred[j-1]) == {0}:
        l_pred[j] = []
    l_pred[j] = np.append(l_pred[j], 0)
    # reconstruct prediction
    for p in reversed(list(l_pred.keys())[:-1]):
        # add value of diff to last value
        pred = l_pred[p][-1]+l_pred[j][-1]
        l_pred[p] = np.append(l_pred[p], pred)
        j -= 1
    predict.append(pred)
print('part1:', np.sum(predict))
