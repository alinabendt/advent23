import numpy as np

# part 1
numbers = []

with open('input1.txt', 'r') as file:
    for line in file:
        line = line.strip()
        number = [s for s in line if s.isdigit()]
        number = number[0]+number[-1]
        numbers.append(int(number))
res = np.sum(numbers)
print('part 1:', res)

# part 2
# numbers can be spelled out, ie four = 4
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
numbers2 = []
with open('input1.txt', 'r') as file:
    for line in file:
        line = line.strip()
        word = []
        number = []
        for s in line:
            word.append(s)
            if any(d in "".join(word) for d in digits):
                for d in digits:
                    if d in "".join(word):
                       number.append(str(digits.index(d)+1))
                word = [s]
            elif s.isdigit():
                number.append(s)
                word = []
        numbers2.append(int(number[0]+number[-1]))
res2 = np.sum(numbers2)
print('part 2:', res2)
