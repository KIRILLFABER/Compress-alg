import bwt


class Node:
    def __init__(self, symbol = None, counter = None, left = None, right = None, parent = None):
        self.symbol = symbol
        self.counter = counter
        self.left = left
        self.right = right
        self.parent = parent

def count(a, text):
    c = 0
    for i in text:
        if (a == i):
            c += 1
    return c

def buildTree(text):
    pass


#  практика (какие то суффиксные массивы)


# def SA(S):
#     SArr = [S[i:] for i in range(len(S))]

#     SArr.sort()
#     print(SArr)
#     return SArr

# def SA_to_BWM(S):
#     S *= 2
#     SArr = SA(S)
#     L = []
#     for suf in SArr:
#         i = suf[0]
#         if i < len(S):
#             L.append(i)



#     return L
# S = "banana"
# SA(S * 2)
# print(SA_to_BWM(S))









