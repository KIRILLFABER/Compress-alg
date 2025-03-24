
from math import log

def entropy(l):
    return -sum([(p * log(p, 2)) for p in l])


def compressFactor(compress_data, data):
    return len(data) / len(compress_data)


def prob(seq):
    uniq = list(set(seq))
    amount = []
    probs = []
    for i in uniq:
        c = 0
        for j in seq:
            if j == i:
                c+= 1
        amount.append(c)
    print(amount)
    for i in range(len(uniq)):
        probs.append(amount[i] / len(seq))
    return probs
















