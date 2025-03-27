import numpy as np

import numpy as np


def prob(data):
    
    counts = np.zeros(256, dtype=np.float64)
    for byte in data:
        counts[byte] += 1
    
    total = len(data)
    return counts / total

def entropy(data):
    P = prob(data)
    P = P[P != 0]
    if len(P) == 0:
        return 0.0
    return -np.sum(P * np.log2(P))

def compressFactor(compress_data, data):
    return len(data) / len(compress_data)


# def prob(seq):
#     uniq = list(set(seq))
#     amount = []
#     probs = []
#     for i in uniq:
#         c = 0
#         for j in seq:
#             if j == i:
#                 c+= 1
#         amount.append(c)
#     print(amount)
#     for i in range(len(uniq)):
#         probs.append(amount[i] / len(seq))
#     return probs
















